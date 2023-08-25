# app.py - The main executable file
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from Test_locators import locators
from Test_data import data
import pytest


class Test_Logimax:
    @pytest.fixture
    

    def booting_function(self):
       self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
       self.driver.get(data.Logi_Data().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(5)
  
  
    def test_vendor_registration(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(8)
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT,value=locators.Logi_Locators().Inventory_module).click()
        sleep(5)
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT,value=locators.Logi_Locators().Lot_Inward_entry).click()
        sleep(6)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().add_lot).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().gold_smith).click()
        sleep(5)
        karigar = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        karigar.send_keys('SHANKAR A 712')
        karigar.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().category).click()
        sleep(5)
        category = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        category.send_keys('GOLD RING & COIN')
        category.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().purity).click()
        sleep(5)
        purity_va = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        purity_va.send_keys('95.0000')
        purity_va.send_keys(Keys.RETURN) 
        sleep(5)
        drop_down = self.driver.find_element(by=By.ID,value=locators.Logi_Locators().branch_division)
        drop_down_list = Select(drop_down)
        drop_down_list.select_by_value('5')
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().lot_add_item).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().product).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().product_list).click()
        sleep(5)
        drop_down_1 = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().design_for)
        design_list = Select(drop_down_1)
        design_list.select_by_value('2')
        sleep(5)
        number = 2
        NO_of_pcs = self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().pieces)       
        NO_of_pcs.send_keys(number) 
        sleep(5)
        number_1 = 400
        gross_wt = self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().gross_wgt)       
        gross_wt.send_keys(number_1) 
        sleep(5)
        number_2 = 20
        less_wt = self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().less_wgt)       
        less_wt.send_keys(number_2) 
        sleep(5)
        number_3 = 12
        wast = self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().wast)       
        wast.send_keys(number_3) 
        sleep(5)
        number_4 = 500
        making_char = self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().making_charge)       
        making_char.send_keys(number_4) 
        sleep(4)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().add_layout).click()
        sleep(4)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().save_all).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : Lot inward  added successfully gold_smith : {a}, category: {b},purity : {c},pieces:{d},gross_wgt{e},less_wgt{f},wast{g},making_charge : {h}". format(a = 'SHANKAR A 712', b= 'GOLD RING & COIN', c='95.0000', d=number, e=number_1, f=number_2, g=number_3, h=number_4))
        
        
        