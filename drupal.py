# Georgios Gerasimos Leventopoulos (csd4152)

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import csv

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# Returns a web element if found, else returns an empty string
def check_exists_by_xpath(xpath_list):
    for item in xpath_list:
        try:
            driver.find_element_by_xpath(item)
            #print(homepage[0], "has this:", item, "and it is a website made using prestashop")
            return driver.find_element_by_xpath(item)
        except NoSuchElementException:
            pass#print("it doesnt have", item)
    return ""

def check_exists_by_class_name(class_list):
    for item in class_list:
        try:
            driver.find_element_by_class_name(item)
            #print(homepage[0], "has this:", item, "and it is a website made using prestashop")
            return driver.find_element_by_class_name(item)
        except NoSuchElementException:
            pass#print("it doesnt have", item)
    return ""

def check_exists_by_id(id_list):
    for item in id_list:
        try:
            driver.find_element_by_id(item)
            #print(homepage[0], "has this:", item, "and it is a website made using prestashop")
            return driver.find_element_by_id(item)
        except NoSuchElementException:
            pass#print("it doesnt have", item) 
    return ""

def check_exists_by_name(name_list):
    for item in name_list:
        try:
            driver.find_element_by_name(item)
            #print(homepage[0], "has this:", item, "and it is a website made using prestashop")
            return driver.find_element_by_name(item)
        except NoSuchElementException:
            pass#print("it doesnt have", item)
    return ""

def check_all_exist_by_xpath(xpath_list):
    for item in xpath_list:
        try:
            temp = driver.find_elements_by_xpath(item)
            return driver.find_elements_by_xpath(item)
        except:
            pass
    return ""

def check_all_exist_by_class_name(class_list):
    for item in class_list:
        try:
            driver.find_elements_by_class_name(item)
            return driver.find_elements_by_class_name(item)
        except NoSuchElementException:
            pass
    return ""

def check_all_exist_by_id(id_list):
    for item in id_list:
        try:
            driver.find_elements_by_id(item)
            return driver.find_elements_by_id(item)
        except NoSuchElementException:
            pass
    return ""

def check_all_exist_by_name(name_list):
    for item in name_list:
        try:
            driver.find_elements_by_name(item)
            return driver.find_elements_by_name(item)
        except NoSuchElementException:
            pass
    return ""

# Returns the webelement if it exists, else returns an empty string.
def find(xpath_list, class_list, id_list, name_list):
    a = check_exists_by_xpath(xpath_list)
    b = check_exists_by_class_name(class_list)
    c = check_exists_by_id(id_list)
    d = check_exists_by_name(name_list)
    if a!="":
        return a
    elif b!="":
        return b
    elif c!="":
        return c
    elif d!="":
        return d
    else:
        return ""

def findAll(xpath_list, class_list, id_list, name_list):   
    a = check_all_exist_by_xpath(xpath_list)
    b = check_all_exist_by_class_name(class_list)
    c = check_all_exist_by_id(id_list)
    d = check_all_exist_by_name(name_list)
    if a!="":
        return a
    elif b!="":
        return b
    elif c!="":
        return c
    elif d!="":
        return d
    else:
        #print("Cannot find items")
        return ""

def verifyLogin():
    xpath_list, class_list, id_list, name_list = ["//*[@id='create_account_error']"], ["alert alert-danger",  "help-block  alert alert-danger", "help-block"], [], []
    signin_error = find(xpath_list, class_list, id_list, name_list)
    if signin_error != "":
        return False  
    return True

def verifySignup():
    return True

def verifyAddItem():
    return True

def verifyRemoveItem():
    return True

def verifySearchItem():
    xpath_list, class_list, id_list, name_list = ["//link[contains(@class, 'results')]", "//span[contains(@class, 'results')]"], [], [], []
    search_results = find(xpath_list, class_list, id_list, name_list)
    if search_results == "":
        return False
    return True

def verifySubscribeNewsletter():
    xpath_list, class_list, id_list, name_list = ["//input[contains(@class, 'newsletter_error')]"], [], [], []
    newsletter_error = find(xpath_list, class_list, id_list, name_list)
    if newsletter_error == "":
        return True
    else:
        return False

def visit(website):
    driver.get(website)
    driver.maximize_window()

