# coding=utf-8
# Copyright 2008, Sean B. Palmer, inamidst.com
# Copyright 2012, Elsie Powell, embolalia.com
# Copyright 2018, Rusty Bower, rustybower.com
# Licensed under the Eiffel Forum License 2.
from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.config.types import StaticSection, ValidatedAttribute
from sopel.module import commands, example, NOLIMIT
from sopel.logger import get_logger

import requests

LOGGER = get_logger(__name__)


class IMDBSection(StaticSection):
    api_key = ValidatedAttribute('api_key', str, default='')


def setup(bot):
    bot.config.define_section('imdb', IMDBSection)


# Walk the user through defining variables required
def configure(config):
    config.define_section('imdb', IMDBSection, validate=False)
    config.imdb.configure_setting(
        'api_key',
        'Enter omdbapi.com API Key:'
    )


@commands('imdb')
@example('.imdb ThisTitleDoesNotExist', '[Error] Movie not found!')
@example('.imdb Citizen Kane', '[Movie] Title: Citizen Kane | Year: 1941 | Rating: 8.4 | Genre: Drama, Mystery | IMDB Link: http://imdb.com/title/tt0033467')
@example('.imdb Chuck', '[Series] Title: Chuck | Seasons: 5 | Year: 2007–2012 | Rating: 8.2 | Genre: Action, Comedy, Drama | IMDB Link: http://imdb.com/title/tt0934814')
def imdb(bot, trigger):
    """
    Returns some information about a movie or series, like Title, Year, Rating, Genre and IMDB Link.
    """
    if bot.config.imdb.api_key is None or bot.config.imdb.api_key is '':
        return bot.reply("OMDb API key missing. Please configure this module.")

    if not trigger.group(2):
        return

    # TODO - Take in an optional year parameter [Twin Peaks (1990-1991) vs Twin Peaks (2017)]
    word = trigger.group(2).rstrip()
    uri = 'https://www.omdbapi.com/'
    data = requests.get(uri, params={'t': word, 'apikey': bot.config.imdb.api_key}, timeout=30,
                        verify=bot.config.core.verify_ssl).json()

    if data['Response'] == 'False':
        if 'Error' in data:
            message = '[Error] %s' % data['Error']
        else:
            LOGGER.warning(
                'Got an error from the OMDb api, search phrase was %s; data was %s',
                word, str(data))
            message = '[Error] Got an error from OMDbapi'
    else:
        if data['Type'] == 'movie':
            message = '[Movie] Title: ' + data['Title'] + \
                      ' | Year: ' + data['Year'] + \
                      ' | Rating: ' + data['imdbRating'] + \
                      ' | Genre: ' + data['Genre'] + \
                      ' | IMDB Link: http://imdb.com/title/' + data['imdbID']
        elif data['Type'] == 'series':
            message = '[Series] Title: ' + data['Title'] + \
                      ' | Seasons: ' + data['totalSeasons'] + \
                      ' | Year: ' + data['Year'] + \
                      ' | Rating: ' + data['imdbRating'] + \
                      ' | Genre: ' + data['Genre'] + \
                      ' | IMDB Link: http://imdb.com/title/' + data['imdbID']
        else:
            return
    bot.say(message)
