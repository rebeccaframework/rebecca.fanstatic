import re
from .interfaces import IFanstaticSet
from .apis import FanstaticSet

def add_fanstatic_resources(config, resources, renderer_name_pattern):
    """ Add fanstatic resources for renderers matched to `renderer_name_pattern`.

    Don't use directly this function. 
    You should use that as directive after include "rebecca.fanstatic".
    """

    fanstatic_set = config.registry.queryUtility(IFanstaticSet)
    if fanstatic_set is None:
        fanstatic_set = FanstaticSet()
        config.registry.registerUtility(fanstatic_set, IFanstaticSet)
    renderer_name_regex = re.compile(renderer_name_pattern)
    resources = [config.maybe_dotted(r) for r in resources]
    
    fanstatic_set.add_fanstatic(resources, renderer_name_regex)
