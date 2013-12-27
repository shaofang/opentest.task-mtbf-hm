#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class MusicTest(unittest.TestCase):
    def setUp(self):
        super(MusicTest, self).setUp()
        d.wakeup()
        u.backHome(d)

    def tearDown(self):
        super(MusicTest, self).tearDown()
        u.backHome(d)

    def testMusicPlayer(self):
        #Find and launch Video app
        #assert d.exists(text='Music') , 'Music app not appear on the home screen'
        #d(text='Music').click.wait()

        d.start_activity(component='com.miui.player/.ui.MusicBrowserActivity')
        assert d(text='4:35').wait.exists(timeout=3000) , 'Music app can not be launched.'
        #assert d(className='android.widget.ImageView', index=2).wait.exists(timeout=3000) , 'play and stop button.'

        d(text='4:35').click.wait()
        assert d(className='android.widget.SeekBar').wait.exists(timeout=3000) , 'Switch to local video.'
        
        #Press 'next' button
        print '0 click the afterward button'
        d(className='android.widget.LinearLayout', index=5).child(className='android.widget.ImageView', index=2).click.wait()
        #print '1 click the afterward button'


        #text1 = d(className='android.widget.LinearLayout', index=2).child(className='android.widget.TextView', index=0).text

        #print 'text1%s'%text1
        #time.sleep(3)

        #text2 = d(className='android.widget.LinearLayout', index=2).child(className='android.widget.TextView', index=0).text
        #print 'text2%s'%text2

        #print 'Sleep 5s'
        #time.sleep(5)
        #print '0 Press stop button'

        #Stop
        d(className='android.widget.LinearLayout', index=5).child(className='android.widget.ImageView', index=1).click.wait()
        text1 = d(className='android.widget.LinearLayout', index=2).child(className='android.widget.TextView', index=0).text
        print text1
        #Start
        d(className='android.widget.LinearLayout', index=5).child(className='android.widget.ImageView', index=1).click.wait()
        #Stop
        d(className='android.widget.LinearLayout', index=5).child(className='android.widget.ImageView', index=1).click.wait()
        text2 = d(className='android.widget.LinearLayout', index=2).child(className='android.widget.TextView', index=0).text
        print text2

        assert text1!=text2, 'Not playing'
        
        d.press('back')\
         .press('back')
