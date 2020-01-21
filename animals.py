class Animal:

    def __init__(self, name, energy=100, init_parameters=dict()):
        if init_parameters:
            self.name = init_parameters.get("name")
            self.energy = init_parameters.get("energy", energy)
        else:
            self.name = name
            self.energy = energy

    def say(self):
        print(f"Hello, i'm {self.__class__.__name__} and my name is {self.name}.")

    def get_energy(self):
        return self.energy

    @property
    def run_energy(self):
        return None

    @property
    def swim_energy(self):
        return None

    @property
    def fly_energy(self):
        return None

    def run(self):
        if self.run_energy:
            print("My name is "+str(self.name)+" and i running.")
            self.energy = self.energy - self.run_energy
        else:
            print(f"My name is {self.name} and I can't run.")

    def swim(self):
        if self.swim_energy:
            print(f"My name is {self.name} and i swimming.")
            self.energy = self.energy - self.swim_energy
        else:
            print(f"My name is {self.name} and I can't swim.")

    def fly(self):
        if self.fly_energy:
            print(f"My name is {self.name} and I flying.")
            self.energy = self.energy - self.run_energy
        else:
            print(f"My name is {self.name} and I can't fly.")
