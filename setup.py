#! /usr/bin/env python

try:
  import pyver
except ImportError:
  import pip
  pip.main (['install', 'pyver'])
  import pyver # pylint: disable=W0611

from setuptools import setup, find_packages

__version__, __version_info__ = pyver.get_version (
    pkg = "atomictempfile",
    public = True)

setup (
    name = "atomictempfile",
    version = __version__,
    description = "An atomic file write context manager",
    long_description = file ("README.rst").read (),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: "
        + "GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Utilities",
    ],
    keywords = "Atomic file write context manager",
    author = "J C Lawrence",
    author_email = "claw@kanga.nu",
    url = "https://github.com/clearclaw/atomictempfile",
    license = "LGPL v3.0",
    test_suite = "tests", 
    packages = find_packages (exclude = ["tests",]),
    package_data = {
    },
    zip_safe = True,
    install_requires = [line.strip ()
        for line in file ("requirements.txt").readlines ()],
    entry_points = {
        "console_scripts": [
        ],
    },
)
