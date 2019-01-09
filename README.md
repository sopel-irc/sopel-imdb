[![PyPI version](https://badge.fury.io/py/sopel-modules.movie.svg)](https://badge.fury.io/py/sopel-modules.movie)
[![Build Status](https://travis-ci.org/RustyBower/sopel-movie.svg?branch=master)](https://travis-ci.org/RustyBower/sopel-movie)
[![Coverage Status](https://coveralls.io/repos/github/RustyBower/sopel-movie/badge.svg?branch=master)](https://coveralls.io/github/RustyBower/sopel-movie?branch=master)

# sopel-movie
sopel-movie is an movie lookup module for Sopel.

Since omdbapi put their API behind a free key, moving this module to a standalone repository and not in core

## Usage
```
# Gets movie info
.movie Citizen Kane
[MOVIE] Title: Citizen Kane | Year: 1941 | Rating: 8.4 | Genre: Drama, Mystery | IMDB Link: http://imdb.com/title/tt0033467
```

## Requirements
#### Ubuntu Requirements
```
apt install enchant
```
#### Python Requirements
```
requests
sopel
```
