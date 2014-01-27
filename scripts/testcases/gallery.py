
#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class GalleryTest(unittest.TestCase):
    def setUp(self):
        super(GalleryTest, self).setUp()
        u.setup(d)

    def tearDown(self):
        super(GalleryTest, self).tearDown()
        u.teardown(d)

    def testGallery(self):
        #Launch gallery and check if successful
        d.start_activity(component='com.miui.gallery/.app.Gallery')
        assert d(textStartsWith='Cloud', className='android.widget.TextView').wait.exists(timeout=5000), 'Launch gallery failed in 5s'
        d(textStartsWith='Cloud', className='android.widget.TextView').click.wait()
        assert d(text='New', className='android.widget.TextView').wait.exists(timeout=5000), 'Switch to cloud images failed in 5s'
        
        #Select and open the cloud gallery
        d.click(510,331)
        u.sleep(2)
        d.click(111,222)
        u.sleep(3)
        for m in range(3):
            for i in range(5):
        	    d().swipe.left()
            for i in range(5):
        	    d().swipe.right()
        d.press('back')
        u.sleep(1)
        d.press('back')
        u.sleep(1)


