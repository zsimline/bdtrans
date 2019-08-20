import os
import sys
import gettext
import getpass
import platform


from bdtrans import conf
from bdtrans import language


def i18n():
    app_name = 'translate'
    local_dir = os.path.abspath("locale")
    gettext.bindtextdomain(app_name, local_dir)
    gettext.textdomain(app_name)
    return gettext.gettext


def check_upgrade():
    sys.exit(0)  # TODO


def check_platform():
    platform_ = platform.system() 
    if platform_ == 'Linux':
        return 'linux'
    if platform_ == 'Darwin':
        return 'macosx'
    if platform_ == 'Windows':
        return 'windows'
    return 'unkownOS'


def get_profile_path():
    platform = check_platform()
    username = getpass.getuser()
    return conf.PROFILE_PATH[platform] % username


def list_langs():
    langs = language.LANGUAGES
    print('------------------------------')
    for lang in langs:
        print('| {:<5}'.format(lang), end='')
        print('{:>5}'.format('-'), end='')
        print('{:\u3000>8} |'.format(langs[lang]))
    print('------------------------------')


def check_source_code(code):
    if hasattr(language.SourceCode, code):
        return True
    else:
        print(('\nInvalid source code!'))
        return False


def check_target_code(code):
    if hasattr(language.TargetCode, code):
        return True
    elif code=='auto':
        print('\nTarget code can not be auto!!!\n')
    else:
        print(('\nInvalid target code!'))
        return False
