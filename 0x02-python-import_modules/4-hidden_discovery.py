#!/usr/bin/python3
import importlib


def no_prefix(value):
    return not value.startswith("__")


if __name__ == "__main__":
    imported_module = importlib.import_module(
        name='hidden_4', package='hidden_4.pyc')
    names = list(filter(no_prefix, dir(imported_module)))
    for name in sorted(names):
        print(name)
