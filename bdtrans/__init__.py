import json

import language
from baidu import Translate
from common import list_langs
from common import get_profile_path


translator = Translate()


def setup(appid, secretkey):
    config = {
        "APPID": appid,
        "SECRETKEY": secretkey,
    }
    profile = get_profile_path()
    with open(profile, 'w') as f:
        json.dump(config, f)
        print('Setup successful!')
        print('Your profile is located at %s.' % profile)
    setup_lang(language.DEFAULT_SOURCE_LANG, 
               language.DEFAULT_TARGET_LANG)


def setup_lang(source_lang, target_lang):
    profile = get_profile_path()
    with open(profile, 'w+') as f:
        config = json.load(f)
        config['SOURCE_LANG'] = source_lang
        config['TARGET_LANG'] = target_lang
        json.dump(config, f)
    print('The default source language is %s' % source_lang)
    print('The default target language is %s' % target_lang)
    print('You can use setup_lang(source_lang, target_lang) change it!')


def trans(words, source_lang=None, target_lang=None, 
          reverse=False, show_raw=False):
    if source_lang:
        translator.set_source(source_lang)
    if target_lang:
        translator.set_target(target_lang)
    if reverse:

    if show_raw:
        translator.set_raw(True)

    result = translator.translate(words)
    print(result)


def set_lang(source_lang, target_lang):
    translator.set_source(source_lang)
    translator.set_target(target_lang)



