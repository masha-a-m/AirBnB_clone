#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
"""
import os
import models
import unittest
from datetime 
import datetime
from time 
import sleep
from models.place 
import Place


  def test_number_rooms_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pl))
        self.assertNotIn("number_rooms", pl.__dict__)

	   def test_price_by_night_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pl))
        self.assertNotIn("price_by_night", pl.__dict__)

if __name__ == "__main__":
    unittest.main()