def detect():
    xpath_list = ["//meta[contains(@content, 'drupal')]", "//link[contains(@rel, 'drupal')]", "//script[contains(@data-drupal-selector, 'drupal')]"]
    class_list = [""]
    id_list = [""]
    name_list = []
    drupal_features = find(xpath_list, class_list, id_list, name_list)

    # If it does not find attributes that Drupal CMS has, then it returns False
    if drupal_features == "":
        return False
    return True

def login():
    time.sleep(3)
    # xpath_list,class_list,id_list,name_list = ["//a[contains(@href, 'account')]", "//a[contains(@href, 'login')]",
    # "//[contains(@class, 'account')]"], [], [], []
    # signin_button = find(xpath_list, class_list, id_list, name_list)
    # if signin_button != "":
    #     signin_button.click()
    xpath_list, class_list, id_list, name_list = ["//*[@id='loginIdInput']", "//input[contains(@id, 'login')]", "//*[@id='edit-name']", "//*[@id='email']", "//*[@id='identifier']", "//input[contains(@name, 'username')]", "//*[@id='form-input-identity']", "//*[@id='IDToken1']"], [], ["email", "identifier"], ["identity", "username", "email"]
    mail_field = find(xpath_list, class_list, id_list, name_list)
    if mail_field != "":
        mail_field.send_keys(gmail)
    time.sleep(2)

    xpath_list, class_list, id_list, name_list = ["//*[@id='passwordInput']", "//input[contains(@id, 'password')]", "//*[@id='form-input-credential']", "//input[contains(@id, 'pass')]", "//*[@id='IDToken2']"], [], ["passwd", "password"], ["credential", "passwd", "password"]
    passfield = find(xpath_list,class_list,id_list,name_list)
    if passfield != "":
        passfield.send_keys(password)
        passfield.send_keys(Keys.RETURN)
    time.sleep(2)
    if verifyLogin() == True:
        return True
    return False

def signup():
    signin = driver.find_element_by_xpath("").click()
    time.sleep(2)

    xpath_list,class_list,id_list,name_list = [],["firstname"],["firstname"],["firstname"]
    firstname_field = find(xpath_list, class_list, id_list, name_list)
    if firstname_field !="":
        firstname_field.send_keys(firstname)
    time.sleep(2)

    xpath_list,class_list,id_list,name_list = [],["lastname"],["lastname"],["lastname"]
    lastname_field = find(xpath_list, class_list, id_list, name_list)
    if lastname_field !="":
        lastname_field.send_keys(lastname)
    time.sleep(2)

    xpath_list,class_list,id_list,name_list = [],[""],["email_address"],["email"]
    email_field = find(xpath_list, class_list, id_list, name_list)
    if email_field !="":
        email_field.send_keys(gmail)
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
    xpath_list, class_list, id_list, name_list = ["//a[contains(@class, 'template')]", "//article[contains(@class, 'product-card')]", "//a[contains(@href, 'add_to_cart')]", "//a[contains(@href, 'shop')]", "//a[contains(@class, 'product')]", "//li[contains(@class, 'product')]", "//a[contains(@class, 'product')]", "//article[contains(@class, 'product')]", 
                    "//div[contains(@class, 'owl-item')]", "//figure[contains(@class, 'product')]"], ["owl-item active", "add"], [], ["Submit"]
    products = findAll(xpath_list, class_list, id_list, name_list)
    return products

def addItem(numberOfProductsUserWants):
    time.sleep(3)
    for i in range(0, numberOfProductsUserWants):
        time.sleep(2)
        products = locateItem()
        if products != "" and len(products) > numberOfProductsUserWants:
            products[i+1].click()
        else:
            print("Cannot find products.")
            return False

        time.sleep(3)
        xpath_list, class_list, id_list, name_list = ["//button[contains(@class, 'add-to-cart')]", "//a[contains(@class, 'add-to-basket')]", "//*[@id='productDetailPageBuyProductForm']/div/div[2]/button", "//*[@id='ap5-add-to-cart']/button"], ["add"], [], ["Submit"]
        add_to_card_button = find(xpath_list, class_list, id_list, name_list)
        if add_to_card_button != "":
            add_to_card_button.click()
            time.sleep(3)
            driver.back()
    if verifyAddItem() == True:
        return True
    return False

