class UnauthorizedAccessException(Exception):
    pass

class Vault:
    def __init__(self,pin_code ):
        self.__pin_code = pin_code

    def open_vault(self, entered_pin):
        if entered_pin == self.__pin_code:
            print("Vault opened successfully!")

        else:
            #print("Wrong PIN! Alarm triggered!")
            raise UnauthorizedAccessException("Wrong PIN! Alarm triggered!")


valt = Vault(201011)
try:
    valt.open_vault(110011)
except UnauthorizedAccessException as e:
    print(f"⚠️ Security System Caught Error: {e}")