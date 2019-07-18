# -*- coding: utf-8 -*-

import unittest
import os

from iconnodectl.utils import *


class TestUtils(unittest.TestCase):
    def setUp(self) -> None:
        self.test_root: str = os.path.dirname(__file__)
        print(self.test_root)

    def test_get_env_content(self):
        env_filepath: str = os.path.join(self.test_root, "data", "env")
        print(env_filepath)
        content: str = create_env_content(env_filepath, "goldworm")

    def test_update_env_file(self):
        env_filepath: str = os.path.join(self.test_root, "data", "env")
        update_env_file(env_filepath, "haha")
