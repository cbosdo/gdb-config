import gdb
import sys
from os.path import expanduser

# Update module path.
dir_ = expanduser('~/.gdb/python')
if not dir_ in sys.path:
    sys.path.insert(0, dir_)

from xml2 import register
register (gdb.current_objfile ())
