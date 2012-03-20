import os
import shutil
import argparse
from fanstatic.registry import get_library_registry
from pyramid.paster import bootstrap
from .apis import get_fanstatic_set

def _print(s):
    print s


def iter_all_libraries():
    reg = get_library_registry()
    return reg.itervalues()

def iter_libraries(names):
    reg = get_library_registry()
    return (v for v in reg.itervalues() if v.name in names)

def iter_libraries_from_config(config):
    env = bootstrap(config)
    request = env['request']
    fanstatic_set = get_fanstatic_set(request)
    if fanstatic_set:
        return fanstatic_set.iter_resources()

def print_fanstatic_resources(destbasedir, library):
    outdir = os.path.join(destbasedir, library.name)
    for name, resource in library.known_resources.iteritems():
        sourcepath = os.path.join(library.path, resource.relpath)
        dest = os.path.join(outdir, resource.relpath)
        _print("%s -> %s" % (sourcepath, dest))

def copy_fanstatic_resources(destbasedir, library):
    outdir = os.path.join(destbasedir, library.name)

    if not os.path.exists(outdir):
        os.mkdir(outdir)

    for name, resource in library.known_resources.iteritems():
        sourcepath = os.path.join(library.path, resource.relpath)
        dest = os.path.join(outdir, resource.relpath)
        destdirname = os.path.dirname(dest)
        if not os.path.exists(destdirname):
            os.mkdir(destdirname)
        _print("copy %s -> %s" % (sourcepath, dest))
        shutil.copyfile(sourcepath, dest)

def list_fanstatic():
    parser = argparse.ArgumentParser(description="Collect fanstatic resources and copy to destination directory.")
    parser.add_argument('-o', '--output-directory', default="fanstatic", 
        help="Set destination directory name. Default directory name is 'fanstatic'.")
    parser.add_argument('-l', '--library', nargs="*", 
        help="Specify copy library names. Accept multiple options.")
    parser.add_argument('--simulate', action='store_true', 
        help="Simulate collecting resources. Print resource paths and destination paths.")
    parser.add_argument('-c', '--config', 
        help="Sepcify pastedeploy config. List resources registered by add_fanstatic_resources directive.")

    args = parser.parse_args()
    if not args.simulate and not os.path.exists(args.output_directory):
        os.mkdir(args.output_directory)

    destbasedir = args.output_directory
    if args.config:
        lib_iter = iter_libraries_from_config(args.config)
    elif args.library:
        lib_iter = iter_libraries(args.library)
    else:
        lib_iter = iter_all_libraries()

    for library in lib_iter:
        if args.simulate:
            print_fanstatic_resources(destbasedir, library)
        else:
            copy_fanstatic_resources(destbasedir, library)

