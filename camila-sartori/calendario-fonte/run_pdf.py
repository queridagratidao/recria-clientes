import sys, importlib.util

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

lib = load("build-lib.py", "buildlib")
lib.build_calendar(sys.argv[1], sys.argv[2])
