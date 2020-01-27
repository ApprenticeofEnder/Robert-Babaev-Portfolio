#! python3
#Robert Babaev
import time, sys, requests, bs4
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def clickByLinkText(element, domain):
    linkElem = domain.find_element_by_link_text(element)
    linkElem.click()

def clickById(ident, domain):
    linkElem = domain.find_element_by_id(ident)
    linkElem.click()

def selectCourse(domain, name):
    courses = domain.find_elements_by_class_name(name)
    for i in range(len(courses)):
        print(f'{i}:{courses[i].text}')
    print(f'{len(courses)}:Exit')
    while True:
        try:
            selection = int(input())
        except Exception as e:
            print(e)
        else:
            if selection < len(courses):
                courses[selection].click()
                break
            else:
                domain.maximize_window()
                sys.exit(0)

def getLinks(domain):
    pass

def openOutlook(binary):
    outlook = webdriver.Firefox(firefox_binary=binary)
    outlook.get('https://outlook.live.com/owa/')
    clickByLinkText('Sign in', outlook)
    username = outlook.find_element_by_name('loginfmt')
    username.send_keys('replacewithyouremail')
    clickById('idSIButton9', outlook)
    
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
    if len(sys.argv[1:]):
        if 'outlook' in sys.argv:
            openOutlook(binary)
        if 'culearn' in sys.argv:
            openCULearn(binary)
    else:
        openOutlook(binary)
        openCULearn(binary)

main()
