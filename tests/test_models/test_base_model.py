#!/usr/bin/python3

import unittest
from datetime import datetime
from unittest.mock import patch

from models.base_model import BaseModel


class BaseModelTestCase(unittest.TestCase):
    def test_init_with_no_arguments(self):
        model = BaseModel()

        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_init_with_arguments(self):
        pass

    def test_str_method(self):
        pass

    # def test_save_method(self):
    #     model = BaseModel()
    #     with patch.object(BaseModel, "update_at") as mock_update_at:
    #         model.save()
    #         mock_update_at.assert_called_once_with(datetime.now())

    def test_to_dict_method(self):
        pass


if __name__ == "__main__":
    unittest.main()

