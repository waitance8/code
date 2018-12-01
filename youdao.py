import urllib.request
import urllib.parse
import json
import time

while True:
    content = input('请输入您要翻译的内容: ')
    if content == 'q!':
        break
    else:
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

        head = {}
        head['User-Agent'] ='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6776.400 QQBrowser/10.3.2577.400'
        data = {'client': 'fanyideskweb',
                'salt': '1542356216453',
                'sign': '2c7e5abe9e63c3e2e7131f8e43831a09',
                'tgt': 'Everybody is good',
                'from': 'AUTO',
                'to': 'AUTO',
                'doctype': 'json',
                'version': '2.1',
                'keyfrom': 'fanyi.web',
                'i': content,
                'smartresult': 'dict',
                'typoResult': 'false',
                'action': 'FY_BY_REALTIME'
                }

        data = urllib.parse.urlencode(data).encode('utf-8')
        req = urllib.request.Request(url, data, head)
        respones = urllib.request.urlopen(req)
        html = respones.read().decode()
        target = json.loads(html)
        print('翻译的结果为：%s' % target['translateResult'][0][0]['tgt'])
        time.sleep(5)