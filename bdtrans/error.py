import urllib

from bdtrans._global import _


ERROR_MSG = {
	'52001': _('request timeout: please retry.'),
	'52002': _('system error: please retry.'),
	'52003': _('unauthorized user: check if your appid is correct or if the '
             'service is open.'),
	'54000': _('the required parameters are blank: check whether the parameters '
             'are missing.'),
	'54001': _('signature error: please check your signature generation method.'),
	'54003': _('restricted access frequency: please reduce your call frequency.'),
	'54004': _('inadequate account balance: please go to the management console '
             'to recharge the account.'),
	'54005': _('long query requests are frequent: please reduce the sending '
             'frequency of long query and try again after 3S.'),
	'58000': _('client IP illegality: check whether the IP address filled in '
             'the personal data is correct or not. You can go to the management '
             'control platform to modify the IP restriction. IP can be left blank.'),
	'58001': _('language Direction of the Translated Language is not Supported: '
             'Check whether the Translated Language is in the Language List.'),
	'58002': _('service is currently closed: please go to the Management Console '
             'to open the service.'),
	'90107': _('certification has not passed or entered into force: please go to '
             'my certification to check the progress of certification.')
}


ConnectError = urllib.error.URLError


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


class TranslationError(Exception):
    def __init__(self):
        pass
    
    def display_msg(self, error_code):
        print(error_code, end=' ')
        print(ERROR_MSG[error_code])
