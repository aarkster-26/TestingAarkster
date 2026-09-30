"""Tiny stdlib-only module used to exercise the AarksterNexus permission-gated development cycle."""


def _shout(text):
    """Return `text` uppercased with its trailing '!' doubled."""
    return text.upper() + "!"


def _validate_name(name):
    """Raise ValueError unless `name` is a non-blank string."""
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name must be a non-empty string")


def greet(name, excited=False):
    """Return a friendly greeting for `name`."""
    _validate_name(name)
    text = f"Hello, {name}!"
    return _shout(text) if excited else text


def farewell(name, excited=False):
    """Return a farewell for `name`."""
    _validate_name(name)
    text = f"Goodbye, {name}!"
    return _shout(text) if excited else text
