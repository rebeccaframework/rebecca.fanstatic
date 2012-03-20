from fanstatic import get_library_registry
from zope.interface import implementer
from .interfaces import IFanstaticSet

def get_fanstatic_set(request):
    reg = request.registry
    fanstatic_set = reg.queryUtility(IFanstaticSet)
    return fanstatic_set

def need_fanstatic(request, renderer_name):
    fanstatic_set = get_fanstatic_set(request)
    if fanstatic_set is None:
        return
    fanstatic_set(renderer_name)

class FanstaticSet(object):
    def __init__(self):
        self.fanstatics = []

    def add_fanstatic(self, resources, renderer_name_pattern):
        self.fanstatics.append(Fanstatic(resources, renderer_name_pattern))

    def __call__(self, renderer_name):

        for f in self.fanstatics:
            f(renderer_name)

class Fanstatic(object):
    def __init__(self, resources, renderer_name_regex):
        self.resources = resources
        self.regex = renderer_name_regex

    def match(self, renderer_name):
        return self.regex.match(renderer_name)

    def __call__(self, renderer_name):
        if self.match(renderer_name):
            for resource in self.resources:
                from fanstatic.core import get_needed
                resource.need()
