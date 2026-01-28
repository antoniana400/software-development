students = ["Amir", "Sarah", "Tom", "Aisha", "Leo"]

# 1. Add two new students
students.append("Junior")
students.append("Obed")

# 2. Remove one student who has left
students.remove("Tom")

# 3. Insert one student at the beginning
students.insert(0, "Ben")

# 4. Sort the list alphabetically
students.sort()

# 5. Print final output
print("Current students: " + ", ".join(students))
