# nccsv
# 
Dump NetCDF files to CSV.

Frustrated by `ncdump`? Try `nccsv`!
- See your data in columns
- Easily inspect values across variables

## Examples

Save the csv to a file.
```bash
nccsv file.nc > file.csv
```

Consider using with the excellent `xsv` utility: https://github.com/martijn/xsv

```bash
nccsv file.nc | xsv table | less -S
```

Beautiful tables in your terminal!

