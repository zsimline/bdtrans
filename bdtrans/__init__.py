import os
import json

from bdtrans import language
from bdtrans.baidu import Translate
from bdtrans import common


_translator = None
_profile = common.get_profile_path()

__all__=['trans']

def _setup(appid, secretkey, source_lang, target_lang):
    config = {
        "APPID": appid,
        "SECRETKEY": secretkey,
        "SOURCE_LANG": source_lang,
        "TARGET_LANG": target_lang
    }
    with open(_profile, 'w') as f:
        json.dump(config, f)
        print('\nSetup successful!')
        print('Your profile is located at %s.' % _profile)
        print('You can change the app info with change_appinfo(appid, secretkey)')
        print(('You can change the dafault source and target languages with '
               'change_lang(source_lang, target_lang)'))


def change_appinfo(appid, secretkey):
    config = None
    with open(_profile, 'r') as f:
        config = json.load(f)
    config['APPID'] = appid
    config['SECRETKEY'] = secretkey
    with open(_profile, 'w') as f:
        json.dump(config, f)
    print('Chagnge app info successful!')
    print('Your appid is => %s' % appid)
    print('Your secretkey is => %s' % secretkey)


def change_lang(source_lang, target_lang):
    config = None
    with open(_profile, 'r') as f:
        config = json.load(f)
    config['SOURCE_LANG'] = source_lang
    config['TARGET_LANG'] = target_lang
    with open(_profile, 'w') as f:
        json.dump(config, f)
    print('Chagnge source and target languages successful!')
    print('The default source language is => %s' % source_lang)
    print('The default target language is => %s' % target_lang)


def set_lang(source_lang, target_lang):
    _translator.set_source(source_lang)
    _translator.set_target(target_lang)


def trans(words, source_lang=None, target_lang=None, 
          reverse=False, show_raw=False):
    if words == '':
        print('Translation content cannot be empty！')
        return

    if source_lang:
        _translator.set_source(source_lang)
    if target_lang:
        _translator.set_target(target_lang)
    if reverse:
        _translator.reverse_lang()
    if show_raw:
        _translator.set_raw(True)

    result = _translator.translate(words)
    return result


def _initialize_app():
    print('At First, you need to configure the appid and secretkey.')
    print(('If you don\'t have an appid, plaese see '
           'https://github.com/zsimline/bdtrans/blob/master/README.md\n'))
    appid = ''
    while(True):
        appid = input('please enter your appid: ')
        if appid is not '':
            break
    secretkey = ''
    while(True):
        secretkey = input('please enter your secretkey: ')
        if secretkey is not '':
            break
    
    print(('\nAnd, it is recommended that you specify common '
           'source and target languages.\nThe following language '
           'codes are legal.\nIf you press Enter directly, the '
           'default source or target language will be specified.\n'))
    common.list_langs()

    while(True):
        source_lang = input('please enter a common source language code: ')
        if source_lang is '':
            source_lang = language.DEFAULT_SOURCE_LANG
            break
        elif common.check_source_code(source_lang):
            break
        else:
            continue
    while(True):
        target_lang = input('please enter a common target language code: ')
        if target_lang is '':
            target_lang =  language.DEFAULT_TARGET_LANG
            break
        elif common.check_target_code(target_lang):
            break
        else:
            continue
    
    _setup(appid, secretkey, source_lang, target_lang)


if os.path.isfile(_profile):
    _translator = Translate()
else:
    _initialize_app()
    _translator = Translate()
