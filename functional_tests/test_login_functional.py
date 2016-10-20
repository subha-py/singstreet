from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from .base import FunctionalTest
from django.test import tag
from django.test.utils import override_settings

class NewVisitorTest(FunctionalTest):

    @tag('functional')
    @override_settings(DEBUG=True)
    def test_can_login_by_google(self):
        '''
        Edith has heard about a cool new online song app.She goes
        to check out its homepage and tries to login
        '''
        #Edith see homepage have a login option
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('artist_login').click()
        #she clicks it adn get redirected to login page
        edith_login_url = self.browser.current_url
        self.assertIn('login',edith_login_url)
        #TODO : Try to find a way to test google and facebook login
        #she goes to the login page
        #it have option of login via google
        #she clicks login via google
        #she is redirected to google login page
        #she give her password
        #she is then asked to put her location and country
        #she then put the location and country
        #she is redirected to profile view page
        #she see all her information there