# Georgios Gerasimos Leventopoulos (csd4152)
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time
import csv

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def alreadyLoggedIn():
    xpath_list = []
    class_list = ["logout", "account-block", "link-out"]
    id_list = ["my-account"]
    name_list = []
    
    sign_out_button = find(xpath_list, class_list, id_list, name_list)
    if sign_out_button=="":
        return False
    return True

# Returns a web element if found, else returns an empty string
def check_exists_by_xpath(xpath_list):
    for item in xpath_list:
        try:
            driver.find_element_by_xpath(item)
            return driver.find_element_by_xpath(item)
        except NoSuchElementException:
            pass
    return ""

def check_exists_by_class_name(class_list):
    for item in class_list:
        try:
            driver.find_element_by_class_name(item)
            return driver.find_element_by_class_name(item)
        except NoSuchElementException:
            pass
    return ""

def check_exists_by_id(id_list):
    for item in id_list:
        try:
            driver.find_element_by_id(item)
            return driver.find_element_by_id(item)
        except NoSuchElementException:
            pass
    return ""

def check_exists_by_name(name_list):
    for item in name_list:
        try:
            driver.find_element_by_name(item)
            return driver.find_element_by_name(item)
        except NoSuchElementException:
            pass
    return ""        

def verifyLogin():
    xpath_list, class_list, id_list, name_list = ["//ul[contains(@class, 'ps-alert-error alert alert-danger')]", "//*[@id='create_account_error']"], ["alert alert-danger",  "help-block  alert alert-danger", "help-block"], [], []
    signin_error = find(xpath_list, class_list, id_list, name_list)
    if signin_error != "":
        return False
    else:
        return True

def verifySignup():
    return True

def verifyAddItem(numberOfProductsUserWants):
    xpath_list, class_list, id_list, name_list = ["//span[contains(@class, 'ajax_cart_quantity')]", "//span[contains(@class, 'data-cart-count')]"], [], [], []
    cart_number = find(xpath_list, class_list, id_list, name_list)
    if cart_number == "":
        return False

    currentNumberOfProducts = cart_number.get_attribute("value")
    if currentNumberOfProducts == "": #cannot find the current number of products
        return False

    if currentNumberOfProducts == numberOfProductsUserWants:
        return True
    return False

def verifyRemoveItem():
    return True

def verifySearch():
    xpath_list, class_list, id_list, name_list = [], ["page-heading product-listing"], [], []
    searchElement = find(xpath_list, class_list, id_list, name_list)
    if searchElement != "":
        return True
    return False

def verifySubscribeNewsletter():
    xpath_list, class_list, id_list, name_list = ["//input[contains(@class, 'newsletter_error')]"], [], [], []
    newsletter_error = find(xpath_list, class_list, id_list, name_list)
    if newsletter_error == "":
        return True
    else:
        return False

def verifyEditAccountDetails():
    xpath_list = [""]
    class_list = ["alert alert-danger",  "help-block  alert alert-danger", "help-block"]
    id_list = []
    name_list = []
    error = find(xpath_list, class_list, id_list, name_list)
    if error != "":
        return False
    return True

def verifyCheckoutCard():
    return True

def visit(website):
    driver.get(website)
    driver.maximize_window()

def detect():
    xpath_list = ["//*[@id='header-user-btn']", "//*[@id='_desktop_user_info']", "//*[@id='header_user_info']", "//*[@id='mobile_links']", "//*[@id='page']"]
    class_list = ["login", "account-block", "popup-title", "al-logged-account"]
    id_list = ["user_info"]
    name_list = []
    # driver.getPageSource().contains("Prestashop");
    # If it does not find attributes that Prestashop CMS has, then it returns False
    if find(xpath_list, class_list, id_list, name_list)=="":
        return False
    return True

