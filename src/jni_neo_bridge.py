# pipe install neo4j
from neo4j import GraphDatabase, Driver
from jni_item import Item

NEO_USERNAME = "neo4j"
NEO_PASSWORD = "password"


class NeoBridge:

	def __init__(self, uri: str):
		self._driver = NeoBridge._create_driver(uri)

	def read_items(self) -> list[Item]:
		items: list[Item] = []

		with self._driver.session() as session:
			query_result = session.run("match (q:Question) "
				"return q.id, q.question, q.yes_answer")
			for record in query_result:
				id = record['q.id']
				question = record['q.question']
				yes_answer = record['q.yes_answer']
				item = Item(id, question, yes_answer)
				items.append(item)
		return items
	
	@staticmethod
	def _create_driver(uri: str) -> Driver:
		driver = GraphDatabase.driver(uri, auth=(NEO_USERNAME, NEO_PASSWORD))
		return driver

	def _destroy(self):
		self._driver.close()
