[![Python Tests](https://github.com/sopel-irc/sopel-imdb/actions/workflows/python-tests.yml/badge.svg?branch=master)](https://github.com/sopel-irc/sopel-imdb/actions/workflows/python-tests.yml)
[![PyPI version](https://badge.fury.io/py/sopel-modules.imdb.svg)](https://badge.fury.io/py/sopel-modules.imdb)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/sopel-irc/sopel-imdb.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/sopel-irc/sopel-imdb/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/sopel-irc/sopel-imdb.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/sopel-irc/sopel-imdb/context:python)

**Maintainer:** [@RustyBower](https://github.com/rustybower)

# sopel-imdb
sopel-imdb is an movie lookup module for Sopel.

Since omdbapi put their API behind a free key, moving this module to a standalone repository and not in core

## Usage
```
# Update your sopel config with the OMDb API key
[imdb]
api_key = 12345678
```

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
sopel>=8
```
