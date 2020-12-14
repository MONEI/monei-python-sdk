# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

NAME = "monei"
VERSION = "0.1.5"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="MONEI PYTHON SDK",
    author="MONEI",
    author_email="hi@monei.net",
    url="",
    keywords=["monei", "monei pay", "pay", "payments", "payment gateway", "python", "sdk", "rest", "api"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    The MONEI SDK will allow you to interact with our API in an easy and predictable way.
    """
)
