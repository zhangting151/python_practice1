# -*- coding: cp936 -*-

import unittest
from selenium import webdriver
import time
import login


class WordPressTestCase(unittest.TestCase):
    dr = None
    login_url = 'http://localhost/wordpress/wp-login.php'
    post_list_url = 'http://localhost/wordpress/wp-admin/edit.php'

    def setUp(self):
        self.dr = webdriver.Firefox()

    def test_modify_post(self):
        con = login.commen(self.dr)
        con.login()
        title = self.modify_post()
        print title
        self.dr.get(self.post_list_url)
        post_list_table = self.dr.find_element_by_class_name('wp-list-table')
        self.assertTrue(title in post_list_table.text)

        
    def modify_post(self):
        post_name = self.create_post()       
        self.dr.get('http://localhost/wordpress/wp-admin/edit.php')
        list1 = self.dr.find_elements_by_class_name('row-title')
        
        for a in list1:
            if a.text == post_name:
                href = a.get_attribute('href') 
                self.dr.get(href)
                title_or_content = post_name + 'gaigai'
                self.dr.find_element_by_name('post_title').clear()
                self.dr.find_element_by_name('post_title').send_keys(title_or_content)
                js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='" + title_or_content + "'"
                print js
                self.dr.execute_script(js)
                self.dr.find_element_by_id('publish').click()
                return title_or_content
    
    def create_post(self):
        create_post_url = 'http://localhost/wordpress/wp-admin/post-new.php'
        self.dr.get(create_post_url)
        title_or_content = raw_input("please enter your post'name\n")
        self.dr.find_element_by_name('post_title').send_keys(title_or_content)
        js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='" + title_or_content + "'"
        print js
        self.dr.execute_script(js)
        self.dr.find_element_by_name('publish').click()
        return title_or_content
        
        
                
                 
                
    def tearDown(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
