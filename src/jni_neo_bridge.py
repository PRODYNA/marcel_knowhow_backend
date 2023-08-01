import os

from neo4j import GraphDatabase, Driver
from jni_types import Item

NEO_URI_ENV_NAME = "MARCEL_DB_URI"
NEO_USERNAME = "neo4j"
NEO_PASSWORD = "password"
BACKUP_NEO_URI = "bolt://localhost:7687"


class NeoBridge:

	def __init__(self):
		uri = BACKUP_NEO_URI 
		if NEO_URI_ENV_NAME in os.environ:
			uri = os.environ[NEO_URI_ENV_NAME]
		self._driver = NeoBridge._create_driver(uri)

	def read_items(self) -> list[Item]:
		try:
			items = self._read_items()
			return items
		except Exception as e:
			err_message = f"Error while reading items from Neo4j: {e}"
			print(err_message)
			print("Attempting to reestablish connection to Neo4j...")
			try:
				self._destroy()
			except Exception as e:
				pass
			try:
				self._driver = NeoBridge._create_driver(BACKUP_NEO_URI)
				print("Reloaded driver")
				items = self._read_items()
				return items
			except Exception as e:
				err_message = f"2nd Error while reading items from Neo4j: {e}"
				print(err_message)
				raise Exception(err_message)

	def _read_items(self) -> list[Item]:
		items: list[Item] = []

		with self._driver.session() as session:
			query_result = session.run("match (q:Question) "
				"return q.id, q.question, q.yes_answer")
			for record in query_result:
				id = record['q.id']
				question = record['q.question']
				yes_answer = record['q.yes_answer']
				item = Item(id=id, question=question, yes_answer=yes_answer)
				items.append(item)
		return items
	
	@staticmethod
	def _create_driver(uri: str) -> Driver:
		driver = GraphDatabase.driver(uri, auth=(NEO_USERNAME, NEO_PASSWORD))
		return driver

	def _destroy(self):
		self._driver.close()
