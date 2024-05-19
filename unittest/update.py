from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest


test_results = []

class Update(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5173')
        self.driver.maximize_window() 
  
        
        
        
        
    def test_update_all(self):
        view_more_btn = self.driver.find_element(By.ID, 'view_more')
        view_more_btn.click()

        WebDriverWait(self.driver, 200).until(
            EC.presence_of_element_located((By.ID, 'update_btn'))
        )

        update_btn = self.driver.find_element(By.ID, 'update_btn')
        update_btn.click()
        time.sleep(3)
        
        
        title = self.driver.find_element(By.ID, 'title')
        title.clear()
        title.send_keys('Updated title')

        
        uploadimg = self.driver.find_element(By.ID, 'user_avatar')
        uploadimg.clear()
        uploadimg.send_keys('https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Start81.png/260px-Start81.png')
        
        content = self.driver.find_element(By.ID, 'content')
        content.clear()
        content.send_keys("Updated content")        
        
        time.sleep(2)

        submit_btn = self.driver.find_element(By.ID, 'update_submit')
        submit_btn.click()
        time.sleep(3)
        
        
        current_url = self.driver.current_url
        if current_url == 'http://localhost:5173/mainpage':
            test_results.append('test update all                      - PASSED')
        else:
            test_results.append('test update all                      - FAILED')
        
    def test_update_title_only(self):
        view_more_btn = self.driver.find_element(By.ID, 'view_more')
        view_more_btn.click()

        WebDriverWait(self.driver, 200).until(
            EC.presence_of_element_located((By.ID, 'update_btn'))
        )

        update_btn = self.driver.find_element(By.ID, 'update_btn')
        update_btn.click()
        time.sleep(3)
        
        
        title = self.driver.find_element(By.ID, 'title')
        title.clear()
        title.send_keys('Updated title')

        time.sleep(2)

        submit_btn = self.driver.find_element(By.ID, 'update_submit')
        submit_btn.click()
        time.sleep(3)
        
        
        current_url = self.driver.current_url
        if current_url == 'http://localhost:5173/mainpage':
            test_results.append('test update title only               - PASSED')
        else:
            test_results.append('test update title only               - FAILED')
        
        
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
    