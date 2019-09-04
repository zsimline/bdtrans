# bdtrans

**A Python Package for Baidu Translation**

*You can use it not only in Python script files or interpreter, but also in terminal command-line tools.*

### Install

You can use the Python package management tool to install it: **`pip install bdtrans`**
<br>
You can also download the source package and run the installation file after decompression: **`python setup.py insatll`**

### Usage

>&emsp;First, you should register an account on [Baidu Translator's official website](http://api.fanyi.baidu.com/), and apply for an AppID and secret key of Baidu Translator's API.
><br>&emsp;When you first try to import the bdtrans package, or use it in a command-line tool, it will guide you to enter information such as AppID, secret key, default translation rules, etc., and generate a configuration file named .bdtrans in your user directory when the input is complete, after which you can use it directly without re-entering AppID and other related information.
><br>&emsp;It should be noted that Baidu translation limits the frequency of API calls to 1s/time, so please do not call API multiple times in 1s.
<br>

### Module Function

+ **trans(words, source_lang=None, target_lang=None, reverse=False)**

Translate user-given sentences and output translation results

|parameter|meaning|
|:----|:----|
|words|sentences you want to translate|
|source_lang|source language code (not required)|
|target_lang|target language code (not required)|
|reverse|whether to reverse the source language and the target language|

```python
>>> import bdtrans
>>> bdtrans.trans('你好，男孩！','zh','en')
>>> Hello, boy!
```   

<br>

+ **io_trans(input_file, output_file=None, quiet=False)**

Read the translation content from the file. If the output file is specified, the translation result will be stored in the output file.

|parameter|meaning|
|:----|:----|
|input_file|name of input file|
|output_file|name of output file|
|quiet|whether to close console output|

<br>

+ **set_lang(source_lang, target_lang)**

Setting source language code and target language code.

|parameter|meaning|
|:----|:----|
|source_lang|source language code|
|target_lang|target language code|

<br>

+ **save(file_name)**

Save translation results to files.

|parameter|meaning|
|:----|:----|
|file_name|saved file name|

<br>

+ **reverse_lang()**

Inversion of source language and target language.

<br>

+ **list_langs()**

Print a list of currently supported languages.

<br>

+ **display_rules**

Display current language translation rules.

<br>

+ **change_appid()**

Follow the wizard to change the AppID in the configuration fil.

<br>

+ **change_lang()**

Follow the wizard to change the default translation rules in the configuration file.

<br>

+ **initialize_app()**

Follow the wizard to initialize APP.

<br>

### Command Line Tool

>It can be used directly from the command line, and most importantly, you can use "bdtrans -S" to enter an interactive translation environment.

**bdtrans [option] text**

#### Option

|option|meaning|
|:----|:----|
|-h, --help|display help message|
|-v, --version|display program version|
|-l, --list|print language list|
|-S, --shell|start an interactive translation environment|
|-s code, --source code|specify the source language|
|-t code, --target code|specify the target language|
|-i filename, --input filename|specify input file|
|-o filename, --output filename|specify output file|
|--init|follow the wizard to initialize APP|
|--changeinfo|change the AppID in the configuration file|
|--changelang|change translation rules in configuration file|

#### Options in an interactive environment

|option|meaning|
|:----|:----|
|/reve|inversion of source language and target language|
|/rule|display current translation rules|
|/list|print a list of supported languages|
|/help|display help message|
|/quit|exit the interactive environment|
|/save filename|save translation results|
|/setlang source_lang target_lang|setting source language and target language|
```shell
user@host:$ bdtrans The earth revolves around the sun.
user@host:$ 地球绕着太阳转。
user@host:$ bdtrans -t ara The earth revolves around the sun.
user@host:$ الأرض تدور حول الشمس
user@host:$ bdtrans -s en The earth revolves around the sun.
user@host:$ You cannot specify only the source language.
```

>In an interactive environment, you can use the specified target language when =code arrives, where the source language is automatically specified as auto, such as "=zh Hello world"
```python
>=th You are eating melon seeds on earth
คุณใช้เมล็ดแตงโมบนโลก
>=jp I eat watermelon on the moon
月でスイカを食べます
```
<br>

### List of supported languages:

|language Code|language|
|:----|:----|
|zh|chinese|
|en|english|
|yue|cantonese|
|wyw|classical chinese|
|jp|japanese|
|kor|korean|
|fra|french|
|spa|spanish|
|th|thai|
|ara|arabic|
|ru|russian|
|pt|portuguese|
|de|german|
|it|italian|
|el|greek|
|nl|dutch|
|pl|polish|
|bul|bulgarian|
|est|estonian|
|dan|danish|
|fin|finnish|
|cs|czech|
|rom|romanian|
|slo|slovenian|
|swe|swedish|
|hu|hungarian|
|cht|traditional chinese|
|vie|vietnamese|
|auto|automatic detection|
