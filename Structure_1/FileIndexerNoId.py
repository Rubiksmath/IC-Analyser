import json
import os


class FileIndexerNoId:
    elements_collapsed: dict[str, set[str]]  # Contains elements (lowercase) and a mapping to each casing variant
    elements: set[str]  # Contains all elements (case-sensitive)
    recipes_bwd: dict[str, set[tuple[str, str, str]]]  # Maps item (case-insensitive) to input ingredients (case-insensitive) which also contains actual result for use as case sensitive
    recipes_fwd: dict[tuple[str, str], str]  # Maps sorted tuple of case-insensitive ingredients to *case-sensitive* result
    use_emojis: bool  # Do I care about emojis or not? default is False
    emojis: dict[str, str]  # Maps element test (case-sensitive) to emoji (default emoji is ⬜ (U+2B1C))

    def __init__(self, initial_items: list[tuple[str]], use_emojis: bool = False):
        self.elements_collapsed = {}
        self.elements = set()
        self.recipes_bwd = {}
        self.recipes_fwd = {}
        self.use_emojis = use_emojis
        if self.use_emojis:
            self.emojis = {}
        for item in initial_items:
            self.add_item(*item)

    def add_item(self, *item: str):
        """Adds items to the structures for cased and uncased. Note that since we reach a set in all cases, .add() is safe."""
        name, *emoji = *item,
        # print(item)
        # print(name)
        # print(emoji)

        self.elements.add(name)
        if name.lower() not in self.elements_collapsed:
            self.elements_collapsed[name.lower()] = set()

        self.elements_collapsed[name.lower()].add(name)
        if self.use_emojis:
            self.emojis[name] = "⬜" if not emoji else emoji[0]  # Unusual negation here to prevent error

        # Just in case, no idea why I'd want it though.
        return self.elements_collapsed[name.lower()]

    def add_recipe(self, item1: str, item2: str, result: str):
        """Adds recipe and additionally syncs items if they aren't present.
         May need to add some kind of way to check if items never get a recipe provided, to mark them somehow."""
        # Keep item1 and item2 in case I need them, while also generating lowercase versions. I don't know if there's a better place to put this.
        item1l, item2l, resultl = item1.lower(), item2.lower(), result.lower()

        # Ensure parity between recipes and elements, note that add_item() handles adding both the case-insensitive and case-sensitive versions
        if item1 not in self.elements:
            self.add_item(item1)

        if item2 not in self.elements:
            self.add_item(item1)

        if result not in self.elements:
            self.add_item(item1)


        if item2l < item1l:
            # Swap them, for ordering purposes.
            item1l, item2l = item2l, item1l

        # Add case-sensitive result to what you get with case-insensitive ingredients (mimics actual game).
        # Note that this will get overwritten since A + B and a + b give same result always, so it should be safe, unless the save is broke.
        self.recipes_fwd[(item1l, item2l)] = result

        if resultl in self.recipes_bwd:
            self.recipes_bwd[resultl].add((item1l, item2l, result))

    def check_elements_exist(self, *items):
        """May or may not use this, exists if I need it for convenience to sync things and return lowercase lol"""
        out = []
        for item in items:
            if item not in self.elements:
                # If the proper casing isn't in, it still adds the collapsed case anyway, which is fine and safe.
                self.add_item(item)
            out.append(item.lower())

        return *out,


def savefile_to_indexer_noid(file_path: str, use_emojis=False) -> FileIndexerNoId:
    name, ext = os.path.splitext(file_path)
    if ext != ".json":
        raise ValueError(f"Improper savefile specified. Expected type '.json', but got type '{ext}'")
    with open(file_path, 'r', encoding='utf-8') as f:
        save_raw = json.load(f)

    try:
        elements_raw = save_raw["elements"]
    except KeyError:
        raise ValueError("Savefile does not contain 'elements' list, aborting...")

    try:
        recipes_raw = save_raw["recipes"]
    except KeyError:
        raise ValueError("Savefile does not contain 'recipes' list, aborting...")


    indexer = FileIndexerNoId([(element.get("text"), element.get("emoji")) for element in elements_raw], use_emojis=use_emojis)
    for recipe_item, recipes in recipes_raw.items():
        # print(recipe_item)
        for item1, item2 in recipes:
            indexer.add_recipe(item1["text"], item2["text"], recipe_item)

    # Stuff
    return indexer

