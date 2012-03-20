from . import apis

def need_fanstatic(event):
    request = event['request']
    name = event['renderer_name']
    apis.need_fanstatic(request, name)
