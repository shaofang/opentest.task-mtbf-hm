#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class BrowserTest(unittest.TestCase):
    def setUp(self):
        super(BrowserTest, self).setUp()
        #d.start_activity(action='android.intent.action.DIAL', data='tel:13581739891', flags=0x04000000)
        d.wakeup()
        u.backHome(d)

    def tearDown(self):
        super(BrowserTest, self).tearDown()
        u.backHome(d)

    def testOpenBrowser_wifi(self):
        self.openBrowser(True)

    def testOpenBrowser_3g(self):
        self.openBrowser(False)


    def openBrowser(self, wifi):
        u.openWifi(d, wifi)
        #Launch browser
        d.start_activity(component='com.android.browser/.BrowserActivity')
        assert d(className='android.widget.ImageButton', index=3).wait.exists(timeout=3000), 'Can not open browser in 3s'

        d(className='android.widget.ImageButton', index=3).click.wait()
        assert d(text="Bookmarks").wait.exists(timeout=3000), 'Open new page failed in 3s'
        d(className='android.widget.EditText').set_text('wap.qq.com')
        #d.click('go.png', threshold=0.01)
        d.press('enter')

        #Sleep 15s to wait loading web page
        d.sleep(15)
        print d.right_dir_path
        if d.find('browser_blank.png') or d(text='Bookmarks'):
            assert False, 'Open the web page failed.'
        else:
            assert True




