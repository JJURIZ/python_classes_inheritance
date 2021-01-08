class Phone():
    """This is a phone class that can be used for inheritance purposes"""
    def __init__(self, phone_number, color):
        self.phone_number = phone_number
        self.color = color

    def __str__(self):
        return f"This phone belongs to {self.phone_number}"
    
    def call(self, other_number):
        print(f"Calling number: {other_number}")

    def text(self, other_number, message):
        print(f"Sending text to {other_number}")
        print(message)

    def open_app(self, app_name):
        print(f"Opening {app_name}")


class Android(Phone):
    def __init__(self, phone_number, color, size):
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery = 50
        self.size = size

    def __str__(self):
        return f"Android phone that belongs to number {self.phone_number} and battery life is {self.battery}."

    def set_passcode(self, passcode):
        self.passcode = passcode

    def unlock_phone(self, passcode):
        if (passcode == self.passcode):
            print("Phone unlocked")
        else: 
            print("You entered the wrong passcode :(.")

    def view_battery_life(self):
        print(f"Battery Life: {self.battery}")

    def charge_phone(self, charging_amount):
        self.battery += charging_amount

        if (self.battery > 100):
            self.battery = 100

    def view_phone_number(self):
        print(f"Phone number: {self.phone_number}")

# frank_phone = Android('888-555-4356', 'black')

# frank_phone.view_battery_life()
# frank_phone.charge_phone(200)
# frank_phone.view_battery_life()
# frank_phone.view_phone_number()
# frank_phone.call('555-867-5309')
# print(frank_phone)

class IPhone(Phone):
    def __init__(self, phone_number, color, siri, wallpaper):
        super().__init__(phone_number, color)
        self.siri = False
        self.wallpaper = None

    def siri_status(self, siri):
        if (siri == False):
            self.siri = True
        else: 
            self.siri = False
    
    def set_wallpaper(self, wallpaper):
        self.wallpaper = wallpaper
        print(f"Your new wallpaper is {wallpaper}")

rome_phone = IPhone('555-867-5309', 'black', True, 'Abstract')
print(rome_phone)
