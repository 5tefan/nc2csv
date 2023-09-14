# nc2csv
# 
Dump NetCDF files to CSV.

Frustrated by `ncdump`? Try `nc2csv`!
- See your data in columns
- Easily inspect values across variables

## Examples

Save the csv to a file.
```bash
nc2csv file.nc > file.csv
```

Consider using with the excellent `xsv` utility: https://github.com/martijn/xsv

```bash
nc2csv file.nc | xsv table | less -S
```

Beautiful tables in your terminal!

