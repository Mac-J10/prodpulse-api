from setuptools import setup, find_packages
setup(
    name="prodpulse-api",
    version="0.1",
    packages=find_packages(),  # should include apps.authentication
    include_package_data=True,
)