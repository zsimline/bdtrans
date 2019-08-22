"""
The translate model is defined here.
"""

import sys
import json
import random
import hashlib
from urllib import request

from bdtrans import error
from bdtrans import common
from bdtrans import language


_ = common.i18n()
_profile = common.get_profile_path()
# API of Baidu Translation
_API = ('https://api.fanyi.baidu.com/api/trans/vip/translate?'
       'appid=%s&q=%s&from=%s&to=%s&salt=%s&sign=%s')


class Translate(object):
    api = _API

    def __init__(self):
        config = None
        with open(_profile, 'r') as f:
            config = json.load(f)
        self.appid = config['APPID']
        self.secretkey = config['SECRETKEY']
        self.source_lang = config['SOURCE_LANG']
        self.target_lang = config['TARGET_LANG']

    def set_source(self, code):
        self.source_lang = code

    def set_target(self, code):
        self.target_lang = code

    def get_rules(self):
        """
        Returns a tuple containing the current translation rules.
        """
        return (self.source_lang, self.target_lang)

    def reverse_lang(self):
        """
        Inversion of Source Language and Target Language.
        """
        temp = self.source_lang
        self.source_lang = self.target_lang
        self.target_lang = temp

    def _set_query(self, words):
        self.query = words
 
    def _make_salt(self):
        """
        Generate and return a random number 
        between 32768 and 65536.
        """
        return str(random.randint(32768, 65536))

    def _make_sign(self, salt):
        """
        Generate and return a signature by salt.
        """
        sign = '%s%s%s%s' % (
            self.appid,self.query,salt,self.secretkey)
        md5obj = hashlib.md5() 
        md5obj.update(sign.encode('UTF-8'))
        return md5obj.hexdigest()

    def _api_request(self, url):
        """
        Send the request to the server and return 
        the response of the server.
        """
        try:
            return request.urlopen(url)
        except error.ConnectError:
            # Capture exception if network connection fails
            self._console('2201 Network not connected')
        except KeyboardInterrupt:
            pass

    def _parse_response(self, response):
        """
        Extraction of translation results.
        The server will return a JSON string.

        When the translation fails, the server will return
        a JSON string containing error_code, through which
        we can know what error has occurred.
        """
        content = response.read()
        content_text = content.decode('UTF-8')
        original = json.loads(content_text)
        try:
            return original['trans_result'][0]['dst']
        except KeyError:
        # Capture exception if parsing translation results fails
            try:
                raise error.TranslationError()
            except error.TranslationError as e:
                e.display_msg(original['error_code'])           

    def _package_words(self, words, source_lang, target_lang, reverse):
        """
        Encapsulating URL based on parameter values.
        """
        self._set_query(words)
        salt = self._make_salt()
        sign = self._make_sign(salt)
        
        # the values of source_lang and target_lang
        # will override the default translation rules.
        source_lang_ = self.source_lang
        target_lang_ = self.target_lang
        if source_lang:
            source_lang_ = source_lang
        if target_lang:
            target_lang_ = target_lang
        if reverse:
            temp = source_lang_
            source_lang_ = target_lang_
            target_lang_ = temp

        param = (self.appid,request.quote(self.query),
                 source_lang_,target_lang_,salt,sign)
        return self.api % param

    def translate(self, words, source_lang, target_lang, reverse):
        response = None
        url = self._package_words(words, source_lang, target_lang, reverse)
        response = self._api_request(url)
        if response is not None:
            return self._parse_response(response)

    def _console(self, message, wrap='\n'):
        print(message, end=wrap)
