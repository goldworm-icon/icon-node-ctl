# -*- coding: utf-8 -*-

__all__ = "init",

from .utils import *
from .constants import DB_ROOT


def init(sub_parser, common_parent_parser):
    _init_for_start(sub_parser, common_parent_parser)
    _init_for_stop(sub_parser, common_parent_parser)


def _init_for_start(sub_parser, parent_parser):
    start_parser = sub_parser.add_parser(
        name="start",
        parents=[parent_parser],
        help="Start service"
    )

    start_parser.add_argument(
        "--reset-db",
        action="store_true",
        required=False,
        help="Remove old database"
    )

    start_parser.add_argument(
        "--tag", "-t",
        type=str,
        required=False,
        default=None,
        help="docker tag"
    )

    start_parser.set_defaults(func=_start)


def _start(args) -> int:
    yes: bool = args.yes
    verbose: bool = args.verbose
    reset_db: bool = args.reset_db
    tag: str = args.tag

    prompt_confirm("Continue? [Y/n]", yes)

    print_verbose("Stopping service", verbose)
    filepath: str = get_docker_compose_filepath()
    control_docker_compose(up=False, path=filepath)

    if tag:
        filepath: str = get_docker_compose_filepath()
        print_verbose(f"Update env file: {filepath}", verbose)
        update_env_file(filepath, tag)

    if reset_db:
        print_verbose("Remove old databases", verbose)
        remove_database(DB_ROOT)

    print_verbose("Starting service", verbose)
    control_docker_compose(up=True, path=filepath)

    return 0


def _init_for_stop(sub_parser, parent_parser):
    stop_parser = sub_parser.add_parser(
        name="stop",
        parents=[parent_parser],
        help="Stop service"
    )

    stop_parser.set_defaults(func=_stop)


def _stop(args) -> int:
    yes: bool = args.yes
    verbose: bool = args.verbose

    prompt_confirm("Continue? [Y/n]", yes)

    filepath: str = get_docker_compose_filepath()
    print_verbose("Stopping service", verbose)
    control_docker_compose(up=False, path=filepath)

    return 0
