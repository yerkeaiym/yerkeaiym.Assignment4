import jwt
from base64 import b64decode
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
from bs4 import BeautifulSoup

class DataScrapper:
    def get_html(self, url):
        r = requests.get(url)
        return r

    def get_price(self, html):
        soup = BeautifulSoup(html.content, "html.parser")
        price = soup.find_all("div", class_="priceValue")
        return price

    def get_name(self, html):
        soup = BeautifulSoup(html.content, "html.parser")
        name = soup.find("h2", class_="sc-lg9q90x-0.jCInrl h1")
        return name

    def get_marketcap(self, html):
        soup = BeautifulSoup(html.content, "html.parser")
        marketcap = soup.find("div", class_="statsValue")
        return marketcap

    def get_circulating_supply(self, html):
        soup = BeautifulSoup(html.content, "html.parser")
        circulating_supply = soup.find("div", class_="sc-16r8icm-0 inUVOz").find("div", class_="statsValue")
        return circulating_supply

    def get_volume(self, html):
        soup = BeautifulSoup(html.content, "html.parser")
        volume = soup.find("div", class_="statsValue").find_next("div", class_="statsValue").find_next("div",
                                                                                                       class_="statsValue")
        return volume

    def get_data_by_name(self, name):
        url = "https://coinmarketcap.com/currencies/" + name.lower() + "/"
        if str(self.get_price(self.get_html(url))) is None:
            print('No such a currency!')
        else:
            print('Name: ', name.capitalize())

            price = ""
            for d in str(self.get_price(self.get_html(url)))[25:]:
                if d == '<':
                    break
                price += d
            print('Price: ', price)

            marketcap = ""
            for s in str(self.get_marketcap(self.get_html(url)))[25:]:
                if s == '<':
                    break
                marketcap += s
            print('Marketcap: ', marketcap)

            circulating_supply = ""
            for g in str(self.get_circulating_supply(self.get_html(url)))[24:]:
                if g == '<':
                    break
                circulating_supply += g
            print('Circulating_Supply: ', circulating_supply)

            volume = ""
            for k in str(self.get_volume(self.get_html(url)))[25:]:
                if k == '<':
                    break
                volume += k
            print('Volume: ', volume)
