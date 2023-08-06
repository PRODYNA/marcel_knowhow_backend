from pydantic import BaseModel


class Item(BaseModel):
    id: int
    question: str
    yes_answer: bool


class ResultsServerRequest(BaseModel):
    questions: list[Item]
    answers: list[bool]
    reactTimes: list[int]


class Answer(BaseModel):
    correct: bool
    question_id: int
    reaction_in_ms: int


class Answering(BaseModel):
    ratio: float
    time_stamp: str
    answers: list[Answer]
