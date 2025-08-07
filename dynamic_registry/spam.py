import typing as t



class Registry(type):
    def __new__(mcs, name, bases, namespace, *, key_field='key'):
        cls = super().__new__(mcs, name, bases, namespace)
        cls._key_field = key_field
        return cls

    @property
    def key_field(cls):
        return cls._key_field

    @property
    def registry(cls) -> t.Dict[t.Hashable, 'Entry']:
        return {key: value for key, value in cls.__dict__.items() if isinstance(value, Entry)}
        # return cls._registry

    def __repr__(cls):
        entries = ', '.join([str(_) for _ in cls.registry])
        return f'<Registry {cls.__name__} with entries: {entries}>'


class Entry:
    def __init__(self, **defaults):
        self._defaults = defaults

    def __set_name__(self, owner: 'Registry', name):
        self._key = name

    def __get__(self, instance: None, owner: 'Registry') -> t.Callable[..., t.Dict[t.Any, t.Any]]:
        return lambda **overrides_: {**self._defaults, **overrides_, owner.key_field: self._key}


##### TESTS ############################################################################################################

class RegistryA(metaclass=Registry):
    ENTRY_A1 = Entry(a=100)
    ENTRY_A2 = Entry(a=200)


print(RegistryA.ENTRY_A1())
print(RegistryA.ENTRY_A2())


class RegistryB(metaclass=Registry, key_field='name'):
    ENTRY_B1 = Entry(b=300)
    ENTRY_B2 = Entry(b=400)


print(RegistryB.ENTRY_B1())
print(RegistryB.ENTRY_B2())

print(RegistryA)
print(RegistryA.ENTRY_A2)
print(RegistryA.registry)
print(RegistryA.key_field)
