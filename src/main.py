from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from jni_item_provider import ItemProvider


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
    return items


@app.post("/quizz_results")
async def create_quizz_results():
    # TODO Create a quizz results class
    # json_content = message.content.strip()
    # dict = json.loads(json_content)
    # selected_option = dict["selected_option"]
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
