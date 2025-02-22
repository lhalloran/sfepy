import os, glob

from .config import Config
from .version import __version__, in_source_tree, top_dir

data_dir = os.path.realpath(top_dir)
base_dir = os.path.dirname(os.path.normpath(os.path.realpath(__file__)))

def get_paths(pattern):
    """
    Get files/paths matching the given pattern in the sfepy source tree.
    """
    if not in_source_tree:
        pattern = '../' + pattern

    files = glob.glob(os.path.normpath(os.path.join(top_dir, pattern)))
    return files

def test(*args):
    """
    Run all the package tests.

    Equivalent to running ``pytest tests/`` in the base directory of
    SfePy. Allows an installed version of SfePy to be tested.

    To test an installed version of SfePy use

    .. code-block:: bash

       $ python -c "import sfepy; sfepy.test()"

    Parameters
    ----------
    *args : positional arguments
        Arguments passed to pytest.
    """
    import pytest  # pylint: disable=import-outside-toplevel

    path = os.path.join(os.path.split(__file__)[0], 'tests')
    pytest.main(args=[path] + list(args))
