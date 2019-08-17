#!/opt/Anaconda/bin/python3.6

import sys
import argparse
import config
import baidu
import common

_ = common.i18n()

def get_parser():
    parser = argparse.ArgumentParser(prog='Baidu Translator', add_help=False)
    parser.add_argument('-h', '--help', action='store_true',
                        help=_("show this help message and exit"))
    parser.add_argument('-v', '--version', action='store_true',
                        help=_("show program's version number and exit"))
    parser.add_argument('-u', '--upgrade', action='store_true',
                        help=_('check for upgrade of this program'))
    parser.add_argument('-l', '--list', action='store_true',
                        help=_('show reference table of languages and exit'))
    parser.add_argument('-S', '--shell', action='store_true',
                        help=_('start an interactive shell'))
    parser.add_argument('-r', '--raw', action='store_true',
                        help=_('show raw API response instead'))
    parser.add_argument('-s', '--source', metavar='CODE',
                        help=_('specify the source language'))
    parser.add_argument('-t', '--target', metavar='CODE', 
                        help=_('specify the target language'))
    parser.add_argument('-i', '--input', metavar='FILENAME', 
                        help=_('specify the input file'))
    parser.add_argument('-o', '--output', metavar='FILENAME', 
                        help=_('specify the output file'))
    return parser


def print_help(parser):
    parser.print_help()
    sys.exit()


def print_version():
    print(__version__)
    sys.exit()


if __name__ == '__main__':
    parser = get_parser()
    
    arguments = parser.parse_known_args()
    args = arguments[0]
    words = arguments[1]

    if args.help:
        print_help(parser)
    if args.version:
        print_version()
    if args.upgrade:
        common.check_upgrade()
    if args.list:
        print_langs()
    
    trans = baidu.Translate()
    trans.set_raw(args.raw)
    trans.set_source(args.source)
    trans.set_target(args.target)
    
    if args.shell:
        trans.repl()

    if args.input:
        pass  # TODO
    if args.output:
        pass  # TODO

    if not words:
        print_help(parser)

    trans.translate(words)


from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter

SQLCompleter = WordCompleter(['select','update','drop','insert','delete'],ignore_case=True)


while True:
    user_input = prompt('>',
                        history=FileHistory('history.txt'),
                        auto_suggest=AutoSuggestFromHistory(),
                        completer=SQLCompleter,
                        )
    print(user_input)
