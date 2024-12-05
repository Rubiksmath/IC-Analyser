class FileIndexerNoId:
    elements: dict[str, dict] = {}  # The items being used. Maps item string to information including recipes, and emoji and fd if those options are selected.
    recipes_fwd: dict[tuple[str, str], str] = {}  # Maps input recipe to result.
    elements_normalised: dict[str, set[str]] = {}  # Maps normalised casing to set of all casing variants. These can be used to lookup other data.
    use_emojis: bool  # Flag for whether we use emojis or not.
    use_fd: bool  # Flag for whether to use or care about first discoveries or not.
    differentiate_casing: bool  # Flag for whether to differentiate casing in any way or not. True means that the behaviour should replicate the server responses.


    def add_item(self, element):

        current_data = self.elements.get(element, {})
        if current_data:
            return  # TODO: Add proper logic here, but the bottom line is that we do not want to overwrite recipes.
        else:
            new_data = current_data
            if self.use_emojis:
                new_data["emoji"] = element.get("emoji", "⬜")  # Default emoji.
            if self.use_fd:
                new_data["discovered"] = element.get("discovered", False)  # Assume not fd if missing. Really just an arbitrary choice.



