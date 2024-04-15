
"""
Module to expose more detailed version info for the installed `numpy`
"""
version = "2.0.0rc1"
__version__ = version
full_version = version

git_revision = "60e9e5fa574b8d5ddbd6791449368a17f5cced85"
release = 'dev' not in version and '+' not in version
short_version = version.split("+")[0]
