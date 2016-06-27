activate_this='/home/loongf/instant/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this)

import sys
sys.path.insert(0,'/var/www/crimemap')
from crimemap import app as application
