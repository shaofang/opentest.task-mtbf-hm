#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class WechatTest(unittest.TestCase):
    def setUp(self):
        super(WechatTest, self).setUp()
        u.setup(d)

    def tearDown(self):
        super(WechatTest, self).tearDown()
        u.teardown(d)

    def testWechat_wifi(self):
        self.weChat(True)
 
    def testWechat_3g(self):
        self.weChat(False)

    def weChat(self, wifi):
        u.openWifi(d, wifi)

        #Start WeChat and check if successful
        d.start_activity(component='com.tencent.mm/.ui.LauncherUI')
        assert d(text="Me").wait.exists(timeout=20000), 'wechat unable to open in 20 secs'
        assert d(text="Discover").wait.exists(timeout=20000), 'wechat unable to open in 20 secs'

        #Switch to groups, moments, and settings
        d(className='android.widget.RadioButton', text='Contacts').click.wait()
        d(text='Groups').wait.exists(timeout=3000), 'Switch to Contacts failed'
        d(className='android.widget.RadioButton', text='Discover').click.wait()
        d(text='Moments').wait.exists(timeout=3000), 'Switch to Discover failed'
        d(className='android.widget.RadioButton', text='Me').click.wait()
        d(text='Settings').wait.exists(timeout=3000), 'Switch to Me failed'
        d(className='android.widget.RadioButton', text='Chats').click.wait()

        #Enter WeChat Team
        d.expect('conversation.png')
        d.click('conversation.png')

        assert d(text='常见问题').wait.exists(timeout=5000), 'Switch to chat failed.'

        #Clear chat history
        d.press('menu')
        d(text='Clear Chat History').click.wait()
        d(text='OK').click.wait()

        #Compose and send out a void message
        d.expect('compose.png', timeout=10)
        d.click('compose.png')
        if d.find('voice.png'):
            d.click('voice.png')

        assert d(className='android.widget.Button', text='Hold to Talk').wait.exists(timeout=3000), 'Can not swith to voice message'
        d(className='android.widget.Button', text='Hold to Talk').swipe.up(steps=100)

        #Check if can get feedback in 60s
        d.expect('chat.png', timeout=60)

