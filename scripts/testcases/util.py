#!/usr/bin/python
# -*- coding:utf-8 -*- 
import random
import json
import time

try:
    import urllib2
except ImportError:
    import urllib.request as urllib2

def openWifi(d, flag):
    d.start_activity(component='com.android.settings/.MiuiSettings')
    assert d(text='WLAN').wait.exists(timeout=3000), 'can not launch settings in 3s'
    d(text='WLAN').click.wait()
    wifi = d(className='android.widget.LinearLayout').child_by_text('WLAN').sibling(className='android.widget.CheckBox')
    #Should open wifi
    if flag:
        i = 0
        while not wifi.checked and i < 2:
            d(text='WLAN')[1].click.wait()
            sleep(3)
            i = i + 1
        assert wifi.checked is True, 'wifi can not be opened'
        #if not wifi.checked:
        #    d(text='WLAN')[1].click.wait()
        #    assert d(className='android.widget.LinearLayout').child_by_text('WLAN').sibling(className='android.widget.CheckBox', checked=True).wait.exists(timeout=10000), "wifi can not be opened"
        #    sleep(3)
    #Should close the wifi
    else:
        i = 0
        while wifi.checked and i < 2:
            d(text='WLAN')[1].click.wait()
            sleep(3)
            i = i + 1
        assert wifi.checked is False, 'wifi can not be closed'
        #if wifi.checked:
        #    d(text='WLAN')[1].click.wait()
        #    assert d(className='android.widget.LinearLayout').child_by_text('WLAN').sibling(className='android.widget.CheckBox', checked=False).wait.exists(timeout=10000), "wifi can not be closed"
        #    sleep(3)
        
    #Wait for network switching
    d.press('home')

def backHome(d):
	d.press('back')
	sleep(1)
	d.press('back')
	sleep(1)
	d.press('home')

def fetchText():
    url = 'http://andymatthews.net/thought/'
    r = ''
    result = None
    jsonr = None
    try:
        req = urllib2.Request(url)
        result = urllib2.urlopen(req, timeout=30)
        jsonr = json.loads(result.read().decode("utf-8"))
    except:
        pass
    finally:
        if result is not None:
            result.close()

    if jsonr is None:
        s = ' !.,abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        r = ''.join(random.sample(s, random.randint(15, 30)))
    else:
        r = jsonr['thought']['thought'][0:64] + '...'
    return r

def registerSysWatchers(d):
    d.watchers.remove()
    d.watcher("AUTO_FC_WHEN_ANR").when(textContains="isn't responding").when(text="Wait").click(text="OK")
    d.watcher("WEIBO_SEARCH_FRIENDS").when(text="搜寻好友").when(text="Skip").click(text="Skip")
    d.watcher("WEIBO_UPDATE").when(text="Download").when(text="Cancel").click(text="Cancel")

def checkSystemWatchers(d):
    if d.watcher("AUTO_FC_WHEN_ANR").triggered:
        raise Exception('AUTO_FC_WHEN_ANR')
    d.watchers.remove()

def sleep(sec):
    time.sleep(sec)

def setup(d):
    d.wakeup()
    d.info
    registerSysWatchers(d)
    backHome(d)

def teardown(d):
    checkSystemWatchers(d)
    backHome(d)
