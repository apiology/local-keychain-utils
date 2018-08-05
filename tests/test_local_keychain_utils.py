#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `local_keychain_utils` package."""


import unittest
from click.testing import CliRunner

from local_keychain_utils import local_keychain_utils
from local_keychain_utils import cli


class TestLocal_keychain_utils(unittest.TestCase):
    """Tests for `local_keychain_utils` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'local_keychain_utils.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
