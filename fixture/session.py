__author__ = 'ja'


class SessionHelper:
    def __init__(self , app):
        self.app = app

    def login(self , username , password):
        wd = self.app.wd
        self.app.open_home_page()
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_id("container").click()

    def logout(self) -> object:
        wd = self.app.wd
        wd.find_element_by_xpath("//form[@class='header']//a[.='Logout']").click()
