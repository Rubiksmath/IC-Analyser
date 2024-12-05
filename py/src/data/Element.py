from typing import TypedDict, Optional, List, Tuple, Dict, Set
class BasicElement:
    text: str  # The name of the element - Note: Must be present.
    emoji: str | None  # The emoji of the element
    discovered: bool | None  # Whether the item is a first discovery or not

    def __init__(self, item: dict | str):
        if isinstance(item, str):
            # Assign the default name, text in this case
            self.text = item

        else:
            current_text = item.get("text", None)
            # Element with no text is silly. Reject these.
            if current_text is None:
                raise ValueError(f'This item has no "text" field: {item}, all elements of the BasicElement class require a text field.')
            self.text = current_text

            # Set to None if not present.
            self.emoji = item.get("emoji", None)
            self.discovered = item.get("discovered", None)






class Properties:
    default_name: str  # The default property name to assign if the constructor is just called with a string

    def __init__(self, default_name : str):
        self.default_name = default_name