def removeItem(numberOfProductsUserWants):
    # Go to the shopping list
    time.sleep(4)
    xpath_list, class_list, id_list, name_list = ["//a[contains(@href, 'cart')]", "//a[contains(@href, 'order')]", "//a[contains(@href, 'comanda-rapida')]", "//div[contains(@class, 'shopping_cart')]", "//div[contains(@class, 'cart cif-book')]", "//*[@id='shopping_cart']", "//div[contains(@class, 'cart')]", "//*[@id='menu_basket']/a", "//*[@id='_desktop_cart']/div/div/a", "//a[contains(@href, 'action=show')]", "//a[contains(@href, 'cart')]", "//a[contains(@class, 'cart')]", "//*[@id='block_cart_button']"], ["cart-dropdow-button"], [], []
    shopping_list = find(xpath_list, class_list, id_list, name_list)
    if shopping_list == "":
        return False
    else:
        shopping_list.click()
    time.sleep(2)

    # Find and delete the product
    xpath_list, class_list, id_list, name_list = ["//a[contains(@class, 'remove-from-cart')]", "//a[contains(@class, 'cart_quantity_delete')]", "//a[contains(@href, 'quantity=0')]", "//a[contains(@class, 'remove')]"], ["remove-from-cart", "cart_quantity_delete", "remove"], [], []
    remove_from_card_button = find(xpath_list, class_list, id_list, name_list)
    if remove_from_card_button != "":
        remove_from_card_button.click() # click delete button
        time.sleep(2)
        return True
    if verifyRemoveItem() == True:
        return True
    return False

def changeFirstName(newFirstName):
    if login() == False:
        return False

    text = "myaccount"
    driver.find_element_by_xpath('//a[contains(@href, "%s")]' % text).click()
    time.sleep(3)

    name = driver.find_element_by_xpath("//*[@id='firstname']")
    name.clear()
    name.send_keys(newFirstName)
    
    passwd = driver.find_element_by_xpath("//*[@id='password']")
    passwd.clear()
    passwd.send_keys(password)
    time.sleep(2)
    driver.find_element_by_id("psgdpr-consent").click()
    driver.find_element_by_name("submitIdentity").click()

    if verifyEditAccountDetails():
        return True
    return False

def changeLastName(newLastName):
    if login() == False:
        return False
    text = "myaccount"
    driver.find_element_by_xpath("").click()
    time.sleep(3)

    name = driver.find_element_by_xpath("//*[@id='lastname']")
    name.clear()
    name.send_keys(newLastName)
    
    passwd = driver.find_element_by_xpath("password")
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

    driver.find_element_by_xpath("password").click() 
    time.sleep(3)
    passwd = driver.find_element_by_xpath("//*[@id='old_passwd']")
    passwd.clear()
    passwd.send_keys(password) # current password
    time.sleep(2)

    driver.find_element_by_xpath("//*[@id='passwd']").send_keys(newPassword)
    driver.find_element_by_xpath("//*[@id='confirm']").send_keys(newPassword) 
    driver.find_element_by_name("submitIdentity").click() #save changes

    if verifyEditAccountDetails():
        return True
    return False

def checkoutCard():
    # add one item just to be sure
    if addItem(1) == True:
        xpath_list, class_list, id_list, name_list = ["//a[contains(@href, 'cart')]", "//a[contains(@href, 'order')]"], [""], [], [""]   # find checkout button 
        checkoutButton = find(xpath_list, class_list, id_list, name_list)
        if checkoutButton != "":
            checkoutButton.click()   # click checkout button
        return True
    if verifyCheckoutCard() == True:
        return True
    return False

