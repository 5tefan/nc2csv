import xarray as xr


def to_csv(filename: str) -> str:
    with xr.open_dataset(filename) as nc_in:
        return nc_in.to_dataframe().to_csv()
