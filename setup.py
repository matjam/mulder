#!/usr/bin/env python
import mulder
from setuptools import setup, find_packages


with open("README.rst") as f:
    readme = f.read()


def install():

    setup(
        name="mulder",
        version=mulder.__version__,
        description="mulder website project",
        long_description=readme,
        author=mulder.__author__,
        license="MIT",
        platforms=["POSIX"],
        classifiers=[
            "Development Status :: 1 - Planning",
            "License :: OSI Approved :: MIT License",
            "Environment :: Console",
            "Operating System :: POSIX",
            "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
            "Framework :: Flask",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
        ],
        packages=find_packages(exclude=("tests",)),
        install_requires=[
            "Flask==1.1.2",
            "Flask-Migrate==2.5.3",
            "Flask-Script==2.0.6",
            "Flask-SQLAlchemy==2.4.1",
            "mysqlclient==1.4.6",
        ],
    )


if __name__ == "__main__":
    install()
