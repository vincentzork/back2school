import os

from .. import directories


def test_directories_exist():
    assert os.path.isdir(directories.base())
    assert os.path.isdir(directories.code())
    assert os.path.isdir(directories.tests())
    assert os.path.isdir(directories.data())
    assert os.path.isdir(directories.test_data())


def test_filenames():
    assert os.path.exists(directories.base("README.md"))
    assert os.path.exists(directories.code("__init__.py"))
    assert os.path.exists(directories.data("README.md"))
    assert os.path.exists(directories.tests("__init__.py"))
    assert os.path.exists(directories.test_data("README.md"))
