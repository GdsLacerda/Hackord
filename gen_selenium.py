# -*- coding: utf-8 -*-

import os

from verify_mail import Verify
from wrinter import wrint

try:
    import datetime
    import json
    import pathlib
    import random
    import re
    import sys
    import time
    import typing
    import httpx
    import undetected_chromedriver as uc
    from colorama import Back, Fore, Style, init

    import aisolver as solver
    from aisolver import HolyChallenger
    from aisolver.exceptions import ChallengePassed

    from pystyle import Colorate, Colors
    from selenium.common.exceptions import (ElementClickInterceptedException,
                                            ElementNotInteractableException)
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait

except Exception as E:
    os.system("pip install -r requirements.bin")

# XXX Wrint Function
p = wrint()

# class Generator
class gen:

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.solved = 0
        self.generated_accounts = 0

    #AI Solver Installation
    def install_solver(self) -> bool:
        try:
            solver.install()
            p.handle("AI Solver installed [ 200 ]")
            return True
        except Exception as e:
            p.error(f"Unable to install AI solver | {e}")
            return False
    
    # Solver Solve
    def hit_challenge(self, driver, challenger: HolyChallenger, retries: int = 10) -> typing.Optional[str]:
        if challenger.utils.face_the_checkbox(driver):
            challenger.anti_checkbox(driver)
            if res := challenger.utils.get_hcaptcha_response(driver):
                return res

        for _ in range(retries):
            try:
                if (resp := challenger.anti_hcaptcha(driver)) is None:
                    continue
                if resp == challenger.CHALLENGE_SUCCESS:
                    return challenger.utils.get_hcaptcha_response(driver)
            except ChallengePassed:
                return challenger.utils.get_hcaptcha_response(driver)
            challenger.utils.refresh(driver)
            time.sleep(0.1)


















    def main(self, threads: int, email: str, password: str, username: str, proxy: any = None, headless: bool = False):

        for i in range(int(threads)):
    

            # New Challenger
            challenger = solver.new_challenger(screenshot=False, debug=False, lang="en")

            # Replace selenium.webdriver.Chrome with driver
            driver = solver.get_challenge_ctx(headless=headless, proxy = proxy, lang="en")



            try:
                driver.get("http://discord.com/register")
                # p.handle(f"Driver: [ {driver.name} ] started successfully.")
            except Exception as e:
                p.error(f"Unable to start webdriver. | Exception: [ {e} ]")
                p.handle("Exception Handled")
                time.sleep(10)
                sys.exit()
  

            try:
                # XXX: Insert Email
                WebDriverWait(driver, 15, ignored_exceptions=(ElementNotInteractableException,)).until(
                    EC.presence_of_element_located((By.NAME, "email"))
                ).send_keys(email)
            except:
                pass
            
            try:
                # XXX: Insert Username
                WebDriverWait(driver, 15, ignored_exceptions=(ElementNotInteractableException,)).until(
                    EC.presence_of_element_located((By.NAME, "username"))
                ).send_keys(username)
            except:
                pass
               
            
            try:
                # XXX: Insert Password
                WebDriverWait(driver, 15, ignored_exceptions=(ElementClickInterceptedException,)).until(
                    EC.presence_of_element_located((By.NAME, "password"))
                ).send_keys(password)
            except:
                pass

            actions = ActionChains(driver)
            
            # BUG: TYPE: Discord DESC: Locating to the first date input then the discord will navigate the focuse to the next input
            driver.find_elements(By.CLASS_NAME, 'css-1hwfws3')[0].click() 
            actions.send_keys(str(random.randint(1,12))) # Submitting the month
            actions.send_keys(Keys.ENTER)
            actions.send_keys(str(random.randint(1,28))) # Submitting the day
            actions.send_keys(Keys.ENTER)
            actions.send_keys(str(random.randint(1990,2001))) # Submitting the year
            actions.send_keys(Keys.ENTER)
            actions.perform() # All the actions are pending and needs to perform all at once 



            # XXX Agree to terms and conditions DISCORD TOS
            try: 
                checkbox_cssselector = (
                    "#app-mount > div.appDevToolsWrapper-1QxdQf > div > div.app-3xd6d0 > div > div > div > form > div > div > div.flex-2S1XBF.flex-3BkGQD.horizontal-112GEH.horizontal-1Piu5-.flex-3BkGQD.directionRow-2Iu2A9.justifyStart-2Mwniq.alignCenter-14kD11.noWrap-hBpHBz.marginTop20-2T8ZJx > label > input"
                ) # Discord ToS Checkbox CSS_SELECTOR
                checkbox_full_xpath = "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[4]/label/input" # RECOMMENDED: Full XPATH
                checkbox_xpath = '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/form/div/div/div[4]/label/input' # Discord ToS Checkbox xpath

                # OLD: checkbox = driver.find_element(By.XPATH, checkbox_full_xpath) # Find Checkbox Element
                # OLD: checkbox.click() # ACTION: Click checkbox - Agree to discord terms and conditions

                WebDriverWait(driver, 15, ignored_exceptions=(ElementClickInterceptedException,)).until(
                    EC.presence_of_element_located((By.XPATH, checkbox_full_xpath))
                ).click()
            except Exception as e:
                p.error(f"Unable to accept Discord TOS")
                driver.quit()


            # XXX Click Signup Button
            try:
                # XXX: Insert Password
                elements = driver.find_elements(By.TAG_NAME, 'button')
                # OLD : p.debug(f"Signup button Located: [ {elements[0].text} ]")
                # OLD : print(elements[0].text)
                elements[0].click()
            except:
                p.error("Unable to click signup button")
                driver.quit()

            p.handle("Creating Account")

            p.solver("Solving Captcha")


            start = time.time()

            try:
                self.hit_challenge(driver, challenger=challenger, retries=10)
            except:
                pass

            end = time.time()

            self.solved += 1


            p.solver(f"Captcha Solved in [ {end - start} ] seconds.")

            class SDEV:
                def __init__(self) -> None:
                    super(SDEV, self)

                def switch_tab(self,  driver: uc.Chrome, tab: int = 0):
                    driver.window_handles[tab]

                def changeurl(self, url: str):
                    driver.get(url)

            p.session(f"Solved Captchas in this session: [ {self.solved} ]")

            vy = Verify(self.api_key)

            rm = vy.ReceiveEmail(email[:-14])
            print(rm)

            token = driver.execute_script('location.reload();var i=document.createElement("iframe");document.body.appendChild(i);return i.contentWindow.localStorage.token').strip('"') # Get the token

            p.handle(f"Attempting to confirm account [{email}]")

            start_confirmmail = time.time()

            SDEV().changeurl(rm)

            start_solvingcaptcha = time.time()
            p.solver("Solving Captcha")

            try:
                self.hit_challenge(driver, challenger=challenger, retries=10)
            except:
                pass

            self.solved += 1
            end_solvingcaptcha = time.time()
            p.solver(f"Captcha Solved in [ {end_solvingcaptcha - start_solvingcaptcha} ] seconds.")   

            end_confirmmail = time.time()
            p.handle(f"Account confirmed in [{end_confirmmail - start_confirmmail}]")

            p.session(f"Solved Captchas in this session: [ {self.solved} ]")

            p.token(f"Token: [ {str(token)} ]")
            p.token(f"Username: [ {str(username)} ]")
            p.token(f"Password: [ {str(password)} ]")

            if str(token) != None:
                self.generated_accounts += 1

            p.session(f"Generated Accounts on this session: [ {self.generated_accounts} ]")

            driver.quit()
