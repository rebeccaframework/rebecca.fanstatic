#

def includeme(config):
    config.add_directive('add_fanstatic_library', '.directives.add_fanstatic_library')
    config.add_subscriber('.subscribers.need_fanstatic', 'pyramid.events.BeforeRender')

