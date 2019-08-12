import sys
import json
import random
import urllib
import hashlib
import requests
import config
import common
import language

class Translate(object):
    appid = config.APPID
    secretkey = config.SECRETKEY
    api = config.API    
    source_lang = config.SOURCE_LANG
    target_lang = config.TARGET_LANG
    raw = False

    def __init__(self):
        pass

    def set_raw(self, raw):
        self.raw = raw

    def set_source(self, code):
        if hasattr(language.SourceCode, code):
            self.source_lang = code
        else:
            self.console('Invalid source code.')
            self.console('The following are legal:')
            sys.exit()

    def set_target(self, code):
        if hasattr(language.TargetCode, code):
            self.to_lang = code
        else:
            self.console('Invalid target code.')
            self.console('The following are legal:')
            sys.exit()


    def set_query(self, words):
        self.query = ' '.join(words)

    def set_salt(self):
        self.salt = str(random.randint(32768, 65536))

    def set_sign(self):
        sign = '%s%s%s%s' % (self.appid,self.query,
                             self.salt,self.secretkey)
        md5obj = hashlib.md5() 
        md5obj.update(sign.encode('UTF-8'))
        self.sign = md5obj.hexdigest()

    def request(self):
        param = (self.appid,urllib.parse.quote(self.query),
                 self.source_lang,self.to_lang,self.salt,self.sign)
        url = self.api % param
        
        try:
            response = requests.request('GET', url)
            return response
        except ConnectionError:
            self.console('2201 Network not connected')
        except KeyboardInterrupt:
            pass

    def display(self, response):
        content = response.content.decode('UTF-8')
        original = json.loads(content)
        if self.raw:
            self.console(original)
            return None
        try:
            result = original['trans_result'][0]['dst']
            self.console(result)
        except KeyError:
            self.console('2202 The return value is incorrect')
            self.console(original)

    def package(self, words):
        self.set_query(words)
        self.set_salt()
        self.set_sign()
        
    def translate(self, words):
        self.package(words)
        response = self.request()
        if response is not None:
            self.display(response)

    def repl(self):
        self.console('Translator Shell')
        self.console('[Ctrl + \\ to quit]')
        while True:
            try:
                content = input('\n> ')
            except KeyboardInterrupt:
                self.console('Good Bye!')
                sys.exit()
            if content == '':
                continue
            words = content.split(' ')
            self.translate(words)

    def console(self, message, wrap='\n'):
        print(message, end=wrap)
