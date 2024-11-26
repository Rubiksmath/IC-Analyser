def pair_to_u64(item1: int, item2: int) -> int:
    if item2 < item1:
        # If they are the same it makes no difference to swap them, all good.
        item1, item2 = item2, item1

    if item2 > 2**32:
        # not good!!
        raise ValueError(f"Item {item2} is too big to fit!")

    return item1 << 32 | item2


def u64_to_pair(recipe_id: int) -> tuple[int, int]:
    if recipe_id > 2**64:
        # Not good!
        raise ValueError(f"Recipe {recipe_id} is too big to fit, something is wrong probably!")

    # Recover first and last parts
    return recipe_id >> 32, recipe_id % 2**32

