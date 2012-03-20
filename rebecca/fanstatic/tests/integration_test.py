import unittest
import webtest
from pyramid import testing

class FunctionalTests(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        from fanstatic.core import init_needed
        init_needed()

    def tearDown(self):
        from fanstatic.core import del_needed
        del_needed()
        testing.tearDown()


    def test_directive(self):
        self.config.include('rebecca.fanstatic')
        self.assertTrue(hasattr(self.config, 'add_fanstatic_resources'))

    def test_notify(self):
        from pyramid.events import BeforeRender
        from fanstatic.core import get_needed


        self.config.include('rebecca.fanstatic')
        self.config.add_fanstatic_resources(['js.jquery.jquery',], r'.*\.mak')

        request = testing.DummyRequest(registry=self.config.registry)
        system_values = {'request': request, 'renderer_name': 'test.mak'}
        event = BeforeRender(system_values)

        self.config.registry.notify(event)

        from js.jquery import jquery
        needed = get_needed()
        self.assertIn(jquery, needed._resources)

