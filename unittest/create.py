from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





test_results = []



class Create(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5173/create')
        self.driver.maximize_window() 

        
    
        
    def test_response_when_fill_all(self):
        title = self.driver.find_element(By.ID, 'title')
        title.send_keys('test1')
        
        uploadimg = self.driver.find_element(By.ID, 'user_avatar')
        uploadimg.send_keys('https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Start81.png/260px-Start81.png')
        
        content = self.driver.find_element(By.ID, 'content')
        content.send_keys("test")
        
        submit = self.driver.find_element(By.ID, 'submit')
        submit.click()
                
        time.sleep(3)
        
        current_url = self.driver.current_url
        if current_url == 'http://localhost:5173/mainpage':
            test_results.append('Pass')
        else:
            test_results.append('Fail')
            
        
    def test_response_when_not_fill_title(self):
        title = self.driver.find_element(By.ID, 'title')
        title.send_keys('test1')

        submit = self.driver.find_element(By.ID, 'submit')
        submit.click()

        time.sleep(3)
        
        current_url = self.driver.current_url
        if current_url == 'http://localhost:5173/create':
            test_results.append('Pass')
        else:
            test_results.append('Fail')    
      
    
    def test_response_when_not_fill_anything(self):
        submit = self.driver.find_element(By.ID, 'submit')
        submit.click()
        
        time.sleep(3)

        current_url = self.driver.current_url
        if current_url == 'http://localhost:5173/create':
            test_results.append('Pass')
        else:
            test_results.append('Fail')
       
       

    def tearDown(self):
        self.driver.close()
        
        
            
def print_test_results():
    print('Test Results:')
    for i in range(len(test_results)):
        print(f'Test {i+1}: {test_results[i]}')


def execute_tests():
    unittest.main(exit=False)


if __name__ == "__main__":
    execute_tests()
    print_test_results()
    

        
        
