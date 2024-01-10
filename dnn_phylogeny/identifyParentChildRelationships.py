import re
from os.path import abspath
from pathlib import Path
from re import Match

import click


def createAbspath(filepath: str | Path) -> Path:
    return Path(abspath(filepath))


def readFile(filepath: Path) -> str:
    with open(file=filepath, mode="r") as file:
        data: str = file.read()
        file.close()
    return data


def identifyTag(tag: str, data: str) -> bool:
    results: Match[str] | None = re.match(pattern=tag, string=data)
    return isinstance(results, Match)


@click.command()
@click.option(
    "filepath",
    "-f",
    "--file",
    type=Path,
    required=True,
    nargs=1,
    help="Path to file to read",
)
@click.option(
    "tag",
    "-t",
    "--tag",
    type=str,
    required=False,
    default="generated_from_trainer",
    nargs=1,
    help="Tag to search for in file",
)
def main(filepath: Path, tag: str) -> None:
    abspath: Path = createAbspath(filepath=filepath)

    data: str = readFile(filepath=abspath)

    print(identifyTag(tag=tag, data=data))


if __name__ == "__main__":
    main()
