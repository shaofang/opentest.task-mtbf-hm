#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class ContactTest(unittest.TestCase):
    def setUp(self):
        super(ContactTest, self).setUp()
        u.setup(d)

    def tearDown(self):
        super(ContactTest, self).tearDown()
        u.teardown(d)

    def testContact(self):
        c_name = 'aaatest'
        c_number = '12345678901'
        #Launch Contacts and check if sucessful
        d.start_activity(component='com.android.contacts/.activities.PeopleActivity')
        assert d(text='New contact', className='android.widget.Button').wait.exists(timeout=5000), 'can not launch contacts in 5s'

        #Delete the contact with the same name, will be added.
        if d(text=c_name).wait.exists(timeout=1000):
        	d(text=c_name).long_click()
        	d(text='Delete').click.wait()
        	d(text='Delete', className='android.widget.Button').click.wait()

        #New contact
        d(text='New contact', className='android.widget.Button').click.wait()

        d(text='Create  contact', className='android.widget.TextView').wait.exists(timeout=5000), 'Can not switch to create contact activity in 5s'
        d(text='Name', className='android.widget.EditText').set_text(c_name)
        assert d(text=c_name), 'Input name failed.'
        d(text='Phone', className='android.widget.EditText').set_text(c_number)
        assert d(text=c_number), 'Input number failed.'
        d(text='OK', className='android.widget.Button').click.wait()	

        #Delete the contact
        assert d(text='About').wait.exists(timeout=3000), 'Add contact failed'
        d.press('menu')
        d(text='Delete', className='android.widget.TextView').click.wait()
        d(text='Delete', className='android.widget.Button').click.wait()
        assert d(text='New contact').wait.exists(timeout=3000), 'Back to contacts list in 3s'
