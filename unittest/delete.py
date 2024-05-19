from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import unittest


test_results = []


class Delete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5173')
        self.driver.maximize_window() 
    
        
        
    def test_delete_acticle(self):
        view_more_btn = self.driver.find_element(By.ID, 'view_more')
        view_more_btn.click()
        
        time.sleep(3)

        WebDriverWait(self.driver, 200).until(
            EC.element_to_be_clickable((By.ID, 'delete_btn'))
        )
        
        delete_btn = self.driver.find_element(By.ID, 'delete_btn')
        delete_btn.click()
        
        
        time.sleep(3)
        
        current_url = self.driver.current_url
        if current_url == 'http://localhost:5173/mainpage':
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
    