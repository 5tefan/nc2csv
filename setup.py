from setuptools import setup

setup(
    name="nccsv",
    version="0.1.0",
    description="Dump NetCDF file to CSV",
    author="Stefan Codrescu",
    author_email="ssmmcc1@gmail.com",
    url="https://github.com/5tefan/nccsv",
    py_modules=["nccsv"],
    include_package_data=True,
    install_requires=[
        "Click",
        "xarray",
        "netcdf4",
    ],
    entry_points={
        "console_scripts": [
            "nccsv=nccsv.cli:cli",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
