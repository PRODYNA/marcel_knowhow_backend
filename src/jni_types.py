from pydantic import BaseModel


class Item(BaseModel):
    id: int
    question: str
    yes_answer: bool


class ResultsServerRequest(BaseModel):
    questions: list[Item]
    answers: list[bool]
    reactTimes: list[int]
