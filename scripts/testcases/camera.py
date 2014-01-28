#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest, self).setUp()
        u.setup(d)

    def tearDown(self):
        super(CameraTest, self).tearDown()
        u.teardown(d)

    def testTakePicture(self):
        #Start camera and check if sucessful
        d.start_activity(component='com.android.camera/.Camera')
        assert d(description='Shutter button').wait.exists(timeout=5000), 'can not launch camera in 5s'

        #Take picture
        d(description='Shutter button').click.wait()
        u.sleep(5)

        #Delete the recent picture
        d(description='Most recent photo').click.wait()
        assert d(text="Delete").wait.exists(timeout=3000), 'No picture to delete.'
        #d(text="Delete").click.wait()
        #d(text="OK").click.wait()
        #If there is not only one picture
        #if d(text="Delete").wait.exists(timeout=2000):
        d.press('back')
        assert d(description="Shutter button").wait.exists(timeout=5000), 'unable back to camera after delete in 5s.'