def login():
    xpath_list = ["//a[contains(@href, 'my-account')]", "//*[@id='header_user_info']", "//div[contains(@class, 'header_user_info')]", "//a[contains(@href, 'mon-compte')]", "//*[@id='header-user-btn']", "//div[contains(@class, 'menu_profile user_panel')]", "//div[contains(@class, 'account')]", "//a[contains(@class, 'login')]", "//*[@id='_desktop_user_info']", "//*[@id='mobile_links']", "//*[@id='contact-link']/a[2]", "//*[@id='header_customer_login']", "//*[@id='header-login']/div"]
    class_list = ["header_user_info", "tvcmsmobile-account-button", "login", "account", "account-link", "account-block", "popup-title", "al-logged-hello", "al-logged-account", "account cif-book", "blockuserinfo header-box", "hidden-sm hidden-xs", "til_user" "am_menu_mon_compte_link"]
    id_list = ["header_user_info", "user_info", "BlockLogin", "user_info", "btnLoginHeader_113"]
    name_list = []
    login_page = find(xpath_list, class_list, id_list, name_list)
    if login_page == "" or login_page.is_displayed() == False:
        print("Can't find login page.")
        return False
    else:
        login_page.click()
        time.sleep(2)

    xpath_list, class_list, id_list, name_list = [["//*[@id='mail_input_long']", "//*[@id='signin_login_input']","//*[@id='email']", "//input[contains(@name, 'email')]"], [], ["email"], ["email", "login"]]
    mail_field = find(xpath_list, class_list, id_list, name_list)
    if mail_field !="" and mail_field.is_displayed():
        mail_field.send_keys(gmail)
    time.sleep(1)

    xpath_list,class_list,id_list,name_list = ["//*[@id='pass_input_long']", '//input[contains(@name, "password")]'],[],["passwd", "password"],["passwd", "password"]
    passfield = find(xpath_list,class_list,id_list,name_list)
    if passfield != "" and passfield.is_displayed():
        passfield.send_keys(password)
        passfield.send_keys(Keys.RETURN)
    time.sleep(2)
    # Verify
    if verifyLogin() == True:
        return True
    return False

def signup():
    xpath_list = ["//a[contains(@href, 'account')]", "//*[@id='header_user_info']", "//div[contains(@class, 'user_info')]", "//div[contains(@class, 'header_user_info')]", "//a[contains(@href, 'mon-compte')]", "//*[@id='header-user-btn']", "//div[contains(@class, 'menu_profile user_panel')]", "//div[contains(@class, 'account')]", "//a[contains(@class, 'login')]", "//*[@id='_desktop_user_info']", "//*[@id='mobile_links']", "//*[@id='contact-link']/a[2]", "//*[@id='header_customer_login']", "//*[@id='header-login']/div"]
    class_list = ["header_user_info", "tvcmsmobile-account-button", "login", "account", "account-link", "account-block", "popup-title", "al-logged-hello", "al-logged-account", "account cif-book", "blockuserinfo header-box", "hidden-sm hidden-xs", "til_user" "am_menu_mon_compte_link"]
    id_list = ["header_user_info", "user_info", "BlockLogin", "user_info", "btnLoginHeader_113"]
    name_list = []
    signup_page = find(xpath_list, class_list, id_list, name_list)
    if signup_page == "":
        print("Can't find signup page.")
        return False
    else:
        signup_page.click()
        time.sleep(2)
    time.sleep(2)

    xpath_list, class_list, id_list, name_list = ["//input[contains(@name, 'email_create')]", "//*[@id='email_create']"], [], [], []
    email_input = find(xpath_list, class_list, id_list, name_list)
    if email_input == "":
        print("Can't find signup page.")
        return False
    else:
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)
        time.sleep(2)

    xpath_list,class_list,id_list,name_list = ["//input[contains(@name, 'firstname')]"], ["firstname"], ["firstname"], ["firstname"]
    firstname_field = find(xpath_list, class_list, id_list, name_list)
    if firstname_field !="":
        firstname_field.send_keys(firstname)
    time.sleep(2)

    xpath_list,class_list,id_list,name_list = ["//input[contains(@name, 'lastname')]"], ["lastname"], ["lastname"], ["lastname"]
    lastname_field = find(xpath_list, class_list, id_list, name_list)
    if lastname_field !="":
        lastname_field.send_keys(lastname)
    time.sleep(2)

    xpath_list,class_list,id_list,name_list = ["//input[contains(@name, 'address')]"], ["email_address"],["email_address"],["email"]
    address_field = find(xpath_list, class_list, id_list, name_list)
    if address_field !="":
        address_field.send_keys(address)
    time.sleep(2)

    xpath_list,class_list,id_list,name_list = [""],[],["password"],["passwd", "password"]
    passfield = find(xpath_list,class_list,id_list,name_list)
    if passfield !="":
        passfield.send_keys(password)
    time.sleep(2)

    xpath_list,class_list,id_list,name_list = [],[],["password-confirmation"],["password_confirmation"]
    passfield = find(xpath_list,class_list,id_list,name_list)
    if passfield !="":
        passfield.send_keys(password)
    time.sleep(2)
   # checkBox = driver.find_element_by_class_name("checkbox")
   # checkBox.click()
    passfield.send_keys(Keys.RETURN)
    if verifySignup() == True:
        return True
    return False

