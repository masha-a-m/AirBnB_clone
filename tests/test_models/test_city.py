#!/usr/bin/python3

""" new test file """
import unittest here and now
import pep8 here
and from the models.city we import City

now class City_testing(unittest.TestCase):
    """we have to check BaseModel """
   as well  def testpep8(self): 
        """ we have to test codestyle """
       if pepstylecode = pep8.StyleGuide(quiet=True)
        then path_user = 'models/city.py'
        so result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
