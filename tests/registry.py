"""
Tests for the registry behavior.
"""
from dynamic_registry import Registry, Entry


def test__registry_default_key_field_is_set_correctly():
    class TestRegistry(metaclass=Registry):
        """Test registry."""

    assert TestRegistry.key_field == 'key'


def test__registry_key_field_reset_works_correctly():
    key_field = 'custom_key_field'

    class TestRegistry(metaclass=Registry, key_field=key_field):
        """Test registry."""

    assert TestRegistry.key_field == key_field


def test__registry_key_field_disabling_works_correctly():
    class TestRegistry(metaclass=Registry, key_field=None):
        """Test registry."""
        ENTRY = Entry()

    assert TestRegistry.ENTRY() == {}


def test__registry_entries_returns_full_and_correct_dict_of_entries():
    entries_num = 3
    entries = [Entry() for _ in range(entries_num)]

    class TestRegistry(metaclass=Registry):
        """Test registry."""
        ENTRY_0 = entries[0]
        ENTRY_1 = entries[1]
        ENTRY_2 = entries[2]

    assert len(TestRegistry.entries) == entries_num

    for idx, entry in enumerate(entries):
        assert TestRegistry.entries[f'ENTRY_{idx}'] is entry
