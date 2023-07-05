import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    # Assertions
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])

    self.assertEqual(stock, 'ABC')
    self.assertAlmostEqual(bid_price, 120.48)
    self.assertAlmostEqual(ask_price, 121.2)
    self.assertAlmostEqual(price, 120.84)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    # Assertions
    stock, bid_price, ask_price, price = getDataPoint(quotes[1])

    self.assertEqual(stock, 'DEF')
    self.assertAlmostEqual(bid_price, 117.87)
    self.assertAlmostEqual(ask_price, 121.68)
    self.assertAlmostEqual(price, 119.775)


if __name__ == '__main__':
    unittest.main()
