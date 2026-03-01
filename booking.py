import datetime
import uuid

class Student:
    def __init__(self, student_id, name, phone):
        self.student_id = student_id
        self.name = name
        self.phone = phone
        self.bookings = []

    def book_room(self, classroom, date_str, time_str):  # ✅ indent ให้อยู่ใน class
        try:
            booking_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            booking_time = datetime.datetime.strptime(time_str, "%H:%M").time()
        except ValueError:
            print("Invalid date or time format.")
            return None

        if classroom.check_availability(booking_date, booking_time):
            booking = Booking(self, classroom, booking_date, booking_time)
            self.bookings.append(booking)
            classroom.schedule.add_booking(booking)  # ✅ ใช้ add_booking แทน append
            print(f"Booking created for {self.name} for classroom {classroom.room_number} on {date_str} at {time_str}. Status: {booking.status}")
            return booking
        else:
            print(f"Classroom {classroom.room_number} is not available on {date_str} at {time_str}.")
            return None

    def cancel_booking(self, booking):  # ✅ indent ให้อยู่ใน class
        if booking in self.bookings:
            if booking.status == "approved":
                print("Approval for booking must be cancelled by admin.")
            else:
                booking.cancel()
                self.bookings.remove(booking)
                classroom = booking.classroom
                classroom.schedule.remove_booking(booking)
                print(f"Booking cancelled by {self.name}.")  # ✅ แก้ typo
        else:
            print("Booking not found in your list.")

    def view_bookings(self):  # ✅ indent ให้อยู่ใน class
        print(f"\n --- Bookings for {self.name} ---")  # ✅ ย้าย print มาก่อน
        if not self.bookings:
            print(f"{self.name} has no bookings.")
            return
        for booking in self.bookings:
            print(f"ID: {booking.booking_id}, Room: {booking.classroom.room_number}, Date: {booking.date}, Time: {booking.time}, Status: {booking.status}")


class Classroom:
    def __init__(self, room_number, capacity, equipment):
        self.room_number = room_number
        self.capacity = capacity
        self.equipment = equipment
        self.schedule = Schedule(self)

    def check_availability(self, date, time):
        return self.schedule.is_available(date, time)

    def __str__(self):  # ✅ เหลือแค่อันเดียว
        return f"Room {self.room_number} (Capacity: {self.capacity}, Equipment: {', '.join(self.equipment)})"


class Booking:
    booking_counter = 0

    def __init__(self, student, classroom, date, time):
        self.booking_id = f"BK{Booking.booking_counter:04d}"
        Booking.booking_counter += 1
        self.student = student
        self.classroom = classroom
        self.date = date
        self.time = time
        self.status = "pending"

    def approve(self):
        self.status = "approved"
        print(f"Booking {self.booking_id} approved for {self.student.name} in classroom {self.classroom.room_number} on {self.date} at {self.time}.")

    def cancel(self):
        self.status = "cancelled"
        print(f"Booking {self.booking_id} cancelled for {self.student.name} in classroom {self.classroom.room_number} on {self.date} at {self.time}.")

    def __str__(self):
        return f"Booking ID: {self.booking_id}, Student: {self.student.name}, Classroom: {self.classroom.room_number}, Date: {self.date}, Time: {self.time}, Status: {self.status}"


class Schedule:
    def __init__(self, classroom):
        self.classroom = classroom
        self.bookings = {}  # ✅ เปลี่ยนเป็น dict

    def is_available(self, date, time):
        key = (date, time)
        # ✅ ว่างถ้าไม่มี key หรือ booking ถูก cancel แล้ว
        return key not in self.bookings or self.bookings[key].status == "cancelled"

    def add_booking(self, booking):
        key = (booking.date, booking.time)
        if self.is_available(booking.date, booking.time):
            self.bookings[key] = booking
            return True
        else:
            print(f"Error: Add booking failed for classroom {self.classroom.room_number} on {booking.date} at {booking.time}.")
            return False

    def remove_booking(self, booking):
        key = (booking.date, booking.time)
        if key in self.bookings and self.bookings[key] == booking:
            del self.bookings[key]
            return True
        else:
            print(f"Error: Remove booking failed for classroom {self.classroom.room_number}.")
            return False

    def get_all_bookings(self):
        return list(self.bookings.values())  # ✅ แก้จาก self.bookings() เป็น .values()


class Admin:
    def __init__(self, admin_id, name):
        self.admin_id = admin_id
        self.name = name

    def approve_booking(self, booking):
        if booking.status == "pending":
            booking.approve()
        elif booking.status == "approved":
            print(f"Booking {booking.booking_id} is already approved.")
        else:
            print(f"Booking {booking.booking_id} cannot be approved, current status: {booking.status}.")

    def cancel_booking(self, booking):
        if booking.status in ["pending", "approved"]:
            booking.cancel()
            booking.student.bookings.remove(booking)
            booking.classroom.schedule.remove_booking(booking)
            print(f"Booking {booking.booking_id} cancelled by admin {self.name}.")
        else:
            print(f"Booking {booking.booking_id} cannot be cancelled, current status: {booking.status}.")

    def view_all_bookings(self, all_classrooms):
        print(f"\n --- All Bookings managed by Admin {self.name} ---")
        found_bookings = False
        for classroom in all_classrooms:
            for booking in classroom.schedule.get_all_bookings():
                print(booking)
                found_bookings = True
        if not found_bookings:
            print("No bookings found across all classrooms.")


# --- ทดสอบ ---
print("--- เริ่มต้นการจำลองการจองห้องเรียน ---")
Student1 = Student("S001", "Alice", "123-456-7890")
Student2 = Student("S002", "Bob", "987-654-3210")

room101 = Classroom("101", 30, ["Projector", "Whiteboard"])
room102 = Classroom("102", 20, ["Whiteboard"])

Admin1 = Admin("A001", "Atsadawut")

print("\n--- สถานะเริ่มต้น ---")
print(room101)
print(room102)

book_Alice_1 = Student1.book_room(room101, "2026-10-01", "10:00")
if book_Alice_1:
    Student1.view_bookings()
    room101.schedule.get_all_bookings()

book_Bob_1 = Student2.book_room(room101, "2026-10-01", "10:00")
if book_Bob_1:
    Student1.view_bookings()
    room101.schedule.get_all_bookings()


book_Bob_1 = Student2.book_room(room102, "2026-10-01", "10:00")
if book_Bob_1:
    Student1.view_bookings()
    room102.schedule.get_all_bookings()
