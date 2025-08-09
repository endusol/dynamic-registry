"""
Tests for the entry behavior.
"""
import pytest
from dynamic_registry import Registry, Entry


def test__entry_name_must_be_uppercase():
    with pytest.raises(NameError):
        class TestRegistry(metaclass=Registry):
            """Test registry."""
            lower_cased_entry = Entry()


def test__entry_key_is_set_as_default_key_field():
    class TestRegistry(metaclass=Registry):
        """Test registry."""
        ENTRY = Entry()

    assert TestRegistry.ENTRY()['key'] == 'ENTRY'


def test__entry_key_is_set_as_custom_key_field():
    key_field = 'custom_key_field'

    class TestRegistry(metaclass=Registry, key_field=key_field):
        """Test registry."""
        ENTRY = Entry()

    assert TestRegistry.ENTRY()[key_field] == 'ENTRY'


def test__entry_returns_correct_and_all_the_defaults():
    defaults = {'a': 13, 'b': 'spam', 'c': [1, 2, 3]}

    class TestRegistry(metaclass=Registry):
        """Test registry."""
        ENTRY = Entry(**defaults)

    defaults.update(key='ENTRY')
    assert TestRegistry.ENTRY() == defaults


def test__entry_key_field_is_rewritten_by_defaults():
    key = 'CUSTOM_ENTRY_KEY'

    class TestRegistry(metaclass=Registry):
        """Test registry."""
        ENTRY = Entry(key=key)

    assert TestRegistry.ENTRY()['key'] == key


def test__entry_key_field_is_rewritten_by_runtime_enrichment_data():
    key = 'CUSTOM_ENTRY_KEY'

    class TestRegistry(metaclass=Registry):
        """Test registry."""
        ENTRY = Entry()

    assert TestRegistry.ENTRY(key=key)['key'] == key


def test__defaults_are_rewritten_by_runtime_enrichment_data():
    class TestRegistry(metaclass=Registry):
        """Test registry."""
        ENTRY = Entry(a=100, b=200)

    enriched = TestRegistry.ENTRY(a=111)
    assert enriched['a'] == 111
    assert enriched['b'] == 200
