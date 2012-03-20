#

def includeme(config):
    config.add_directive('add_fanstatic_resources', '.directives.add_fanstatic_resources')
    config.add_subscriber('.subscribers.need_fanstatic', 'pyramid.events.BeforeRender')

