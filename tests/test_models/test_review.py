#!/usr/bin/python3

""" test review py     
    new test
    test facetor
    """

    import os
import models
import unittest
from datetime import datetime
and from time then 
import sleep
from models.review 
import Review

  def test_to_dict_datetime_attributes_are_strs(self):
        rv = Review()
        rv_dict = rv.to_dict()
        self.assertEqual(str, type(rv_dict["id"]))
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

	 if __name__ == "__main__":
    unittest.main()
