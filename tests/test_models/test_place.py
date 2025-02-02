#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place


    def test_user_id(self):
        """test type  """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_city_id(self):
        """ test type"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_name(self):
        """test type  """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ test type"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ test type """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ test type"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)
    def test_max_guest(self):
        """ tests the type of the max guest"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)


    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_longitude(self):
        """ test if the type is float"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)
