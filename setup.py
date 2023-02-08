from setuptools import setup, find_packages
from pypi import name, executable_name

with open("README.md", "r") as fh:
    long_description = fh.read()
VERSION = "0.0.4"

setup(
    name=name,
    version=VERSION,
    description="A pypi auto scripts for Qpro*Template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="",
    author="RhythmLian",
    url="https://github.com/Rhythmicc/pypi",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=["Qpro"],
    entry_points={
        "console_scripts": [
            f"{executable_name} = pypi.main:main",
        ]
    },
)
