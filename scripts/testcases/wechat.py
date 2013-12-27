#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class WechatTest(unittest.TestCase):
    def setUp(self):
        super(WechatTest, self).setUp()
        #d.start_activity(action='android.intent.action.DIAL', data='tel:13581739891', flags=0x04000000)
        d.wakeup()
        u.backHome(d)

    def tearDown(self):
        super(WechatTest, self).tearDown()
        u.backHome(d)

    def testWechat_wifi(self):
        self.weChat(True)
 
    def testWechat_3g(self):
        self.weChat(False)

    def weChat(self, wifi):
        u.openWifi(d, wifi)

        #assert d.exists(text='WeChat') , 'wechat app not appear on the home screen'
        #d(text='WeChat').click.wait()
        d.start_activity(component='com.tencent.mm/.ui.LauncherUI')
        assert d(text="Me").wait.exists(timeout=10000), 'wechat unable to open in 10 secs'
        assert d(text="Discover").wait.exists(timeout=1000), 'wechat unable to open in 10 secs'

        d(className='android.widget.RadioButton', text='Contacts').click.wait()
        d(text='Groups').wait.exists(timeout=3000), 'Switch to Contacts failed'
        d(className='android.widget.RadioButton', text='Discover').click.wait()
        d(text='Moments').wait.exists(timeout=3000), 'Switch to Discover failed'
        d(className='android.widget.RadioButton', text='Me').click.wait()
        d(text='Settings').wait.exists(timeout=3000), 'Switch to Me failed'
        d(className='android.widget.RadioButton', text='Chats').click.wait()

        d.expect('icon_list.png')

        d.click('icon_list.png')

        assert d(text='WeChat Team').wait.exists(timeout=3000), 'No WeChat Team in chat list.'
        d(text='WeChat Team').click.wait()
        assert d(text='常见问题').wait.exists(timeout=3000), 'Switch to chat failed.'

        d.press('menu')
        assert d(text='Clear Chat History').wait.exists(timeout=3000), 'Launch menu failed'
        d(text='Clear Chat History').click.wait()
        d(text='OK').wait.exists(timeout=3000), 'No delete dialog'
        d(text='OK').click.wait()

        d.click('compose.png')
        d(className='android.widget.Button', text='Hold to Talk').swipe.up(steps=200)

        d.expect('icon_chat.png', timeout=20)

