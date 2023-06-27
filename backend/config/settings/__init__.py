from .base import *

env_name = os.getenv('ENV_NAME', 'local')

if env_name == 'production':
    from .prod import *
elif env_name == 'development':
    from .stage import *
else:
    from .local import *