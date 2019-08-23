import sys

import prompt_toolkit
from prompt_toolkit.contrib import completers

from bdtrans import lib
from bdtrans import error
from bdtrans import deploy
from bdtrans._global import _


commands = ['/reve','/rule','/list','/help','/quit','/save','/setlang']
_file_history =  prompt_toolkit.history.FileHistory('history.txt')
_word_completer = completers.WordCompleter(commands, ignore_case=True)
_auto_suggest_from_history = prompt_toolkit.auto_suggest.AutoSuggestFromHistory()


def _print_help():
    print(_('\nThe following commands are supported：\n'))
    print(_('  /reve  \n\treverse source language and target language'))
    print(_('  /rule  \n\tshow current translation rules'))
    print(_('  /list  \n\tshow reference table of languages and exit'))
    print(_('  /help  \n\tprint help information'))
    print(_('  /quit  \n\tquit the program'))
    print(_('  /save filename \n\tsave translation results'))
    print(_('  /setlang source_lang target_lang'))
    print(_('  \tset the source and target languages'))
    print(_('\nTry to use =code to temporarily specify the target language,'
           '\nthen the source language is automatically specified as auto,'
           '\nfor example "=zh hello world"\n'))
    print(_('Want more help information? Please see:\n'
           'https://github.com/zsimline/immortal/blob/master/README.md\n'))


def _exit_cmdline():
    print(_('Good Bye!'))
    sys.exit(0)


def _check_command(user_input, error_code, nums):
    cmds = user_input.split(' ')
    try:
        if len(cmds) != nums:
            raise error.CommandError(error_code)
        for cmd in cmds:
            if cmd == '':
                raise error.CommandError(error_code)
        return cmds
    except error.CommandError:
        return False


def _set_lang(user_input):
    cmds = _check_command(user_input, 1101, 3)
    if cmds:
        lib.set_lang(cmds[1],cmds[2])


def _save_result(user_input):
    cmds = _check_command(user_input, 1102, 2)
    if cmds:
        lib.save(cmds[1])


def _execute_command(user_input):
    """
    Execute commands entered by users
    """
    command = user_input.split(' ')[0]
    if   command == '/reve':
        lib.reverse_lang()
    elif command == '/rule':
        lib.display_rules()
    elif command == '/list':
        lib.list_langs()
    elif command == '/help':
        _print_help()
    elif command == '/quit':
        _exit_cmdline()
    elif command == '/save':
        _save_result(user_input)
    elif command == '/setlang':
        _set_lang(user_input)
    elif command == '/':
        pass
    else:
        _print_help()


def _trans(first, user_input):
    result = None
    if first[0] == '=':
        # set the target language when the first character is =
        target_lang = user_input.split(' ')[0][1:]
        if lib.check_target_code(target_lang):
            words = ' '.join(user_input.split(' ')[1:])
            result = lib.trans(words, 'auto', target_lang)
    else:
        result = lib.trans(user_input)
    print(result)


def _select_operate(user_input):
    first = user_input.split(' ')[0]
    if first in commands:
        _execute_command(user_input)
    else:
        _trans(first, user_input)


def translate_loop():
    while True:
        try:
            user_input = prompt_toolkit.prompt(
                '> ',history=_file_history,
                auto_suggest=_auto_suggest_from_history,    
                completer=_word_completer)
            if user_input:
                _select_operate(user_input)
        except KeyboardInterrupt:
            print(_('To exit, type /quit'))
