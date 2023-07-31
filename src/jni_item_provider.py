from jni_item import Item
from jni_neo_bridge import NeoBridge


class ItemProvider:
	
	_instance: "None | ItemProvider" = None

	@staticmethod
	def get_instance() -> "ItemProvider":
		if ItemProvider._instance is None:
			ItemProvider._instance = ItemProvider()
		return ItemProvider._instance

	def __init__(self):
		neo_bridge = NeoBridge()
		self.items = neo_bridge.read_items()
	
	def get_item(self, item_id) -> Item | None:
		print(f"get_item({item_id})")

		for item in self.items:
			if item.id == item_id:
				return item
		return None

	def get_items(self) -> list[Item]:
		return self.items
