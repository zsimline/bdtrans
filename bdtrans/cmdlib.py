import sys
sys.path.append('/home/mxsyx/desktop/bdtrans/')
sys.path.remove('/home/mxsyx/desktop/bdtrans/bdtrans')
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory 
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter

from bdtrans import baidu
from bdtrans import error
from bdtrans import deploy
from bdtrans import common


commands = ['/reve','/rule','/list','/help','/quit',
            '/save','/setlang','/changeinfo','/changelang']
_file_history = FileHistory('history.txt')
_auto_suggest_from_history = AutoSuggestFromHistory()
_word_completer = WordCompleter(commands, ignore_case=True)


def _print_help():
    print('\nThe following commands are supported：\n')
    print('  /reve  \n\treverse source language and target language')
    print('  /rule  \n\tshow current translation rules')
    print('  /list  \n\tprint supported language code')
    print('  /help  \n\tprint help information')
    print('  /quit  \n\tquit the program')
    print('  /save filename \n\tsave translation results')
    print('  /setlang source_lang target_lang')
    print('  \tset the source and target languages')
    print('  /changeinfo  \n\tchange app information in the configuration file')
    print('  /changelang  \n\tchange translation rules in the configuration file')
    print(('\nTry to use =code to temporarily specify the target language,'
           '\nthen the source language is automatically specified as auto,'
           '\nfor example "=zh hello world"\n'))
    print(('Want more help information? Please see:\n'
          'https://github.com/zsimline/immortal/blob/master/README.md\n'))


def _exit_cmdline():
    print('Good Bye!')
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
        baidu.set_lang(cmds[1],cmds[2])


def _save_result(user_input):
    cmds = _check_command(user_input, 1102, 2)
    if cmds:
        baidu.save(cmds[1])


def _change_info():
    info = deploy.read_info()
    deploy.change_info(info['appid'], info['secretkey'])


def _change_lang():
    lang = deploy.read_lang()
    deploy.change_lang(lang['source_lang'], lang['target_lang'])


def _execute_command(user_input):
    command = user_input.split(' ')[0]
    if   command == '/reve':
        baidu.reverse_lang()
    elif command == '/rule':
        baidu.display_rules()
    elif command == '/list':
        common.list_langs()
    elif command == '/help':
        _print_help()
    elif command == '/quit':
        _exit_cmdline()
    elif command == '/save':
        _save_result(user_input)
    elif command == '/setlang':
        _set_lang(user_input)
    elif command == '/changeinfo':
        _change_info()
    elif command == '/changelang':
        _change_lang()
    elif command == '/':
        pass
    else:
        _print_help()


def _trans(first, user_input):
    result = None
    if first[0] == '=':
        target_lang = user_input.split(' ')[0][1:]
        if common.check_target_code(target_lang):
            words = ' '.join(user_input.split(' ')[1:])
            result = baidu.trans(words, 'auto', target_lang)
    else:
        result = baidu.trans(user_input)
    print(result)


def _select_operate(user_input):
    first = user_input.split(' ')[0]
    if first in commands:
        _execute_command(user_input)
    else:
        _trans(first, user_input)


def translate_loop():
    try:
        while True:
            user_input = prompt('> ',history=_file_history,
                   auto_suggest=_auto_suggest_from_history,    
                   completer=_word_completer)
            if user_input:
                _select_operate(user_input)
    except KeyboardInterrupt:
        _exit_cmdline()


if __name__ == '__main__':
    translate_loop()
