## Copyright 2016-2019 Ray Holder
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
## http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.

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
