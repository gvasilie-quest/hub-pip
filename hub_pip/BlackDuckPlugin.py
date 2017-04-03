
import os

from setuptools import Command

from docopt import docopt
from hub_pip.BlackDuckConfig import BlackDuckConfig
from hub_pip.BlackDuckCore import BlackDuckCore
from hub_pip.Main import main

from . import __version__ as VERSION


class BlackDuckCommand(Command):

    description = "Setuptools hub_pip"

    user_options = [
        ("Config=", "c", "Path to Black Duck Configuration file"),
        ("Hub-Url=", None, None),
        ("Hub-Username=", None, None),
        ("Hub-Password=", None, None),
        ("Hub-Proxy-Host=", None, None),
        ("Hub-Proxy-Port=", None, None),
        ("Hub-Proxy-Username=", None, None),
        ("Hub-Proxy-Password=", None, None),
        ("Hub-Timeout=", None, None),
        ("Hub-ScanTimeout=", None, None),
        ("Hub-CodeLocationName=", None, None),
        ("OutputDirectory=", None, None),
        ("RequirementsFile=", None, None),
        ("IgnoreFailure=", None, None),
        ("CreateFlatDependencyList=", None, None),
        ("CreateTreeDependencyList=", None, None),
        ("CreateHubBdio=", None, None),
        ("DeployHubBdio=", None, None),
        ("CheckPolicies=", None, None),

    ]

    options = None

    def initialize_options(self):
        """Set default values for options."""
        # Each user option must be listed here with their default value.
        self.Config = None
        self.Hub_Url = None
        self.Hub_Username = None
        self.Hub_Password = None
        self.Hub_Proxy_Host = None
        self.Hub_Proxy_Port = None
        self.Hub_Proxy_Username = None
        self.Hub_Proxy_Password = None
        self.Hub_Timeout = None
        self.Hub_ScanTimeout = None
        self.Hub_CodeLocationName = None
        self.OutputDirecotry = None
        self.RequirementsFile = None
        self.IgnoreFailure = None
        self.CreateFlatDependencyList = None
        self.CreateTreeDependencyList = None
        self.CreateHubBdio = None
        self.DeployHubBdio = None
        self.CheckPolicies = None

    def finalize_options(self):
        self.options = {
            '-c': self.Config,
            '--Config': self.Config,
            '--Hub-Url': self.Hub_Url,
            '--Hub-Username': self.Hub_Username,
            '--Hub-Password': self.Hub_Password,
            '--Hub-Proxy-Host': self.Hub_Proxy_Host,
            '--Hub-Proxy-Port': self.Hub_Proxy_Port,
            '--Hub-Proxy-Username': self.Hub_Proxy_Username,
            '--Hub-Proxy-Password': self.Hub_Proxy_Password,
            '--Hub-Timeout': self.Hub_Timeout,
            '--Hub-ScanTimeout': self.Hub_ScanTimeout,
            '--Hub-CodeLocationName': self.Hub_CodeLocationName,
            '--OutputDirecotry': self.OutputDirecotry,
            '--RequirementsFile': self.RequirementsFile,
            '--IgnoreFailure': self.IgnoreFailure,
            '--CreateFlatDependencyList': self.CreateFlatDependencyList,
            '--CreateTreeDependencyList': self.CreateTreeDependencyList,
            '--CreateHubBdio': self.CreateHubBdio,
            '--DeployHubBdio': self.DeployHubBdio,
            '--CheckPolicies': self.CheckPolicies,
            '<hub_config.ini>': self.Config
        }

    def run(self):
        """Run command."""
        main(self.options)
        """
        raise_on_fail = self.raise_on_matching_fail

        # The user's project's artifact and version
        project_name = self.distribution.get_name()
        project_version = self.distribution.get_version()

        self.config.project_name = project_name
        self.config.project_version_name = project_version

        core = BlackDuckCore(self.config)
        tree = core.run()
        """


def string_to_boolean(string):
    if string == True:
        return True
    if string == False:
        return False
    if string == "True":
        return True
    elif string == "False":
        return False
    else:
        raise ValueError
