from fanstatic import Library, Resource

dummy_library = Library('rebecca.fanstatic.dummy_library', 'dummy_resources')
dummy1_js = Resource(dummy_library, 'dummy1.js')
dummy2_js = Resource(dummy_library, 'dummy2.js')
dummy_css = Resource(dummy_library, 'dummy.css')
