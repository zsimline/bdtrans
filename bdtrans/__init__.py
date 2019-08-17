import os

from bdtrans.baidu import Translate
from bdtrans.common import list_langs
from bdtrans.common import get_profile_path
from bdtrans.deploy import initialize_app
from bdtrans.deploy import change_appinfo
from bdtrans.deploy import change_lang


__version__ = 'v1.0'
__all__  = ['trans']


_translator = None
_profile = get_profile_path()


def set_lang(source_lang, target_lang):
    if common.check_source_code(source_lang):
        _translator.set_source(source_lang)
    if common.check_target_code(target_lang):
        _translator.set_target(target_lang)


def reverse_lang():
    _translator.reverse_lang()


def display_rules():
    rules = _translator.get_rules()
    print('source language: %s' % rules[0])
    print('target language: %s' % rules[1])


def trans(words, source_lang=None, target_lang=None, 
          reverse=False, show_raw=False):
    if words == '':
        return 'Translation content cannot be empty！'
    result = _translator.translate(
        words, source_lang, target_lang, reverse, show_raw)
    return result


if os.path.isfile(_profile):
    _translator = Translate()
else:
    initialize_app()
    _translator = Translate()

