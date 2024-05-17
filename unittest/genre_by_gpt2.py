from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest



test_results = []



class GenreByCrawlData(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5173/create')
        self.driver.maximize_window() 
        

        
    def test_case1(self):
        model_gpt2 = self.driver.find_element(By.ID, 'gpt2_submit')
        model_gpt2.click()
        
        time.sleep(5)
        
        
        key_word = self.driver.find_element(By.ID, 'keyword')
        key_word.send_keys('ronaldo')
        time.sleep(2)
        
        generate_btn = self.driver.find_element(By.ID, 'generate_data')
        generate_btn.click()
        
        time.sleep(120)
        
        submit = self.driver.find_element(By.ID, 'submit')
        submit.click()
        
        time.sleep(5)
        
        if self.driver.current_url == 'http://localhost:5173/mainpage':
            test_results.append('Pass')
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
    
        
        
        