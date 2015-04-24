from ppm.commands import install, uninstall

commands = [
    install.InstallCommand,
    uninstall.UninstallCommand,
]


def register_commands(commands_dict):
    for command in commands:
        commands_dict[command.name] = command
