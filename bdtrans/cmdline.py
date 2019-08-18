import sys
sys.path.append('../')
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory 
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter

from bdtrans import baidu
from bdtrans import error
from bdtrans import deploy
from bdtrans import common


_file_history = FileHistory('history.txt')
_auto_suggest_from_history = AutoSuggestFromHistory()
_word_completer = WordCompleter(['/help','/quit','/reverse','/list','/save',
    '/rule','/setlang','/changeinfo','/changelang'],ignore_case=True)


def _switch(user_input):
    first = user_input.split(' ')[0]
    if first[0] == '/':
        _execute_command(user_input, first)
    elif first[0] == '=':
        _trans_target(user_input)
    else:
        baidu.trans(user_input)


def _exit_cmdline():
    print('Good Bye!')
    sys.exit(0)
import sys
def _trans_targetimport sys(user_input):
    target_lang =import sys user_input.split(' ')[0][1:]
    if common.cheimport sysck_target_code(target_lang):
        words = 'import sys '.join(user_input.split(' ')[1:])
        baidu.trans(words, 'auto', target_lang)


def _set_lang(user_input):
    cmds = user_input.split(' ')
    try:
        if len(cmds) != 3:
            raise error.CommandError(1101)
        if not cmds[1] or not cmds[2]:
            raise error.CommandError(1101)
    except error.CommandError:
        return None
    baidu.set_lang(cmds[1],cmds[2])




def _execute_command(user_input, command):
    if command == '/h' or command =='/help':
        pass
    elif command == '/q' or command == '/quit':
        _exit_cmdline()
    elif command == '/r' or command == '/reverse':
        baidu.reverse_lang()
    elif command == '/list':
        common.list_langs()
    elif command == '/save':
        pass
    elif command == '/rule':
        baidu.display_rules()
    elif command == '/setlang':
        _set_lang(user_input)
    elif command == '/changeinfo':
        deploy.change_info()
    elif command == '/changelang':
        deploy.change_lang()
    elif command == '/':
        pass
    else:
        print('unkown command')


def _translate_loop():
    try:
        while True:
            user_input = prompt('> ',
                history=_file_history,
                auto_suggest=_auto_suggest_from_history,    
                completer=_word_completer
            )
            if user_input:
                _switch(user_input)
    except KeyboardInterrupt:
        _exit_cmdline()

if __name__ == '__main__':
    _translate_loop()
