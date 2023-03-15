class Vault:
    def __init__(self, galleons=8, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"Galleons [{self.galleons}], Sickles [{self.sickles}], Knuts [{self.knuts}]"

    def __add__(self, other):
        return Vault(self.galleons+other.galleons, self.sickles+other.sickles, self.knuts+other.knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter+weasley
print(total)
