# pylint: disable=missing-docstring
import argparse
import unittest
from pathlib import Path

from handsdown.cli_parser import (
    CLINamespace,
    abs_path,
    dir_abs_path,
    existing_dir_abs_path,
    git_repo,
    parse_args,
)


class TestCLIParser(unittest.TestCase):
    def test_git_repo(self):
        self.assertEqual(
            git_repo("git@github.com:myuser/project.git"),
            "https://github.com/myuser/project/",
        )
        self.assertEqual(
            git_repo("https://github.com/myuser/project.git"),
            "https://github.com/myuser/project/",
        )
        self.assertEqual(
            git_repo("https://github.com/myuser/project"),
            "https://github.com/myuser/project/",
        )
        with self.assertRaises(argparse.ArgumentTypeError):
            git_repo("https://test.test")

    def test_abs_path(self):
        self.assertTrue(abs_path(Path("test.py").as_posix()).absolute())

    def test_dir_abs_path(self):
        self.assertTrue(dir_abs_path(Path(__file__).parent.as_posix()).absolute())
        self.assertTrue(dir_abs_path(Path("/non/existing").as_posix()).absolute())

        with self.assertRaises(argparse.ArgumentTypeError):
            dir_abs_path(Path(__file__).as_posix())

    def test_existing_dir_abs_path(self):
        self.assertTrue(existing_dir_abs_path(Path(__file__).parent.as_posix()).absolute())

        with self.assertRaises(argparse.ArgumentTypeError):
            self.assertTrue(existing_dir_abs_path(Path("/non/existing").as_posix()).absolute())

        with self.assertRaises(argparse.ArgumentTypeError):
            existing_dir_abs_path(Path(__file__).as_posix())

    def test_parse_args(self):
        self.assertIsInstance(parse_args([]), CLINamespace)

    def test_get_source_code_url(self):
        namespace = parse_args([])
        assert namespace.get_source_code_url() == ""

        namespace.branch = "master"
        assert namespace.get_source_code_url() == ""

        namespace.source_code_url = "path/"
        assert namespace.get_source_code_url() == "path/blob/master/"

        namespace.source_code_url = "https://github.com/author/repo"
        namespace.branch = "main"
        assert namespace.get_source_code_url() == "https://github.com/author/repo/blob/main/"

        namespace.source_code_url = ""
        assert namespace.get_source_code_url() == ""
