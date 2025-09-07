from setuptools import setup, find_packages

setup(
    name="prodpulse-api",
    version="0.1.0",
    packages=find_packages(),
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