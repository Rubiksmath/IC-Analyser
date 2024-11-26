from utils import pair_to_u64, u64_to_pair

USE_ID = True

class FileIndexer:
    result_ids: dict[int, str]  # Structure for case sensitive id matching.
    ing_ids: dict[str, int]  # Structure to match string to uncased id.
    def __init__(self):
        self.items = {}


    def add_element(self, element_name: str):
        """Adds element to the data structure by adding its id, in both case sensitive and case insensitive forms.
        Note that case-sensitive is important only for the final output (excluding banned elements), and so therefore
        case insensitive when querying recipes should be used. Unless you can think of something i didnt consider. """

        unique_id = len(self.result_ids)
        self.result_ids[unique_id] = element_name
        if element_name in self.ing_ids



    def add_name


    def get_name(self, item_id: int) -> str:
        try:
            return self.ids_cs[item_id]
        except KeyError:
            raise ValueError(f"Item id {item_id} doesnt exist in self.ids_cs")


if USE_ID:
    pass