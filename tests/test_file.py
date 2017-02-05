# -*- coding: utf-8 -*-
"""Unit tests of data util functions
"""
from pdb import set_trace as debug
import unittest
import pytest
import datetime
import pydsutils.file as F


def test_set_pathpath():
    dir = F.set_pythonpath(__file__, level=0, verbose=1)
    assert "/pydsutils/tests" in dir

    dir = F.set_pythonpath(__file__, level=1, verbose=1)
    assert "pydsutils" in dir
    assert "pydsutils/" not in dir
    assert "tests" not in dir
