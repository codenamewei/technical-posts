from setuptools import find_packages
from setuptools import setup

with open("readme.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='facescan',
    version='0.0.1a0',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "ultralytics==8.0.188",
        "sahi==0.11.14",
        "facenet-pytorch==2.5.2",
        "torch==1.13.0",
        "torchvision==0.14.0"
    ],
    python_requires=">=3.10.0",
    url='None',
    license='AGPL',
    author='codenamewei',
    author_email='codenamewei@gmail.com',
    description='Your main project',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
