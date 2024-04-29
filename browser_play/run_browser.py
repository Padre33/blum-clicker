import time
import re
from playwright.sync_api import Playwright, sync_playwright, expect
import random


class BrowserPlay:
    __WIDTH = random.randint(400, 500)
    __HEIGHT = random.randint(850, 950)
    __app_url = ''
    __trigger = True

    def __init__(self, profile, proxy_host, url):
        self.__profile = profile
        self.__PROXY_IP = proxy_host
        self.__app_url = url

    def parse(self):
        with sync_playwright() as playwright:
            args = [f"--profile-directory={self.__profile}"]
            browser = playwright.chromium.launch_persistent_context(
                user_data_dir=f'C:\\Users\\Geometry\\AppData\\Local\\Google\\Chrome\\User Data\\',
                channel='chrome',
                args=args,
                headless=False
            )
            # browser = playwright.chromium.launch(headless=False)
            print("Started " + self.__profile)
            self.page = browser.new_page()
            self.page.set_default_timeout(60_000)
            self.page.goto("https://web.telegram.org/k/#@herewalletbot")
            self.page.get_by_role("link", name=" Open Wallet 🎯").click()
            self.page.get_by_role("button", name="Launch").click()
            self.page.set_default_timeout(60_000)
            try:
                balance = self.page.locator('div > p.sc-fqkvVR.sc-iGgWBj.hYsjZR.kQLkDU.fitted').nth(0).all_text_contents()
                print(f'Balance {balance[0]} Account {self.__profile}')
            except Exception as e:
                print(e)
            self.page.frame_locator("iframe").get_by_role("heading", name="Storage").click()
            self.page.set_default_timeout(10_000)
            try:
                self.page.frame_locator("iframe").get_by_role("button", name="Check NEWS").click()
            except Exception as e:
                print("No News button " + self.__profile)

            if self.page.frame_locator("iframe").get_by_role("button", name="Claim HOT").is_disabled():
                print("Claim disabled " + self.__profile)
            if self.page.frame_locator("iframe").get_by_role("button", name="Claim HOT").is_enabled():
                self.page.frame_locator("iframe").get_by_role("button", name="Claim HOT").click()
                self.page.wait_for_timeout(60_000)
                print('Claimed ' + self.__profile)

        print("Ended " + self.__profile)