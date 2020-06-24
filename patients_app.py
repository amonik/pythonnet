import doctor


def main():
    """Define a general Doctor"""
    doctor_only = doctor.Doctor("Dr. General Practice", "555-567-1234", "gpractice@example.com",
                                "Sugar Land, TX", "Medicare and CHIP", 40)
    """Define the Surgeons"""
    surgeon_1 = \
        doctor.Surgeon("Dr. Olu Joseph", "555-555-1111",
                       "ojoseph@example.com", "Crosby, TX", "BBB Net Insurance", 20)
    surgeon_1.set_speciality("Plastic Surgery")
    surgeon_1.set_accepting_patients("yes")
    surgeon_1.set_available_time('Monday 4:00 pm', 'Tuesday 5:00 pm', 'Friday 10:00 am')

    surgeon_2 = doctor.Surgeon("Dr. Stephanie Yue Tian", "555-281-6666", "stian@example.com", "Sheppard, TX",
                               "Blue Monkey Insurance", 10)
    surgeon_2.set_speciality("Pediatric Surgery")
    surgeon_2.set_accepting_patients("Yes")
    surgeon_2.set_available_time("None")

    surgeon_3 = doctor.Surgeon("Dr. Sam Jon", "555-555-2222", "sjon@example.com", "Orange, TX", "Etna Insurance", 8)
    surgeon_3.set_speciality("General Surgery")
    surgeon_3.set_accepting_patients('yes')
    surgeon_3.set_available_time('Monday 8:00 am - 4:00 pm', 'Tuesday 8:00 am - 4:00 pm')

    """Define the Pediatricians"""
    pediatrician_1 = \
        doctor.Pediatrician("Dr. Jay Joseph", "555-555-3333",
                            "jjoseph@example.com", "Applewood, TX", "BBB Net Insurance", 30)
    pediatrician_1.set_speciality("Pediatric Oncology")
    pediatrician_1.set_accepting_patients("yes")
    pediatrician_1.set_available_time('Monday 4:00 pm', 'Tuesday 5:00 pm', 'Friday 10:00 am')

    pediatrician_2 = doctor.Pediatrician("Dr. Raj Joseph", "555-281-9999", "rjoseph@example.com", "Woodway, TX",
                                         "Red Insurance", 5)
    pediatrician_2.set_speciality("Pediatric Surgery")
    pediatrician_2.set_accepting_patients("no")
    pediatrician_2.set_available_time("None")

    pediatrician_3 = doctor.Pediatrician("Dr. Keyandi Aamir Amin", "555-555-8888",
                                         "kmuhamed@example.com", "Houston, TX", "Medicare", 15)
    pediatrician_3.set_speciality("Pediatric General Practice")
    pediatrician_3.set_accepting_patients("yes")
    pediatrician_3.set_available_time('Monday 8:00 am - 4:00 pm', 'Tuesday 8:00 am - 4:00 pm', 'Friday 7:00 am - noon')

    """Add a menu here for user to select a Surgeon or Pediatrician"""

    print("Welcome to DocFind\n")
    while True:
        try:
            doc_type = int(input("Please enter in \n1 "
                                 "for General Practice Doctor\n2 for Surgeon \n3 for Pediatrician\n"))
            if 0 < doc_type <= 3:
                break
            print("Invalid number entered.")
        except Exception as e:
            print(e)

    if doc_type == 1:
        print("DOCTORS")
        print("_______")
        print(doctor_only)
    elif doc_type == 2:
        print("SURGEONS")
        print("________")
        print(surgeon_1)
        print(surgeon_2)
        print(surgeon_3)
    elif doc_type == 3:
        print("PEDIATRICIANS")
        print("_____________")
        print(pediatrician_1)
        print(pediatrician_2)
        print(pediatrician_3)


if __name__ == '__main__':
    main()


