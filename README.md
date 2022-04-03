# Quick Data Visualization in Python ![GitHub](https://img.shields.io/github/license/b3nk4n/quick-data-visualization)

A demo project to compare various Python libraries to do quick data visualization.

## Getting started

### Prerequisites

You need to have [pyenv](https://github.com/pyenv/pyenv) and [pipenv](https://pipenv-fork.readthedocs.io/en/latest/) installed.

### Installation

First install all dependencies using the project's python version.

```bash
$ pipenv install --python 3.9.11
```

Optionally, then activate / deactivate the virtual environment using the following commands.

```bash
$ pipenv shell
$ pipenv --rm
```

### Usage

You can run any of the visualization examples, such as `tablulate_example.py` using the following command,
which will a help page with the available params.

```bash
(quick-data-visualization) $ pipenv run tabulate
```

## Covered libraries

- [python-tabulate](https://pypi.org/project/tabulate/)
- [uniplot](https://pypi.org/project/uniplot/)

## License

This work is published under [MIT][mit] License.

[mit]: https://github.com/b3nk4n/quick-data-visualization/blob/main/LICENSE