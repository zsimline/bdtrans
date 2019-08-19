import os
import json

from bdtrans import model
from bdtrans import deploy
from bdtrans import common


_translator = None
_trans_hisory = {}
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


def trans(words, source_lang=None, target_lang=None, reverse=False):
    if words == '':
        return 'Translation content cannot be empty！'
    result = _translator.translate(words, source_lang, target_lang, reverse)
    if result:
        _record_words(words, result)
        return result


def _record_words(source, result):
    _trans_hisory[source] = result


def save(filename='output'):
    try:
        with open('%s.%s' % (filename,'txt'), 'w') as f:
            f.write('\n'.join(_trans_hisory))
        with open('%s.%s' % (filename,'json'), 'w') as f:
            json.dump(_trans_hisory, f, ensure_ascii=False)
        return True
    except Exception :
        return False


if os.path.isfile(_profile):
    _translator = model.Translate()
else:
    deploy.initialize_app()
    _translator = model.Translate()

