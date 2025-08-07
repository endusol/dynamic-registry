import typing as t



class Registry(type):
    def __new__(mcs, name, bases, namespace, *, key_field='key'):
        namespace['_registry'] = {}
        cls = super().__new__(mcs, name, bases, namespace)
        cls._key_field = key_field
        cls._registry = namespace['_registry']  # Need this just for autocomplete.

        # Clean-up the entries from the class root so they are presented only in the registry attribute.
        for _ in [key for key, value in cls.__dict__.items() if isinstance(value, Entry)]:
            delattr(cls, _)
        return cls

    @property
    def key_field(cls):
        return cls._key_field

    @property
    def registry(cls) -> t.Dict[t.Hashable, 'Entry']:
        return cls._registry

    def __repr__(cls):
        return f'<Registry {cls.__name__} with entries: {", ".join(cls._registry)}>'

    def __getattr__(self, item):
        try:
            return self.__dict__[item]
        except KeyError:
            return self._registry[item]


class Entry:
    def __init__(self, **defaults):
        self._defaults = defaults

    def __set_name__(self, owner: 'Registry', name):
        self._key = name
        self._owner = owner
        owner.registry[name] = self

    def __call__(self, **overrides):
        return {**self._defaults, **overrides, self._owner.key_field: self._key}

    def __repr__(self):
        return f'<Registry entry {self._key} with defaults: {self._defaults}>'


##### TESTS ############################################################################################################

class RegistryA(metaclass=Registry):
    ENTRY_A1 = Entry(a=100)
    ENTRY_A2 = Entry(a=200)
    # key_field = Entry(a=None)


print(RegistryA.ENTRY_A1())
print(RegistryA.ENTRY_A2())


class RegistryB(metaclass=Registry, key_field='name'):
    ENTRY_B1 = Entry(b=300)
    ENTRY_B2 = Entry(b=400)


print(RegistryB.ENTRY_B1())
print(RegistryB.ENTRY_B2())

print(RegistryA)
print(RegistryA.ENTRY_A2)
print(RegistryA.key_field)
print(RegistryA.registry)
