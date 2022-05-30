# Helm image updater



# Requirements

- Python > 3.10.
- Poetry.
- Docker (Only for build a container).

## Build

 - **Install requirements:**

    `poetry install`
 ## Run

```bash
Usage: image-updater.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  image
  repository
  tag
```


## Set new tag.

```bash
./image-updater.py tag --file  ~/workspace/valuestest.yaml -v v1.0
```

## Set new repository.

```bash
./image-updater.py repository --file  ~/workspace/valuestest.yaml -r occmundial/api-vader
```

If you have two charts or more in the same values.yaml, you can use `--chart [chartname]` to set new version or new repository.

```bash
./image-updater.py repository --file  ~/workspace/valuestest.yaml -r occmundial/api-vader --chart vader.
```
```bash
./image-updater.py tag --file  ~/workspace/valuestest.yaml -v v1.0 --chart vader
```

## Set both values and repository

    ./image-updater.py image --file  ~/workspace/valuestest.yaml -v v1.0 -r occmundial/vader --chart vader 

## Contributing

See [CONTRIBUTING.md]()

