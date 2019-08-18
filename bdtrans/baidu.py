import os

from bdtrans import model
from bdtrans import deploy
from bdtrans import common


_translator = None
_profile = common.get_profile_path()


def display_rules():
    rules = _translator.get_rules()
    print('current source language: %s' % rules[0])
    print('current target language: %s' % rules[1])


def set_lang(source_lang, target_lang):
    if common.check_source_code(source_lang):
        _translator.set_source(source_lang)
    if common.check_target_code(target_lang):
        _translator.set_target(target_lang)


def reverse_lang():
    _translator.reverse_lang()
    display_rules()


def trans(words, source_lang=None, target_lang=None, 
          reverse=False, show_raw=False):
    if words == '':
        return 'Translation content cannot be empty！'
    result = _translator.translate(
        words, source_lang, target_lang, reverse, show_raw)
    return result


if os.path.isfile(_profile):
    _translator = model.Translate()
else:
    deploy.initialize_app()
    _translator = model.Translate()
