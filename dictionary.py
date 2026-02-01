# dictionary
students = [{"name":"Somchai",
            "age":20,
            "GRADE":"A",
            "city":"bangkok",
            "hobbies":["อ่านหนังสือ","เขียนโค้ด"]
},
{
            "name":"atsadawut",
            "age":20,
            "GRADE":"A+",
            "city":"bangkok",
            "hobbies":["นอน","เขียนโค้ด"]
}]
print(students)
print("/n")
for student in students :
    print(f"ชื่อ: {student['name']}")

students.append( {"name":"man",
            "age":20,
            "GRADE":"A",
            "city":"bangkok",
            "hobbies":["วิ่ง","เขียนโค้ด"]}
            )
print(students)
print("/n")
for student in students :
    print(f"ชื่อ: {student['name']}")

# #ลบ
# students.remove( {"name":"man",
#             "age":20,
#             "GRADE":"A",
#             "city":"bangkok",
#             "hobbies":["วิ่ง","เขียนโค้ด"]}
#             )
# print(students)
# print("/n")
# for student in students :
#     print(f"ชื่อ: {student['name']}")

#เพิ่มจากกการพิมพ์
name = (input("กรุณากรอกชื่อ:"))
print("ชื่อ: ",name)
age = int(input("กรุณากรอกอายุ:"))
print("อายุ: ",age)
GRADE = (input("กรุณากรอกเกรด:"))
print("เกรด: ",GRADE)
city = (input("กรุณากรอกที่อยู่:"))
print("ที่อยู่: ",city)
hobbies = input("กรุณากรอกงานอดิเรก (คั่นด้วย ,): ").split(",")
print("งานอดิเรก: ",hobbies)

students.append( {"name":name,
        "age":age,
        "GRADE":GRADE,
        "city":city,
        "hobbies":hobbies}
)
print("\n")
for student in students :
    print(students)



