import unittest
from uber import SignUp, CombineData


class TestApp(unittest.TestCase):

    def test_validate_email_value_error(self):
        with self.assertRaises(ValueError):
            SignUp.validate_email('greg@gmail.com-=')

    def test_validate_email_returns_email(self):
        signup = SignUp.validate_email('greg@gmail.com')
        self.assertEqual(signup, 'greg@gmail.com')

    def test_validate_mobile_value_error(self):
        with self.assertRaises(ValueError):
            SignUp.validate_mobile('qww234455')

    def test_validate_email_returns_phone_number(self):
        mobile = SignUp.validate_mobile('703100999')
        self.assertEqual(mobile, '703100999')

    def test_full_name(self):
        name = CombineData('greg', 't', '+256', '703100999', 'greg@gmail.com')
        self.assertEqual(name.combine_name(), 'greg  t')


if __name__ == '__main__':
    unittest.main()