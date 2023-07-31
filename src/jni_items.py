class Item:
	def __init__(self, id: int, question: str, yes_answer: bool):
		self.id = id
		self.question = question
		self.yes_answer = yes_answer


class ItemProvider:
	
	_instance: "None | ItemProvider" = None

	@staticmethod
	def get_instance() -> "ItemProvider":
		if ItemProvider._instance is None:
			ItemProvider._instance = ItemProvider()
		return ItemProvider._instance

	def __init__(self):
		self.items = []
		# FIXME load items from neo4j
		self.items.append(Item(1, "Is the sky blue?", True))
		self.items.append(Item(2, "Is the grass green?", True))
		self.items.append(Item(3, "Is the sun black?", False))
	
	def get_item(self, item_id) -> Item | None:
		print(f"get_item({item_id})")

		for item in self.items:
			if item.id == item_id:
				return item
		return None

	def get_items(self) -> list[Item]:
		return self.items
