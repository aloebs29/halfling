from pathlib import Path
from setuptools import setup

with open(Path(__file__).parent / "VERSION") as f:
    VERSION = f.read().strip()

with open(Path(__file__).parent / "README.md") as f:
    README = f.read()

setup(
    name="halfling",
    version=VERSION,
    description="Small, practical build and task automation system written in Python.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/aloebs29/halfling",
    author="Andrew Loebs",
    license="MIT",

    packages=["halfling"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "halfling = halfling.main:main",
        ]
    },
)
