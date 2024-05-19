from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


test_results = []

class Update(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5173')
        self.driver.maximize_window() 
  
        
        
        
        
    def test_case1(self):
        view_more_btn = self.driver.find_element(By.ID, 'view_more')
        view_more_btn.click()
        time.sleep(3)
        
        update_btn = self.driver.find_element(By.ID, 'update_btn')
        update_btn.click()
        time.sleep(3)
        
        
        title = self.driver.find_element(By.ID, 'title')
        title.clear()
        title.send_keys('Updated title')
        
        
        submit_btn = self.driver.find_element(By.ID, 'update_submit')
        submit_btn.click()
        time.sleep(3)
        
        
        current_url = self.driver.current_url
        if current_url == 'http://localhost:5173/mainpage':
            test_results.append( 'Pass')
        else:
            test_results.append('Fail')
            
    def test_case2(self):
        view_more_btn = self.driver.find_element(By.ID, 'view_more')
        view_more_btn.click()
        time.sleep(3)
        
        update_btn = self.driver.find_element(By.ID, 'update_btn')
        update_btn.click()
        time.sleep(3)
        
        
        title = self.driver.find_element(By.ID, 'content')
        title.clear()
        title.send_keys('Updated content')
        time.sleep(3)
        
        
        submit_btn = self.driver.find_element(By.ID, 'update_submit')
        submit_btn.click()
        time.sleep(3)
        
        
        current_url = self.driver.current_url
        if current_url == 'http://localhost:5173/mainpage':
            test_results.append( 'Pass')
        else:
            test_results.append('Fail')
        
        
    def tearDown(self):
        self.driver.close()
     
            
   
        
            
def print_test_results():
    print("\n\n\n")
    print("======")
    print("Result")
    for i in range(len(test_results)):
        print(f"Test case {i+1}: {test_results[i]}")


def execute_tests():
    unittest.main(exit=False)


if __name__ == "__main__":
    execute_tests()
    print_test_results()
    