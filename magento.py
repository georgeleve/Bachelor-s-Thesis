# Georgios Gerasimos Leventopoulos (csd4152)
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
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

def verifyLogin():
    xpath_list, class_list, id_list, name_list = ["//*[@id='create_account_error']"], ["alert alert-danger",  "help-block  alert alert-danger", "help-block"], [], []
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

def verifySearchItem():
    xpath_list, class_list, id_list, name_list = ["//input[contains(@class, 'search_error')]"], [], [], []
    search_error = find(xpath_list, class_list, id_list, name_list)
    if newsletter_error != "":
        return False
    return False

def verifySubscribeNewsletter():
    xpath_list, class_list, id_list, name_list = ["//input[contains(@class, 'newsletter_error')]"], [], [], []
    newsletter_error = find(xpath_list, class_list, id_list, name_list)
    if newsletter_error != "":
        return False
    return True

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
    xpath_list = ["//link[contains(@href, 'Magento')]", "//link[contains(@href, 'magento')]", "//link[contains(@href, 'skin')]", "//link[contains(@href, 'frontend')]", "//script[contains(@type, 'magento')]"]
    class_list = []
    id_list = []
    name_list = []

    # If it does not find attributes that Magento CMS has, then it returns False
    if find(xpath_list, class_list, id_list, name_list)=="":
        return False
    return True

def login():
    time.sleep(4)
    xpath_list, class_list, id_list, name_list = ["//a[contains(@href, 'login')]", "//li[contains(@class, 'account')]", "//[contains(@href, 'account')]", "//a[contains(@href, 'login')]", "//body[contains(@class, 'sign-in')]"],["nav-button active"],[],[]
    signin_button = find(xpath_list, class_list, id_list, name_list)
    if signin_button != "":
      signin_button.click()

    xpath_list, class_list, id_list, name_list = ["//input[contains(@name, 'login[username]')]", "//input[contains(@id, 'email')]", "//input[contains(@name, 'email')]"], [], ["email"], ["username", "email", "customer[email]"]
    mail_field = find(xpath_list, class_list, id_list, name_list)
    if mail_field !="":
        mail_field.send_keys(gmail)

    xpath_list, class_list, id_list, name_list = ["//input[contains(@name, 'login[password]')]", "//input[contains(@id, 'pass')]", "//input[contains(@name, 'password')]", "//*[@id='pass']", "//*[@id='password']"],[],["passwd", "password", "pass"],["passwd", "password"]
    passfield = find(xpath_list,class_list,id_list,name_list)
    if passfield !="":
        passfield.send_keys(password)
        passfield.send_keys(Keys.RETURN)
    time.sleep(3)
    if verifyLogin() == True:
        return True
    return False

def signup():
    signin = driver.find_element_by_xpath("//*[@id='id8Myqc2Xh']").click()
    time.sleep(2)

    xpath_list,class_list,id_list,name_list = [],[],["firstname"],["firstname"]
    firstname_field = find(xpath_list, class_list, id_list, name_list)
    if firstname_field !="":
        firstname_field.send_keys(firstname)
    time.sleep(2)

    xpath_list,class_list,id_list,name_list = [],[],["lastname"],["lastname"]
    lastname_field = find(xpath_list, class_list, id_list, name_list)
    if lastname_field !="":
        lastname_field.send_keys(lastname)
    time.sleep(2)

    xpath_list,class_list,id_list,name_list = [],[],["email_address"],["email"]
    email_field = find(xpath_list, class_list, id_list, name_list)
    if email_field !="":
        email_field.send_keys(gmail)
    time.sleep(2)

    xpath_list,class_list,id_list,name_list = ["//*[@id='social-login-popup-create-pass']"],[],["passwd", "password"],["passwd", "password"]
    passfield = find(xpath_list,class_list,id_list,name_list)
    if passfield !="":
        passfield.send_keys(password)
    time.sleep(2)

    xpath_list,class_list,id_list,name_list = [],[],["password-confirmation"],["password_confirmation"]
    passfield = find(xpath_list,class_list,id_list,name_list)
    if passfield !="":
        passfield.send_keys(password)
    time.sleep(2)

    checkBox = driver.find_element_by_class_name("checkbox")
    checkBox.click()

    passfield.send_keys(Keys.RETURN)
    if verifySignup() == True:
        return True
    return False

