from setuptools import find_packages, setup

from skeleton.const import __version__

setup(
    name="skeleton",
    version=__version__,
    license='MIT License',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    zip_safe=False,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
