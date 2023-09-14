import click

from .nc2csv import to_csv


@click.command()
@click.argument(
    "filename", type=click.Path(exists=True, dir_okay=False, file_okay=True)
)
def cli(filename) -> None:
    """
    Dump a NetCDF file to CSV
    """
    click.echo(to_csv(filename))


if __name__ == "__main__":
    cli()