def removeItem(numberOfProductsUserWants):
    # Go to the shopping list
    time.sleep(4)
    xpath_list, class_list, id_list, name_list = ["//a[contains(@href, 'order')]", "//a[contains(@href, 'comanda-rapida')]", "//div[contains(@class, 'shopping_cart')]", "//div[contains(@class, 'cart cif-book')]", "//*[@id='shopping_cart']", "//div[contains(@class, 'cart')]", "//*[@id='menu_basket']/a", "//*[@id='_desktop_cart']/div/div/a", "//a[contains(@href, 'action=show')]", "//a[contains(@href, 'cart')]", "//a[contains(@class, 'cart')]", "//*[@id='block_cart_button']"], ["cart-dropdow-button"], [], []
    shopping_list = find(xpath_list, class_list, id_list, name_list)
    if shopping_list == "":
        return False
    else:
        shopping_list.click()
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
    time.sleep(3)
    xpath_list, class_list, id_list, name_list = ["//span[contains(@class,'header-search')]", "//li[contains(@class,'user-menu__item--search')]", "//button[contains(@class,'header-block-search')]", "//li[contains(@class,'search')]", "//div[contains(@class,'earch')]", "//span[contains(@class,'earch')]", "//button[contains(@id,'earch')]", "//a[contains(@class,'search')]", "//*[@id='search_widget']", "//*[@id='header-search-btn']"], ["search-button", "user-menu__item--search", "m-r-6 link underline-h is-active", "icon search", "search-toggle", "user-menu__link", "action show-search", "header__icon", "item toggle-search", "hover-text", "search-button"], ["menu-element-search"], []
    search_drop_bar = find(xpath_list, class_list, id_list, name_list)
    if search_drop_bar != "" and search_drop_bar.is_displayed() and search_drop_bar.is_enabled():
        search_drop_bar.click()
    time.sleep(2)

    xpath_list, class_list, id_list, name_list = ["//*[@id='global_search_form']/input[1]", "//*[@id='search']", "//input[contains(@class,'search-input')]", "//input[contains(@class,'search')]", "//input[contains(@id,'search')]", "//input[contains(@class,'Search')]", "//*[@id='search_query_top']", "//*[@id='search']", "//*[@id='quick-search-input']", "//*[@id='page-header']"], ["search-wrapper"], ["search-input"], []
    search_bar = find(xpath_list, class_list, id_list, name_list)
    if search_bar == "" or search_bar.is_displayed()==False or search_bar.is_enabled()==False:
        return False
    else:
        search_bar.send_keys(searchTerm)
        search_bar.send_keys(Keys.RETURN)
    time.sleep(3)
    if verifySearchItem() == True:
        return True
    return False

def subscribeNewsletter():
    xpath_list, class_list, id_list, name_list = ["//*[@id='newsletter']", "//*[@id='subemail']", "//input[contains(@name, 'email')]", "//input[contains(@name, 'newsletter')]", "//input[contains(@id, 'newsletter')]", "//input[contains(@id, 'email')]"], [], ["newsletter", "newsletter-email", "footerNewsletterInput"], ["emailSignUp", "mws-footer_email", "EMAIL", "email", "newsletter"]
    newsletter_field = find(xpath_list, class_list, id_list, name_list)
    time.sleep(2)
    if newsletter_field != "" and newsletter_field.is_displayed() and newsletter_field.is_enabled():
        newsletter_field.send_keys(gmail)
    else:
        return False

    xpath_list, class_list, id_list, name_list = ["//input[contains(@name, 'checkbox')]", "//input[contains(@class, 'checkbox')]", "//*[@id='customCheck1']"], [], [], []
    checkbox = find(xpath_list, class_list, id_list, name_list)
    time.sleep(2)
    if checkbox != "" and checkbox.is_displayed()==True and checkbox.is_enabled()==True:
        checkbox.click()
        
    newsletter_field.send_keys(Keys.RETURN)

    time.sleep(2)
    if verifySubscribeNewsletter() == True:
        return True
    return False

def checkoutCard():
    # add one item just to be sure
    if addItem(1) == True:
        xpath_list, class_list, id_list, name_list = ["//a[contains(@href, 'cart')]", "//a[contains(@href, 'order')]"], [""], [], [""]   # find checkout button 
        checkoutButton = find(xpath_list, class_list, id_list, name_list)
        if checkoutButton != "":
            checkoutButton.click()   # click checkout button
    
    if verifyCheckoutCard() == True:
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
    
    passwd = driver.find_element_by_xpath("//*[@id='old']")
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
    text = "myaccount"
    driver.find_element_by_xpath('//a[contains(@href, "%s")]' % text).click()
    time.sleep(3)

    name = driver.find_element_by_xpath("//*[@id='lastname']")
    name.clear()
    name.send_keys(newLastName)
    
    passwd = driver.find_element_by_xpath("//*[@id='old']")
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

    driver.find_element_by_xpath('//a[contains(@href, "%s")]' % text).click() 
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

def locateItem():
    time.sleep(3)
    product_urls = []  # "//div[contains(@class, 'card-image-wrapper')]", "//div[contains(@class, 'slick-slide')]", "//div[contains(@class, 'swiper-slide ng-star-inserted')]", "//div[contains(@class, 'product')]", "//div[contains(@class, 'item')]", "//li[contains(@class, 'nosto-list-item')]"], ["owl-item active", "add"], [], ["Submit"]
    xpath_list = ["//a[contains(@class, 'product')]", "//a[contains(@href, 'nosto-image-container')]", "//div[contains(@class, 'tombstone')]", "//div[contains(@class, 'nosto-image-container')]", "//a[contains(@data-test, 'ProductCard__ProductCardSC')]", "//li[contains(@class, 'product-item')]", "//a[contains(@class, 'item--link')]", "//a[contains(@class, 'swiper-slide')]", "//div[contains(@class, 'product-img')]", "//a[contains(@class, 'grid-view-item')]", "//a[contains(@id, 'link')]", "//a[contains(@id, 'pro_first_box')]", "//a[contains(@class, 'item-content')]"]
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

