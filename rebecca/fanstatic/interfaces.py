from zope.interface import Interface

class IFanstaticSet(Interface):

    def add_fanstatic(resources, renderer_name_regex):
        """ add fanstatic resources needed by renderer matches renderer_name_pattern"""


    def __call__(renderer_name):
        """ invoke `Resource.need` trigger of matched resources"""
