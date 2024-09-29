from setuptools import setup, find_packages

setup(
    name="decorum_generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List dependencies here, e.g., 'requests>=2.25.1'
        "setuptools>=75.1.0",
    ],
    author="Yunfan Yang",
    author_email="yunfan.yang1@outlook.com",
    description="A decorum (board game) generator",
    url="https://github.com/cloudyyoung/decorum-generator",
)
