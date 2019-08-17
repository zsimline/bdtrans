import sys
import json
import random
import hashlib
import requests
from urllib.parse import quote

from bdtrans import conf
from bdtrans import common
from bdtrans import language


_profile = common.get_profile_path()


class Translate(object):
    api = conf.API

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
        return (self.source_lang, 
                self.target_lang)

    def reverse_lang(self):
        temp = self.source_lang
        self.source_lang = self.target_lang
        self.target_lang = temp

    def _set_query(self, words):
        self.query = words
 
    def _make_salt(self):
        return str(random.randint(32768, 65536))

    def _make_sign(self, salt):
        sign = '%s%s%s%s' % (
               self.appid,self.query,salt,self.secretkey)
        md5obj = hashlib.md5() 
        md5obj.update(sign.encode('UTF-8'))
        return md5obj.hexdigest()

    def _api_request(self, url):
        try:
            response = requests.request('GET', url)
            return response
        except ConnectionError:
            self._console('2201 Network not connected')
        except KeyboardInterrupt:
            pass

    def _display(self, response, show_raw):
        content = response.content.decode('UTF-8')
        original = json.loads(content)
        if show_raw:
            self._console(original)
            return None
        try:
            result = original['trans_result'][0]['dst']
            self._console(result)
        except KeyError:
            self._console('2202 The return value is incorrect')
            self._console(original)

    def _package_words(self, words, source_lang, 
                       target_lang, reverse):
        self._set_query(words)
        salt = self._make_salt()
        sign = self._make_sign(salt)
        
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

        param = (self.appid, quote(self.query),
                 source_lang_,target_lang_,salt,sign)
        return self.api % param

    def translate(self, words, source_lang, target_lang, reverse, show_raw):
        response = None
        url = self._package_words(words, source_lang, target_lang, reverse)
        response = self._api_request(url)
        if response is not None:
            self._display(response, show_raw)

    def _console(self, message, wrap='\n'):
        print(message, end=wrap)
