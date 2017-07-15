from . import exceptions, request, version
__all__ = ()

from orderedattrdict import DefaultAttrDict
tree = lambda: DefaultAttrDict(tree)

config = tree()
config.api.key = None
config.domain.id = None
config.domain.name = None
config.team.id = None

