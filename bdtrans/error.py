import urllib

from bdtrans._global import _


class CommandError(Exception):
    def __init__(self, error_code):
        if error_code == 1101:
            self._set_lang_error()
        elif error_code == 1102:
            self._save_error()

    def _set_lang_error(self):
        print(_('[error] please use the command in this way:'
                '\n\t/setlang source_lang target_lang'
                '\n\tsuch as setlang en zh'))
    
    def _save_error(self):
        print(_('[error] please use the command in this way:'
                '\n\t/save filename\n\tsuch as save my_result'))


ConnectError = urllib.error.URLError


class TranslationError(Exception):
    def __init__(self):
        pass
    
    def display_msg(self, error_code):
        pass
