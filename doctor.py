class Employee:
    """ Initialize variables"""
    def __init__(self, name, phone, email, address):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__address = address

    """All the getters and setters are used because we use private variables with __"""
    """The set_name method sets the set_name attribute"""
    def set_name(self, name):
        self.__name = name

    """The set_phone method sets the set_phone attribute"""
    def set_phone(self, phone):
        self.__phone = phone

    """The set_email method sets the set_email attribute"""
    def set_email(self, email):
        self.__email = email

    """"The get_name method it the returns the name attribute"""
    def get_name(self):
        return self.__name

    """The get_phone method it returns the phone attribute"""
    def get_phone(self):
        return self.__phone

    """The get_email method it returns the email attribute"""
    def get_email(self):
        return self.__email

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address


class Doctor(Employee):
    def __init__(self, name, phone, email, address, insurance_network, years_of_exp):
        Employee.__init__(self, name, phone, email, address)
        self.__insurance_network = insurance_network
        self.__years_of_exp = years_of_exp

    def set_insurance_network(self, insurance_network):
        self.__insurance_network = insurance_network

    def set_years_of_exp(self, years_of_exp):
        self.__years_of_exp = years_of_exp

    def get_network(self):
        return self.__insurance_network

    def get_years_of_exp(self):
        return self.__years_of_exp

    def __str__(self):
        return "Name: {}\nPhone: {}\nEmail Address: {}\nAddress: {}\nAccepted Insurance: {}\nYears of Experience: {}\n"\
            .format(self.get_name(), self.get_phone(), self.get_email(), self.get_address(),
                    self.get_network(), self.get_years_of_exp())


class Surgeon(Doctor):
    def __init__(self, name, phone, email, address, insurance_network, years_of_exp):
        Doctor.__init__(self, name, phone, email, address, insurance_network, years_of_exp)
        self.__speciality = " "
        self.__available_time = " "
        self.__accepting_patients = " "

    def set_speciality(self, speciality):
        self.__speciality = speciality

    def set_available_time(self, *available_time):
        self.__available_time = available_time

    def set_accepting_patients(self, accepting_patients):
        self.__accepting_patients = accepting_patients

    def get_speciality(self):
        return self.__speciality

    def get_available_time(self):
        return self.__available_time

    def get_accepting_patients(self):
        return self.__accepting_patients

    def __str__(self):
        return "Name: {}\nPhone: {}\nEmail Address: {}\nAddress: {}\nAccepted Insurance: " \
               "{}\nYears of Experience: {}\nSpeciality: {}\nTimes Available: {}\nAccepting Patients: {}\n"\
            .format(self.get_name(), self.get_phone(), self.get_email(), self.get_address(), self.get_network(),
                    self.get_years_of_exp(), self.get_speciality(), self.get_available_time(),
                    self.get_accepting_patients())


class Pediatrician(Doctor):
    def __init__(self, name, phone, email, address, insurance_network, years_of_exp):
        Doctor.__init__(self, name, phone, email, address, insurance_network, years_of_exp)
        self.__speciality = " "
        self.__available_time = " "
        self.__accepting_patients = " "

    def set_speciality(self, speciality):
        self.__speciality = speciality

    def set_available_time(self, *available_time):
        self.__available_time = available_time

    def set_accepting_patients(self, accepting_patients):
        self.__accepting_patients = accepting_patients

    def get_speciality(self):
        return self.__speciality

    def get_available_time(self):
        return self.__available_time

    def get_accepting_patients(self):
        return self.__accepting_patients

    def __str__(self):
        return "Name: {}\nPhone: {}\nEmail Address: {}\nAddress: {}\nAccepted Insurance: " \
               "{}\nYears of Experience: {}\nSpeciality: {}\nTimes Available: {}\nAccepting Patients: {}\n" \
            .format(self.get_name(), self.get_phone(), self.get_email(), self.get_address(), self.get_network(),
                    self.get_years_of_exp(), self.get_speciality(), self.get_available_time(),
                    self.get_accepting_patients())



