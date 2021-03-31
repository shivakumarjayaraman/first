#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest

class NewVisitorTest(unittest.TestCase) :

    def setUp(self) :
        self.browser = webdriver.Firefox()

    def tearDown(self) :
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it(self) :
        # Edith checks out the TO DO list app
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)

        ## She is invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        ## She types 'buy peacock flowers' into a text box
        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER) 
        time.sleep(1) 

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')  1
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)

        ## Page should list the item

        ## She enters another to-do item

        ## Page now shows both items

        ## Site has generated a unique URL for her

        ## She visits that URL and the list is still there


if __name__ == '__main__' :
    unittest.main(warnings='ignore')
