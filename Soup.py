#Nikki's Class
class Fiber:
    """This is the different types of fiber,
    and it shows the project idea and the method used to spin into
    useable fiber for the projects."""
    def __init__(self, source, project):
        self.type = source
        self.project = project
        type_pieces = source.split(" ")
        self.first_part = type_pieces[0]
        self.last_part = type_pieces[-1]
    def ounces(self):
        """Keep track of how many ounces of fiber to spin"""
        grams = int(11)
        ounces = int(2)
        if grams == 16:
            ounces + 1
        print(f'{ounces}oz + {grams}grams')
fiber1 = Fiber("Alpaca", "Sweater")
fiber1.type = "Alpaca"
fiber1.project = "Sweater"
fiber1.wheel = "Ashford"
fiber2 = Fiber("Cotton Bolls", "Woven Hankie")
fiber2.type = "Cotton Bolls"
fiber2.project = "Woven Hankie"
fiber2.spindle = "Charka"
print(fiber1.last_part)
print(fiber2.first_part)
print(fiber1.ounces())