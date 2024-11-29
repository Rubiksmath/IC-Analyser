def do_nothing(*args):
    return None

def handle_emoji_conflict(target, current, value):
    if current is not None and value == "⬜":
        # Don't need to do anything here
        return None

