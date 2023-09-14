from setuptools import setup

setup(
    name="nc2csv",
    version="0.1.2",
    description="Dump NetCDF file to CSV",
    author="Stefan Codrescu",
    author_email="ssmmcc1@gmail.com",
    url="https://github.com/5tefan/nc2csv",
    packages=["nc2csv"],
    install_requires=[
        "Click",
        "xarray",
        "netcdf4",
    ],
    entry_points={
        "console_scripts": [
            "nc2csv=nc2csv.cli:cli",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
