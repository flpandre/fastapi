## Requirements

* [Warden](https://github.com/wardenenv/warden) 0.14.1 or later.

## Installation

* Clone this repository
* `warden sign-certificat app.fastapi.test`
* `warden env build`
* `warden env up`

### Accessing the Python container
`warden env exec web bash`

## Useful links
* Base url [https://app.fastapi.test](https://app.fastapi.test)
* Docs: [https://app.fastapi.test/docs](https://app.fastapi.test/docs)
* Redoc: [https://app.fastapi.test/redoc](https://app.fastapi.test/redoc)

## Basic Poetry Usage

We are using [Poetry](https://python-poetry.org/docs/) for package management. Any dependencies needed, please add to the `pyproject.toml` file.

* Add new package `poetry add package` or edit `pyproject.toml`
* Install dependencies: `poetry install`
* Update dependencies: `poetry update` / `poetry update package`
* Create lock file: `poetry lock`

Commit both `pyproject.toml` and `poetry.lock` files when updating dependencies. Similar to Composer.