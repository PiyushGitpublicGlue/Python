class Thermostat:
    def __init__(self,room_name,temperature=22):
        self.room_name = room_name
        self.temperature= temperature

    def set_temperature(self,new_temperature):
        if 15<=new_temperature<=30:
            self.temperature = new_temperature
        else:
            print("Temperature out of safe limits!")

    def status(self):
        print(f"The {self.room_name} is currently at {self.temperature} degrees.")

thermo = Thermostat("Bedroom")
thermo.status()
thermo.set_temperature(25)
thermo.status()
thermo.set_temperature(30)
thermo.status()