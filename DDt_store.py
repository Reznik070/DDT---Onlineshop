import unittest
from time import sleep
from selenium import webdriver
import datetime
from ddt import ddt, data, unpack



@ddt
class MyTest_store_ddt(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        print("--------------------------------")
        print("Test Environment Created")
        print("Test_Run began at :" + str(datetime.datetime.now()))

    #@data(*get_data("file.csv")) - Used only when retrieving data from a .csv file - File can be .csv used to store data

    @data(("akemzo07@hotmail.com", "rocker07"),("kemzo07@hotmail.com", "rocker07"),("akmzo07@hotmail.com","ocker07"))
    @unpack

    def test_userLogin(self, EXP_email, EXP_password):

        self.driver.get("http://automationpractice.com/index.php")
        sleep(3)
        print(self.driver.title)
        self.assertEqual("My Store", self.driver.title)
        login = self.driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()
        email = self.driver.find_element_by_xpath("//*[@id='email']").send_keys(EXP_email)
        password = self.driver.find_element_by_xpath("//*[@id='passwd']").send_keys(EXP_password)
        sign_in = self.driver.find_element_by_xpath("//*[@id='SubmitLogin']/span")
        sign_in.click()
        sleep(4)
        # Assertion to ensure only the correct email and password used to sign in actually worked
        self.assertEqual(EXP_email, "akemzo07@hotmail.com")
        self.assertEqual(EXP_password, "rocker07")
        # Assertion to ensure only the correct email and password used to sign in actually worked

        current_page = self.driver.page_source

        if "MY ACCOUNT" in current_page:
            print("Proper sign-in credentials where used and worked as intended")
        else:
            print("Improper sign-in credentials where used and rejected as intended")


    def tearDown(self):
        if self.driver != None:
           print("--------------------------------")
           print("Test Environment Destroyed")
           print("Run completed at :" + str(datetime.datetime.now()))
           self.driver.close()


if __name__ == '__main__':
    unittest.main()
