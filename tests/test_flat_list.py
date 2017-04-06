import os

import pip

from helper import *
from hub_pip.BlackDuckCore import BlackDuckCore
from hub_pip.FileHandler import get_file_path, FLAT_EXTENSION


class TestFlatList:

    def test_flat_render(self):
        config = get_config(VALID)
        items = [
            "configparser",
            "docopt",
            "requests",
            "six"
        ]
        self._test_flat(config, items)

    def test_flat_render_with_requirements(self):
        config = get_config(VALID)
        config.requirements_file_path = REQUIREMENTS
        items = [
            "Babel",
            "Delorean",
            "SQLAlchemy",
            "appdirs",
            "backports-abc",
            "botocore",
            "certifi",
            "collectd-gnocchi-status",
            "configparser",
            "docopt",
            "docutils",
            "environment-manager",
            "envmgr-cli",
            "future",
            "humanize",
            "hyml",
            "jmespath",
            "jsonpickle",
            "mjetplex",
            "numpy",
            "packaging",
            "progressbar2",
            "psutil",
            "psycopg2",
            "pyhomematic",
            "pymesh",
            "pynamodb",
            "pyparsing",
            "python-dateutil",
            "python-utils",
            "pytz",
            "pyvdp",
            "repoze.lru",
            "requests",
            "semver",
            "setuptools",
            "simplejson",
            "singledispatch",
            "six",
            "tabulate",
            "tornado",
            "tzlocal",
            "ustudio-hmac-tornado",
            "vceffort",
        ]
        self._test_flat(config, items)

    def _test_flat(self, config, items):

        config.flat_list = True
        flat_list_name = get_file_path(
            "hub-pip", config.output_path, FLAT_EXTENSION)

        core = BlackDuckCore(config)
        core.run()

        assert(os.path.exists(flat_list_name))

        flat_list = pip.req.parse_requirements(
            flat_list_name, session=pip.download.PipSession())

        count = 0
        for item in flat_list:
            count += 1
            assert(item.req.name in items)

        assert(count == len(items))

        cleanup(flat_list_name)
