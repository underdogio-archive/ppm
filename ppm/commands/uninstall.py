import os

from pip.commands.uninstall import UninstallCommand as PipUninstallCommand
from pip.req import InstallRequirement, RequirementSet, parse_requirements

from ppm.commands.base import BaseCommand


class UninstallCommand(PipUninstallCommand, BaseCommand):
    def __init__(self, *args, **kwargs):
        super(UninstallCommand, self).__init__(*args, **kwargs)

        self.cmd_opts.add_option(
            '-s', '--save',
            action='store_true',
            dest='remove_uninstalled',
            default=False,
            help='Update requirements.txt after uninstalling'
        )

        self.cmd_opts.add_option(
            '--save-file',
            dest='save_file',
            default='requirements.txt',
            help='requirements file to update when using --save option',
            metavar='file'
        )

    def run(self, options, args):
        super(UninstallCommand, self).run(options, args)
        if not options.remove_uninstalled:
            return

        with self._build_session(options) as session:
            requirement_set = RequirementSet(
                build_dir=None,
                src_dir=None,
                download_dir=None,
                isolated=options.isolated_mode,
                session=session,
            )

            for name in args:
                requirement_set.add_requirement(
                    InstallRequirement.from_line(
                        name, isolated=options.isolated_mode
                    )
                )
            for filename in options.requirements:
                for req in parse_requirements(
                        filename,
                        options=options,
                        session=session):
                    requirement_set.add_requirement(req)

            if not requirement_set.has_requirements:
                return

            here = os.getcwd()
            requirements_file = os.path.abspath(os.path.join(here, options.save_file))
            requirements = self._parse_requirements(requirement_set.requirements.values())
            self._update_requirements_file(requirements_file, remove_requirements=requirements, session=session)
