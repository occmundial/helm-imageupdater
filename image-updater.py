#!/usr/bin/python3
from types import NoneType
import yaml
import click


@click.group()
def cli():
    pass


@click.option("-r", "--repository", help="New repository to set in values.yaml")
@click.option("-f", "--file", help="Path for values.yaml", required=True)
@click.option("-v", "--version", help="New version to set in values.yaml")
@click.option("--chart", help="Chart to replace tag")
@click.command()
def image(version, repository, file, chart):
    try:
        values_file = file_loader(file)
        if isinstance(version, NoneType) and isinstance(repository, NoneType):
            print("Should set a value for version or/and repository")
        if chart:
            if isinstance(version, str):
                if version != values_file[f"{chart}"]["image"]["tag"]:
                    values_file[f"{chart}"]["image"]["tag"] = version
                    file_saver(file, values_file)
                    print(
                        f"Version {version} has been setted successfully in the chart {chart}"
                    )
                elif version == values_file[f"{chart}"]["image"]["tag"]:
                    print(f"New version { version } is the same in the values.yaml")
            if isinstance(repository, str):
                if repository != values_file[f"{chart}"]["image"]["repository"]:
                    values_file[f"{chart}"]["image"]["repository"] = repository
                    file_saver(file, values_file)
                    print(
                        f"Version {repository} has been setted successfully in the chart {chart}"
                    )
                elif repository == values_file[f"{chart}"]["image"]["repository"]:
                    print(
                        f"New repository { repository } is the same in the values.yaml for the chart {chart}"
                    )
        if not chart:
            if isinstance(version, str):
                if version != values_file["image"]["tag"]:
                    values_file["image"]["tag"] = version
                    file_saver(file, values_file)
                    print(f"Version {version} has been setted successfully.")
                elif version != values_file["image"]["tag"]:
                    print(f"New version { version } is the same in the values.yaml")
            if isinstance(repository, str):
                if repository != values_file["image"]["repository"]:
                    values_file["image"]["repository"] = repository
                    file_saver(file, values_file)
                    print(f"Repository {repository} has been setted successfully.")
                elif repository == values_file["image"]["repository"]:
                    print(
                        f"New repository { repository } is the same in the values.yaml."
                    )
    except:
        print("An Exception occurred")


def file_loader(filepath):
    with open(filepath, "r") as f:
        data = yaml.full_load(f)
    return data


def file_saver(filepath, values):
    with open(filepath, "w") as f:
        data = yaml.dump(values, f)
    return data


@click.option(
    "-v", "--version", help="New version to set in values.yaml", required=True
)
@click.option("-f", "--file", help="Path for values.yaml", required=True)
@click.option("--chart", help="Chart to replace tag")
@click.command()
def tag(version, file, chart):
    try:
        values_file = file_loader(file)

        if chart:
            if version != values_file[f"{chart}"]["image"]["tag"]:
                values_file[f"{chart}"]["image"]["tag"] = version
                file_saver(file, values_file)
                print(
                    f"Version {version} has been setted successfully in the chart {chart}"
                )
            elif version == values_file[f"{chart}"]["image"]["tag"]:
                print(f"New version { version } is the same in the values.yaml")
        if not chart:
            if version != values_file["image"]["tag"]:
                values_file["image"]["tag"] = version
                file_saver(file, values_file)
                print(f"Version {version} has been setted successfully.")
            elif version != values_file["image"]["tag"]:
                print(f"New version { version } is the same in the values.yaml")
    except Exception as e:
        print(f"An error occurred {e}")


@click.option(
    "-r", "--repository", help="New repository to set in values.yaml", required=True
)
@click.option("-f", "--file", help="Path for values.yaml", required=True)
@click.option("--chart", help="Chart to replace tag")
@click.command()
def repository(repository, file, chart):
    try:
        values_file = file_loader(file)
        if chart:
            if repository != values_file[f"{chart}"]["image"]["repository"]:
                values_file[f"{chart}"]["image"]["repository"] = repository
                file_saver(file, values_file)
                print(values_file[f"{chart}"]["image"]["repository"])
                print(
                    f"Version {repository} has been setted successfully in the chart {chart}"
                )
            elif repository == values_file[f"{chart}"]["image"]["repository"]:
                print(
                    f"New repository { repository } is the same in the values.yaml for the chart {chart}"
                )
        if not chart:
            if repository != values_file["image"]["repository"]:
                values_file["image"]["repository"] = repository
                file_saver(file, values_file)
                print(f"Repository {repository} has been setted successfully.")
            elif repository == values_file["image"]["repository"]:
                print(f"New repository { repository } is the same in the values.yaml.")
    except Exception as e:
        print(f"An error occurred {e}")


cli.add_command(tag)
cli.add_command(repository)
cli.add_command(image)

if __name__ == "__main__":
    cli()
