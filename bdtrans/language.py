"""
The languages code are defined here.
"""
import os

from bdtrans._global import _


class Code(object):
    zh = 'zh'
    en = 'en'
    de = 'de'
    it = 'it'
    cs = 'cs'
    jp = 'jp'
    th = 'th'
    ru = 'ru'
    pt = 'pt'
    el = 'el'
    nl = 'nl'
    pl = 'pl'
    hu = 'hu'
    yue = 'yue'
    wyw = 'wyw'
    kor = 'kor'
    fra = 'fra'
    spa = 'spa'
    ara = 'ara'
    bul = 'bul'
    est = 'est'
    dan = 'dan'
    fin = 'fin'
    rom = 'rom'
    slo = 'slo'
    swe = 'swe'
    cht = 'cht'
    vie = 'vie'


class SourceCode(Code):
    """ 
    Defines the source language code.
    """
    auto = 'auto'


class TargetCode(Code):
    """ 
    Defines the target language code.
    Notice that: Target language code cannot be auto.
    """
    pass


# Language List
LANGUAGES = {
    'zh':  _('Chinese'),
    'en':  _('English'),
    'jp':  _('Japanese'),
    'kor': _('Korean'),
    'fra': _('French'),
    'spa': _('Spanish'),
    'th':  _('Thai'),
    'ara': _('Arabic'),
    'ru':  _('Russian'),
    'pt':  _('Portuguese'),
    'de':  _('German'),
    'it':  _('Italian'),
    'el':  _('Greek'),
    'nl':  _('Dutch'),
    'pl':  _('Polish'),
    'bul': _('Bulgarian'),
    'est': _('Estonian'),
    'dan': _('Danish'),
    'fin': _('Finnish'),
    'cs':  _('Czech'),
    'rom': _('Romanian'),
    'slo': _('Slovenian'),
    'swe': _('Swedish'),
    'hu':  _('Hungarian'),
    'yue': _('Cantonese'),
    'vie': _('Vietnamese'),
    'wyw': _('Classical Chinese'),
    'cht': _('Traditional Chinese'),
    'auto':_('automatic')
}

DEFAULT_SOURCE_LANG = 'en'
DEFAULT_TARGET_LANG = 'zh'
