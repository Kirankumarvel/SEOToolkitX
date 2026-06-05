import click
from .core import generate_sitemap_from_file

@click.command()
@click.argument("input_file", type=click.Path(exists=True, dir_okay=False))
@click.option("--base-url", help="Base URL for relative paths (e.g., https://example.com)")
def main(input_file, base_url):
    """Generate XML sitemap(s) from a text file containing one URL per line."""
    generate_sitemap_from_file(input_file, base_url)

if __name__ == "__main__":
    main()