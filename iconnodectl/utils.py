# -*- coding: utf-8 -*-

__all__ = (
    "control_docker_compose",
    "remove_database",
    "get_docker_compose_filepath",
    "create_env_content",
    "update_env_file",
    "prompt_confirm",
    "print_verbose"
)

import os
import shutil
import functools

from .constants import *


def control_docker_compose(up: bool, path: str):
    if up:
        arguments = "up -d"
    else:
        arguments = "down"

    cmd: str = f"cd {DOCKER_SCRIPT_ROOT}; docker-compose -f {path} {arguments}"
    print(f"> {cmd}")

    # return os.system(cmd)


def remove_database(db_root: str):
    def onerror(*args):
        _path: str = args[0]
        print(f'Failed to remove "{_path}"')

    for basename in (".score_data", ".storage"):
        path: str = os.path.join(db_root, basename)
        shutil.rmtree(
            path,
            ignore_errors=False,
            onerror=functools.partial(onerror, path))


def get_docker_compose_filepath() -> str:
    return os.path.join(DOCKER_SCRIPT_ROOT, DOCKER_COMPOSE_FILENAME)


def create_env_content(filepath: str, docker_tag: str) -> str:
    lines = []

    with open(filepath, "rt") as f:
        for line in f:
            key, value = line.split("=")

            if key.startswith("TAG"):
                line: str = f"{key}={docker_tag}\n"

            lines.append(line)

    return "".join(lines)


def update_env_file(filepath: str, docker_tag: str):
    backup_path: str = f"{filepath}.bak"

    if os.path.isfile(backup_path):
        os.unlink(backup_path)

    os.rename(filepath, backup_path)

    content: str = create_env_content(backup_path, docker_tag)
    with open(filepath, "wt") as f:
        f.write(content)


def prompt_confirm(prompt: str, yes: bool) -> bool:
    if not yes:
        ret: str = input(f"> {prompt}")
        if ret == "n":
            return False

    return True


def print_verbose(msg: str, verbose: bool):
    if verbose:
        print(msg)
