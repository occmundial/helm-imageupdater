# Helm image updater.

image-updater.py helps you to update the tag and repository of your values.yaml, you can integrate image-updater in your CI/CD pipeline to update the tag for new version or new repository.

# Requirements.

- Python > 3.10.
- Poetry.
- Docker (Only for build a container).

## Build.

 - **Install requirements:**

    `poetry install`
 
 ## Usage.

```bash
Usage: image-updater.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  image
  repository
  tag
```


### Set new tag.

```bash
./image-updater.py tag --file  ~/workspace/valuestest.yaml -v v1.0
```

### Set new repository.

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

### Set both values and repository.

    ./image-updater.py image --file  ~/workspace/valuestest.yaml -v v1.0 -r occmundial/vader --chart vader 

## Contributing.

See [CONTRIBUTING.md](CONTRIBUTING.md)

