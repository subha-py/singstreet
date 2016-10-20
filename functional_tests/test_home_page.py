from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from .base import FunctionalTest
from django.test import tag
class NewVisitorTest(FunctionalTest):

    @tag('functional')
    def test_can_start_a_list_and_retrive_it_later(self):
        '''
        Edith has heard about a cool new online song app.She goes
        to check out its homepage
        '''
        # self.browser.get(self.server_url)
        #
        # #she notices the page title and header mention singstreet
        # self.assertIn('singstreet',self.browser.title)
        # header_text=self.browser.find_element_by_tag_name('h1').text
        # self.assertIn('singstreet',header_text)
        #
        # # she is invited to search straight away
        #
        # inputbox=self.get_item_input_box()
        # self.assertEqual(
        #     inputbox.get_attribute('placeholder'),
        #     'search'
        # )
        #
        # #She types 'The Riddle of the model' into a text box (Edith's is
        # # a big fan of sing street band )
        # inputbox.send_keys('The Riddle of the model')
        #
        # #When she hits enter, the page updates, and now the page 'song view' shows
        # #Riddle of the model
        # inputbox.send_keys(Keys.ENTER)
        # edith_list_url=self.browser.current_url
        # self.assertRegex(edith_list_url,'/songs/.+')
        # self.check_for_song_in_page('riddle of the model')
        # #There is still a text box inviting her to go to another page. She
        # #enters another song name Drive it Like You Stole It
        # inputbox=self.get_item_input_box()
        # inputbox.send_keys('drive it like you stole it')
        # inputbox.send_keys(Keys.ENTER)
        # #The page updates again, and now shows both items on her list
        # inputbox.send_keys(Keys.ENTER)
        # edith_list_url = self.browser.current_url
        # self.assertRegex(edith_list_url, '/song/.+')
        # self.check_for_song_in_page('riddle of the model')
        # #Now a new user, Francis, comes along to the site.
        #
        # #We use a new browser session to make sure that no information
        # ##of Edith's is coming through from cookies etc
        # self.browser.quit()
        # self.browser=webdriver.Firefox()
        # self.browser.get(self.server_url)
        # #Francis starts a new list by enteriing a new iitem. He
        # #is less interesting than Edith..
        #
        # inputbox=self.get_item_input_box()
        # inputbox.send_keys('Buy milk')
        # inputbox.send_keys(Keys.ENTER)
        #
        # #francis gets his own unique URL
        # francis_list_url=self.browser.current_url
        # self.assertRegex(francis_list_url,'/lists/.+')
        # self.assertNotEqual(francis_list_url,edith_list_url)
        #
        # #Again,there is no trace of Ediith's List
        # page_text=self.browser.find_element_by_tag_name('body').text
        # self.assertNotIn('Buy peacock feathers',page_text)
        # self.assertIn('Buy milk',page_text)
        #
        # #Satisfied, they both go back to sleep
