from selenium import webdriver
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException
import csv
from selenium.webdriver.common.keys import Keys 


URL = 'https://edadeal.ru/moskva/retailers/5ka'
HEADERS = { 'user - agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36',
  'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
HOST = 'https://edadeal.ru'  
FILE = 'product.csv'  



browser = webdriver.Chrome()
browser.maximize_window ()
browser.get('https://edadeal.ru/moskva/offers?retailer=avoska')
time.sleep(3)
#https://edadeal.ru/moskva/offers?retailer=5ka&retailer=avoska&retailer=billa&retailer=dixy&retailer=magnit-univer&retailer=perekrestok&retailer=verno&retailer=victoria&retailer=vkusvill
z=[]
list_of_name = ['Продукты', 'Алкоголь', 'Для дома', 'Косметика и гигиена']
#list_of_name = ['Алкоголь']

button_len = browser.find_elements_by_class_name('b-button__root')
counter_=int(button_len[-2].text) #количество страниц
button_len2 = browser.find_elements_by_class_name('b-accordion__item2')#наименование подкатегорий
c=1
def incr():
    global c
    c += 1
def decr():
    global c 
    c-=1

def FUNC(lll):
    incr()
    print(c)
    for i in lll:
        search_from = browser.find_element_by_tag_name('html')
        #search_from.send_keys(Keys.PAGE_DOWN)
        browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
        continue_link = browser.find_element_by_link_text('{}'.format(i))                
        continue_link.click()
        browser_wait = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'b-image__root')))
        button_items = [i.text for i in browser.find_elements_by_class_name('b-accordion__item{}'.format(c))]
        if button_items:
            print(button_items)
            FUNC(button_items)    
        else: print("ggg") 
        #FUNC(button_items)    
    decr()
    print(c)



FUNC(list_of_name)
#for i in list_of_name:
 #       continue_link = browser.find_element_by_partial_link_text('{}'.format(i))
  #      continue_link.click()
   #     button_items = [i.text for i in browser.find_elements_by_class_name('b-accordion__item2')]#наименование подкатегорий
    #    print(button_items)
     #   for j in button_items:
      #          button_link = browser.find_element_by_partial_link_text('{}'.format(j))
       #         button_link.click()
        #        button_items2 = [i.text for i in browser.find_elements_by_class_name('b-accordion__item3')]
         #       print(button_items2)
          #      for r in button_items2:
           #         button_link = browser.find_element_by_link_text('{}'.format(r))
            #        button_link.click()
             #       time.sleep(5)
#for j in range(counter_):

        #browser_wait = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'b-offer__price-old')))
#        time.sleep(random.randint(3, 5))
 #       search_from = browser.find_element_by_tag_name('html')
  #      productimg = browser.find_elements_by_class_name('b-image__img')#.get_attribute('src')
   #     product_img = productimg[::2]
    #    card_product_date = browser.find_elements_by_class_name('b-offer__dates')
     #   card_product_name = browser.find_elements_by_class_name('b-offer__description')
      #  card_product_price_new = browser.find_elements_by_class_name('b-offer__price-new')
       # card_product_price_old = browser.find_elements_by_class_name('b-offer__price-old')
        #for i in range(len(card_product_date)):
         #       page_list_product = [card_product_date[i].text, card_product_name[i].text,\
          #                           card_product_price_new[i].text, product_img[i].get_attribute('src')]
           #     z.append(page_list_product)
        #
      #  try:
       #         continue_link.click()
        #        
     #   except Exception:
        #        pass
                

#with open('product.csv','w', encoding ='utf16', newline='') as file:
 #       writer = csv.writer(file, delimiter=';')
  #      writer.writerow(['дата','название','цена со скидкой','картинка'])
   #     for item in z:
    #        writer.writerow([item[0], item[1], item[2], item[3]])

#with open('namep_roduct.csv','w', encoding ='utf16', newline='') as file:
 #       writer = csv.writer(file, delimiter=';')
  #      writer.writerow(['название'])
   #     for item in z:
    #        writer.writerow([item[1]])

