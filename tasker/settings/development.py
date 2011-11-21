from tasker.settings.common import *

INSTALLED_APPS += (
    'debug_toolbar',
)

try:
    from tasker.settings.local import *
except ImportError:
    pass
