class Patient:
    def __init__(self, first_name, middle_name, last_name, emergency_contact):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__emergency_contact = emergency_contact

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_emergency_contact(self, emergency_contact):
        self.__emergency_contact = emergency_contact

    def get_first_name(self):
        return self.__first_name

    def get_middle_name(self):
        return self.__middle_name

    def get_last_name(self):
        return self.__last_name

    def get_emergency_contact(self):
        return self.__emergency_contact
