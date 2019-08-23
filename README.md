# bdtrans
### 一个用于百度翻译的Python包

注意：你不仅可以在Python脚本文件或交互式环境中使用它，也可以在终端下通过命令行工具使用它。


# 使用方式

>首先，你应该去百度翻译的[官网](http://api.fanyi.baidu.com/)上注册一个账户，并取得百度翻译API的appid与秘钥。

### 模块函数

+ **trans(words, source_lang=None, target_lang=None, reverse=False)**

    作用：翻译用户给定的句子，输出翻译结果。

|参数|含义|
|:----|:----|
|words|你想要翻译的句子|
|source_lang|源语言代码（非必须）|
|target_lang|目标语言代码（非必须）|
|reverse|是否反转源语言与目标语言|

```python
>>> import bdtrans
bdtrans.trans('Hello, boy!','en','zh')
```
输出：你好，男孩！
   
<br>

+ **io_trans(input_file, output_file=None, quiet=False)**
    
    作用：从文件读取翻译内容，如果指定了输出文件，翻译结果将被存储到输出文件中。

|参数|含义|
|:----|:----|
|input_file|输入文件名|
|output_file|输出文件名|
|quiet|是否关闭控制台输出|

