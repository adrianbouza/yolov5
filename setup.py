from distutils.core import setup
from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = "yolov5"
DESCRIPTION = "YOLOV5 object detector"
URL = "https://github.com/adrianbouza/yolov5"
VERSION = "1.0.0"
setup(
    name=NAME,
    description=DESCRIPTION,
    url=URL,
    version=VERSION,
    packages=find_packages()
)
