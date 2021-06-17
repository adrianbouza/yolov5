from distutils.core import setup
from Cython.Build import cythonize
import numpy
from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = "yolov5"
DESCRIPTION = "YOLOV5 object detector"
URL = "https://github.com/adrianbouza/EfficientDet"
VERSION = "1.0.0"
setup(
    name=NAME,
    description=DESCRIPTION,
    url=URL,
    version=VERSION,
    packages=find_packages()
)
