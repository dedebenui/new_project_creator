import argparse
import getpass
import os
import subprocess
from datetime import datetime
from os.path import join

from .constants import LICENSE, README, SETUP_CFG, SETUP_PY


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
