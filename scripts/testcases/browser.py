#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class BrowserTest(unittest.TestCase):
    def setUp(self):
        super(BrowserTest, self).setUp()
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
        
        #Launch browser and check if launch sucessful
        d.start_activity(component='com.android.browser/.BrowserActivity')
        assert d(className='android.widget.ImageButton', index=3).wait.exists(timeout=5000), 'Launch browser failed in 5s'

        #Open a new page
        #and go to www.qq.com
        d(className='android.widget.ImageButton', index=3).click.wait()
        assert d(text="Bookmarks").wait.exists(timeout=3000), 'Open new page failed in 3s'
        d(className='android.widget.EditText').set_text('wap.qq.com')
        d.press('enter')

        #Sleep 15s to wait loading web page
        u.sleep(15)
        flag = True
        i = 0
        while(flag and i < 9):
            i = i + 1
            d.swipe(400, 1000, 400, 500, steps=6)
            u.sleep(5)
            if not d.find('browser_blank.png'):
                flag = False
        if flag:
            assert False, 'Open the web page failed in 60s.'
        else:
            assert True