def subscribeNewsletter():
    time.sleep(4)

    xpath_list, class_list, id_list, name_list = ["//input[contains(@name,'email')]", "//*[@id='mce-EMAIL']", "//*[@id='hpEmailSignUp']", "//*[@id='email']", "//*[@id='contentinfo']/div[2]/div[1]/div[1]/div[2]/div/form/div/div[3]/div/div/input", "//*[@id='root']/div/form/div[3]/input", "//*[@id='newsletterPageEmail']", "//input[contains(@id,'newsletter')]", "//*[@id='block-rockhallfooterblock']/section/div[1]/div[2]/div[4]/div[1]/div/form/div[1]/div/input", "//*[@name='email']", "//*[@id='teradata-email']", "//input[contains(@id,'email')]", "//input[contains(@class,'newsletter')]"], [], ["email"], ["email"]
    newsletter_field = find(xpath_list, class_list, id_list, name_list)
    if newsletter_field != "" and newsletter_field.is_displayed() and newsletter_field.is_enabled():
        newsletter_field.send_keys(gmail)
    else:
        return False

    xpath_list, class_list, id_list, name_list = [], [], [""], ["name"]
    name_field = find(xpath_list, class_list, id_list, name_list)
    if name_field != "" and name_field.is_displayed() and name_field.is_enabled():
        name_field.send_keys(firstname)
    
    xpath_list, class_list, id_list, name_list = ["//*[@id='footer-confirm-box']", "//*[@id='edit-terms']", "//*[@id='label-checkbok-hpEmailSignUp']"], [], [], []
    checkbox = find(xpath_list, class_list, id_list, name_list)
    if checkbox != "" and checkbox.is_displayed() and checkbox.is_enabled():
        checkbox.click()
    
    newsletter_field.send_keys(Keys.RETURN) # hit enter (instead of pressing a button)

    time.sleep(5)
    if verifySubscribeNewsletter() == True:
        return True
    return False

def search(searchTerm):
    time.sleep(2)
    xpath_list, class_list, id_list, name_list = ["//button[contains(@class,'search')]", "//button[contains(@class,'search-submit')]", "//div[contains(@class,'search-block')]", "//div[contains(@class,'search-bar')]", "//button[contains(@data-behavior,'search')]", "//button[contains(@class,'search-icon')]", "//button[contains(@class,'g-menu__toggle')]", "//button[contains(@class,'icon search js-activate')]", "//*[@id='global-search-onscreen-toggle']", "//button[contains(@class,'menu')]", "//button[contains(@class,'search')]", "//div[contains(@class, 'search-bar')]", "//a[contains(@class, 'search')]", "//i[contains(@class,'icon-search')]"], [], [], []
    search_drop_bar = find(xpath_list, class_list, id_list, name_list)
    if search_drop_bar != "" and search_drop_bar.is_displayed() and search_drop_bar.is_enabled():
        search_drop_bar.click()
    time.sleep(1)

    xpath_list, class_list, id_list, name_list = ["//*[@id='edit-query']", "//*[@id='branded-section-search-input']", "//input[contains(@placeholder,'Search')]", "//*[@id='edit-keys']","//input[contains(@id,'quer')]", "//input[contains(@name,'quer')]", "//input[contains(@id,'search')]", "//input[contains(@class,'search')]", "//*[@id='edit-key']",
    "//input[contains(@name,'keys')]", "//input[contains(@id,'edit-key')]", "//input[contains(@name,'search')]"], ["light", "search-wrapper"], ["search-input"], []
    search_bar = find(xpath_list, class_list, id_list, name_list)    
    if search_bar != "" and search_bar.is_displayed() and search_bar.is_enabled():
        search_bar.send_keys(searchTerm)
        time.sleep(1)
        search_bar.send_keys(Keys.RETURN)
    else:
        return False
    
    time.sleep(2)

    if verifySearchItem() == True:
        return True
    return False


def locateItem1111111():
    time.sleep(3)
    product_urls = []
    xpath_list = ["//a[contains(@class, 'product')]", "//a[contains(@class, 'item--link')]", "//a[contains(@class, 'swiper-slide')]", "//div[contains(@class, 'product-img')]", "//a[contains(@class, 'grid-view-item')]", "//a[contains(@id, 'link')]", "//a[contains(@id, 'pro_first_box')]", "//a[contains(@class, 'item-content')]"]
    for xpath in xpath_list:
        products = driver.find_elements_by_xpath(xpath)
        #print(products)
        if len(products) > 0: # if we find products
            break

    for product in products:
        product_urls.append(product.get_attribute("href"))
    if len(product_urls)>0 and product_urls[0] == None:
        return []
    #print(len(product_urls))
    #print(product_urls)
    return product_urls    

