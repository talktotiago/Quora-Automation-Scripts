#Login to Quora
def LoginPage():
    #Credentials
    username = 'tiagoluizd@gmail.com'
    pwd = 'Amoroma1982'
    #Login Form
    form = driver.find_element_by_class_name("form_inputs")
    usernamefield = form.find_element_by_name("email")
    usernamefield.send_keys(username)
    pwdfield = form.find_element_by_name("password")
    pwdfield.send_keys(pwd)
    pwdfield.send_keys(Keys.RETURN)
LoginPage()