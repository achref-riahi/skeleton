# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

from setuptools import find_packages, setup

from skeleton.const import __version__

setup(
    name="skeleton",
    version=__version__,
    license='MIT License',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "skeleton_web=skeleton.web.main:main"
        ]
    },
    scripts=['bin/skeleton_worker'],
    zip_safe=False,
    extras_require={
        'worker': ["celery", "redis"],
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
