from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from jni_items import ItemProvider


app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def read_root() -> dict[str, bool]:
    return {"system_okay": True}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    provider = ItemProvider.get_instance()
    item = provider.get_item(item_id)
    if item is not None:
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.get("/items")
def read_items():
    provider = ItemProvider.get_instance()
    items = provider.get_items()
    return items


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
