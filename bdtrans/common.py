from bdtrans import language
from bdtrans._global import _

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
        print(_('\nInvalid source code!'))
        return False


def check_target_code(code):
    """
    Checking the target language code.
    """
    if hasattr(language.TargetCode, code):
        return True
    elif code=='auto':
        print(_('\nTarget code can not be auto!!!\n'))
    else:
        print(_('\nInvalid target code!'))
        return False
