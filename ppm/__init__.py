__all__ = [
    'main',
]

from pip import (
    main,
    commands_dict
)

from ppm.commands import register_commands

register_commands(commands_dict)
