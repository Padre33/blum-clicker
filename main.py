import datetime
import pytz
import time
import configparser

import pandas as pd

from browser_play.HereApp import HereApp

import logging


def get_csv():
    config = configparser.ConfigParser()
    config.read('conf')
    csv = pd.read_csv(config['CSV']['link'])
    return csv


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='logs.log',
                        format='%(asctime)s %(levelname)s %(message)s')

    while True:
        c = get_csv().to_dict(orient='index')

        start_time = datetime.datetime.now(pytz.timezone('Asia/Almaty'))

        print("Claiming started at: ", start_time)
        for index in c:
            acc_info = c.get(index)
            account = HereApp(
                index,
                acc_info['account'],
                acc_info['browser_profile'],
                'conf'
            )
            try:
                account.run()
            except Exception as e:
                logging.error(f'Account {acc_info["account"]} has error: ', e)
                print(f'Account {acc_info["account"]} has error: \n', '\n____________')

        print("Claiming enden at: ", datetime.datetime.now(pytz.timezone('Asia/Almaty')))
        print(datetime.datetime.now(pytz.timezone('Asia/Almaty'))-start_time)

        time_to_sleep = 8*60
        print('Sleep for ',
              ((time_to_sleep * 60) - (datetime.datetime.now(pytz.timezone('Asia/Almaty')) - start_time).seconds) / 60)
        time.sleep(
            abs((time_to_sleep * 60) - (datetime.datetime.now(pytz.timezone('Asia/Almaty')) - start_time).seconds))

        # time.sleep((8*60*60))
