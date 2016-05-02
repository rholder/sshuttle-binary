import os
import zipimport
import zipfile

# are we inside of an egg?
EGG = None
try:
    EGG_PATH = os.path.dirname(__file__)
    EGG = zipfile.ZipFile(EGG_PATH, 'r')
except:
    pass

# monkey patch reading module code from raw files to read from inside zip
def readfile(name):
    full_path = name.replace('.', '/')
    return ZIP_IMPORT.get_source(full_path).encode("UTF8")

if EGG:
    # we're totally inside of an egg, patch patch patch
    import sshuttle.ssh
    ZIP_IMPORT = zipimport.zipimporter(EGG_PATH)
    sshuttle.ssh.readfile = readfile

# sshuttle main kicks off immediately on import
from sshuttle import __main__
