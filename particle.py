class Particle:

    def __init__ (self, name, mass, charge):
        self.name = name
        self.mass = mass
        self.charge = charge

    def table(self):
        return f"Particles: \n Name: {self.name} \n Mass: {self.mass} \n Charge: {self.charge} \n"

electron = Particle("Electron", 9.1e-31, -1.6e-19)
proton = Particle("Proton", 1.7e-27, 1.6e-19)

print(electron.table())
print(proton.table())