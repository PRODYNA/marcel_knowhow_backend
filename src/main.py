from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from jni_item_provider import ItemProvider
from jni_types import ResultsServerRequest


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
    answers = request.answers
    react_times = request.reactTimes

    # Count the number of correct answers.
    correct_answers = 0
    for i in range(len(questions)):
        if questions[i].yes_answer == answers[i]:
            correct_answers += 1

    # Compute and return the ratio of correct answers.
    correctness_ratio = correct_answers / len(questions)
    return {"ratio": correctness_ratio}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
