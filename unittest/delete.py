from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


test_results = []


class Delete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5173')
        self.driver.implicitly_wait(10)
        
    def tearDown(self):
        self.driver.close()
        
        
    def test_case1(self):
        view_more_btn = self.driver.find_element_by_xpath("//button[contains(text(), 'View more')]")
        view_more_btn.click()
        time.sleep(1)
        
        delete_btn = self.driver.find_element_by_xpath("//button[contains(text(), 'delete')]")
        delete_btn.click()
        
        if self.driver.current_url == 'http://localhost:5173/':
            test_results.append('Pass')
        else:
            test_results.append('Fail')
            
    def test_case2(self):
        def test_case2(self):
            view_more_btn = self.driver.find_elements_by_xpath("//button[contains(text(), 'View more')]")[2]
            view_more_btn.click()
            time.sleep(1)
            
            delete_btn = self.driver.find_element_by_xpath("//button[contains(text(), 'delete')]")
            delete_btn.click()
            
            if self.driver.current_url == 'http://localhost:5173/':
                test_results.append('Pass')
            else:
                test_results.append('Fail')
            
       
def print_test_results():
    print("\n\n\n")
    print("Result")
    for test_case_name, result in test_results:
        if result:
            print("========================================\n")
            print(f"{test_case_name}\n")
            print(f"Result : {result}\n\n")
        else:
            print("========================================\n")
            print(f"{test_case_name}\n")
            print(f"Result : {result}\n\n")


def execute_tests():
    unittest.main(exit=False)


if __name__ == "__main__":
    execute_tests()
    print_test_results()
    