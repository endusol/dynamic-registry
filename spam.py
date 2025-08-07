from dynamic_registry import Registry, RegistryEntry, _RegistryMeta


# TODO: need to solve the `_key_field` entry problem - separate the registry into the separate variable `self._registry`
class ErrorsRegistry(metaclass=_RegistryMeta):
    ERROR_500 = RegistryEntry(description='General internal server error!')
    ERROR_501 = RegistryEntry(description='Not authorized!')


# ERRORS = ErrorsRegistry(key_field='name')
# print(ERRORS.ERROR_501(user='some_user'))
# print(ERRORS.ERROR_500())
# print(ERRORS.registry)
print(ErrorsRegistry.registry)
print(Registry.registry)
