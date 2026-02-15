class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
    
    def get_balance(self):
        return self._balance
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"ฝากเงิน {amount} บาท สำเร็จ. ยอดเงินคงเหลือ: {self._balance} บาท.")
        else:
            print("จำนวนเงินที่ฝากต้องมีค่ามากกว่า 0 บาท.")

    def withdraw(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print(f"ถอนเงิน {amount} บาท สำเร็จ. ยอดเงินคงเหลือ: {self._balance} บาท.")
            else:
                print("ยอดเงินในบัญชีไม่เพียงพอสำหรับการถอน.")
        else:
            print("จำนวนเงินที่ถอนต้องมีค่ามากกว่า 0 บาท.")


# my_account = BankAccount("1234567890", 1000)
# print(f"ยอดเงินคงเหลือ: {my_account.get_balance()} บาท.")
# my_account.deposit(1000)
# my_account.withdraw(1500)
# print()

try :print(my_account._balance)
except AssertionError as e:
    print(f"พิสุจการเข้าถึง -balance โดยตรงไม่ได้")

try : my_account._balance = 9999999
except AssertionError as e:
    print(f"ยอดคงเหลือหลังจากพยายามแก้ไขโดยตรง: {my_account.get_balance()} บาท.")