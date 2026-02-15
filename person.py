class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"สวัสดชั้นชื่อ {self.name} และอายุ {self.age} ปี."

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id


    def study(self):
        return f"{self.name} กำลังเรียนอยู่."

    def introduce(self):
        parent_introduction = super().introduce()
        return f"{parent_introduction} รหัสนักศึกษา {self.student_id}."

# person1 = Person("อัษฎาวุธ", 20)
# print(person1.introduce())

# student1 = Student("อัษฎาวุธ", 20, "671102392")
# print(student1.introduce())
# print(student1.study())

#สร้างคลาส  teacher โดยมี method  ตัดเกรดจากคะแนน5 ช่อง
# method ตัดเกรดจากคะแนน5 ช่อง จิตพิสัย สอบกลางภาค สอบปลายภาค ปฏิบัติ งานที่ได้รับมอบหมาย 
# method ตัดเกรด
# methot รายงานผลคะแนน

class Teacher(Person):
    def __init__(self,name,age,subjectid):
        super().__init__(name,age)
        self.subjectid = subjectid
        self.introduction = f"{self.name} สอนวิชา {self.subjectid}."



    def calculate_score(self, action, midetrm, final, workshop, assignment):
        self.action = action
        self.midetrm = midetrm
        self.final = final
        self.workshop = workshop
        self.assignment = assignment
        self.total = self.action + self.midetrm + self.final + self.workshop + self.assignment

    def calculate_grade(self):
        if self.total >= 90:
            return "A"
        elif self.total >= 80:
            return "B"
        elif self.total >= 70:
            return "C"
        elif self.total >= 60:
            return "D"
        else:
            return "F"
        

    def report(self):
        grade = self.calculate_grade()
        return (
            f"อาจารย์ {self.name} วิชา {self.subjectid}\n"
            f"คะแนนรวม: {self.total}\n"
            f"เกรด: {grade}"
        )
teacher1 = Teacher("อัษฎาวุธ", 30, "คณิตศาสตร์")
teacher1.calculate_score(10, 20, 30, 20, 10)
print(teacher1.report())





