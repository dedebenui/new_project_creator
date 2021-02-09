import argparse
import os
from os.path import join
from datetime import datetime
import getpass
import subprocess

SETUP_CFG = """[metadata]
name = {name}
version = 0.0.1
description = please enter description
author = {username}
author_email = 
long_description = file: README.md
long_description_content_type = text/markdown
keywords = no keywords yet
license = MIT
classifiers =
    License :: OSI Approved :: MIT
    Programming Language :: Python :: 3

[options]
zip_safe = False
packages = find:
package_dir = 
    = src

[options.packages.find]
where = src

# [options.entry_points]
# console_scripts = 
#     {name} = 

"""

SETUP_PY = """from setuptools import setup

setup()
"""

LICENSE = """Copyright (c) {year} {username}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

README = ""


def create_parser():
    parser = argparse.ArgumentParser(
        description="Create a folder and set everything up for a new python project"
    )

    parser.add_argument("name", type=str, help="the project name")

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    name = args.name
    username = getpass.getuser()

    if os.path.exists(name):
        print(f"file/folder named {name} already exists, please choose another one.")

    os.mkdir(name)
    os.mkdir(join(name, "src"))
    os.mkdir(join(name, "src", name))

    with open(join(name, "setup.cfg"), "w") as file:
        file.write(SETUP_CFG.format(name=name, username=username))

    with open(join(name, "setup.py"), "w") as file:
        file.write(SETUP_PY)

    with open(join(name, "src", name, "__init__.py"), "w") as file:
        file.write("")

    with open(join(name, "LICENSE"), "w") as file:
        file.write(LICENSE.format(year=datetime.now().year, username=username))

    with open(join(name, "README.md"), "w") as file:
        file.write(README)

    subprocess.run(["code", name])


if __name__ == "__main__":
    main()
