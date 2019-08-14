import sys
import json
import random
import urllib
import hashlib
import requests

from bdtrans import conf
from bdtrans import language
from bdtrans.common import get_profile_path


class Translate(object):
    api = conf.API
    show_raw = False

    def __init__(self):
        config = None
        profile = get_profile_path()
        with open(profile, 'r') as f:
            config = json.load(f)
        self.appid = config['APPID']
        self.secretkey = config['SECRETKEY']
        self.source_lang = config['SOURCE_LANG']
        self.target_lang = config['TARGET_LANG']

    def set_raw(self, show_raw):
        self.show_raw = show_raw

    def set_source(self, code):
        self.source_lang = code

    def set_target(self, code):
        self.target_lang = code

    def reverse_lang(self):
        temp = self.source_lang
        self.source_lang = self.target_lang
        self.target_lang = temp

    def _set_query(self, words):
        self.query = words
 
    def _set_salt(self):
        self.salt = str(random.randint(32768, 65536))

    def _set_sign(self):
        sign = '%s%s%s%s' % (self.appid,self.query,
                             self.salt,self.secretkey)
        md5obj = hashlib.md5() 
        md5obj.update(sign.encode('UTF-8'))
        self.sign = md5obj.hexdigest()

    def _request(self):
        param = (self.appid,urllib.parse.quote(self.query),
                 self.source_lang,self.target_lang,
                 self.salt,self.sign)
        url = self.api % param
        
        try:
            response = requests.request('GET', url)
            return response
        except ConnectionError:
            self._console('2201 Network not connected')
        except KeyboardInterrupt:
            pass

    def _display(self, response):
        content = response.content.decode('UTF-8')
        original = json.loads(content)
        if self.show_raw:
            self._console(original)
            return None
        try:
            result = original['trans_result'][0]['dst']
            self._console(result)
        except KeyError:
            self._console('2202 The return value is incorrect')
            self._console(original)

    def _package_words(self, words):
        self._set_query(words)
        self._set_salt()
        self._set_sign()
        
    def translate(self, words):
        response = None
        self._package_words(words)
        response = self._request()
        if response is not None:
            self._display(response)

    def _console(self, message, wrap='\n'):
        print(message, end=wrap)
