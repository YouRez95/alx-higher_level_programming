#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ test base class """

    def setUp(self):
        """ setup """
        Base._nb_objects = 0

    def test_id(self):
        """ test id """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_init(self):
        """ test init """
        with self.assertRaises(TypeError) as err:
            Base.__init__()
        err_msg = "Base.__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(err_msg, str(err.exception)) 

    def test_more_id(self):
        """ id """
        b = Base()
        b = Base()
        b = Base(12)
        b = Base()
        self.assertEqual(getattr(Base, "_nb_objects"), b.id)

if __name__ == '__main__':
    unittest.main()
