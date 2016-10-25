from .default import *

try:
    from .development import *
    print 'Development settings (development.py) have been found and imported'
except ImportError as e:
    from .production import *
    print 'Production settings (production.py) have been found and imported'
    print e
