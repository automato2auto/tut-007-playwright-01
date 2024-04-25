from playwright.sync_api import sync_playwright

CONTACTS_PAGE_URL = 'https://crm.na1.insightly.com/list/Contact/'
EMAIL = 'tarek.harba2001b@gmail.com'
PASSWORD = 'G4CZTh5PmRUH3Cb'

SALUTATION = 'Mr.'
FIRST_NAME = 'Saeed'
LAST_NAME = 'Ahmad'
CONTACT_EMAIL_ADDRESS = 'saeed.ahmad@email.com'
PHONE_NUMBER = '+966 123 456789'
COUNTRY = 'Saudi Arabia'
STATE = 'Makkah'
CITY = 'Jeddah'

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto(CONTACTS_PAGE_URL, timeout=120000)

    #* LOGIN PAGE
    login_email_field = page.locator('#emailaddress')
    login_email_field.fill(EMAIL)
    continue_button = page.locator('#continue-button')
    continue_button.click()
    login_password_field = page.locator('#password')
    login_password_field.fill(PASSWORD)
    login_button = page.locator('#login-button')
    login_button.click()

    #* CONTACTS PAGE
    new_contact_button = page.locator('#AddNewButton a')
    new_contact_button.click()
    contact_salutation_field = page.locator('#Contact_SALUTATION')
    contact_salutation_field.fill(SALUTATION)
    first_name_field = page.locator('#Contact_FIRST_NAME')
    first_name_field.fill(FIRST_NAME)
    last_name_field = page.locator('#Contact_LAST_NAME')
    last_name_field.fill(LAST_NAME)
    email_field = page.locator('#Contact_EMAIL_ADDRESS')
    email_field.fill(CONTACT_EMAIL_ADDRESS)
    phone_field = page.locator('#Contact_PHONE')
    phone_field.fill(PHONE_NUMBER)
    country_menu = page.locator('#Contact_ADDRESS_MAIL_COUNTRY')
    country_menu.select_option(COUNTRY)
    country_menu.selec
    state_field = page.locator('#Contact_ADDRESS_MAIL_STATE')
    state_field.fill(STATE)
    city_field = page.locator('#Contact_ADDRESS_MAIL_CITY')
    city_field.fill(CITY)
    save_contact_button = page.locator('#btn-save')
    save_contact_button.click()

    page.pause()
