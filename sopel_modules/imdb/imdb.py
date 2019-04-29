# coding=utf-8
# Copyright 2008, Sean B. Palmer, inamidst.com
# Copyright 2012, Elsie Powell, embolalia.com
# Copyright 2018, Rusty Bower, rustybower.com
# Licensed under the Eiffel Forum License 2.
from __future__ import unicode_literals, absolute_import, print_function, division

import re
import requests
from sopel.module import commands, example, rule
from sopel.config.types import StaticSection, ValidatedAttribute
from sopel.logger import get_logger
from sopel.tools import SopelMemory


LOGGER = get_logger(__name__)

yearfmt = re.compile(r'\(?(\d{4})\)?')
imdb_re = re.compile(r'.*(https?:\/\/(www\.)?imdb\.com\/title\/)(tt[0-9]+).*')


class IMDBSection(StaticSection):
    api_key = ValidatedAttribute('api_key', str, default='')


# Walk the user through defining variables required
def configure(config):
    config.define_section('imdb', IMDBSection, validate=False)
    config.imdb.configure_setting(
        'api_key',
        'Enter omdbapi.com API Key:'
    )


def setup(bot):
    bot.config.define_section('imdb', IMDBSection)
    if not bot.memory.contains('url_callbacks'):
        bot.memory['url_callbacks'] = SopelMemory()
    bot.memory['url_callbacks'][imdb_re] = imdb_re


def shutdown(bot):
    del bot.memory['url_callbacks'][imdb_re]


@commands('imdb', 'movie')
@example('.imdb ThisTitleDoesNotExist', '[Error] Movie not found!')
@example('.imdb Citizen Kane', '[Movie] Title: Citizen Kane | Year: 1941 | Rating: 8.3 | Tomatometer: 100% | Genre: Drama, Mystery | Plot: Following the death of a publishing tycoon, news reporters scramble to discover the meaning of his final utterance. | IMDB Link: http://imdb.com/title/tt0033467')
@example('.imdb Chuck', '[Series] Title: Chuck | Seasons: 5 | Year: 2007–2012 | Rating: 8.2 | Genre: Action, Comedy, Drama | Plot: When a twenty-something computer geek inadvertently downloads critical government secrets into his brain, the C.I.A. and the N.S.A. assign two age[…] | IMDB Link: http://imdb.com/title/tt0934814')
@example('.imdb Death Wish 1974', '[Movie] Title: Death Wish | Year: 1974 | Rating: 7.0 | Tomatometer: 65% | Genre: Action, Crime, Drama, Thriller | Plot: A New York City architect becomes a one-man vigilante squad after his wife is murdered by street punks in which he randomly goes out[…] | IMDB Link: http://imdb.com/title/tt0071402')
def imdb(bot, trigger):
    """
    Returns some information about a movie or series, like Title, Year, Rating, Genre and IMDB Link.
    """
    if bot.config.imdb.api_key is None or bot.config.imdb.api_key == '':
        return bot.reply("OMDb API key missing. Please configure this module.")

    if not trigger.group(2):
        return
    word = trigger.group(2).rstrip()
    params = {}

    # check to see if there is a year e.g. (2017) at the end
    last = word.split()[-1]
    yrm = yearfmt.match(last)
    if yrm is not None:
        params['y'] = yrm.group(1)
        word = ' '.join(word.split()[:-1])

    params['t'] = word
    bot.say(run_omdb_query(params, bot.config.core.verify_ssl, bot.config.imdb.api_key, True))


def run_omdb_query(params, verify_ssl, api_key, add_url=True):
    uri = "http://www.omdbapi.com/"
    if 'i' in params:
        data = requests.get(uri, params={'i': params['i'], 'apikey': api_key}, timeout=30, verify=verify_ssl)
    elif 'y' in params:
        data = requests.get(uri, params={'t': params['t'], 'y': params['y'], 'apikey': api_key}, timeout=30, verify=verify_ssl)
    else:
        data = requests.get(uri, params={'t': params['t'], 'apikey': api_key}, timeout=30, verify=verify_ssl)

    data = data.json()
    if data['Response'] == 'False':
        if 'Error' in data:
            message = '[Error] %s' % data['Error']
        else:
            LOGGER.info(
                'Got an error from the OMDb api, search parameters were %s; data was %s',
                str(params), str(data))
            message = '[Error] Got an error from OMDbapi'
    else:
        if data['Type'] == 'movie':
            message = '[Movie] Title: ' + data['Title']
        elif data['Type'] == 'series':
            message = '[Series] Title: ' + data['Title'] + \
                      ' | Seasons: ' + data['totalSeasons']
        elif data['Type'] == 'episode':
            parent = requests.get(uri, params={'i': data["seriesID"], 'apikey': api_key}, timeout=30, verify=verify_ssl)
            parent = parent.json()
            message = '[Episode] Title: ' + parent['Title'] + \
                      ' | Episode: ' + data['Title'] + \
                      ' (' + data['Season'] + 'x' + data['Episode'] + ')'

        message += ' | Year: ' + data['Year'] + \
                   ' | Rating: ' + data['imdbRating']
        for rating in data['Ratings']:
            if rating['Source'] == 'Rotten Tomatoes':
                message += ' | Tomatometer: ' + rating['Value']

        message += ' | Genre: ' + data['Genre'] + \
                   ' | Plot: {}'

        if add_url:
            message += ' | IMDB Link: http://imdb.com/title/' + data['imdbID']

        plot = data['Plot']
        if len(message.format(plot)) > 300:
            cliplen = 300 - (len(message) - 2 + 3)  # remove {} add […]
            plot = plot[:cliplen] + '[…]'
        message = message.format(plot)
    return message


@rule(imdb_re)
def imdb_url(bot, trigger, found_match=None):
    match = found_match or trigger

    if bot.config.imdb.api_key is None or bot.config.imdb.api_key == '':
        return bot.reply("OMDb API key missing. Please configure this module.")

    bot.say(run_omdb_query({'i': match.group(3)}, bot.config.core.verify_ssl, bot.config.imdb.api_key, False))


if __name__ == "__main__":
    from sopel.test_tools import run_example_tests
    run_example_tests(__file__)
