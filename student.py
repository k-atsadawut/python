class Student :
    def __init__(self, name,  student_id,):#Attribute
        #Instance variables
        self.name = name
        self.student_id = student_id
        
    def introduce(self):
        print(f"ชั้นชื่อ {self.name} รหัสนักศึกษา {self.student_id}")

student1 = Student("ซันราคุ", "S67890")
student1.introduce()

def calculate_score(score):
    action= int(input("กรุณากรอกคะแนนจิตพิสัย(10คะแนน) :"))
    print ("คะแนนจิตพิสัย : ",action)
    midetrm = int(input("กรุณากรอกคะแนนกลางภาค(45คะแนน) :"))
    print ("คะแนนกลางภาค : ",midetrm)
    final = int(input("กรุณากรอกคะแนนปลายภาค(45คะแนน) :"))
    print ("คะแนนปลายภาค : ",final)
    total_score = score + action + midetrm + final
    print("คะแนนรวมทั้งหมด :", total_score)
    return total_score

def calculate():
    score = calculate_score(0)
    if score >=80:
        print("เกรด A")
        return score, "A"
    elif score >=75:
        print("เกรด B")
        return score, "B"
    elif score >=60:
        print("เกรด C")
        return score, "C"
    else:
        print("เกรด F")
        return score, "F"
    
    


score,grade = calculate()

print("---------------")
print(f"ผลลัพธ์การคำนวณเกรดสำหรับนักศึกษา :{student1.name} รหัส : {student1.student_id} คือ คะแนน {score} เกรด {grade}")