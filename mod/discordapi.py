# -*- coding: utf-8 -*-

import httpx, time, json, random, string, re, os

from base64 import b64encode

from urllib.request import Request, urlopen

from haisolver import AioHcaptcha

from asyncio import get_event_loop



from mod.tempmail import TempMail
from mod.printf import printf
from mod.cookies import Cookie








p = printf()
tm = TempMail


CONFIGFILE = open(f"data/config.json").read()
config = json.loads(CONFIGFILE)


# --------> Discord API V1 <-------- #

class DiscordAPI:
    
    def __init__(self):
        super(DiscordAPI, self).__init__()

        #init > timeout > config['Request']['timeout']
        self.timeout = int(config['Request']['timeout'])
        
        # init > Config > ChromeDriver
        self.chromedriver_executable_path = config["Chromedriver"]["chromedriver-path"]
        
        # init > Config > Change_Captcha_Solver
        # Available Captcha Types: [ 2captcha.com , hcaptcha_ai ]
        self.captcha_solver_type = config["Captcha"]["Captcha_Solver_Type"]
        
        #init > Generator > Tokens
        self.check_tokens_after_generating = config["Token-Generator"]["check-after-generating"]
        
        # init > Config > Requests > Headers
        self.useragent = config["Request"]["user-agent"]
        self.x_super_properties = config["Request"]["x-super-properties"]
        self.referer = config["Request"]["referer"]
        self.content_type = config["Request"]["content-type"]
        self.accept = config["Request"]["accept"]
        self.accept_language = config["Request"]["accept-language"]
        self.connection = config["Request"]["connection"]
        self.DNT = config["Request"]["DNT"]
        self.origin = config["Request"]["origin"]  
        self.sec_fetch_dest = config["Request"]["sec-fetch-dest"]
        self.sec_fetch_mode = config["Request"]["sec-fetch-mode"]
        self.sec_fetch_site = config["Request"]["sec-fetch-site"]
        self.TE = config["Request"]["TE"]
        self.x_debug_options = config["Request"]["x-debug-options"]
        
        # init > 2Captcha > Solver
        self.default_captcha_solving_time = float(config["Captcha"]["wait_for_solved_captcha"])  
        
        # init > Discord > 2Captcha
        self.captcha_get_url = config["Captcha"]["2captcha"]["captcha_get_url"]
        self.captcha_submit_url = config["Captcha"]["2captcha"]["captcha_submit_url"]
        self.captcha_api_key = config["Captcha"]["2captcha"]["captcha_api_key"]
        self.discord_hcaptcha_id = config["Captcha"]["2captcha"]["discord_hcaptcha_sitekey"]
        self.discord_captcha_referer = config["Captcha"]["2captcha"]["discord_captcha_referer"]
        
        # init > Discord > AI_Captcha_Solver
        self.ai_captcha_sitekey = config["Captcha"]["hcaptcha_ai"]["solver-sitekey"]
        self.ai_captcha_host = config["Captcha"]["hcaptcha_ai"]["solver-host"]
        self.captcha_retries = int(config["Captcha"]["hcaptcha_ai"]["solver-retries"])
        
        # init > Discord > Tokens
        self.valid_tokens = 0
        self.invalid_tokens = 0
        self.rate_limited_tokens = 0
        self.locked_tokens = 0  
        
        # init > Discord > Guilds
        self.guild_name = None
        self.guild_id = None
        self.channel_id = None
        self.invite = None
        
        # init > Discord > Tokens > Guilds
        self.total_server_joins_success = 0
        self.total_server_joins_locked = 0
        self.total_server_joins_invalid = 0
        self.total_server_leave_success = 0
        self.total_server_leave_locked = 0
        self.total_server_leave_invalid = 0
        # TODO: self.total_dms_success = 0
        # TODO: self.total_dms_fail = 0
        # TODO: self.invalid_token_dm = 0
        # TODO: self.locked_token_dm = 0
        
        # init > Discord > Tokens > Rate Limits
        self.ratelimit_delay = float(config["Rate_Limit"]["ratelimit_delay"])
        self.rate_limits = 0


















    def proxy_isworking(self, proxy: any, print: bool = False):

        start_checking_proxy = time.time()
        if print:
            p.debug(f"Checking Proxy: [ {proxy} ]")
        try:
            end_checking_proxy = time.time()
            p.warning(f"Max proxy timeout set to [ {self.timeout} ]")
            res = httpx.get("https://ipinfo.io/json", proxies=proxy, timeout=self.timeout)
            if res.status_code == 200 or 201:
                p.info(f"Using Proxy: [ {res.json()['ip']} | {res.json()['country']} ]")
                return True
            else:
                p.error("Proxy Server Error")
                return False
        except httpx.TimeoutException:
            end_checking_proxy = time.time()
            if print:
                p.handle(f"Proxy Server not responding ( timed out ): [ {proxy} ] >>> [ AUTO PROXY CHANGER ]")
            return False
        except httpx.ProxyError:
            p.warning(f"Proxy not working [ {proxy} ]")
            p.handle(f"Changing proxy {proxy} to >>> now random proxy from {config['Proxies']['proxy_file']}")
            return False
        except httpx.ProtocolError:
            p.warning(f"Proxy type not match with provided proxy type! [ Provided proxy type: [ {config['Proxies']['type']} ] ]")
            return False
        except WindowsError as ew:
            p.warning(f"Windows Error | Check proxy format and try again ;[ | Exception: [ {ew} ]")
            return False
        except Exception as rf:
            p.warning(f"Unexcepted Proxy Error | Exception: [ {rf} ]")
            return False



        



        
        
    def get_fingerprint(self, proxy: str = None) -> str:
        res = httpx.get("https://discord.com/api/v10/experiments", proxies=proxy)
        jres = res.json()
        # > print(jres["fingerprint"])
        return jres["fingerprint"]
        



    def headers(self, token):
        return {
            "Authorization": token,
            "accept": self.accept,
            "accept-language": self.accept_language,
            "connection": self.connection,
            "DNT": self.DNT,
            "origin": self.origin,
            "sec-fetch-dest": self.sec_fetch_dest,
            "sec-fetch-mode": self.sec_fetch_mode,
            "sec-fetch-site": self.sec_fetch_site,
            "referer": self.referer,
            "TE": self.TE,
            "User-Agent": self.useragent,
            "x-debug-options": self.x_debug_options,
            "x-fingerprint": self.get_fingerprint(),
            "X-Super-Properties": self.x_super_properties
        }


        
    async def __solve_hcaptcha_by_ai(self, proxy: any = None):
        try:
            solver = AioHcaptcha(self.ai_captcha_sitekey, f"https://demo.hcaptcha.com/solve?site_key={self.ai_captcha_sitekey}&host={self.ai_captcha_host}",         
                                chromedriver_args={
                                    "executable_path": f"{self.chromedriver_executable_path}"
                                                    }
                                )

            while True:
                try:
                    resp = await solver.solve(retry_count=4, custom_params=None)
                    break
                except:
                    print("[-] Captcha Error ( RESOLVING )")
        except:
            pass
        return resp
    
    def AI_Captcha(self, proxy: any = None):
        """Ai HCaptcha Solver"""
        loop = get_event_loop()
        try:
            captcha_solution = loop.run_until_complete(self.__solve_hcaptcha_by_ai())
            return captcha_solution
        except Exception as e:
            print(e)
            return "ERROR"
        
    @property
    def fakename(self):
        """Generate Fake Name"""
        nameresp = httpx.get('https://story-shack-cdn-v2.glitch.me/generators/username-generator?')
        return nameresp.json()["data"]["name"]
    

    def get_trackers(self, xtrack: bool, encoded: bool = True):
        """Get Trackers"""
        payload = {
            "os": "Windows",
            "browser": "Chrome",
            "device": "",
            "system_locale": "fr-FR",
            "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "browser_version": "98.0.4758.102",
            "os_version": "10",
            "referrer": "",
            "referring_domain": "",
            "referrer_current": "",
            "referring_domain_current": "",
            "release_channel": "stable",
            "client_build_number": 130153,
            "client_event_source": None
        }

        return b64encode(json.dumps(payload, separators=(',', ':')).encode()).decode() if encoded else payload
        
        
        


  



    
    
    def submit_cap_key(self, proxy: any = None):
        """2Captcha Solver [ Submit Captcha Key ]"""
        url = self.captcha_submit_url
        querystring = {
            "key": self.captcha_api_key,
            "method": "hcaptcha",
            "sitekey": self.discord_hcaptcha_id,
            "pageurl": self.discord_captcha_referer
        }
        headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
        submitclient = httpx.Client(headers=headers, proxies=proxy)
        subresp:httpx.Response = submitclient.post(url, params=querystring)
        text = subresp.text
        # print(text)
        return text.split("|", 1)[1]
    

    def get_discord_captcha(self, captcha_key_response: any, proxy: any = None):
        """2Captcha Solver [ Get Captcha ]"""
        params = {"key": self.captcha_api_key, "action": "get", "id": captcha_key_response}
        getcapclient = httpx.Client(proxies=proxy)
        capresponse:httpx.Response = getcapclient.get(self.captcha_get_url, params=params)
        text = capresponse.text
        return text.split("|", 1)

    def getCaptcha(self, proxy: any = None):
        """
        > 2Captcha Solver [ __fire__ ]\n
        > Solve Captcha
        """
        captcha_step_one = self.submit_cap_key(proxy)
        p.solver(f"Captcha: [ {captcha_step_one} ]")
        looping = True
        while looping:
            # > print(f'Waiting for captcha [ {self.default_captcha_solving_time} seconds ]')
            time.sleep(self.default_captcha_solving_time)
            captcha_step_two = self.get_discord_captcha(captcha_step_one, proxy)
            try:
                if len(captcha_step_two[1]) > 60:
                    p.solver(f"Captcha Solution: [ {captcha_step_two[1][:10]}... ]")
                    return captcha_step_two[1]
            except IndexError:
                p.solver("Captcha not done yet!", end="\r")
                pass
        
        
        
        

    def Login(self, token: str, proxy: any = None):
            """Login [ TOKEN, PROXY ] >>> Check_Tokens"""
            p.info(f"Checking token with proxy [ {proxy} ]")
            try:

                client = httpx.Client(headers=self.headers(token), proxies=proxy)
                response = client.get("https://discord.com/api/v10/users/@me/library")
                try:
                    json_resp = response.json()
                    # DEBUG > print(json_resp)
                    code = json_resp["code"]
                except:
                    code = ""
                if response.status_code == 200:
                    p.DiscordToken().valid(f"[ {response.status_code} ] Valid Token: ( {token} )")
                    self.valid_tokens += 1
                if response.status_code == 401:
                    p.DiscordToken().invalid(f"[ {response.status_code} ] Invalid Token: ( {token} )")
                    self.invalid_tokens += 1
                    # TODO > self.tokens.remove(token)
                if response.status_code == 403:
                    p.DiscordToken().locked(f"[ {response.status_code} ] Locked Token: ( {token} )")
                    self.locked_tokens += 1
                    # TODO > self.tokens.remove(token)
                if response.status_code == 429:
                    p.DiscordToken().ratelimited(f"[ {response.status_code} ] Rate Limited: ( {token} )")
                    self.rate_limited_tokens += 1
                    time.sleep(self.ratelimit_delay)
                    self.rate_limits += 1
                    self.Login(token, proxy)

            except httpx.ProxyError:
                p.error("Proxy error")

            except Exception as exception:
                print(f"Error: {exception}")
                
                







    def Confirm_Email(self, inbox: str, token: str, proxy: any = None):
        """Confirm Discord Email""" 
           
        def DiscordMail():
            # > Getting the email confirmation link from the email
            scrape_emails = True
            while scrape_emails:
                emails = tm.getEmails(inbox)
                for mail in emails:
                    p.info(f"{mail}")
                    if "mail.discord.com" in str(mail.sender):
                        for word in mail.body.split():
                            if "https://click.discord.com" in word:
                                email_link = word
                                scrape_emails = False
                                break
            email_link: str = email_link.replace("[", "").replace("]", "")
            return email_link


        confirmation_email = DiscordMail()

        p.info(f"Got Discord Email Confirmation link | {confirmation_email}")

        with open("data/confirmation_emails.txt", "a") as writemail:
            writemail.write(confirmation_email + "\n")
            writemail.close()
        
        p.ok("Discord confirmation link saved in [ data/confirmation_emails.txt ] ")
        

        
        
        p.solver(f"Solving Captcha [ Service: [ {self.captcha_solver_type } ] ]")
        sstart = time.time()

        if self.captcha_solver_type == "2captcha.com":
            captcha_key = self.getCaptcha(proxy)
            #print("2Captcha.com Captcha: " + captcha_key)
        elif self.captcha_solver_type == "hcaptcha_ai":
            captcha_key = self.AI_Captcha(proxy=proxy)
            #print("AI_Captcha: " + captcha_key)
        
        payload = {
            "token": f"{token}",
            "captcha_key": f"{captcha_key}"
        }

        send = time.time()

        p.solver(f"Captcha Solved in {send-sstart}: [ {captcha_key[:24]} ]")



        headers = {
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "accept-language": "en",
                    #"content-length": f"{int(verifyapi_dc_size)+int(verifyb_dc_size)}",
                    "cookie": "__sdcfduid=f18a95b15ee011edbbc6ab4f5f4487a2c5f38df498d0a79e4fb5a54be4744075aa3b50f6208e292e9270ed5eeef716d4; locale=en-US",
                    "origin": "https://discord.com",
                    "referer": "https://discord.com/verify",
                    "sec-ch-ua": 'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    #"x-fingerprint": f"{self.get_fingerprint(proxy)}",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny44MiBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTMuMC40NTc3LjgyIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2NvcmQuY29tL2xvZ2luIiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NjYyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
                    }
            

        er = httpx.post("https://discord.com/api/v10/auth/verify", headers=headers, json=payload, proxies=proxy)
                
        p.info(f"Discord email verifier response: [ {er.text} ] | Status: [ {er.status_code} ]")


        p.info("This email confirmer is not done yet, it may show a lot of errors. If email is not confirming automaticly confirm it manually.")     
        
        
        
        

    
    
    
    
                
                
            
            
        
            
    
            
        
    def JoinGuild(self, token: str, invite_code: str, proxy: any = None):
            invite = httpx.get(f"https://discord.com/api/v10/invites/{invite_code}")

            if invite.status_code == 200:
                inviteGuild = invite.json().get("guild").get("id")
                inviteChannel = invite.json().get("channel").get("id")
                inviteChannelType = invite.json().get("channel").get("type")
                magicStuff = str(b64encode((f'{{"location":"Join Guild","location_guild_id":{inviteGuild},"location_channel_id":{inviteChannel},"location_channel_type":{inviteChannelType}}}').encode('ascii'))).split("'")[1]
        
                try:
                    headers = self.headers(token)
                    headers.update({"x-context-properties": magicStuff,})
                    #json = response.json()
                    if self.captcha_solver_type == "2captcha.com":
                        captcha_key = self.getCaptcha(proxy)
                        #print("2Captcha.com Captcha: " + captcha_key)
                    elif self.captcha_solver_type == "hcaptcha_ai":
                        captcha_key = self.AI_Captcha(proxy=proxy)
                        #print("AI_Captcha: " + captcha_key)
                    hcap_join = httpx.Client(headers=headers, proxies=proxy)
                    response = hcap_join.post(f"https://discord.com/api/v10/invites/{invite_code}", json={"captcha_key": captcha_key}, follow_redirects=True)
                    if response.status_code == 200:
                        
                        print(f"Successfully joined %s by using hcap bypass " % (token[:59]))
                        self.total_server_joins_success += 1
                    elif response.status_code == 401:
                        print(
                            f"Invalid account %s" % (token[:59]))
                        # TODO: self.tokens.remove(token)
                        self.total_server_joins_invalid += 1
                    elif response.status_code == 403:
                        print(f"Locked account %s" % (token[:59]))
                        self.total_server_joins_locked += 1
                        # TODO: self.tokens.remove(token)
                    elif response.status_code == 429:
                        print(
                            f"Rate limited %s" % (token[:59]))
                        self.total_rate_limits += 1
                        time.sleep(self.ratelimit_delay)
                        self.JoinGuild(token, proxy)
                    elif response.status_code == 404:
                        print(f"Server-Invite is invalid or has expired :/")
                                    
                    elif response.status_code == 400:
                        # > self.tokens.remove(token)
                        print(f"Error Response [ {response.text} ] [ {response.status_code} ]")

                    else:
                        # > self.tokens.remove(token)
                        pass
                except:
                    raise Exception
                
                



    def vlink(self, inbox):
        def DiscordMail():
            # > Getting the email confirmation link from the email
            scrape_emails = True
            while scrape_emails:
                emails = tm.getEmails(inbox)
                for mail in emails:
                    if "mail.discord.com" in str(mail.sender):
                        for word in mail.body.split():
                            if "https://click.discord.com" in word:
                                email_link = word
                                scrape_emails = False
                                break
            email_link: str = email_link.replace("[", "").replace("]", "")
            return email_link


        confirmation_email = DiscordMail()

        p.info(f"Saving link to [ data/confirmation_emails.txt ] | {confirmation_email[:5]}...")
        with open("data/confirmation_emails.txt", "a") as writemail:
            writemail.write(confirmation_email + "\n")
            writemail.close()
        return confirmation_email







                
    def Register(self, proxy: any = None):
        """
        Auto Registration: [ https://discord.com/register ]
        """


        # >>> Proxy Handler
        if self.proxy_isworking(proxy, True) == True:

            
        
            generating_token_time_start = time.time()


            # >>> Get Cookies
            GET_COOKIE = httpx.get("https://discord.com/register", proxies=proxy).headers['set-cookie']
            sep = GET_COOKIE.split(";")
            sx = sep[0]
            sx2 = sx.split("=")
            dfc = sx2[1]
            split = sep[6]
            split2 = split.split(",")
            split3 = split2[1]
            split4 = split3.split("=")
            sdc = split4[1]

            inbox = tm.generateInbox()
            inbox_token = inbox.token
            
            
            
            email_addr = inbox.address
            username = self.fakename
            password = "".join((random.choice(string.ascii_uppercase)) + (random.choice(string.ascii_lowercase)*7) + (random.choice(string.digits)*4))
            
            date_of_birth = f"197{random.randrange(0,9)}-0{random.randrange(1,9)}-0{random.randrange(1,9)}"
            
            p.solver(f"Solving Captcha [ Captcha Service: ( {self.captcha_solver_type} ) ]")
            
            solving_captcha_time_start = time.time()
            if self.captcha_solver_type == "hcaptcha_ai":
                captcha_solution = self.AI_Captcha(proxy=proxy)
            elif self.captcha_solver_type == "2captcha.com":
                captcha_solution = self.getCaptcha(proxy=proxy)
            solving_captcha_time_end = time.time()
            p.solver(f"Captcha solved in [ {solving_captcha_time_end-solving_captcha_time_start} seconds]")


            payload= {
                "username": f"{username}",
                "email": f"{email_addr}",
                "date_of_birth": date_of_birth,
                "password": password,
                "fingerprint": f"{self.get_fingerprint(proxy)}",
                "gift_code_sku_id": "null",
                "invite": "null",
                "consent": "true", 
                "captcha_key": f"{captcha_solution}"
            }


            payload = {
                "captcha_service": "hcaptcha",
                "captcha_key": captcha_solution,
                "consent": "true",
                "date_of_birth": f"{date_of_birth}",
                "email": f"{email_addr}",
                "gift_code_sku_id": "null",
                "invite": "null",
                "password": password,
                "promotional_email_opt_in": "false",
                "username": username,
            }



            headers = {
                "accept" : "*/*",
                "accept-encoding" : "gzip, deflate, br",
                "accept-language" : "en-US",
                "content-type":"application-json",
                # "cookie":f"__dcfduid={dfc}; __sdcfduid={sdc}; _gcl_au=1.1.33345081.1647643031; _ga=GA1.2.291092015.1647643031; _gid=GA1.2.222777380.1647643031; OptanonConsent=isIABGlobal=false&datestamp=Fri+Mar+18+2022+18%3A53%3A43+GMT-0400+(%E5%8C%97%E7%BE%8E%E4%B8%9C%E9%83%A8%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __cf_bm=.fksdoBlzBs1zuhiY0rYFqFhDkstwwQJultZ756_yrw-1647645226-0-AaluVZQHZhOL5X4GXWxqEIC5Rp3/gkhKORy7WXjZpp5N/a4ovPxRX6KUxD/zpjZ/YFHBokF82hLwBtxtwetYhp/TSrGowLS7sC4nnLNy2WWMpZSA7Fv1tMISsR6qBZdPvg==; locale=en-US",
                "cookie": f"__dcfduid={dfc}; __sdcfduid={sdc}; _gcl_au=1.1.33345081.1647643031; _ga=GA1.2.291092015.1647643031; _gid=GA1.2.222777380.1647643031; OptanonConsent=isIABGlobal=false&datestamp=Fri+Mar+18+2022+18%3A53%3A43+GMT-0400+(%E5%8C%97%E7%BE%8E%E4%B8%9C%E9%83%A8%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __cf_bm=.fksdoBlzBs1zuhiY0rYFqFhDkstwwQJultZ756_yrw-1647645226-0-AaluVZQHZhOL5X4GXWxqEIC5Rp3/gkhKORy7WXjZpp5N/a4ovPxRX6KUxD/zpjZ/YFHBokF82hLwBtxtwetYhp/TSrGowLS7sC4nnLNy2WWMpZSA7Fv1tMISsR6qBZdPvg==; locale=en-US",
                "origin":"https://discord.com",
                "referer":"https://discord.com/register",
                "sec-ch-ua" : "Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99",
                "sec-ch-ua-mobile":"?0",
                "sec-ch-ua-platform":"macOS",
                "sec-fetch-dest":"empty",
                "sec-fetch-mode":"cors",
                "sec-fetch-site":"same-origin",
                "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
                "x-discord-locale": "en-US",
                "x-fingerprint": self.get_fingerprint(proxy),
                "x-super-properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJ6aC1DTiIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85OS4wLjQ4NDQuNzQgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijk5LjAuNDg0NC43NCIsIm9zX3ZlcnNpb24iOiIxMC4xNS43IiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjExOTc2MSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
            }
            client = httpx.Client(headers=headers, proxies=proxy)
            client.headers['x-track' if config['Token-Generator']['invite_code'] == '' else 'x-super-properties'] = self.get_trackers(0 if config['Token-Generator']["invite_code"] == '' else None, True if config['Token-Generator']["invite_code"] == '' else False)
            client.headers['referer'] = f'https://discord.com/invite/{config["Token-Generator"]["invite_code"]}' if config['Token-Generator']["invite_code"] != '' else ''
            client.headers['content-length'] = str(len(json.dumps(payload)))



            resp = client.post("https://discord.com/api/v10/auth/register", json=payload, timeout=self.timeout)


            if config["Token-Generator"]["invite_code"] == '':
                client.headers.pop('x-track')
            
            if resp.status_code == 200 or 201:
                try:
                    token = resp.json()["token"]
                    generating_token_time_end = time.time()
                    p.success(f"Generated Token: [ {token} ] | Generating Time: [ {generating_token_time_end-generating_token_time_start} ]") 
                    self.valid_tokens += 1
                    try:
                        with open(config["Tokens"]["tokens-file"], mode="a+") as writetoken:
                            writetoken.write(token + "\n")
                            writetoken.close()
                    except FileNotFoundError:
                        p.warning(f"File [ {config['Tokens']['tokens-file']} ] not found.")
                    except Exception as e:
                        p.warning(f"Unable to save discord token due to unhandled exception! | Exception: [ {e} ]")
                    
                except:
                    token = ""
                    if resp.json()["message"] == "The resource is being rate limited.":
                        retry_after = float(resp.json()["retry_after"])
                        p.ratelimit(f"Rate Limited | Retry After: [ {retry_after} ] | Changing Proxy")
                        DiscordAPI().Register(proxy)
                    
                
            elif resp.status_code == 429:
                self.rate_limits += 1
                retry_after = float(resp.json()["retry_after"])
                p.ratelimit(f"Rate Limited | Retry After: [ {retry_after} ]")
                time.sleep(retry_after)
                DiscordAPI().Register(proxy)
            
            else:
                p.error(resp.status_code + "     " + resp.text)
                
                
            if bool(self.check_tokens_after_generating) == True:
                if resp.status_code == 200 or 201:
                    try:
                        token = resp.json()["token"]
                        self.Login(token, proxy)
                    except KeyError:
                        token = ""
                        if resp.json()["message"] == "The resource is being rate limited.":
                            retry_after = float(resp.json()["retry_after"])
                            p.ratelimit(f"Rate Limited | Retry After: [ {retry_after} ] | Changing Proxy")
                            DiscordAPI().Register(proxy)
                    
        
            return [token, inbox]

        else:
            # >>> If proxy not working return false
            return False