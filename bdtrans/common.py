import os
import sys
import gettext
import getpass
import platform

from bdtrans import language


_PROFILE_PATH = {
    'linux': '/home/%s/.bdtrans',
    'macosx': '/Users/%s/.bdtrans',
    'windows': 'C:/Users/%s/AppData/Local/.bdtrans',
    'unknowOS': './.bdtrans'
}


def i18n():
    app_name = 'translate'
    local_dir = os.path.abspath("locale")
    gettext.bindtextdomain(app_name, local_dir)
    gettext.textdomain(app_name)
    return gettext.gettext


def check_upgrade():
    """
    Detection program update.
    """
    sys.exit(0)  # TODO


def check_platform():
    """
    Return the Operating System used by the user.
    """
    platform_ = platform.system() 
    if platform_ == 'Linux':
        return 'linux'
    if platform_ == 'Darwin':
        return 'macosx'
    if platform_ == 'Windows':
        return 'windows'
    return 'unkownOS'


def get_profile_path():
    """
    Get the program configuration file path
    """
    platform = check_platform()
    username = getpass.getuser()
    return _PROFILE_PATH[platform] % username


def list_langs():
    """
    Print Language List.
    """
    langs = language.LANGUAGES
    print('------------------------------')
    for lang in langs:
        print('| {:<5}'.format(lang), end='')
        print('{:>5}'.format('-'), end='')
        print('{:\u3000>8} |'.format(langs[lang]))
    print('------------------------------')


def check_source_code(code):
    """
    Checking the source language code.
    """
    if hasattr(language.SourceCode, code):
        return True
    else:
        print(('\nInvalid source code!'))
        return False


def check_target_code(code):
    """
    Checking the target language code.
    """
    if hasattr(language.TargetCode, code):
        return True
    elif code=='auto':
        print('\nTarget code can not be auto!!!\n')
    else:
        print(('\nInvalid target code!'))
        return False
