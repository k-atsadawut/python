# print("hello")
# name = "atsadawut"
# print(name)
# print( 123)
# print(1.26)

# #name = input("กรุณากรอกชื่อ : ")
# #print("สวัสดี ", name)

# age = 99
# height = 176.5
# is_Student = True
# name = "atsadawut"

# print(type(age))
# print(type(height))
# print(type(is_Student))
# print(type(name))

# a = 10
# b = 3
# print (a+b)
# print (a-b)
# print (a*b)
# print (a/b)
# print (a%b)


# print (a>b)
# print (a<b)
# print (a==b)
# print (a!=b)


#รับค่าผ่านคีย์บอร์ด
#score = int(input("กรุณากรอกคะแนน :"))
# print ("คะแนน : ",score)
# if score >=80:
#     print("เกรด A")
# elif score >=75:
#     print("เกรด B+")
# elif score >=70:
#     print("เกรด B")
# elif score >=65:
#     print("เกรด C+")
# elif score >=60:
#     print("เกรด C")
# elif score >=55:
#     print("เกรด D+")
# elif score >=50:
#     print("เกรด D")
# else:
#     print("ไม่ผ่าน")


# for i in range(1,6):
#     print("รอบที่:",i)


# count = 1
# while count <=5:
#     print("นับ ",count)
#     count +=1

count = 1
sum = 0
while count <=5:
    print("\nครั้งที่ : ",count)
    num = int(input("กรุณากรอกตัวเลข :"))
    print("ตัวเลข: ",num)
    sum +=num
    count +=1
average = sum/5
print(f"\nผลรวม {sum}")
print(f"\nค่าเฉลี่ย {average}")
