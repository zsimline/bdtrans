# bdtrans

**一个用于百度翻译的Python包**

*你不仅可以在Python脚本文件或解释器中使用它，也可以在终端下通过命令行工具使用它。*

### 安装

你可以直接使用Python包管理工具来安装它： **`pip install bdtrans`**
<br>你也可以下载源码包，解压后运行安装文件： **`python setup.py insatll`**

### 使用方式

>&emsp;&emsp;首先，你应该去百度翻译的[官网](http://api.fanyi.baidu.com/)上注册一个账户，并申请一个百度翻译API的AppID与秘钥。
><br>&emsp;&emsp;当你首次尝试导入bdtrans包，或者在命令行工具下使用它时，它将会指引你输入AppID、秘钥、默认的翻译规则等信息，并在输入完成后在你的用户目录下生成一个名为.bdtrans的配置文件，之后你就可以直接使用它而无需再次输入AppID等相关信息了。
><br>&emsp;&emsp;需要注意的是，百度翻译限制调用API的频率为1s/次，所以请不要在1s内调用多次API
<br>

### 模块函数

+ **trans(words, source_lang=None, target_lang=None, reverse=False)**

作用：翻译用户给定的句子，输出翻译结果

|参数|含义|
|:----|:----|
|words|你想要翻译的句子|
|source_lang|源语言代码（非必须）|
|target_lang|目标语言代码（非必须）|
|reverse|是否反转源语言与目标语言|

```python
>>> import bdtrans
>>> bdtrans.trans('Hello, boy!','en','zh')
>>> 你好，男孩！
```   

<br>

+ **io_trans(input_file, output_file=None, quiet=False)**

作用：从文件中读取翻译内容，如果指定了输出文件，翻译结果将被存储到输出文件中

|参数|含义|
|:----|:----|
|input_file|输入文件名|
|output_file|输出文件名|
|quiet|是否关闭控制台输出|

<br>

+ **set_lang(source_lang, target_lang)**

作用：设置源语言代码与目标语言代码

|参数|含义|
|:----|:----|
|source_lang|源语言代码|
|target_lang|目标语言代码|

<br>

+ **save(file_name)**

作用：保存翻译结果到文件中

|参数|含义|
|:----|:----|
|file_name|保存的文件名|

<br>

+ **reverse_lang()**

作用：反转源语言与目标语言

<br>

+ **list_langs()**

作用：打印目前支持的语言列表

<br>

+ **display_rules**

作用：显示当前的语言翻译规则

<br>

+ **change_appid()**

作用：按照向导改变配置文件中的AppID

<br>

+ **change_lang()**

作用：按照向导改变配置文件中的默认翻译规则

<br>

+ **initialize_app()**

作用：按照向导初始化APP

<br>

### 命令行工具

>可以直接在命令行下使用它，最重要的是你可以使用 bdtrans -S 进入交互式的翻译环境。

**bdtrans [选项] 待翻译文本**

#### 选项：

|选项|含义|
|:----|:----|
|-h, --help|显示帮助消息|
|-v, --version|显示程序版本|
|-l, --list|打印语言列表|
|-S, --shell|启动交互式翻译环境|
|-s code, --source code|指定源语言|
|-t code, --target code|指定目标语言|
|-i filename, --input filename|指定输入文件|
|-o filename, --output filename|指定输出文件|
|--init|按照向导初始化APP|
|--changeinfo|改变配置文件中的AppID|
|--changelang|改变配置文件中的翻译规则|

#### 交互环境下的选项：
|选项|含义|
|:----|:----|
|/reve|反转源语言与目标语言|
|/rule|显示当前的翻译规则|
|/list|打印支持的语言列表|
|/help|显示帮助信息|
|/quit|退出交互环境|
|/save filename|保存翻译结果|
|/setlang source_lang target_lang|设置源语言与目标语言|
```shell
user@host:$ bdtrans 德玛西亚万岁
user@host:$ Long live Demasia
user@host:$ bdtrans -t ara 德玛西亚万岁
user@host:$ فيفا دي مارسيا
user@host:$ bdtrans -s 德玛西亚万岁
user@host:$ 不可以只指定源语言！
```

>在交互环境下可以使用 =code 来临时的指定目标语言，此时源语言将自动的被指定为auto, 例如 " =zh hello world "
```python
>=th 你在地球嗑瓜子
คุณใช้เมล็ดแตงโมบนโลก
>=jp 我在月球吃西瓜
月でスイカを食べます
```
<br>

### 支持的语言列表：

|语言代码|语言|
|:----|:----|
|zh|中文|
|en|英语|
|yue|粤语|
|wyw|文言文|
|jp|日语|
|kor|韩语|
|fra|法语|
|spa|西班牙语|
|th|泰语|
|ara|阿拉伯语|
|ru|俄语|
|pt|葡萄牙语|
|de|德语|
|it|意大利语|
|el|希腊语|
|nl|荷兰语|
|pl|波兰语|
|bul|保加利亚语|
|est|爱沙尼亚语|
|dan|丹麦语|
|fin|芬兰语|
|cs|捷克语|
|rom|罗马尼亚语|
|slo|斯洛文尼亚语|
|swe|瑞典语|
|hu|匈牙利语|
|cht|繁体中文|
|vie|越南语|
|auto|自动检测|
