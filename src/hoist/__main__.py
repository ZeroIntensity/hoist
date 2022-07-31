import click
from .server import Server


@click.command()
def main():
    server = Server()
    server.start()


if __name__ == "__main__":
    main()
