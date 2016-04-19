#coding:utf-8
import re
import json
import urllib
import time
import os

def needUpdata():

    """ Change it later. """

    need = True
    return need

def getAccount():
    if needUpdata():
        url = 'http://www.ishadowsocks.com'
        htmlData = urllib.urlopen(url).read().decode('utf-8')
        #f = open('ishadowsocks.html')
        #htmlData = f.read()
        #f.close()
        #change  .+?  to  .*?
        reg1 = r'col-lg-4[\s\S]+?:(.*?)</h4>[\s\S]+?:(.*?)</h4>[\s\S]+?:(.*?)</h4>[\s\S]+?:(.*?)</h4>'
        between = r':(.*?)</h4>[\s\S]*?'
        reg = u'服务器地址' + between + u'端口' + between + u'密码' + between + u'加密方式' + r':(.*?)</h4>'
        accountList = re.findall(reg1, htmlData)
        print 'get account: '
        print accountList
    else:
        pass

    return accountList

def setAccount(accountList):
    f = open('gui-config.json')
    data = json.loads(f.read())
    for index, account in enumerate(accountList):
        if len(data['configs']) < (index + 1):
            data['configs'].append({})
        data['configs'][index]['server'] = account[0]
        data['configs'][index]['server_port'] = account[1]
        data['configs'][index]['password'] = account[2]
        data['configs'][index]['method'] = account[3]
    dataJson = json.dumps(data, indent = 2)
    f.close()
    f = open('gui-config.json', 'w')
    f.write(dataJson)
    f.close()

def main():
    time.sleep(3)
    accountList = getAccount()
    setAccount(accountList)
    time.sleep(3)
    try:
        os.system("C:\Users\evann\Downloads\Shadowsocks-win-2.5.6\Shadowsocks.exe")
    except:
        pass
    print 'start shadowsocks OK'

if __name__ == '__main__':
    main()
