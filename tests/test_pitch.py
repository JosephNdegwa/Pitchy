import unittest
from app.models import User


class UserTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the User class
    '''

    def setup(self):
        '''
        Set up method that will run before every Test
        '''
        self  = User('Be your own boss')

        
    def test_instance(self):
        self.assertTrue(isinstance(self.get_pitch, User))