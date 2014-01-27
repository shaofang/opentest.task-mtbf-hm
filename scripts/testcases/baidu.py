#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import time
import util as u

class BaiduTest(unittest.TestCase):
    def setUp(self):
        super(BaiduTest, self).setUp()
        u.setup(d)

    def tearDown(self):
        super(BaiduTest, self).tearDown()
        u.teardown(d)

    def testBaidumaps(self):
        #Check and set wifi
        u.openWifi(d, True)

        #Launch Baidu map app
        d.start_activity(component='com.baidu.BaiduMap/com.baidu.baidumaps.WelcomeScreen')

        if d(text='不要福利').wait.exists(timeout=5000):
            d(text='不要福利').click.wait()

        #Check if baidu map can be launched successfully
        assert d(text='附近').wait.exists(timeout=10000), 'No enter main map activity'
        assert d(text='路线').wait.exists(timeout=2000), 'No enter main map activity'

        #Swipe on the map
        d.swipe(340, 340, 340, 900, steps=5)

        #Locate to current location
        d.expect('location.png')
        d.click('location.png')

        #Located successful
        assert d(text='我的位置').wait.exists(timeout=3000), 'can not locate'

