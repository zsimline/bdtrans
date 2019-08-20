import sys
sys.path.append('/home/mxsyx/desktop/bdtrans/')
sys.path.remove('/home/mxsyx/desktop/bdtrans/bdtrans')
import argparse


from bdtrans import repl
from bdtrans import baidu
from bdtrans import common

_ = common.i18n()
__version = '0.2.0'


def _print_help(parser):
    parser.print_help()
    sys.exit(0)


def _print_version():
    print(__version__)
    sys.exit(0)


def _change_info():
    info = deploy.read_info()
    deploy.change_info(info['appid'], info['secretkey'])


def _change_lang():
    lang = deploy.read_lang()
    deploy.change_lang(lang['source_lang'], lang['target_lang'])


def _set_lang(source_lang, target_lang):
    if  source_lang and target_lang:
        baidu.set_lang(source_lang, target_lang)
    elif not source_lang and target_lang:
        baidu.set_lang('auto', target_lang)
    elif source_lang and not target_lang:
        print("Can't just specify the source language !")
        sys.exit(0)
    else:
        return

def _io_trans(input_file, output_file, quiet):
    if  input_file and not output_file:
        baidu.io_trans(input_file, None, quiet) 
    else:
        baidu.io_trans(input_file, output_file, quiet) 
    sys.exit(0)

def _get_parser():
    parser = argparse.ArgumentParser(prog='China Baidu Translator',
                                     add_help=False)
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
    parser.add_argument('-s', '--source', metavar='CODE',
                        help=_('specify the source language'))
    parser.add_argument('-t', '--target', metavar='CODE', 
                        help=_('specify the target language'))
    parser.add_argument('-i', '--input', metavar='FILENAME', 
                        help=_('specify the input file'))
    parser.add_argument('-o', '--output', metavar='FILENAME', 
                        help=_('specify the output file'))
    parser.add_argument('-q', '--quiet',action='store_true',
                help=_('do not print translation results to the console'))
    return parser


def _trans(words, output_file, quiet=False):
    words = ' '.join(words)
    result = baidu.trans(words)
    if output_file:
        with open(output_file, 'w') as f:
            f.write(result)
    if not quiet:
        print(result)


if __name__ == '__main__':
    parser = _get_parser()
    arguments = parser.parse_known_args()
    args = arguments[0]
    words = arguments[1]

    if args.help:
        _print_help(parser)
    if args.version:
        _print_version()
    if args.upgrade:
        common.check_upgrade()
    if args.list:
        common.list_langs()
    if args.shell:
        repl.translate_loop()
        sys.exit(0)

    _set_lang(args.source, args.target)
    if args.input:
        _io_trans(args.input, args.output, args.quiet)
    else:
        _trans(words, args.output, args.quiet)
