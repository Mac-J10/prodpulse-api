from setuptools import setup, find_packages

setup(
    name="ProdPulseAPI",
    packages=find_packages(exclude=["tests*", "docs*", "scripts*", "configs*"]),
    version="0.1.0",
    include_package_data=True,
    install_requires=[],
    description="Core backend package for ProdPulse",
    author="Jack",
    author_email="jacksonjay916@email.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)