def locateItem():
    time.sleep(3)
    product_urls = []
    xpath_list = ["//div[contains(@class, 'product-img')]", "//a[contains(@class, 'product')]", "//a[contains(@class, 'grid-view-item')]", "//a[contains(@id, 'link')]", "//a[contains(@id, 'pro_first_box')]", "//a[contains(@class, 'item-content')]"] # "//a[contains(@class, 'content_img')]", "//a[contains(@class, 'product')]"]
    for xpath in xpath_list:
        products = driver.find_elements_by_xpath(xpath)
        #print(products)
        if len(products) > 0:
            break

    for product in products:
        product_urls.append(product.get_attribute("href"))
    if len(product_urls)>0 and product_urls[0] == None:
        return []
    #print(len(product_urls))
    #print(product_urls)
    return product_urls    

def addItem(numberOfProductsUserWants):
    if numberOfProductsUserWants <= 0:
        return False

    products = locateItem()

    if len(products) <= 0:
        print("cannot find products")
        return False

    for i in range(0, numberOfProductsUserWants):
        visit(products[i])
        time.sleep(2)

        xpath_list, class_list, id_list, name_list = ["//button[contains(@data-button-action, 'add-to-cart')]", "//button[contains(@name, 'add')]", "//*[@id='add_to_cart']/button", "//button[contains(@name, 'Submit')]", "//p[contains(@id, 'add_to_cart')]", "//button[contains(@class, 'add-to-cart')]", "//button[contains(@name, 'submit')]", "//button[@type='submit']", "//button[contains(@type, 'submit')]", "//*[@id='add_to_cart']/button", "//button[contains(@class, 'btn product-form__cart-submit')]", "//*[@id='productDetailPageBuyProductForm']/div/div[2]/button", "//*[@id='ap5-add-to-cart']/button"], ["add"], [], ["Submit"]
        add_to_card_button = find(xpath_list, class_list, id_list, name_list)
        time.sleep(1)
        if add_to_card_button != "" and add_to_card_button.is_displayed()==True and add_to_card_button.is_enabled()==True:
            add_to_card_button.click()
            time.sleep(2)

    if verifyAddItem(numberOfProductsUserWants) == True:
       return True
    return False

def removeItem(numberOfProductsUserWants):
    # Go to the shopping list
    time.sleep(4)
    xpath_list, class_list, id_list, name_list = ["a//[contains(@href, 'cart')]", "//div[contains(@class, 'cart')]", "//li[contains(@class, 'cart')]", "//a[contains(@href, 'order')]", "//a[contains(@href, 'comanda-rapida')]", "//div[contains(@class, 'shopping_cart')]", "//div[contains(@class, 'cart cif-book')]", "//*[@id='shopping_cart']", "//div[contains(@class, 'cart')]", "//*[@id='menu_basket']/a", "//*[@id='_desktop_cart']/div/div/a", "//a[contains(@href, 'action=show')]", "//a[contains(@href, 'cart')]", "//a[contains(@class, 'cart')]", "//*[@id='block_cart_button']"], ["cart-dropdow-button"], [], []
    cart_page = find(xpath_list, class_list, id_list, name_list)
    if cart_page == "":
        return False
    else:
        temp = cart_page.get_attribute("href") 
        visit(temp)
        #shopping_list.click()
    time.sleep(2)

    # Find and delete the product
    xpath_list, class_list, id_list, name_list = ["//a[contains(@class, 'remove-from-cart')]", "//a[contains(@class, 'cart_quantity_delete')]", "//a[contains(@class, 'remove')]"], ["remove-from-cart", "cart_quantity_delete", "remove"], [], []
    remove_from_card_button = find(xpath_list, class_list, id_list, name_list)
    if remove_from_card_button != "":
        remove_from_card_button.click()     # click delete button
        time.sleep(2)
        return True
    if verifyRemoveItem() == True:
        return True
    return False

