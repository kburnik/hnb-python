#!/usr/bin/env python
import os
import urllib2

class UrlFetcher(object):
  def fetch(self, url):
    return urllib2.urlopen(url).read()

class Currency(object):
  def __init__(self, currency=None, buy_price=0, mid_price=0, sell_price=0):
    self.buy_price = buy_price
    self.mid_price = mid_price
    self.sell_price = sell_price

class CurrencyTable(object):
  def __init__(self, raw_data):
    self._table = {}
    for line in raw_data.split("\r\n"):
      parts = line.split()
      if len(parts) != 4:
        continue

      parts[0] = parts[0][3:6]
      for i in range(1, 4):
        parts[i] = float(parts[i].replace(',', '.'))

      print parts
      self._table[parts[0]] = Currency(parts[0], parts[1], parts[2], parts[3])

  def get(self, currency):
    return self._table[currency]

url="http://hnb.hr/tecajn/f290815.dat"

url_fetcher = UrlFetcher()
data = url_fetcher.fetch(url)
table = CurrencyTable(data)

print table.get('USD')
