from dynamic_registry import Registry, Entry


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
