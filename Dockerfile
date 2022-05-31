FROM python:3.10.4-bullseye as builder

WORKDIR /code
COPY ./poetry.lock  /code/poetry.lock
COPY ./pyproject.toml /code/pyproject.toml
RUN apt update && apt install -y curl tree
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN $HOME/.poetry/bin/poetry config virtualenvs.create false \
  && $HOME/.poetry/bin/poetry install --no-interaction --no-ansi
RUN pip install pyinstaller
COPY image-updater.py .
RUN pyinstaller --clean --onefile image-updater.py

FROM debian

WORKDIR /code
COPY --from=builder /code/dist/image-updater /usr/bin/image-updater





