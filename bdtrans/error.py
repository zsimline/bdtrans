
class EmptyError(Exception):
    pass


class CommandError(Exception):
    def __init__(self, error_code):
        if error_code == 1101:
            self._set_lang_error()

    def _set_lang_error(self):
        print(('Error, please set the language code ' 
               'in this way:\n  setlang source_lang '
               'target_lang \nsuch as setlang en zh '))
