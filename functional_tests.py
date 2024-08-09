from selenium import webdriver
import unittest

class NewvisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Chrome()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    self.browser.get('http://localhost:8000')
    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the test!')
    #self.fail(f'Browser title was \"{browser.title}\"')

# assert 'To-Do' in browser.title, f'Browser title was \"{browser.title}\"'
if __name__ == '__main__':
  unittest.main(warnings='ignore')
