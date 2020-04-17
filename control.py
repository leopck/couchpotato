from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class WebControl:
    def __init__(self, handle = None, options = None):
        if handle == None:
            self.startChrome(options)
        else:
            self = handle

    def startChrome(self, options=None):
        if options == None:
            options = Options()
            options.binary_location = "/usr/bin/google-chrome"    #chrome binary location specified here
            options.add_argument("--start-maximized") #open Browser in maximized mode --start-fullscreen
            # options.add_argument("--start-fullscreen") #open Browser in maximized mode --start-fullscreen
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=options, executable_path=r'/usr/bin/chromedriver')
        self.go('https://9anime.to/watch/plunderer.55jj/yn51xz')
        return self.driver
    
    def getDriver(self):
        return self.driver

    def go(self, url):
        self.driver.get(url)

    def getURL(self):
        return self.driver.current_url

    def getTitle(self):
        return self.driver.title

    def getClassName(self, classname):
        return self.driver.find_element_by_class_name(classname)

    def getTagName(self, tagname):
        return self.driver.find_element_by_tag_name(tagname)

    def sendKey(self, element, key):
        return element.send_keys(key)

    def scrollWebsite(self, position = 0):
        return self.driver.execute_script("window.scrollTo(0, " + position + ")")
    
    # Deleting (Calling destructor) 
    def __del__(self): 
        self.driver.quit()