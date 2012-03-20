from setuptools import setup, find_packages

requires = [
    "pyramid",
    "fanstatic",
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

setup(name="rebecca.fanstatic",
    install_requires=requires,
    entry_points=points,
)

