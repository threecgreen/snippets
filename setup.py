"""
Example setup.py implementation where the required packages as defined in requirements.txt are installed when 
`$ python setup.py install` is run.
"""
from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession
from os import path


here = path.abspath(path.dirname(__file__))

# parse_requirements() returns a generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt", session=PipSession())

# Create list of required packages
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="PACKAGE NAME",
    version="0.1.0",
    description="DESCRIPTION",
    author="Carter Green",
    license="MIT License",
    packages=find_packages(exclude=[".cache", ".idea", "doc", "tests"]),
    install_requires=reqs,
)
