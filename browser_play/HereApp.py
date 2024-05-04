import logging
import configparser
import time
import pyautogui

from playwright.sync_api import Playwright, sync_playwright, expect


class HereApp:
    logging.basicConfig(level=logging.INFO, filename='logs.log',
                        format='%(asctime)s %(levelname)s %(message)s')

    def __init__(self, index, account, profile, config_file_path):
        self.__index = index
        self.__account = account
        self.__url = 'https://web.telegram.org/a/#6865543862'
        self.__profile = profile
        self.config = configparser.ConfigParser()
        self.config.read(config_file_path)

    def run(self) -> None:
        with sync_playwright() as playwright:
            logging.info(f"ID: {self.__index} Started " + self.__account)

            args = [f"--profile-directory={self.__profile}"]
            browser = playwright.chromium.launch_persistent_context(
                user_data_dir=f'C:\\Users\\Geometry\\AppData\\Local\\Google\\Chrome\\User Data\\',
                headless=False,
                channel='chrome',
                args=args
            )

            page = browser.new_page()
            page.set_default_timeout(120_000)
            # input("Press Enter to go next")
            page.goto(self.__url)
            try:
                time.sleep(15)
                # page.get_by_role("button", name=" Launch Blum").last.click()
                # page.get_by_role("span", name="Launch Blum").last.click()
                page.get_by_text("Launch Blum").click()
                # page.get_by_role("button", name="Launch Blum ").nth(0).click()
                time.sleep(10)
                try:
                    page.get_by_role("button", name="Confirm").nth(0).click()
                except Exception as e:
                    pass
                time.sleep(60)
                try:
                    page.frame_locator("iframe[title=\"Blum Web App\"]").get_by_role("button", name="Claim").click()
                except Exception as e:
                    print("No Claim button")
                time.sleep(10)

                page.frame_locator("iframe[title=\"Blum Web App\"]").get_by_role("button", name="Start farming").click()
                time.sleep(10)
                try:
                    page.frame_locator("iframe[title=\"Blum Web App\"]").get_by_role("button",
                                                                                     name="Start farming").click()
                except Exception as e:
                    pass

                page.frame_locator("iframe[title=\"Blum Web App\"]").get_by_role("link", name="Frens").click()
                time.sleep(5)
                try:
                    page.frame_locator("iframe[title=\"Blum Web App\"]").get_by_role("button", name="Claim").click()
                except Exception as e:
                    pass
                time.sleep(5)
                page.frame_locator("iframe[title=\"Blum Web App\"]").get_by_role("button", name="Frens").click()
            except Exception as e:
                print(e)
            page.close()
            browser.close()
            logging.info("Ended " + self.__account + f" ID: {self.__index}")

