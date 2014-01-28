#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class VideoTest(unittest.TestCase):
    def setUp(self):
        super(VideoTest, self).setUp()
        u.setup(d)

    def tearDown(self):
        super(VideoTest, self).tearDown()
        u.teardown(d)

    def testVideoPlayer(self):
        #Launch video and check if successful
        d.start_activity(component='com.miui.video/.HomeActivity')
        assert d(text='电视直播').wait.exists(timeout=5000) , 'video app can not be launched.'

        #Switch to local video and find bbb.mp4 to play
        if d(text='我的视频').wait.exists(timeout=1000):
            d(text='我的视频').click.wait()
        if d(text='Local').wait.exists(timeout=1000):
            d(text='Local').click.wait()
        assert d(text='bbb.mp4').wait.exists(timeout=3000) , 'Switch to local video.'
        d(text='bbb.mp4').click.wait()
        assert d(text='bbb.mp4').wait.gone(timeout=3000), 'Not switch to playing'

        #After finish playing, should back to video list
        u.sleep(600)
        assert d(text='bbb.mp4').wait.exists(timeout=10000)
        d.press('back')
        

