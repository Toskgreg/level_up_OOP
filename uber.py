import re


class SignUp(object):

    def __init__(self, first_name, last_name, country_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.country_code = country_code
        self.phone_number = SignUp.validate_mobile(phone_number)
        self.email_address = SignUp.validate_email(email)

    @staticmethod
    def validate_email(email):
        email_regex = re.compile(r"^[A-Za-z0-9_-]+@[A-Za-z0-9_-]+\.[a-zA-Z]*$")
        if not email_regex.match(email):
            print('invalid email')
            raise ValueError("Wrong email format")
        else:
            print('valid email')
            print(email)
            return email

    @staticmethod
    def validate_mobile(phone_number):

        rule = re.compile(r"^[0-9]{9,14}$")
        if not rule.search(phone_number):
            print("Invalid mobile number.")
            raise ValueError("Wrong phone number")
        else:
            return phone_number


class CombineData(SignUp):

    def __init__(self, first_name, last_name, country_code, phone_number, email):
        super().__init__(first_name, last_name, country_code, phone_number, email)

    def combine_name(self):
        full_name = '{}  {}'.format(self.first_name, self.last_name)
        print(full_name)
        return full_name

    def combine_phone_number(self):
        full_number = '{}{}'.format(self.country_code, self.phone_number)
        print(full_number)
        return full_number

    def combine_all_data_and_save_to_file(self):
        all_data = '{} {} {}{} {}'.format(self.first_name, self.last_name, self.country_code, self.phone_number, self.email_address)
        save_data = all_data + '\n'
        data = open('data.txt', 'a')
        data.write(save_data)
        data.close()
        print(all_data)
        return all_data


name = CombineData('greg', 't', '+256', '703100999', 'greg@gmail.com')
name.combine_name()
name.combine_phone_number()
name.combine_all_data_and_save_to_file()

