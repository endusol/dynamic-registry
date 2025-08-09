import typing as t


class Registry(type):
    """
    Registry metaclass.
    """
    def __new__(mcs, name, bases, namespace, *, key_field='key'):
        cls = super().__new__(mcs, name, bases, namespace)
        cls._key_field = key_field
        return cls

    @property
    def key_field(cls) -> t.Hashable:
        """
        Field ``key_field``. The field used in all the registry entries to represent unique key/name of the entry.
        """
        return cls._key_field

    @property
    def entries(cls) -> t.Dict[str, 'Entry']:
        """
        All the entries as a dictionary.
        """
        return {key: value for key, value in cls.__dict__.items() if isinstance(value, Entry)}

    def __repr__(cls):
        entries_names = ', '.join([str(_) for _ in cls.entries])
        return f'<Registry {cls.__name__} with entries: {entries_names}>'


class Entry:
    """
    Registry entry.
    :param defaults: keyword arguments representing default entry data.
    """
    def __init__(self, **defaults):
        self._defaults = defaults

    def __set_name__(self, owner: 'Registry', name: str):
        if not name.isupper():
            raise NameError(f'Registry entry name `{name}` must be uppercase!')
        self._key = name
        self._owner = owner

    def __call__(self, **overrides) -> t.Dict[t.Hashable, t.Any]:
        return {**self._defaults, **overrides, self._owner.key_field: self._key}

    def __repr__(self):
        return f'<Entry `{self._key}` with defaults: {self._defaults}>'


##### TESTS ############################################################################################################

class RegistryA(metaclass=Registry):
    ENTRY_A1 = Entry(a=100)
    ENTRY_A2 = Entry(a=200)
    ENTRY_A3 = Entry()


print(RegistryA.ENTRY_A1())
print(RegistryA.ENTRY_A2())


class RegistryB(metaclass=Registry, key_field='name'):
    ENTRY_B1 = Entry(b=300)
    ENTRY_B2 = Entry(b=400)


print(RegistryB.ENTRY_B1())
print(RegistryB.ENTRY_B2())

print(RegistryA)
print(RegistryA.ENTRY_A2)
print(RegistryA.entries)
print(RegistryA.key_field)
