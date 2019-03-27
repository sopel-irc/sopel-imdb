[![PyPI version](https://badge.fury.io/py/sopel-modules.imdb.svg)](https://badge.fury.io/py/sopel-modules.imdb)
[![Build Status](https://travis-ci.com/RustyBower/sopel-imdb.svg?branch=master)](https://travis-ci.com/RustyBower/sopel-imdb)
[![Coverage Status](https://coveralls.io/repos/github/RustyBower/sopel-imdb/badge.svg?branch=master)](https://coveralls.io/github/RustyBower/sopel-imdb?branch=master)

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
