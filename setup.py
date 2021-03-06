"""
Example setup.py implementation where the required packages as defined in requirements.txt are installed when 
`$ python setup.py install` is run.
`$ python setup.py develop` to allow changes to code without having to rerun install.
`$ python setup.py test` to run the test suite to ensure things are working properly.

For pytest to work through `setup.py test`, also create a setup.cfg containing:
[aliases]
test=pytest
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
    # For pytest to work correctly
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
