import os
import platform
from setuptools import setup
from setuptools.command.install import install

def create_file():
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    os.makedirs(desktop, exist_ok=True)
    file_path = os.path.join(desktop, "demo_warning.txt")
    with open(file_path, "w") as f:
        f.write("operation complete\n")

class RunInstallCommand(install):
    def run(self):
        create_file()
        install.run(self)

setup(
    name="malicious-demo",
    version="0.1",
    packages=["malicious_demo"],
    cmdclass={"install": RunInstallCommand},
)
