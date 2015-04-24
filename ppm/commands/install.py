import os

from pip.commands.install import InstallCommand as PipInstallCommand

from ppm.commands.base import BaseCommand


class InstallCommand(PipInstallCommand, BaseCommand):
    def __init__(self, *args, **kwargs):
        super(InstallCommand, self).__init__(*args, **kwargs)

        self.cmd_opts.add_option(
            '-s', '--save',
            action='store_true',
            dest='save_installed',
            default=False,
            help='Update requirements.txt after installing'
        )

        self.cmd_opts.add_option(
            '--save-file',
            dest='save_file',
            default='requirements.txt',
            help='requirements file to update when using --save option',
            metavar='file'
        )

    def run(self, options, args):
        result = super(InstallCommand, self).run(options, args)

        if options.save_installed and result.requirements.keys():
            here = os.getcwd()
            requirements_file = os.path.abspath(os.path.join(here, options.save_file))
            requirements = self._parse_requirements(result.requirements.values())
            self._update_requirements_file(requirements_file, add_requirements=requirements, session=result.session)
        return result
