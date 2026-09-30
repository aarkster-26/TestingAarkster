"""Tiny stdlib-only module used to exercise the AarksterNexus permission-gated development cycle."""


def _shout(text):
    """Return `text` uppercased with its trailing '!' doubled."""
    return text.upper() + "!"


def _validate_name(name):
    """Raise ValueError unless `name` is a non-blank string."""
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name must be a non-empty string")


_GREETING_STYLES = {
    "casual": "Hello, {name}!",
    "formal": "Good day, {name}.",
}


def greet(name, excited=False, style="casual"):
    """Return a greeting for `name` in the given `style` ('casual' or 'formal')."""
    _validate_name(name)
    if style not in _GREETING_STYLES:
        raise ValueError(f"unsupported style: {style!r}")
    text = _GREETING_STYLES[style].format(name=name)
    return _shout(text) if excited else text


def farewell(name, excited=False):
    """Return a farewell for `name`."""
    _validate_name(name)
    text = f"Goodbye, {name}!"
    return _shout(text) if excited else text
