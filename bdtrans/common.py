import os
import sys
import gettext
import getpass
import platform

import language
from conf import PROFILE_PATH


def i18n():
    app_name = 'translate'
    local_dir = os.path.abspath("locale")
    gettext.bindtextdomain(app_name, local_dir)
    gettext.textdomain(app_name)
    return gettext.gettext


def check_upgrade():
    sys.exit()  # TODO


def check_platform():
    return dict(
        linux = platform.system() == 'Linux',
        macosx = platform.system() == 'Darwin',
        windows = platform.system() == 'Windows'
    )


def get_current_user():
    username = getpass.getuser()
    return username


def get_profile_path():
    platform = check_platform()
    username = get_current_user()
    if platform['linux']:
        return PROFILE_PATH['linux'] % username
    if platform['macosx']:
        return PROFILE_PATH['macosx'] % username
    if platform['windows']:
        return PROFILE_PATH['windows'] % username
    return PROFILE_PATH['unknowos'] % username


def list_langs():
    langs = language.LANGUAGES
    print('------------------------------')
    for lang in langs:
        print('| {:<5}'.format(lang), end='')
        print('{:>5}'.format('-'), end='')
        print('{:\u3000>8} |'.format(langs[lang]))
    print('------------------------------')