def search(searchTerm):
    xpath_list, class_list, id_list, name_list = ["//div[contains(@class, 'search')]", "//*[@id='search_widget']", "//*[@id='search_widget']/span/i" "//*[@id='header-search-btn']"], [], [], []
    search_drop_bar = find(xpath_list, class_list, id_list, name_list)
    if search_drop_bar != "" and search_drop_bar.is_displayed() == True and search_drop_bar.is_enabled():
        search_drop_bar.click()
    time.sleep(1)
    
    xpath_list, class_list, id_list, name_list = ["//*[@id='search_query_top']", "//input[contains(@name, 'search')]", "//*[@id='search_widget']/form/input[2]", "//*[@id='search_query']", "//*[@id='collapseSearch']/form/div/input", "//input[contains(@id, 'search')]", "//input[contains(@class, 'search')]", "//*[@id='search_query_top']", "//*[@id='search']"], [], [], []
    search_bar = find(xpath_list, class_list, id_list, name_list)
    if search_bar == "" or search_bar.is_displayed() == False:
        return False
    else:
        search_bar.send_keys(searchTerm)
        search_bar.send_keys(Keys.RETURN) #press Enter

    if verifySearch() == True:
        return True
    return False

def checkoutCard():
    # add one item just to be sure
    if addItem(1) == True:
        xpath_list, class_list, id_list, name_list = ["//a[contains(@href, 'cart')]", "//a[contains(@href, 'order')]"], [""], [], [""] # find checkout button
        checkoutButton = find(xpath_list, class_list, id_list, name_list)
        if checkoutButton != "":
            checkoutButton.click()   # click checkout button
        return True
    if verifyCheckoutCard() == True:
        return True
    return False

def changeFirstName(newFirstName):
    if login() == False:
        return False

    driver.find_element_by_xpath('//a[contains(@href, "%s")]' % "identity").click()
    time.sleep(3)

    name = driver.find_element_by_xpath("//*[@id='firstname']")
    name.clear()
    name.send_keys(newFirstName)
    
    passwd = driver.find_element_by_xpath("//*[@id='old_passwd']")
    passwd.clear()
    passwd.send_keys(password) #current password
    time.sleep(2)
    driver.find_element_by_id("psgdpr-consent").click()
    driver.find_element_by_name("submitIdentity").click() #save changes
    
    if verifyEditAccountDetails():
        return True
    return False

def changeLastName(newLastName):
    if login() == False:
        return False
  
    driver.find_element_by_xpath("//a[contains(@href, 'identity')]").click()
    time.sleep(3)

    name = driver.find_element_by_xpath("//*[@id='lastname']")
    name.clear()
    name.send_keys(newLastName)
    
    passwd = driver.find_element_by_xpath("//*[@id='old_passwd']")
    passwd.clear()
    passwd.send_keys(password) #current password
    time.sleep(2)
    driver.find_element_by_id("psgdpr-consent").click()
    driver.find_element_by_name("submitIdentity").click() #save changes

    if verifyEditAccountDetails():
        return True
    return False

def changePassword(password, newPassword):
    if login() == False:
        return False
  
    driver.find_element_by_xpath("//a[contains(@href, 'identity')]").click()
    time.sleep(3)

    passwd = driver.find_element_by_xpath("//*[@id='old_passwd']")
    passwd.clear()
    passwd.send_keys(password) #current password
    time.sleep(2)

    driver.find_element_by_xpath("//*[@id='passwd']").send_keys(newPassword)
    driver.find_element_by_xpath("//*[@id='confirmation']").send_keys(newPassword) 

    driver.find_element_by_id("psgdpr-consent").click()
    driver.find_element_by_name("submitIdentity").click() #save changes

    if verifyEditAccountDetails():
        return True
    return False

