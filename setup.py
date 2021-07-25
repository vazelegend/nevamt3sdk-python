from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyneva",
    version="0.4.0",
    description="Custom library for electricity meters Neva MT 3xx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nikita Nemirovsky",
    author_email="vaze.legend@gmail.com",
    url="https://github.com/vazelegend/pyneva",
    license="MIT",
    packages=find_packages(),
    install_requires=["pyserial"],
    python_requires=">=3.9",
)
