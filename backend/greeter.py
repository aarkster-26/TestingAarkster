"""Tiny stdlib-only module used to exercise the AarksterNexus permission-gated development cycle."""


def _shout(text):
    """Return `text` uppercased with its trailing '!' doubled."""
    return text.upper() + "!"


def greet(name, excited=False):
    """Return a friendly greeting for `name`."""
    text = f"Hello, {name}!"
    return _shout(text) if excited else text


def farewell(name, excited=False):
    """Return a farewell for `name`."""
    text = f"Goodbye, {name}!"
    return _shout(text) if excited else text