def addItem1111111(numberOfProductsUserWants):
    if numberOfProductsUserWants <= 0:
        return False

    products = locateItem1111111()

    if len(products) <= 0:
        print("cannot find products")
        return False

    for i in range(0, numberOfProductsUserWants):
        if i > len(products):
            print("The user asked for ", numberOfProductsUserWants, " products, but we only found ", i, " products.")
            return False

        visit(products[i])
        time.sleep(2)

        xpath_list, class_list, id_list, name_list = ["//*[@id='product-addtocart-button']", "//button[contains(@data-button-action, 'add-to-cart')]", "//button[contains(@class, 'tocart')]", "//button[contains(@name, 'add')]", "//*[@id='add_to_cart']/button", "//button[contains(@name, 'Submit')]", "//p[contains(@id, 'add_to_cart')]", "//button[contains(@class, 'add-to-cart')]", "//button[contains(@name, 'submit')]", "//button[@type='submit']", "//button[contains(@type, 'submit')]", "//*[@id='add_to_cart']/button", "//button[contains(@class, 'btn product-form__cart-submit')]", "//*[@id='productDetailPageBuyProductForm']/div/div[2]/button", "//*[@id='ap5-add-to-cart']/button"], ["add"], [], ["Submit"]
        add_to_card_button = find(xpath_list, class_list, id_list, name_list)
        time.sleep(1)
        if add_to_card_button != "" and add_to_card_button.is_displayed()==True and add_to_card_button.is_enabled()==True:
            add_to_card_button.click()
            time.sleep(2)

    if verifyAddItem(numberOfProductsUserWants) == True:
       return True
    return False

###################################### TESTING ######################################
gmail = "boxken4@gmail.com"
password = "#%myrandomGmail"
firstname = "Ken"
lastname = "Box"

# most famous websites made with drupal
websites = ["ericclapton.com/", "rigorousthemes.com/", "jysk.co.uk/bathroom/bath-mats", "lush.com/uk/en/c/new-products", "sevillafc.es/en", "gurneysresorts.com/", "press.princeton.edu/", "rockhall.com/", "instabar.eu/", "thinkglobalhealth.org/", "en.swissquote.lu/challenge-the-code",
"catchoftheday.stubru.be/", "k2.pl/en", "nationalforest.org/", "hotelicon.com/", "benech-neurochirurgia.it/en/", "www.zinodavidoff.com/", "ew.com",
"london.gov.uk/", "ny.gov/", "australia.gov.au/", "taboola.com/", "box.com", "verizon.com/", "business.pinterest.com/en/", "developer.twitter.com/en", "ebayinc.com/", "timex.com/", 
"nokia.com/", "mcdonalds.com.au/", "schwab.com/", "principal.com/", "harvard.edu/", "stanford.edu/", "ladygaga.com/", "ericclapton.com/", "emmys.com/", "nasa.gov/",
"taboola.com/", "ncaa.com/", "fiji.travel/", "newsroom.pinterest.com/en", "lush.com/uk/en", "wmg.com/", "bbcgoodfood.com/",
 "tesla.com", "lacity.org/", "ox.ac.uk/", "warnerrecords.com/", "arsenal.com/", "virgin.com/", "childrenssociety.org.uk/", "bycyklen.dk/"]

evalutationWebsites = ["artellite.co.uk/", "lush.com/uk/en", "makeupforever.com/fr/", "cartier.com/en-fi/", "eldumrett.is/", 
"obermeyer.com/", "verizon.com/", "fooda.com/", "us.mentos.com/", "www.ericclapton.com/"]

print(len(evalutationWebsites))
print(len(websites))
numberOfItems = 2
drupal_websites = 0
for i in range(0, 52):
    visit("http://" + evalutationWebsites[i])
    if search("helloWorld"):
        print("Search was successful")
    else:
        print("Can not find seach bar")

    # if subscribeNewsletter():
    #     print("Successfully executed subscribe newsletter task for the website", evalutationWebsites[i])
    # else:
    #     print("Unable to subscribe to the newsletter")

    # if detect() == False:
    #     print("This website is not made using drupal")
    # else:
    #     print("This website is made using drupal")
    #     drupal_websites += 1
    # print(drupal_websites)
    
    # addItem(numberOfItems)

    # if removeItem(numberOfItems) == True:
    #     print("Items removed successfully")
    # else:
    #     print("Cannot remove items")

    # if login():
    #     print("Login successfully")
    # else:
    #     print("Unable to login")
   #driver.quit()

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
