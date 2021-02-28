#!/usr/bin/env python

from selenium import webdriver

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
        ##self.fail('Finish the test')

        ## She is invited to enter a to-do item

        ## She types 'buy peacock flowers' into a text box

        ## Page should list the item

        ## She enters another to-do item

        ## Page now shows both items

        ## Site has generated a unique URL for her

        ## She visits that URL and the list is still there


if __name__ == '__main__' :
    unittest.main(warnings='ignore')