def subscribeNewsletter():
    time.sleep(2)
    # xpath_list, class_list, id_list, name_list = [], [], [], ["mailing_name"]
    # name_input = find(xpath_list, class_list, id_list, name_list)
    # if name_input != "" and name_input.is_displayed()==True and name_input.is_enabled()==True:
    #     name_input.send_keys(firstname)

    xpath_list = ["//*[@id='newsletter-input']", "//input[contains(@id, 'newsletter')]", "//input[contains(@id, 'ewsletter')]", "//input[contains(@name, 'email')]",
     "//input[contains(@class, 'email')]", "//input[contains(@class, 'id')]", "//input[contains(@class, 'name')]"]
    class_list, id_list, name_list = ["email"], ["newsletter", "email"], ["email"]
    newsletter = find(xpath_list, class_list, id_list, name_list)

    if newsletter == "" or newsletter.is_displayed() == False or newsletter.is_enabled()==False:
        return False
    newsletter.send_keys(gmail)

    newsletter.send_keys(Keys.RETURN)
    time.sleep(2)
    if verifySubscribeNewsletter() == True:
        return True
    return False

###################################### TESTING ######################################
#driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
websites = ['onlyhangers.com/', 'hatshowroom.com', 'lecuine.com', 'masalledebain.com', 'kubii.fr', 'ultimateguard.com', 'compressport.com',
'capdeco-france.com','maplatine.com','cosmoptical.gr','monsieurchaussure.com', 'kliknklik.com','maniac-auto.com','huygens.fr',
'excelsiormilano.com','papiertigre.fr','bobbies.com/en/men', 'aquariumdirect.ca','itabnav.com','augarten.com','poupadou.com/en/','egarpi.es','saguaro-arms.com',
'jardinetsaisons.fr','leseditionsdunet.com','auzou.fr','cokitec.fr','enoraantoine.com',
'wkx-racing.com','rawa-bening.com','prestahero.com','feriabebe.com','simoshop.ro','lovecar.es',
'italpouf.de','zaparzymy.pl','inncii.com','proecodreams.pl', 'vente-du-diable.com/', 'sachacosmetics.com/en/',
'janod.com/en/', 'jonessnowboards.com', 'cultureindoor.eu', 'labaiedhalong.com', 'dog-cat.fi', "janod.com/en/", "jeanpaulhevin.com"]

evalutationWebsites = ["lechocolatdesfrancais.com", "shirtmax.com", "spprecision.com", "3fvape.com", "safetyrestore.com",
"saddleonline.com", "sheepskintown.com", "pylones.com/en", "charucashop.com/en", "pipolaki.com/en/"]

print(len(websites))
print(len(evalutationWebsites))

firstname = "Box"
lastname = "Ken"
email = "boxken4@gmail.com"
gmail = "boxken4@gmail.com"
password = "#%myrandomGmail"
address = "mySecretAddress 5"
numberOfItems = 2

for i in range(7, 10):
    visit("http://www." + evalutationWebsites[i])
    addItem(numberOfItems)
    time.sleep(2)
    #removeItem(numberOfItems)

    # driver.quit()    
    # if detect() == False:
    #     print("The website", websites[i], "is not made using prestashop")
    # else:
    #     print("The website", websites[i], "is made using prestashop")
    # if subscribeNewsletter() == True:
    #     print("Successfully subscribed to the newsletter")
    # else:
    #     print("Unable to subscribe to the newsletter")
    # time.sleep(2)
    # if search("hello_world"):
    #     print("Search was successful for the website:", websites[i])
    # else:
    #     print("Can not find the search bar for the website:", websites[i])
    #signup()
    # if login():
    #     print("Login successfully")
    # else:
    #     print("Unable to login")

    # if changeFirstName("Box"):
    #     print("Login successfully")
    # else:
    #     print("Unable to login")

    # if changeLastName("Ken"):
    #     print("Login successfully")
    # else:
    #     print("Unable to login")

    # if changePassword(password, "newPassword"):
    #     print("Login successfully")
    # else:
    #     print("Unable to login")
    # driver.current_url()