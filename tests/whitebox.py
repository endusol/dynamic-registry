"""
White-box tests for internal entry/registry state.
"""
from dynamic_registry import Registry, Entry


def test__entry_key_set_correctly():
    class TestRegistry(metaclass=Registry):
        """Test registry."""
        ENTRY = Entry()

    assert TestRegistry.ENTRY._key == 'ENTRY'


def test__entry_owner_set_correctly():
    class TestRegistry(metaclass=Registry):
        """Test registry."""
        ENTRY = Entry()

    assert TestRegistry.ENTRY._owner is TestRegistry


def test__registry_key_field_is_set_correctly():
    key_field = 'custom_key_field'
    class TestRegistry(metaclass=Registry, key_field=key_field):
        """Test registry."""

    assert TestRegistry._key_field == key_field
