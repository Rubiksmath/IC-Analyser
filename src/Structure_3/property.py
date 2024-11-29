import conflicthandler
class Property:
    name: str  # The name of the property, e.g. "emoji".
    value_type: type  # The type of value that this property stores, e.g. str.
    conflict_handler: callable = conflicthandler.do_nothing  # The conflict handler.

    def __init__(self, name: str, value_type: type):
        self.name = name
        self.value_type = value_type

    def set_value(self, target, value):
        # Ensure types match
        if type(value) != self.value_type:
            raise TypeError(f"PropertyError: Type of value passed to this property does not match the defined type specified, "
                            f"expected type {self.value_type}, got {type(value)}")

        current = target.get(self.name)
        if current is not None and current != value:
            # Conflict occurred, handle accordingly
            self.conflict_handler(target, current, value)
        else:
            # Set property
            target.properties[self.name] = value



    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
