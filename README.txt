rebecca.fanstatic
========================

fanstatic utilities for `pyramid web framework <http://www.pyramidproject.org>`_.

``add_fanstatic_resources`` directive
---------------------------------------------------

Add fanstatic resources for renderers matched to ``renderer_name_pattern``.


usage::

 config.include('rebecca.fanstatic')
 config.add_fanstatic_resources(['js.jquery.jquery', 'js.jqueryui.jqueryui'], r'.*\.pt')

`list_fanstatic` command
-----------------------------

::

   usage: list_fanstatic [-h] [-o OUTPUT_DIRECTORY] [-l [LIBRARY [LIBRARY ...]]]
                         [--simulate]
   
   Collect fanstatic resources and copy to destination directory.
   
   optional arguments:
     -h, --help            show this help message and exit
     -o OUTPUT_DIRECTORY, --output-directory OUTPUT_DIRECTORY
                           Set destination directory name. Default directory name
                           is 'fanstatic'.
     -l [LIBRARY [LIBRARY ...]], --library [LIBRARY [LIBRARY ...]]
                           Specify copy library names. Accept multiple options.
     --simulate            Simulate collecting resources. Print resource paths
                           and destination paths.
