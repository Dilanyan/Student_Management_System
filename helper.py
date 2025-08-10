import re

class Helper:
    """
        In this class collected all methods that will help to do something, for example:
         user input, 
         checking input
         collect user data
         write in a file
         ...
    """
    # This method checks if a user inputs a digit then return int
    @staticmethod
    def input_digit_from_user(inpt_text, field_text=''):
        while not inpt_text.isdigit() or inpt_text == "0":
            inpt_text = input(f"{field_text}: ")
        return int(inpt_text)

    # This method for name and surname the input text will be cleared from numbers and other characters
    @staticmethod
    def input_username_surname(input_text, field_text=''):
        reg_patt = r"^[A-Za-z]+(?:[-' ][A-Za-z]+)*$"
        is_this_valid_name = False if re.findall(reg_patt, input_text) else True

        while is_this_valid_name:
            input_text = input(f"{field_text}: ")
        return input_text.capitalize()