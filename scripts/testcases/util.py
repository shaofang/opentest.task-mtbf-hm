#!/usr/bin/python
# -*- coding:utf-8 -*- 
def openWifi(d, flag):
    d.start_activity(component='com.android.settings/.MiuiSettings')
    assert d(text='WLAN').wait.exists(timeout=3000), 'can not launch settings in 3s'
    d(text='WLAN').click.wait()
    wifi = d(className='android.widget.LinearLayout').child_by_text('WLAN').sibling(className='android.widget.CheckBox')
    #Should open wifi
    if flag:
        if not wifi.checked:
            wifi.click.wait()
            assert d(className='android.widget.LinearLayout').child_by_text('WLAN').sibling(className='android.widget.CheckBox', checked=True).wait.exists(timeout=10000), "wifi can not be opened"
            d.sleep(3)
    #Should close the wifi
    else:
        if wifi.checked:
            wifi.click.wait()
            assert d(className='android.widget.LinearLayout').child_by_text('WLAN').sibling(className='android.widget.CheckBox', checked=False).wait.exists(timeout=10000), "wifi can not be closed"
            d.sleep(3)
        
    #Wait for network switching
    d.press('home')

def backHome(d):
	d.press('back')
	d.sleep(1)
	d.press('back')
	d.sleep(1)
	d.press('home')

