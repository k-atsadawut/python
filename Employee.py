class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def get_salary(self):
        return self.salary
    def set_salary(self, new_salary):
        if new_salary <= 15000:
            self.salary = new_salary
            print(f"อัปเดตเงินเดือนเป็น {new_salary} บาท สำเร็จ.")
        else:
            print("เงินเดือนน้อยกว่าค่าแรงขั้นต่ำ ไม่สามารถอัปเดตได้.")
    def show_info(self):
        print(f"ชื่อ: {self.name}")
        print(f"รหัสพนักงาน: {self.employee_id}")
        print(f"เงินเดือน: {self.salary} บาท")

Employee1 = Employee("อัษฎาวุธ", "E001", 2000)
Employee1.show_info()
Employee1.set_salary(15000)