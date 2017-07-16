from . import exceptions, api
__all__ = ()

__version__ = '0.8.1'


from orderedattrdict import DefaultAttrDict
tree = lambda: DefaultAttrDict(tree)

config = tree()
config.api.key = None
config.domain.id = None
config.domain.name = None
config.team.id = None

