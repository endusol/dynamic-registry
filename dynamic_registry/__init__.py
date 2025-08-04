"""
Dynamic registry library. Allows to create registries with
entries that may be enriched with some additional data just on time.

Example::

    from dynamic_registry import Registry, RegistryEntry

    class ErrorsRegistry(Registry):
        ERROR_500 = RegistryEntry(description='General internal server error!')
        ERROR_501 = RegistryEntry(description='Not authorized!')


    ERRORS = ErrorsRegistry(key_field='name')
    print(ERRORS.ERROR_501(user='some_user'))
    print(ERRORS.ERROR_500())
"""
import typing as t


class RegistryEntry:
    """
    Registry entry.
    :param defaults: keyword arguments that represents an entry default values.
    """
    def __init__(self, **defaults):
        self._defaults = defaults

    def __set_name__(self, owner: 'Registry', name):
        self._key = name

    def __get__(self, instance: 'Registry', owner: '_RegistryMeta') -> t.Callable[..., t.Dict[t.Any, t.Any]]:
        return lambda **overrides_: {**self._defaults, **overrides_, instance.key_field: self._key}

    def __repr__(self):
        return f'<Registry entry {self._key} with defaults: {self._defaults}>'


class _RegistryMeta(type):
    def __repr__(cls):
        return f'<Registry {cls.__name__} with entries: {", ".join(cls.entries)}>'

    @property
    def entries(cls) -> t.Dict[str, 'RegistryEntry']:
        """
        Return all registry entries.
        :return: all th entries as a dict.
        """
        return {key: value for key, value in cls.__dict__.items() if isinstance(value, RegistryEntry)}


class Registry(metaclass=_RegistryMeta):
    """
    Dynamic registry. Dynamic here means, that each entry may be enriched with additional data just in time.
    """
    def __init__(self, key_field: t.Union[t.Hashable, None] = 'key'):
        self._key_field = key_field

    @property
    def key_field(self) -> t.Union[t.Hashable, None]:
        """
        Name of the field used as entry key (unique name) within the registry.
        :return: name of the field.
        """
        return self._key_field
