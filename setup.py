from setuptools import setup, find_packages
import os

__version__ = '0.1'
__author__ = 'Atsushi Odagiri'

requires = [
    "fanstatic",
]

testing_requires = [
    "nose",
    "coverage",
    "mock",
    "webtest",
]

try:
    import argparse
except ImportError:
    requires.append('argparse')

points = {
    "console_scripts": [
        "list_fanstatic=rebecca.fanstatic.commands:list_fanstatic",
    ],
    "fanstatic.libraries": [
        "rebecca.fanstatic.dummy_library=rebecca.fanstatic.tests.dummylibrary:dummy_library",
    ],
}
here = os.path.dirname(__file__)

def _read(name):
    try:
        return open(os.path.join(here, name)).read()
    except:
        return ""

        
readme = _read("README.txt")
changes = _read("CHANGES.txt")

setup(name="rebecca.fanstatic",
    version=__version__,
    author=__author__,
    author_email="aodagx@gmail.com",
    url="http://github.com/rebeccaframework/rebecca.fanstatic",

    install_requires=requires,
    entry_points=points,
    extras_require= {
        "testing": testing_requires,
    },
    description="fanstatic utilities",
    long_description=readme+"\r\n"+changes,
    license="MIT",
)

