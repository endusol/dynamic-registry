"""
Isolation tests for multiple registries.
"""
import pytest
from dynamic_registry import Registry, Entry


def test__multiple_registries_do_not_share_key_field():
    class TestRegistryDefault(metaclass=Registry):
        """Test registry with default ``key_field``."""

    class TestRegistryCustom(metaclass=Registry, key_field='custom_key_field'):
        """Test registry with custom ``key_field``."""

    assert TestRegistryDefault.key_field != TestRegistryCustom.key_field


def test__multiple_registries_do_not_share_entries():
    class TestRegistryA(metaclass=Registry):
        """Test registry A."""
        ENTRY_WITH_THE_SAME_KEY = Entry()
        ENTRY_A = Entry()

    class TestRegistryB(metaclass=Registry):
        """Test registry B."""
        ENTRY_WITH_THE_SAME_KEY = Entry()
        ENTRY_B = Entry()

    assert TestRegistryA.ENTRY_WITH_THE_SAME_KEY is not TestRegistryB.ENTRY_WITH_THE_SAME_KEY

    with pytest.raises(AttributeError):
        getattr(TestRegistryA, 'ENTRY_B')

    with pytest.raises(AttributeError):
        getattr(TestRegistryB, 'ENTRY_A')
