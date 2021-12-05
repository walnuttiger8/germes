from application.models import Registry
from base import ICreateRegistryResponse


class CreateRegistrySuccessResponse(ICreateRegistryResponse):

    def __init__(self, registry: Registry):
        self._registry = registry

    @property
    def registry(self):
        return self._registry
