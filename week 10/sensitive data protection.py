# HOSPITAL PATIENT DATA SECURITY PROTOTYPE
# Command-Line Application (Learning Prototype)


# LOGIN / AUTHENTICATION SECTION

correct_username = "drSmith"
correct_password = "Cardiology123"

staff_identity = "drSmith@hospital.nhs"
staff_role = "doctor"          # doctor / nurse / admin
staff_department = "cardiology"

attempts = 3
authenticated = False

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("\nLogin successful.\n")
        authenticated = True
        break
    else:
        attempts -= 1
        print(f"Incorrect credentials. Attempts remaining: {attempts}")

if authenticated == False:
    print("\nToo many failed attempts. Access denied.")
    exit()

# INITIALISE DATA STORAGE

patient_pii = ""
encrypted_pii = ""
stored_identity = ""
stored_signature = 0

# MAIN MENU LOOP


while True:
    print("\n--- Hospital Secure Data System ---")
    print("1. Enter or update patient details")
    print("2. Encrypt patient data")
    print("3. Decrypt patient data")
    print("4. Convert patient data (binary / decimal / octal / hex)")
    print("5. Show staff identity and permissions")
    print("6. Exit system")

    choice = input("Choose an option (1-6): ")


    # OPTION 1: ENTER PATIENT DETAILS

    if choice == "1":
        full_name = input("Full name: ")
        dob = input("Date of birth (YYYY-MM-DD): ")
        place_of_birth = input("Place of birth (city/town): ")
        country_of_birth = input("Country of birth: ")
        address = input("Full address: ")

        patient_pii = (
            "Name: " + full_name +
            " | DOB: " + dob +
            " | Place of Birth: " + place_of_birth +
            " | Country of Birth: " + country_of_birth +
            " | Address: " + address
        )

        print("\nPatient details stored successfully.")

    # OPTION 2: ENCRYPT PATIENT DATA

    elif choice == "2":
        if patient_pii == "":
            print("No patient data to encrypt.")
        else:
            encrypted_pii = ""
            stored_signature = 0

            for char in patient_pii:
                encrypted_char = chr(ord(char) + 3)
                encrypted_pii += encrypted_char
                stored_signature += ord(encrypted_char)

            stored_identity = staff_identity

            print("\nPatient data encrypted successfully.")
            print("Data linked to staff identity:", stored_identity)


    # OPTION 3: DECRYPT PATIENT DATA
    # IBE + ABE + DIGITAL SIGNATURE

    elif choice == "3":
        if encrypted_pii == "":
            print("No encrypted data available.")
        else:
            # Attribute-Based Access Control
            if staff_role != "doctor" and staff_role != "nurse":
                print("Access denied: insufficient role permissions.")
            else:
                # Identity-Based Encryption check
                if staff_identity != stored_identity:
                    print("Access denied: identity mismatch.")
                else:
                    # Digital signature check
                    current_signature = 0
                    for char in encrypted_pii:
                        current_signature += ord(char)

                    if current_signature == stored_signature:
                        print("Data integrity check passed: patient record appears unchanged.\n")

                        decrypted_pii = ""
                        for char in encrypted_pii:
                            decrypted_pii += chr(ord(char) - 3)

                        print("Decrypted Patient Information:")
                        print(decrypted_pii)
                    else:
                        print("WARNING: Patient record may have been altered.")


    # OPTION 4: NUMBER FORMAT CONVERSIONS

    elif choice == "4":
        if encrypted_pii == "" and patient_pii == "":
            print("No data available for conversion.")
        else:
            if staff_role != "admin":
                print("Access denied: only admin staff may perform conversions.")
            else:
                data_choice = input("Convert (E)ncrypted or (D)ecrypted data? ").lower()

                if data_choice == "e":
                    data = encrypted_pii
                else:
                    data = patient_pii

                print("\nCharacter conversions:")
                for char in data:
                    value = ord(char)
                    print(
                        f"'{char}' -> "
                        f"Binary: {bin(value)}, "
                        f"Decimal: {value}, "
                        f"Octal: {oct(value)}, "
                        f"Hex: {hex(value)}"
                    )


    # OPTION 5: SHOW STAFF INFO
    elif choice == "5":
        print("\n--- Staff Information ---")
        print("Identity:", staff_identity)
        print("Role:", staff_role)
        print("Department:", staff_department)


    # OPTION 6: EXIT SYSTEM

    elif choice == "6":
        print("\nExiting system. Goodbye.")
        break

    else:
        print("Invalid option. Please choose 1-6.")
