import json

from bdtrans.baidu import Translate
from bdtrans.common import get_profile_path


translator = Translate()


def setup(appid, secretkey):
    config = {
        "APPID": appid,
        "SECRETKEY": secretkey
    }
    profile = get_profile_path()
    with open(profile, 'w') as f:
        json.dump(config, f)
        print('Setup successful!')
        print('Your profile is located at %s.' % profile)




def trans(words, source_lang=None, target_lang=None):
    if source_lang:
        translator.set_source(source_lang)
    if target_lang:
        translator.set_target(target_lang)

    result = translator.translate(words)
    print(result)

