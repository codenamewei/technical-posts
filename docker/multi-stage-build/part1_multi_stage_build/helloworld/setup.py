from setuptools import find_packages
from setuptools import setup

with open("readme.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='helloworld',
    version='0.0.1',
    install_requires=['numpy>1.21'],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
    url='https://github.com/your-name/your_app',
    license='MIT',
    author='Your NAME',
    author_email='your@email.com',
    description='Your main project',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ]
)
