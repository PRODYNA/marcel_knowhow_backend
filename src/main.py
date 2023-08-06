from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from jni_item_provider import ItemProvider
from jni_types import Answer, Answering, ResultsServerRequest


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root() -> dict[str, bool]:
    return {"system_health": True}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    provider = ItemProvider.get_instance()
    item = provider.get_item(item_id)
    if item is not None:
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.get("/items")
async def read_items():
    provider = ItemProvider.get_instance()
    items = provider.get_items()
    return {"questions": items}


@app.post("/quizz_results")
async def create_quizz_results(request: ResultsServerRequest):
    questions = request.questions
    in_answers = request.answers
    react_times = request.reactTimes

    neo_answers: list[Answer] = []
    # Count the number of correct answers.
    correct_answers = 0
    for i in range(len(questions)):
        answer_correct = questions[i].yes_answer == in_answers[i]
        if answer_correct:
            correct_answers += 1
        neo_answering = Answer(
            correct=answer_correct, 
            question_id=questions[i].id, 
            reaction_in_ms=react_times[i]
        )
        neo_answers.append(neo_answering)

    # Compute and return the ratio of correct answers.
    correctness_ratio = correct_answers / len(questions)
    neo_answering = Answering(
        ratio=correctness_ratio, 
        time_stamp=datetime.now().isoformat(),
        answers=neo_answers
    )
    
    # Write the results to the database.
    provider = ItemProvider.get_instance()
    provider.write_resultsAsCoroutine(neo_answering)
    
    return {"ratio": correctness_ratio}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
