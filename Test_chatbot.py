from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constants import globalConstants as c
from time import sleep

class Test_tobetoPlatformLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.set_window_size(827, 728)

    def teardown_method(self):
        self.driver.quit()

    # 1) Giriş yap alanı görüntülenebilir ve işlevselliği test edilecektir.
    def test_visibility_of_login_page(self):
       
       self.driver.execute_script("window.scrollTo(0,5600)")
       sleep(8)
       iframe_element = self.driver.find_element(By.ID, "exw-launcher-frame")
       self.driver.switch_to.frame(iframe_element)

    # İlgili HTML elementini bulup tıkla
       chat_bot_button = self.driver.find_element(By.XPATH, "//img[contains(@src,'https://tobeto.services.exairon.com/uploads/channels/launcher_button_1.svg')]")
       chat_bot_button.click()

    
      

   