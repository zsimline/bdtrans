#!/usr/bin/env python3

import sys
import argparse

from bdtrans import lib
from bdtrans import repl
from bdtrans import deploy
from bdtrans._global import _


__version__ = '0.4.0'


def _print_help(parser):
    """
    Print help information and exit.
    """
    parser.print_help()
    sys.exit(0)


def _print_langs():
    lib.list_langs()
    sys.exit(0)


def _print_version():
    """
    Print version information and exit.
    """
    print(__version__)
    sys.exit(0)


def _change_appid():
    info = deploy.read_info()
    deploy.change_appid(info['appid'], info['secretkey'])
    sys.exit(0)


def _change_lang():
    lang = deploy.read_lang()
    deploy.change_lang(lang['source_lang'], lang['target_lang'])
    sys.exit(0)


def _set_lang(source_lang, target_lang):
    """
    Setting source language code and target language code.
    
    If only the target language is specified,
    the source language will be specified as auto.
    If only the source language is specified, 
    an error message is prompted.
    """
    if  source_lang and target_lang:
        lib.set_lang(source_lang, target_lang)
    elif not source_lang and target_lang:
        lib.set_lang('auto', target_lang)
    elif source_lang and not target_lang:
        print(_("Can't just specify the source language !"))
        sys.exit(0)
    else:
        return


def _initialize_app():
    deploy.initialize_app()
    sys.exit(0)


def _get_parser():
    """
    Create and return a command line parameter parser.
    """
    parser = argparse.ArgumentParser(prog='bdtrans', add_help=False)
    parser.add_argument('-h', '--help', action='store_true',
                        help=_("show this message and exit"))
    parser.add_argument('-v', '--version', action='store_true',
                        help=_("show program's version number and exit"))
    parser.add_argument('-l', '--list', action='store_true',
                        help=_('show reference table of languages and exit'))
    parser.add_argument('-S', '--shell', action='store_true',
                        help=_('start an interactive shell'))
    parser.add_argument('-q', '--quiet',action='store_true',
                        help=_('do not print translation results to the console'))
    parser.add_argument('-s', '--source', metavar='CODE',
                        help=_('specify the source language'))
    parser.add_argument('-t', '--target', metavar='CODE', 
                        help=_('specify the target language'))
    parser.add_argument('-i', '--input', metavar='FILENAME', 
                        help=_('specify the input file'))
    parser.add_argument('-o', '--output', metavar='FILENAME', 
                        help=_('specify the output file'))
    parser.add_argument('--init', action='store_true',
                        help=_('follow the wizard to initialize app'))
    parser.add_argument('--changeinfo', action='store_true',
                        help=_('change AppID in configuration file'))
    parser.add_argument('--changelang', action='store_true',
                        help=_('change translation rules in configuration file'))
    return parser


def _io_trans(input_file, output_file, quiet):
    if  input_file and not output_file:
        lib.io_trans(input_file, None, quiet) 
    else:
        lib.io_trans(input_file, output_file, quiet) 
    sys.exit(0)


def _trans(words, output_file, quiet=False):
    words = ' '.join(words)
    result = lib.trans(words)
    if output_file:
        with open(output_file, 'w') as f:
            f.write(result)
    if not quiet:
        print(result)


def start_cmd():
    parser = _get_parser()
    arguments = parser.parse_known_args()
    args = arguments[0]
    words = arguments[1]

    if args.help:
        _print_help(parser)
    if args.version:
        _print_version()
    if args.list:
        _print_langs()
    if args.init:
        _initialize_app()
    if args.changeinfo:
        _change_appid()
    if args.changelang:
        _change_lang()
    if args.shell:
        repl.translate_loop()

    _set_lang(args.source, args.target)
    # when the user specifies the input file, 
    # translate the sentences in the file.
    if args.input:
        _io_trans(args.input, args.output, args.quiet)
    # otherwise, translate the sentences entered
    # by the user on the command line.
    else:
        _trans(words, args.output, args.quiet)
