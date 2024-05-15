from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in de_tinkerhub/__init__.py
from de_tinkerhub import __version__ as version

setup(
	name="community_management",
	version=version,
	description="App For Event Management",
	author="Aysha",
	author_email="ayshahakeem02@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
