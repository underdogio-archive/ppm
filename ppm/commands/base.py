from __future__ import print_function

from pip.req import parse_requirements
import ordereddict


class BaseCommand(object):
    def _read_requirements(self, filename, session):
        requirements = parse_requirements(filename, session=session)
        return self._parse_requirements(requirements)

    def _parse_requirements(self, raw_requirements):
        return dict((req.name, req) for req in raw_requirements)

    def _update_requirements_file(self, filename, add_requirements=None, remove_requirements=None, session=None):
        print('Updating %s' % (filename, ))
        existing_requirements = self._read_requirements(filename, session)

        if remove_requirements:
            for name, _ in remove_requirements.iteritems():
                if name in existing_requirements:
                    del existing_requirements[name]

        if add_requirements:
            existing_requirements.update(add_requirements)

        existing_requirements = ordereddict.OrderedDict(sorted(existing_requirements.items(), key=lambda t: t[0]))
        with open(filename, 'w') as fp:
            for _, req in existing_requirements.iteritems():
                fp.write(self._requirement_line(req))
                fp.write('\r\n')

    def _requirement_line(self, req):
        if req.installed_version:
            return '%s==%s' % (req.name, req.installed_version)
        else:
            return '-e %s' % (req.link.url, )
