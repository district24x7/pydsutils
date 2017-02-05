"""
Setup file

Tutorial:
http://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html
"""

# from distutils.core import setup  # this is for sdist
from setuptools import setup  # this is for bdist_wheel
import pydsutils

setup(
	name="pydsutils",
	version=pydsutils.__version__,
	author_email="district24x7@gmail.com",
	url="",
	packages=["pydsutils", ],
	license=""
)
