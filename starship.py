class Starship():
    """ This is a class that defines starships from Star Trek"""
    def __init__(self, name, registry, size, crew_complement, speed):
        self.name = name
        self.registry = registry
        self.size = size
        self.crew_complement = 0
        self.speed = 0

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.registry, self.size, self.crew_complement)

    def warp(self, speed):
        self.speed = speed
        print(f"Ship's warp factor is {self.speed}")

    def set_crew_size(self, crew_complement):
        self.crew_complement = crew_complement
        print(f"The ship's crew complement is {self.crew_complement}")


    def description(self, name, registry, size, crew_complement, speed):
        print(f"{self.registry} {self.name} is a {self.size} ship that holds {self.crew_complement}. Maximum warp is {self.speed}")

    def slow_down(self):
        self.speed -= 1
        print(f"Warp factor is now {self.speed}")

enterprise = Starship("Enterprise", "NCC 1701-D", "Constitution", 500, 9)

# print(enterprise)
enterprise.warp(9)
enterprise.set_crew_size(500)
# print(enterprise.warp)
enterprise.description("Enterprise", "NCC 1701-D", "Constitution", 500, 9)

