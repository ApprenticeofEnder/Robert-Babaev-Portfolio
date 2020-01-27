#! python3
#Robert Babaev
import time, sys, requests, bs4
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#Finds a button by link text
def clickByLinkText(element, domain):
    linkElem = domain.find_element_by_link_text(element)
    linkElem.click()

#Finds a link by ID
def clickById(ident, domain):
    linkElem = domain.find_element_by_id(ident)
    linkElem.click()

#Lets the user select the course they want to access
def selectCourse(domain, name):
    '''
    Input: domain (a Selenium browser), name (a string)
    '''
    #Finds all the courses by using a given name argument
    courses = domain.find_elements_by_class_name(name)
    #Displays the courses an an exit option
    for i in range(len(courses)):
        print(f'{i}:{courses[i].text}')
    print(f'{len(courses)}:Exit')
    #Control loop to ensure valid user input
    while True:
        try:
            selection = int(input())
        except Exception as e:
            print('Input invalid. Please use a numerical input.')
            print(e)
        else:
            #And finally access the selected course
            if selection < len(courses):
                courses[selection].click()
                break
            else:
                domain.maximize_window()
                sys.exit(0)

def getLinks(domain):
    pass


#Opens and partially logs into Outlook
def openOutlook(binary):
    outlook = webdriver.Firefox(firefox_binary=binary)
    outlook.get('https://outlook.live.com/owa/')
    clickByLinkText('Sign in', outlook)
    username = outlook.find_element_by_name('loginfmt')
    username.send_keys('replacewithyouremail')
    clickById('idSIButton9', outlook)
   
#Opens, logs into CuLearn and selects a course
def openCULearn(binary):
    cuLearn = webdriver.Firefox(firefox_binary=binary)
    cuLearn.get('https://carleton.ca/culearn/')
    cuLearn.minimize_window()
    username = cuLearn.find_element_by_name('username')
    username.send_keys('replacewithyourusername')
    password = cuLearn.find_element_by_name('password')
    password.send_keys('replacewithyourpassword')
    clickById('submit',cuLearn)
    selectCourse(cuLearn, 'course_link')
    cuLearn.maximize_window()
    

def main():
    binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    #Arguments specify which site to open
    if len(sys.argv[1:]):
        if 'outlook' in sys.argv:
            openOutlook(binary)
        if 'culearn' in sys.argv:
            openCULearn(binary)
    #otherwise open both
    else:
        openOutlook(binary)
        openCULearn(binary)

main()
