from oslo_config import cfg
from db_migration.db import migration

CONF = cfg.CONF


class MultipleModulesRevisions(Exception):
    def __init__(self, revision):
        self.revision = revision
        super(MultipleModulesRevisions, self).__init__(
            "Can't apply revision %s." % revision)


class DBCommand(object):

    def __init__(self):
        self.do_upgrade = migration.upgrade
        self.do_revision = migration.revision
        self.do_stamp = migration.stamp
        self.do_version = migration.version

    def upgrade(self):
        revision = CONF.command.revision
        if revision != "head":
            raise MultipleModulesRevisions(revision)
        self.do_upgrade(revision)

    def revision(self):
        self.do_revision(CONF.command.message, CONF.command.autogenerate)

    def stamp(self):
        self.do_stamp(CONF.command.revision)

    def version(self):
        self.do_version()


def add_command_parsers(subparsers):
    command_object = DBCommand()

    parser = subparsers.add_parser('upgrade')
    parser.set_defaults(func=command_object.upgrade)
    parser.add_argument('--revision', nargs='?')

    parser = subparsers.add_parser('stamp')
    parser.set_defaults(func=command_object.stamp)
    parser.add_argument('--revision', nargs='?')

    parser = subparsers.add_parser('revision')
    parser.set_defaults(func=command_object.revision)
    parser.add_argument('-m', '--message')
    parser.add_argument('--autogenerate', action='store_true')

    parser = subparsers.add_parser('version')
    parser.set_defaults(func=command_object.version)


command_opt = cfg.SubCommandOpt('command',
                                title='Command',
                                help='Available commands',
                                handler=add_command_parsers)

CONF.register_cli_opt(command_opt)


def main():
    import sys
    argv = sys.argv
    cfg.CONF(argv[1:], project='db_migration')
    print(CONF.command.func.__name__)
    CONF.command.func()



main()
