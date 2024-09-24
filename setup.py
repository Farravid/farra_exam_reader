"""Python setup.py for farra_exam_reader package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("farra_exam_reader", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="farra_exam_reader",
    version=read("farra_exam_reader", "VERSION"),
    description="Awesome farra_exam_reader created by Farravid",
    url="https://github.com/Farravid/farra_exam_reader/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Farravid",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["farra_exam_reader = farra_exam_reader.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
