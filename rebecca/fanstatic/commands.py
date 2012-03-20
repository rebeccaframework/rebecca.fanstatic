import os
import shutil
import argparse
import pkg_resources

def iter_all_libraries():
    return pkg_resources.iter_entry_points('fanstatic.libraries')

def iter_libraries(eggspecs):
    for eggspec in eggspecs:
        dist, name = eggspec.split(":")
        ep = pkg_resources.get_entry_info(dist, 'fanstatic.libraries', name)
        yield ep

def list_fanstatic():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output-directory', default="fanstatic")
    parser.add_argument('-e', '--egg-spec', nargs="*")

    args = parser.parse_args()
    if not os.path.exists(args.output_directory):
        os.mkdir(args.output_directory)

    destbasedir = args.output_directory
    if not args.egg_spec:
        lib_iter = iter_all_libraries()
    else:
        lib_iter = iter_libraries(args.egg_spec)

    for ep in lib_iter:
        library = ep.load()
        copy_fanstatic_resources(destbasedir, library)

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
        print "copy %s -> %s" % (sourcepath, dest)
        shutil.copyfile(sourcepath, dest)
