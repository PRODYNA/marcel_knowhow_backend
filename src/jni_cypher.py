from typing import Tuple

from neo4j import Query
from jni_types import Answer, Answering


def create_answering_cypher(answering: Answering) -> Tuple[Query, dict]:
	query = Query("CREATE (a:Answering { "
		"timestamp: $timestamp, "
		"ratio: $ratio}) " 
		"SET a.uuid = apoc.create.uuid() "
		"RETURN a.uuid;")
	params = {
		"timestamp": answering.time_stamp,
		"ratio": answering.ratio
	}
	return (query, params)


def create_answer_cypher(answer: Answer, answering_uuid: str) -> Tuple[Query, dict]:
	query = Query("MATCH (q:Question { id: $question_id }) "
		"MATCH (b:Answering { uuid: $answering_uuid }) "
		"CREATE (a:Answer { "
		"correct: $correct, "
		"reaction_time_ms: $reaction_time_ms}) " 
		"SET a.uuid = apoc.create.uuid() "
		"CREATE (a)-[:ANSWERED]->(q) "
		"CREATE (a)-[:BELONGS_TO]->(b)"
		"RETURN a.uuid;")
	params = {
		"question_id": answer.question_id,
		"answering_uuid": answering_uuid,
		"reaction_time_ms": answer.reaction_in_ms,
		"correct": answer.correct
	}
	return (query, params)
