# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import unittest

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC




# test_results = []



# class Add(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get('http://localhost:5173/create')
#         self.driver.implicitly_wait(10)

#     def tearDown(self):
#         self.driver.close()
        
        
        
#     def test_case1(self):
#         parent_element = self.driver.find_element_by_xpath("//parent_element_xpath")
#         title_textarea = parent_element.find_element_by_id("title")
        
#         title_textarea = self.driver.find_element_by_id("title")
#         title_textarea.send_keys("Your input text")
        
#         uploadimg = self.driver.find_element_by_xpath("//input[@name='image']")
#         uploadimg.send_keys('https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Start81.png/260px-Start81.png')
        
#         content = self.driver.find_element_by_xpath("//textarea[@name='content']")
#         content.send_keys('Mục tiêu của Wikipedia tiếng Việt ngày một phát triển. Đây là một trong 88 chòm sao mờ trên bầu trời bán cầu bắc và là chòm sao Ptolemy và là chòm sao hiện đại được Liên đoàn Thiên văn Quốc tế công nhận. Đây là một trong 88 chòm sao Ptolemy và là một trong 88 chòm sao có diện tích nhỏ thứ ba. Sự phát triển của Wikipedia tiếng Việt ngày một phát triển. Delta, Epsilon, Zeta và Theta Sagittae là sao sáng nhất trong chòm sao Ptolemy và là chòm sao hiện đại được Liên đoàn Thiên văn Quốc tế công nhận. Đây là một chòm sao có diện tích nhỏ thứ ba. Thiên Tiễn là một trong 48 chòm sao mờ trên bầu trời bán cầu bắc và là một trong 48 chòm sao có diện tích nhỏ thứ ba. Mục tiêu của Wikipedia tiếng Việt ngày một phát triển. Đây là một trong 48 chòm sao có diện tích nhỏ thứ ba. Delta, Epsilon, Zeta và Theta Sagittae là sao sáng nhất trong chòm sao mờ trên bầu trời bán cầu bắc và là chòm sao hiện đại được Liên đoàn Thiên văn Quốc tế công nhận.')
        
#         submit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
#         self.driver.execute_script("arguments[0].scrollIntoView();", submit)
#         submit.click()
        
#         time.sleep(2)
        
#         if self.driver.current_url == 'http://localhost:5173/':
#             test_results.append('Pass')
#         else:
#             test_results.append('Fail')
            
    
#     # def test_case2(self):
#     #     create_button = self.driver.find_element_by_xpath("//a[@href='/create']")
#     #     create_button.click()
      
#     #     title = self.driver.find_element_by_xpath("//input[@name='title']")
        
#     #     title.send_keys('test')
        
#     #     uploadimg = self.driver.find_element_by_xpath("//input[@name='image']")
#     #     uploadimg.send_keys('https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Start81.png/260px-Start81.png')
        
#     #     content = self.driver.find_element_by_xpath("//textarea[@name='content']")
#     #     content.send_keys('Mục tiêu của Wikipedia tiếng Việt ngày một phát triển. Đây là một trong 88 chòm sao mờ trên bầu trời bán cầu bắc và là chòm sao Ptolemy và là chòm sao hiện đại được Liên đoàn Thiên văn Quốc tế công nhận. Đây là một trong 88 chòm sao Ptolemy và là một trong 88 chòm sao có diện tích nhỏ thứ ba. Sự phát triển của Wikipedia tiếng Việt ngày một phát triển. Delta, Epsilon, Zeta và Theta Sagittae là sao sáng nhất trong chòm sao Ptolemy và là chòm sao hiện đại được Liên đoàn Thiên văn Quốc tế công nhận. Đây là một chòm sao có diện tích nhỏ thứ ba. Thiên Tiễn là một trong 48 chòm sao mờ trên bầu trời bán cầu bắc và là một trong 48 chòm sao có diện tích nhỏ thứ ba. Mục tiêu của Wikipedia tiếng Việt ngày một phát triển. Đây là một trong 48 chòm sao có diện tích nhỏ thứ ba. Delta, Epsilon, Zeta và Theta Sagittae là sao sáng nhất trong chòm sao mờ trên bầu trời bán cầu bắc và là chòm sao hiện đại được Liên đoàn Thiên văn Quốc tế công nhận.')
#     #     submit = self.driver.find_element_by_xpath("//button[@type='submit']")
#     #     submit.click()
        
#     #     if self.driver.current_url == 'http://localhost:5173/':
#     #         test_results.append('Pass')
#     #     else:
#     #         test_results.append('Fail')
            
        
        
            
# def print_test_results():
#     print("\n\n\n")
#     print("Result")
#     for test_case_name, result in test_results:
#         if result:
#             print("========================================\n")
#             print(f"{test_case_name}\n")
#             print(f"Result : {result}\n\n")
#         else:
#             print("========================================\n")
#             print(f"{test_case_name}\n")
#             print(f"Result : {result}\n\n")


# def execute_tests():
#     unittest.main(exit=False)


# if __name__ == "__main__":
#     execute_tests()
#     print_test_results()
    

        
        
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # or webdriver.Chrome(), etc.
        self.driver.get('http://localhost:5173/create')  # replace with your URL

    def test_form_submission(self):
        title = self.driver.find_element(By.ID, "title")
        title.send_keys('test')
        
        
        uploadimg = self.driver.find_element(By.ID, "user_avatar")
        uploadimg.send_keys('https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Start81.png/260px-Start81.png')

        content = self.driver.find_element(By.ID,"content")
        content.send_keys('Mục tiêu của Wikipedia tiếng Việt ngày một phát triển')

        submit = self.driver.find_element(By.ID,"submit")
        submit.click()
        
        time.sleep(15)

        WebDriverWait(self.driver, 10).until(EC.url_changes(self.driver.current_url))

        self.assertEqual(self.driver.current_url, 'http://localhost:5173/')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()