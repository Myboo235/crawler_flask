from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import unittest



test_results = []



class GenreByCrawlData(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5173/create')
        self.driver.maximize_window() 
        

        
    def test_generate_data_blog_by_gpt2(self):
        model_gpt2 = self.driver.find_element(By.ID, 'gpt2_submit')
        model_gpt2.click()
        
        WebDriverWait(self.driver, 200).until(
            EC.presence_of_element_located((By.ID, 'keyword'))
        )
        
        key_word = self.driver.find_element(By.ID, 'keyword')
        key_word.send_keys('ronaldo')
        
        time.sleep(2)

        generate_btn = self.driver.find_element(By.ID, 'generate_data')
        generate_btn.click()
        
        WebDriverWait(self.driver, 200).until(
            EC.element_to_be_clickable((By.ID, 'submit'))
        )
        
        submit = self.driver.find_element(By.ID, 'submit')
        submit.click()
        
        time.sleep(5)
        
        if self.driver.current_url == 'http://localhost:5173/mainpage':
            test_results.append('test generate data blog by gpt2      - PASSED')
        else:
            test_results.append('test generate data blog by gpt2      - FAILED')
            
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
    
        
        
        