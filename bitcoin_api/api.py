from apscheduler.schedulers.background import BackgroundScheduler
from requests import Session
from requests.adapters import HTTPAdapter, Retry
from datetime import datetime
from flask import Flask
import statistics
import requests
import logging
import sys



log_Format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.WARNING, stream=sys.stdout, format=log_Format)


class Btc:
    def __init__(self):
        self.bitcoin_price_list = []
        self.latest_price = "App init, still no price"
        self.logger = logging.getLogger("Btc")

    def add_to_list(self, char: float) -> None:
        """
        This function is meant to implement a "queue" like logic
        """
        if len(self.bitcoin_price_list) >= 60:
            del self.bitcoin_price_list[0]
            self.bitcoin_price_list.append(char)
        else:
            self.bitcoin_price_list.append(char)

    def requests_retry_session(self) -> Session:
        """
        The function returns a requests http session that
        implements a retrying mechanism with backoff
        """
        session = requests.session()
        retry = Retry(total=10,
                      backoff_factor=20
                      )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('https://', adapter)
        return session

    def get_bitcoin_rate(self, coin: str = "USD") -> None:
        self.logger.info("Running get_bitcoin_rate")
        # todo maybe implement a url randomization for the retries ?
        http_session = self.requests_retry_session()
        url = f"https://cex.io/api/last_price/BTC/{coin}"
        try:
            response = http_session.get(url)
            response.raise_for_status()
            response_text = response.json()['lprice']
            self.latest_price = f"{response_text} {coin} at: {datetime.now()}"
            self.add_to_list(float(response_text))
        except requests.exceptions.RequestException as ex:
            self.logger.error(f"{ex}")

    def get_ten_min_average(self) -> str:
        if len(self.bitcoin_price_list) >= 10:
            try:
                average_value = statistics.mean(self.bitcoin_price_list[-60:])
                return str(average_value)
            except Exception as ex:
                self.logger.error(f"An error occurred : {ex}")

        else:
            # todo change that, decide whats the best thing to return
            return f"Not running enough time to calculate 10 min average \n " \
                   f"average for the last {len(self.bitcoin_price_list) * 10 / 60} minutes is : {statistics.mean(self.bitcoin_price_list)}"


app = Flask(__name__)
bitcoin_api = Btc()
scheduler = BackgroundScheduler()
scheduler.add_job(func=bitcoin_api.get_bitcoin_rate, trigger="interval", seconds=10, max_instances=1)
scheduler.start()


@app.route("/btc/average", methods=["GET"])
def tem_min_average_price():
    return bitcoin_api.get_ten_min_average()


@app.route("/btc/USD", methods=["GET"])
def bitcoin_usd_price():
    return bitcoin_api.latest_price

@app.route("/liveness", methods=["GET"])
def liveness():
    return "OK"


@app.route("/readiness", methods=["GET"])
def readinesshealth():
    return "OK"


if __name__ == '__main__':
    app.run()