def addItem(numberOfProductsUserWants):
    if numberOfProductsUserWants <= 0:
        return False

    products = locateItem()

    if len(products) <= 0:
        print("cannot find products")
        return False

    for i in range(0, numberOfProductsUserWants):
        if i > len(products):
            print("The user asked for ", numberOfProductsUserWants, " products, but we only found ", i, " products.")
            return False

        visit(products[i])
        time.sleep(2)

        xpath_list, class_list, id_list, name_list = ["//button[contains(@class, 'button btn-cart')]", "//*[@id='add-to-bag-container']/div[2]/div/button", "//*[@id='top-cart-btn-cart']", "//button[contains(@data-test, 'AddToCart__Button')]", "//*[@id='product-addtocart-button']", "//button[contains(@data-button-action, 'add-to-cart')]", "//button[contains(@class, 'tocart')]", "//button[contains(@name, 'add')]", "//*[@id='add_to_cart']/button", "//button[contains(@name, 'Submit')]", "//p[contains(@id, 'add_to_cart')]", "//button[contains(@class, 'add-to-cart')]", "//button[contains(@name, 'submit')]", "//button[@type='submit']", "//button[contains(@type, 'submit')]", "//*[@id='add_to_cart']/button", "//button[contains(@class, 'btn product-form__cart-submit')]", "//*[@id='productDetailPageBuyProductForm']/div/div[2]/button", "//*[@id='ap5-add-to-cart']/button"], ["add"], [], ["Submit"]
        add_to_card_button = find(xpath_list, class_list, id_list, name_list)
        time.sleep(1)
        if add_to_card_button != "" and add_to_card_button.is_displayed()==True and add_to_card_button.is_enabled()==True:
            add_to_card_button.click()
            time.sleep(2)

    if verifyAddItem(numberOfProductsUserWants) == True:
       return True
    return False

###################################### TESTING ######################################
websites = []
gmail = "boxken4@gmail.com"
password = "#%myrandomGmail"
firstname = "Ken"
lastname = "Box"

# found some top websites on this page:  https://paulnrogers.com/magento-websites/
# These are the most famous magento websites (50 in total)
websites = ["robertdyas.co.uk/", "zadig-et-voltaire.com", "byredo.com", "conranshop.com", "made.com",
 "paulsmith.com/uk/mens", "endclothing.com", "paperchase.co.uk", "tomdixon.net", "bulkpowders.co.uk",
 "missguided.co.uk", "omegawatches.com", "ospreylondon.com", "oneills.com/int_en/", "kurtgeiger.com",
 "christianlouboutin.com", "lee.com", "richersounds.com", "harveynichols.com", "nobelbiocare.com", "chopard.com",
 "accessories.ford.com", "micro-scooters.co.uk", "lecreuset.co.uk", "selcobw.com", "swooneditions.com", 
 "alexandani.com", "7forallmankind.com", "oliversweeney.com", "urbanista.com",
 "bjornborg.com", "marahoffman.com", "bulgari.com", "smythson.com", "cobragolf.com",
 "pepejeans.com", "oddbins.com", "sergiorossi.com", "radley.co.uk", "gievesandhawkes.com", "fredperry.com",
 "zumiez.com", "charlottetilbury.com", "hartsofstur.com", "oliverbonas.com", "packtpub.com/", "vam.ac.uk/", "pantone.com/eu/en/", "agentprovocateur.com/", "vbulletin.com/"]

evaluationWebsites = ["vivobarefoot.com/eu/", "shop.sunoco.com/", "www.interiordefine.com/",
"sportys.com/", "shop.iccsafe.org/", "vortexoptics.com/", "scufgaming.com/eu", "jerrysartarama.com/",
"spanx.com/", "jeulia.com/"]

numberOfItems = 2
print(len(websites))
for i in range(, 50):
    visit("http://" + evaluationWebsites[i])
    addItem(numberOfItems)

    # if search("laptops") == True:
    #     print("Search was successful")
    # else:
    #     print("Can not find seach bar")
    #     print(evaluationWebsites[i])

    # if detect() == False:
    #     print("The website", websites[i], "is not made using magento")
    # else:
    #     print("The website", websites[i], "is made using magento")

    # if subscribeNewsletter():
    #     print("Successfully do subscribe newsletter task")
    # else:
    #     print("Unable to subscribe to the newsletter")
    
    # if login():
    #     print("Login successfully")
    # else:
    #     print("Unable to login")
    
    #addItem(2)

    # search("helloWorld")
    # if login():
    #     print("Login successfully")
    # else:
    #     print("Unable to login")

    # driver.quit()

    # if detect() == False:
    #     print("This website is not made using magento")
    # else:
    #     print("This website is made using magento")

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