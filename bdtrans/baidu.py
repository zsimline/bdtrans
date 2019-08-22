import os
import time
import json

from bdtrans import model
from bdtrans import deploy
from bdtrans import common


_translator = None
_ = common.i18n()
_trans_hisory = {}
_profile = common.get_profile_path()


def display_rules():
    """
    Display current translation rules.
    """
    rules = _translator.get_rules()
    print('current source language: %s' % rules[0])
    print('current target language: %s' % rules[1])


def set_lang(source_lang, target_lang):
    """
    Setting source language code and target language code,
    the program will validate the user-specified language code.
    
    Args:
        source_lang
            source language code
        target_lang
            target language code
    """
    if common.check_source_code(source_lang):
        _translator.set_source(source_lang)
    if common.check_target_code(target_lang):
        _translator.set_target(target_lang)


def _record_words(source, result):
    """
    After each successful translation, the program
    will records the translation results.
    """
    _trans_hisory[source] = result


def reverse_lang():
    """
    Reverse translation rules and display 
    rules after inversion.
    """
    _translator.reverse_lang()
    display_rules()


def save(file_name):
    """
    Save translation results.
    Args:
        file_name
            The output file you must specified   
    
    The translation results will be saved in two formats.
    One is plain text format containing only the target language
    for translation. The other is JSON format that contains both
    source and target languages.
    """
    try:
        with open('%s.%s' % (file_name,'txt'), 'w') as f:
            f.write('\n'.join(_trans_hisory))
        with open('%s.%s' % (file_name,'json'), 'w') as f:
            json.dump(_trans_hisory, f, ensure_ascii=False)
        print('Save translation results successfully！')
        print('TEXT file is stored in %s' % '%s.%s' % (file_name,'txt'))
        print('JSON file is stored in %s' % '%s.%s' % (file_name,'json'))
    except Exception as e:
        print('Save translation results failed! %s' % e)


def trans(words, source_lang=None, target_lang=None, reverse=False):
    """
    Translate sentences, returns the translation result.
    Args:
        words  sentences you want to translate（unnullable string）
        source_lang  source language code, only in this translation.
        target_lang  target language code, only in this translation.
        reverse  whether to reverse the rules of translation.
    """
    if words == '':
        return 'Translation content cannot be empty！'
    result = _translator.translate(words, source_lang, target_lang, reverse)
    if result:
        # record translation information after each successful translation
        _record_words(words, result)
        return result
    else:
        return ''


def io_trans(input_file, output_file=None, quiet=False):
    """
    Translation from Documents.

    Args:
        input_file
            You should specify an input file, the program will
            read sentences from the file you specify.
        output_file
            If the output file is specified, the program saves
            the translation results in the output file.
        quiet
            If you don't want to display information on the console,
            please set quiet to True.
    """
    lines = None
    results = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
    print('%s lines in total' % len(lines))
    for i in range(1, len(lines)):
        print('current line: %s\r' % i, end='')
        if lines[i] == '\n':
            continue
        result = trans(lines[i])
        results.append(result)
        if not quiet:
            print(result)
        time.sleep(1)
    if output_file:
        with open(output_file, 'w') as f:
            f.write('\n'.join(results))
    print('\nAll lines have been translated.')


if not os.path.isfile(_profile):
    # Initialize APP for first use
    deploy.initialize_app()

_translator = model.Translate()
