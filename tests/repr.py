"""
Tests for string representations (`__repr__`) for the entry and the registry objects.
"""
from dynamic_registry import Registry, Entry



def test__repr_of_registry():
    class TestRegistry(metaclass=Registry):
        """Test registry."""
        ENTRY_1 = Entry()
        ENTRY_2 = Entry()

    expected_entries = ', '.join(f'`{_}`' for _ in TestRegistry.entries)
    expected_repr = f'<Registry `{TestRegistry.__name__}` with entries: {expected_entries}>'
    assert repr(TestRegistry) == expected_repr


def test__repr_of_entry():
    defaults = {'a': 13, 'b': 'spam', 'c': [1, 2, 3]}

    class TestRegistry(metaclass=Registry):
        """Test registry."""
        ENTRY = Entry(**defaults)

    expected_repr = f'<Entry `ENTRY` with defaults: {defaults}>'
    assert repr(TestRegistry.ENTRY) == expected_repr
