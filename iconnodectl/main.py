# -*- coding: utf-8 -*-

import argparse
import sys

from . import command


def main():
    handlers = command.init,

    parser = argparse.ArgumentParser(
        prog="iconnodectl", description="ICON Node Controller with docker")
    sub_parser = parser.add_subparsers(title="subcommands")

    common_parser = create_common_parser()

    for handler in handlers:
        handler(sub_parser, common_parser)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        return 1

    args = parser.parse_args()
    ret = args.func(args)
    print(ret)

    return ret


def create_common_parser() -> argparse.ArgumentParser:
    parent_parser = argparse.ArgumentParser(add_help=False)

    parent_parser.add_argument(
        "--verbose", "-v",
        required=False,
        action="store_true"
    )

    parent_parser.add_argument(
        "--yes", "-y",
        action="store_true",
        required=False,
        help="Automatic yes to prompts"
    )

    return parent_parser


if __name__ == "__main__":
    main()
