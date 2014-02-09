from selenium import webdriver

class commen:
    def __init__(self,dr):
        self.dr = dr

    def login(self):
        self.dr.get('http://localhost/wordpress/wp-login.php')
        self.dr.find_element_by_name('log').send_keys('admin')
        self.dr.find_element_by_name('pwd').send_keys('111111')
        self.dr.find_element_by_name('wp-submit').click()


