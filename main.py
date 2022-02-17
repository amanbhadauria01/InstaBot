from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import randint, uniform
from time import time, sleep
import pandas as pd
import logging

DEFAULT_IMPLICIT_WAIT = 1

class InstaDM(object) :
    def __init__ (self, username, password, headless=True, instapy_workspace=None, profileDir=None):
        self.selectors = {
            "accept_cookies": "//button[text()='Accept']",
            "home_to_login_button": "//button[text()='Log In']",
            "not_now" : "//button[text()='Not Now']",
            "comment_icon" : '//*[@id="react-root"]/section/main/div/div/article/div/div[3]/div/div/section[1]/span[2]/button/div[2]',
            "comment_field" : '//*[@id="react-root"]/section/main/section/div/form/textarea',
            "comment_post" : '//*[@id="react-root"]/section/main/section/div/form/button',
            "comment_username" : '//*[@id="react-root"]/section/main/div/ul/ul/div/li/div/div/div[2]/h3/div/a',
            "comment_text" : '//*[@id="react-root"]/section/main/div/ul/ul/div/li/div/div/div[2]/span',
            "delete_comment_btn" : '//button[text()="Delete"]',
            "reply_comment_btn" : "//button[text()='Reply']",
            "reply_comment_field" : '//*[@id="react-root"]/section/main/section/div[1]/form/textarea',
            "more_comment_btn" : '//*[@id="react-root"]/section/main/div/ul/li/div/button/div',
            "follower_btn" : '//*[@id="react-root"]/section/main/div/ul/li[2]',
            "follower_handle" : 't2ksc',
            "follower_name" : '//*[@id="react-root"]/section/main/div/ul/div/li[1]/div/div[1]/div[2]/div[2]',
            "follow_btn" : '//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div/span/span[1]/button',
            "msg_btn" : '//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div[1]/button',
            "msg_field" : '//*[@id="react-root"]/section/div[2]/div/div/div[2]/div/div/div/textarea',
            "send_msg_btn" : '//*[@id="react-root"]/section/div[2]/div/div/div[2]/div/div/div[2]/button',
            "cancel" : "//button[text()='Cancel']",
            "username_field": "username",
            "password_field": "password",
            "button_login": "//button/*[text()='Log In']",
            "login_check": "//*[@aria-label='Home'] | //button[text()='Save Info'] | //button[text()='Not Now']",
            "search_user": "queryBox",
            "select_user": '//div[text()="{}"]',
            "name": "((//div[@aria-labelledby]/div/span//img[@data-testid='user-avatar'])[1]//..//..//..//div[2]/div[2]/div)[1]",
            "next_button": "//button/*[text()='Next']",
            "textarea": "//textarea[@placeholder]",
            "send": "//button[text()='Send']"
        }
        # options
        options = webdriver.ChromeOptions()

        # specific profile
        profile_added = False
        # profile_added = True
        # options.add_argument("user-data-dir=C:\\Users\\Amandeep\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 13")
        # options.add_argument("user-data-dir=C:\\Users\\aggar\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 13")
        # mobile
        mobile_emulation = {
            "userAgent": 'Mozilla/5.0 (Linux; Android 10.0; iPhone Xs Max Build/IML74K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/535.19'
        }
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(
            PATH, options=options)
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(414, 936)
        maahipiclink = 'https://www.instagram.com/p/B8i2DhXlwW0/'
        maahi_profile_handle = 'mahi7781'
        mplpoker_handle = 'mplpoker'
        mypiclink = 'https://www.instagram.com/p/CZbpcllPEBY/'
        user_handle = 'amandrive105'
        text = 'hi'
        try:
            if(profile_added == False):
                self.login(username, password)
            # self.dm(user_handle,text)
            # self.post_comments_on_pic('https://www.instagram.com/p/CZbpcllPEBY/')
            # self.read_comments_on_pic(mypiclink)
            # self.delete_comments_on_pic('https://www.instagram.com/p/CZbpcllPEBY/')
            self.followers_list(mplpoker_handle)
            # self.reply_comments_on_pic(mypiclink)
            # what this bot can do :
            # 1. scrolling a little and accessing more comments - done
            # 2. editing comments - cannot do on instagram
            # 3. deleting comments - done
            # 4. followers list - done
            #    4.1 scaling followers list found 1472,1840,2813,2520,5204 handles found in different attempts
            # 5. replying to comments - done
            # 6. dm
        except Exception as e:
            print(str(e))

    def login(self,username,password):
        # homepage
        self.driver.get('https://instagram.com/?hl=en')
        self.__random_sleep__(3, 5)
        if self.__wait_for_element__(self.selectors['accept_cookies'], 'xpath', 10):
            self.__get_element__(
                self.selectors['accept_cookies'], 'xpath').click()
            self.__random_sleep__(3, 5)
        if self.__wait_for_element__(self.selectors['home_to_login_button'], 'xpath', 10):
            self.__get_element__(
                self.selectors['home_to_login_button'], 'xpath').click()
            self.__random_sleep__(5, 7)
        #login
        logging.info(f'Login with {username}')
        self.__scrolldown__()

        if not self.__wait_for_element__(self.selectors['username_field'], 'name', 10):
            print('Login Failed: username field not visible')
        else:
            self.driver.find_element(By.NAME,
                self.selectors['username_field']).send_keys(username)
            self.driver.find_element(By.NAME,
                self.selectors['password_field']).send_keys(password)
            self.__get_element__(
                self.selectors['button_login'], 'xpath').click()
            self.__random_sleep__(3, 5)
            if self.__wait_for_element__(self.selectors['login_check'], 'xpath', 10):
                print('Login Successful')
            self.__random_sleep__(3, 5)
            if self.__wait_for_element__(self.selectors['not_now'],'xpath',10) :
                self.__get_element__(self.selectors['not_now'],'xpath').click()
                print('clicked on Not Now')
            self.__random_sleep__(3, 5)
            if self.__wait_for_element__(self.selectors['cancel'],'xpath',10):
                self.__get_element__(self.selectors['cancel'],'xpath').click()
                print('clicked on Cancel')
            else:
                print('Login Failed: Incorrect credentials')

    def dm(self,user_handle,text):
        link = f'https://www.instagram.com/{user_handle}/?hl=en'
        self.__random_sleep__(3,5)
        self.driver.get(link)
        # if not followed follow it
        if self.__wait_for_element__(self.selectors['follow_btn'],'xpath',10):
            print('following')
            self.__get_element__(self.selectors['follow_btn'],'xpath').click()
            if self.__wait_for_element__(self.selectors['cancel'],'xpath',10):
                print('cancelling')
                self.__get_element__(self.selectors['cancel'],'xpath').click()
        else:
            print('already followed')
        # msging
        if self.__wait_for_element__(self.selectors['msg_btn'],'xpath',10):
            print('msg btn found')
            self.__get_element__(self.selectors['msg_btn'],'xpath').click()
            if self.__wait_for_element__(self.selectors['msg_field'],'xpath',10):
                print('msg field found')
                self.__get_element__(self.selectors['msg_field'],'xpath').send_keys(text)
                if(self.__wait_for_element__(self.selectors['send_msg_btn'],'xpath',10)) :
                    print('send msg btn found')
                    self.__get_element__(self.selectors['send_msg_btn'],'xpath').click()
        else :
            print('msg btn not found')


    def reply_comments_on_pic(self,post_link):
        self.__random_sleep__(3, 5)
        self.driver.get(post_link)
        self.__random_sleep__(3, 5)
        # finding comment icon
        if self.__wait_for_element__(self.selectors['comment_icon'], 'xpath', 10):
            self.__get_element__(self.selectors['comment_icon'], 'xpath').click()
            print('went to comment section')
        else :
            print("comment_icon not found")
            return
        # finding comments
        if self.__wait_for_element__(self.selectors['comment_username'],'xpath',10):
            usernames = self.__get_elements__(self.selectors['comment_username'],'xpath')
            comment_text = self.__get_elements__(self.selectors['comment_text'],'xpath')
            size = len(usernames)
            print(str(size) + ' comments')
            for i in range(0,size):
                if(self.is_element_present(By.XPATH,"..",usernames[i])):
                    print("parent found")
                    parent = self.__get_element__("..",'xpath',usernames[i])
                    print(parent.text)
                    if(self.is_element_present(By.XPATH,self.selectors['reply_comment_btn'],parent)):
                        print("reply btn found")
                        reply_btn = self.__get_element__(self.selectors['reply_comment_btn'],'xpath',parent)
                        reply_btn.click()
                        self.__random_sleep__(3,5)
                        if(self.is_element_present(By.XPATH,self.selectors['reply_comment_field'])):
                            print("reply field found")
                            line = "custom reply"
                            self.driver.find_element(By.XPATH, self.selectors['reply_comment_field']).send_keys(line)
                            print('wrote comment in comment_field')
                            if self.__wait_for_element__(self.selectors['comment_post'],'xpath',10):
                                self.__scrollup__()
                                self.__get_element__(self.selectors['comment_post'],'xpath').click()
                                print('posted reply comment ' + line)
                            else :
                                print('couldnot post reply comment')


                self.__random_sleep__(300,500)

    def delete_comments_on_pic(self,post_link):
        self.__random_sleep__(3, 5)
        self.driver.get(post_link)
        self.__random_sleep__(3, 5)
        # finding comment icon
        if self.__wait_for_element__(self.selectors['comment_icon'], 'xpath', 10):
            self.__get_element__(self.selectors['comment_icon'], 'xpath').click()
            print('went to comment section')
        else :
            print("comment_icon not found")
            return
        # finding comments
        if self.__wait_for_element__(self.selectors['comment_username'],'xpath',10):
            usernames = self.__get_elements__(self.selectors['comment_username'],'xpath')
            comment_text = self.__get_elements__(self.selectors['comment_text'],'xpath')
            size = len(usernames)
            print(str(size) + ' comments')
            for i in range(0,1):
                if(self.__offensive__(comment_text[i].text)):
                    actions = ActionChains(self.driver)
                    actions.move_to_element(comment_text[i])
                    actions.click_and_hold(on_element=comment_text[i])
                    actions.pause(3)
                    actions.perform()
                    self.__random_sleep__(3,5)
                    if self.__wait_for_element__(self.selectors['delete_comment_btn'], 'xpath', 10):
                        print('delete_comment_btn found')
                        delete_comment_btn = self.__get_element__(self.selectors['delete_comment_btn'],'xpath')
                        delete_comment_btn.click()
                        print('comment deleted')
                    else :
                        print('delete_comment_btn not found')

        else :
            print("no comments found")
            return

    def post_comments_on_pic(self,post_link):
        self.__random_sleep__(3, 5)
        self.driver.get(post_link)
        self.__random_sleep__(3, 5)
        essay =  '''So my parents, who were on a waiting list, got a call in the middle of the night asking: “We have an unexpected baby boy; do you want him?” They said: “Of course.” My biological mother later found out that my mother had never graduated from college and that my father had never graduated from high school. She refused to sign the final adoption papers. She only relented a few months later when my parents promised that I would someday go to college.

And 17 years later I did go to college. But I naively chose a college that was almost as expensive as Stanford, and all of my working-class parents’ savings were being spent on my college tuition. After six months, I couldn’t see the value in it. I had no idea what I wanted to do with my life and no idea how college was going to help me figure it out. And here I was spending all of the money my parents had saved their entire life. So I decided to drop out and trust that it would all work out OK. It was pretty scary at the time, but looking back it was one of the best decisions I ever made. The minute I dropped out I could stop taking the required classes that didn’t interest me, and begin dropping in on the ones that looked interesting.

It wasn’t all romantic. I didn’t have a dorm room, so I slept on the floor in friends’ rooms, I returned Coke bottles for the 5¢ deposits to buy food with, and I would walk the 7 miles across town every Sunday night to get one good meal a week at the Hare Krishna temple. I loved it. And much of what I stumbled into by following my curiosity and intuition turned out to be priceless later on. Let me give you one example:

Reed College at that time offered perhaps the best calligraphy instruction in the country. Throughout the campus every poster, every label on every drawer, was beautifully hand calligraphed. Because I had dropped out and didn’t have to take the normal classes, I decided to take a calligraphy class to learn how to do this. I learned about serif and sans serif typefaces, about varying the amount of space between different letter combinations, about what makes great typography great. It was beautiful, historical, artistically subtle in a way that science can’t capture, and I found it fascinating.

None of this had even a hope of any practical application in my life. But 10 years later, when we were designing the first Macintosh computer, it all came back to me. And we designed it all into the Mac. It was the first computer with beautiful typography. If I had never dropped in on that single course in college, the Mac would have never had multiple typefaces or proportionally spaced fonts. And since Windows just copied the Mac, it’s likely that no personal computer would have them. If I had never dropped out, I would have never dropped in on this calligraphy class, and personal computers might not have the wonderful typography that they do. Of course it was impossible to connect the dots looking forward when I was in college. But it was very, very clear looking backward 10 years later.

Again, you can’t connect the dots looking forward; you can only connect them looking backward. So you have to trust that the dots will somehow connect in your future. You have to trust in something — your gut, destiny, life, karma, whatever. This approach has never let me down, and it has made all the difference in my life.

My second story is about love and loss.

I was lucky — I found what I loved to do early in life. Woz and I started Apple in my parents’ garage when I was 20. We worked hard, and in 10 years Apple had grown from just the two of us in a garage into a $2 billion company with over 4,000 employees. We had just released our finest creation — the Macintosh — a year earlier, and I had just turned 30. And then I got fired. How can you get fired from a company you started? Well, as Apple grew we hired someone who I thought was very talented to run the company with me, and for the first year or so things went well. But then our visions of the future began to diverge and eventually we had a falling out. When we did, our Board of Directors sided with him. So at 30 I was out. And very publicly out. What had been the focus of my entire adult life was gone, and it was devastating.

I really didn’t know what to do for a few months. I felt that I had let the previous generation of entrepreneurs down — that I had dropped the baton as it was being passed to me. I met with David Packard and Bob Noyce and tried to apologize for screwing up so badly. I was a very public failure, and I even thought about running away from the valley. But something slowly began to dawn on me — I still loved what I did. The turn of events at Apple had not changed that one bit. I had been rejected, but I was still in love. And so I decided to start over.

I didn’t see it then, but it turned out that getting fired from Apple was the best thing that could have ever happened to me. The heaviness of being successful was replaced by the lightness of being a beginner again, less sure about everything. It freed me to enter one of the most creative periods of my life.

During the next five years, I started a company named NeXT, another company named Pixar, and fell in love with an amazing woman who would become my wife. Pixar went on to create the world’s first computer animated feature film, Toy Story, and is now the most successful animation studio in the world. In a remarkable turn of events, Apple bought NeXT, I returned to Apple, and the technology we developed at NeXT is at the heart of Apple’s current renaissance. And Laurene and I have a wonderful family together.

I’m pretty sure none of this would have happened if I hadn’t been fired from Apple. It was awful tasting medicine, but I guess the patient needed it. Sometimes life hits you in the head with a brick. Don’t lose faith. I’m convinced that the only thing that kept me going was that I loved what I did. You’ve got to find what you love. And that is as true for your work as it is for your lovers. Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. If you haven’t found it yet, keep looking. Don’t settle. As with all matters of the heart, you’ll know when you find it. And, like any great relationship, it just gets better and better as the years roll on. So keep looking until you find it. Don’t settle.

My third story is about death.

When I was 17, I read a quote that went something like: “If you live each day as if it was your last, someday you’ll most certainly be right.” It made an impression on me, and since then, for the past 33 years, I have looked in the mirror every morning and asked myself: “If today were the last day of my life, would I want to do what I am about to do today?” And whenever the answer has been “No” for too many days in a row, I know I need to change something.

Remembering that I’ll be dead soon is the most important tool I’ve ever encountered to help me make the big choices in life. Because almost everything — all external expectations, all pride, all fear of embarrassment or failure — these things just fall away in the face of death, leaving only what is truly important. Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose. You are already naked. There is no reason not to follow your heart.

About a year ago I was diagnosed with cancer. I had a scan at 7:30 in the morning, and it clearly showed a tumor on my pancreas. I didn’t even know what a pancreas was. The doctors told me this was almost certainly a type of cancer that is incurable, and that I should expect to live no longer than three to six months. My doctor advised me to go home and get my affairs in order, which is doctor’s code for prepare to die. It means to try to tell your kids everything you thought you’d have the next 10 years to tell them in just a few months. It means to make sure everything is buttoned up so that it will be as easy as possible for your family. It means to say your goodbyes.

I lived with that diagnosis all day. Later that evening I had a biopsy, where they stuck an endoscope down my throat, through my stomach and into my intestines, put a needle into my pancreas and got a few cells from the tumor. I was sedated, but my wife, who was there, told me that when they viewed the cells under a microscope the doctors started crying because it turned out to be a very rare form of pancreatic cancer that is curable with surgery. I had the surgery and I’m fine now.

This was the closest I’ve been to facing death, and I hope it’s the closest I get for a few more decades. Having lived through it, I can now say this to you with a bit more certainty than when death was a useful but purely intellectual concept:

No one wants to die. Even people who want to go to heaven don’t want to die to get there. And yet death is the destination we all share. No one has ever escaped it. And that is as it should be, because Death is very likely the single best invention of Life. It is Life’s change agent. It clears out the old to make way for the new. Right now the new is you, but someday not too long from now, you will gradually become the old and be cleared away. Sorry to be so dramatic, but it is quite true.

Your time is limited, so don’t waste it living someone else’s life. Don’t be trapped by dogma — which is living with the results of other people’s thinking. Don’t let the noise of others’ opinions drown out your own inner voice. And most important, have the courage to follow your heart and intuition. They somehow already know what you truly want to become. Everything else is secondary.

When I was young, there was an amazing publication called The Whole Earth Catalog, which was one of the bibles of my generation. It was created by a fellow named Stewart Brand not far from here in Menlo Park, and he brought it to life with his poetic touch. This was in the late 1960s, before personal computers and desktop publishing, so it was all made with typewriters, scissors and Polaroid cameras. It was sort of like Google in paperback form, 35 years before Google came along: It was idealistic, and overflowing with neat tools and great notions.

Stewart and his team put out several issues of The Whole Earth Catalog, and then when it had run its course, they put out a final issue. It was the mid-1970s, and I was your age. On the back cover of their final issue was a photograph of an early morning country road, the kind you might find yourself hitchhiking on if you were so adventurous. Beneath it were the words: “Stay Hungry. Stay Foolish.” It was their farewell message as they signed off. Stay Hungry. Stay Foolish. And I have always wished that for myself. And now, as you graduate to begin anew, I wish that for you.'''
        lines = essay.split('.')
        if self.__wait_for_element__(self.selectors['comment_icon'],'xpath',10):
            self.__get_element__(self.selectors['comment_icon'],'xpath').click()
            print('went to comment section')
            for line in lines :
                self.__random_sleep__(15, 30)
                if self.__wait_for_element__(self.selectors['comment_field'],'xpath',10):
                    self.driver.find_element(By.XPATH, self.selectors['comment_field']).send_keys(line)
                    print('wrote comment in comment_field')
                    if self.__wait_for_element__(self.selectors['comment_post'],'xpath',10):
                        self.__scrollup__()
                        self.__get_element__(self.selectors['comment_post'],'xpath').click()
                        print('posted comment ' + line)
                    else :
                        print('couldnot post comment')
                else :
                    print('couldnot find comment_field')
        else :
            print('couldnot find comment_icon')

    def read_comments_on_pic(self,post_link):
        self.__random_sleep__(3, 5)
        self.driver.get(post_link)
        self.__random_sleep__(3, 5)
        data = set()
        # finding comment icon
        if self.__wait_for_element__(self.selectors['comment_icon'], 'xpath', 10):
            self.__get_element__(self.selectors['comment_icon'], 'xpath').click()
            print('went to comment section')
        else :
            print("comment_icon not found")
            return
        # finding comments
        while len(data) < 5 :
            if self.__wait_for_element__(self.selectors['comment_username'],'xpath',10):
                usernames = self.__get_elements__(self.selectors['comment_username'],'xpath')
                comment_text = self.__get_elements__(self.selectors['comment_text'],'xpath')
                size = len(usernames)
                print(str(size) + ' comments')
                for i in range(0,size):
                    data.add(usernames[i].text + " : " + comment_text[i].text)
            else :
                print("not comments found")
                return
            if self.__wait_for_element__(self.selectors['more_comment_btn'],'xpath',10):
                self.__get_element__(self.selectors['more_comment_btn'],'xpath').click()
            else :
                print("more_comment_btn not found scolling up")
                self.__scrollup__()
            self.__random_sleep__(3, 5)
        print(data)

    def __offensive__(self,text):
        return True

    def followers_list(self,profile_handle):
        profile_link = 'https://www.instagram.com/' + profile_handle
        self.__random_sleep__(3, 5)
        self.driver.get(profile_link)
        self.__random_sleep__(3, 5)
        follower_data = set()
        # finding follower button
        if self.__wait_for_element__(self.selectors['follower_btn'],'xpath',10) :
            self.__get_element__(self.selectors['follower_btn'],'xpath').click()
            print("found follower_btn")
            while len(follower_data) < 100000 :
                sleep(0.1)
                if self.__wait_for_element__(self.selectors['follower_handle'],'class',10):
                    print("follower_hande found ",end = "")
                    handles = self.__get_elements__(self.selectors['follower_handle'],'class')
                    size = len(handles)
                    for i in range(0,size):
                        current_iteration_data = handles[i].text.split('\n')
                        if len(current_iteration_data) >= 2 :
                            follower_data.add(current_iteration_data[0] + " : " + current_iteration_data[1])
                        else :
                            follower_data.add(current_iteration_data[0] + " : ")
                    self.__scrolldown__()
                else :
                    print("follower_handle not found")
                print(len(follower_data))
        else :
            print("follower_btn not found")
        # printing
        for data in follower_data :
            print(data)

    def __get_element__(self, element_tag, locator,dr = -1):
        if dr == -1 :
            dr = self.driver
        """Wait for element and then return when it is available"""
        try:
            locator = locator.upper()
            if locator == 'ID' and self.is_element_present(By.ID, element_tag, dr):
                return WebDriverWait(dr, 15).until(lambda d: dr.find_element(By.ID,element_tag))
            elif locator == 'NAME' and self.is_element_present(By.NAME, element_tag, dr):
                return WebDriverWait(dr, 15).until(lambda d: dr.find_element(By.NAME,element_tag))
            elif locator == 'XPATH' and self.is_element_present(By.XPATH, element_tag, dr):
                return WebDriverWait(dr, 15).until(lambda d: dr.find_element(By.XPATH,element_tag))
            elif locator == 'CSS' and self.is_element_present(By.CSS_SELECTOR, element_tag, dr):
                return WebDriverWait(dr, 15).until(lambda d: dr.find_element(By.CSS_SELECTOR,element_tag))
            elif locator == "CLASS" and self.is_element_present(By.CLASS_NAME,element_tag, dr):
                return WebDriverWait(dr, 15).until(lambda d: dr.find_element(By.CLASS_NAME,element_tag))
            else:
                logging.info(f"Error: Incorrect locator = {locator}")
        except Exception as e:
            logging.error(e)
        logging.info(f"Element not found with {locator} : {element_tag}")
        return None

    def __get_elements__(self, element_tag, locator,dr = -1):
        if dr == -1 :
            dr = self.driver
        """Wait for element and then return when it is available"""
        try:
            locator = locator.upper()
            if locator == 'ID' and self.is_element_present(By.ID, element_tag, dr):
                return WebDriverWait(dr, 15).until(lambda d: dr.find_elements(By.ID,element_tag))
            elif locator == 'NAME' and self.is_element_present(By.NAME, element_tag, dr):
                return WebDriverWait(dr, 15).until(lambda d: dr.find_elements(By.NAME,element_tag))
            elif locator == 'XPATH' and self.is_element_present(By.XPATH, element_tag, dr):
                return WebDriverWait(dr, 15).until(lambda d: dr.find_elements(By.XPATH,element_tag))
            elif locator == 'CSS' and self.is_element_present(By.CSS_SELECTOR, element_tag, dr):
                return WebDriverWait(dr, 15).until(lambda d: dr.find_elements(By.CSS_SELECTOR,element_tag))
            elif locator == "CLASS" and self.is_element_present(By.CLASS_NAME,element_tag, dr):
                return WebDriverWait(dr, 15).until(lambda d: dr.find_elements(By.CLASS_NAME,element_tag))
            else:
                logging.info(f"Error: Incorrect locator = {locator}")
        except Exception as e:
            logging.error(e)
        logging.info(f"Element not found with {locator} : {element_tag}")
        return None

    def is_element_present(self, how, what, dr=-1):
        """Check if an element is present"""
        if dr == -1 :
            dr = self.driver
        try:
            dr.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def  __wait_for_element__(self,element_tag,locator,timeout = 30,dr = -1):

        result = False
        locator = locator.upper()
        for i in range(timeout):
            initTime = time()
            try:
                if locator == 'ID' and self.is_element_present(By.ID, element_tag,dr):
                    result = True
                    break
                elif locator == 'NAME' and self.is_element_present(By.NAME, element_tag,dr):
                    result = True
                    break
                elif locator == 'XPATH' and self.is_element_present(By.XPATH, element_tag,dr):
                    result = True
                    break
                elif locator == 'CSS' and self.is_element_present(By.CSS_SELECTORS, element_tag,dr):
                    result = True
                    break
                elif locator == 'CLASS' and self.is_element_present(By.CLASS_NAME, element_tag,dr) :
                    result = True
                    break
                else:
                    logging.info(f"Error: Incorrect locator = {locator}")
            except Exception as e:
                logging.error(e)
                print(f"Exception when __wait_for_element__ : {e}")

            sleep(max(0,1 - (time() - initTime)))
        else:
            print(
                f"Timed out. Element not found with {locator} : {element_tag}")
        self.driver.implicitly_wait(DEFAULT_IMPLICIT_WAIT)
        return result

    def __random_sleep__(self, minimum=2, maximum=7):
        t = randint(minimum, maximum)
        logging.info(f'Wait {t} seconds')
        sleep(t)
    def __scrolldown__(self,dr=-1):
        if dr == -1 :
            dr = self.driver
        dr.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

    def __scrollup__(self,dr=-1):
        if dr == -1 :
            dr = self.driver
        dr.execute_script(
            "window.scrollTo(0, -document.body.scrollHeight);")

def main():
    accounts = pd.read_csv('accounts.csv')
    obj = InstaDM(accounts.iloc[3,0],accounts.iloc[3,1])
    sleep(100000)

if __name__ == "__main__" :
    main()