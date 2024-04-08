import importlib.metadata

try:
    __version__ = importlib.metadata.version("pieces")
except importlib.metadata.PackageNotFoundError:
    print("Could not find the 'pieces' package in the Python environment. Is it installed?")
    __version__ = "unknown"

