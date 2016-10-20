from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from unittest import skip
import time
import sys
class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url='http://'+arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url=cls.live_server_url
    @classmethod
    def tearDownClass(cls):
        if cls.server_url==cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser=webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_song_in_page(self,row_text):
        pass


    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_search')
