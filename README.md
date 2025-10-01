[![Python Tests](https://github.com/sopel-irc/sopel-imdb/actions/workflows/python-tests.yml/badge.svg?branch=master)](https://github.com/sopel-irc/sopel-imdb/actions/workflows/python-tests.yml)
[![PyPI version](https://badge.fury.io/py/sopel-modules.imdb.svg)](https://badge.fury.io/py/sopel-modules.imdb)

**Maintainer:** [@RustyBower](https://github.com/rustybower)

**Important: This package is no longer updated.** Please install [sopel-imdb](https://pypi.org/project/sopel-imdb/) for use with Sopel 8.0 and higher.

# sopel-imdb
sopel-imdb is an movie lookup module for Sopel.

Since omdbapi put their API behind a free key, moving this module to a standalone repository and not in core

## Usage
```
# Get Movie info
.imdb Citizen Kane
[Movie] Title: Citizen Kane | Year: 1941 | Rating: 8.4 | Genre: Drama, Mystery | IMDB Link: http://imdb.com/title/tt0033467

# Get TV Series info
.imdb Chuck
[Series] Title: Chuck | Seasons: 5 | Year: 2007–2012 | Rating: 8.2 | Genre: Action, Comedy, Drama | IMDB Link: http://imdb.com/title/tt0934814
```

## Requirements
```
requests
sopel
```
