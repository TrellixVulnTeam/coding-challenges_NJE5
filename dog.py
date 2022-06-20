class Dog:

    def __init__(self,name):
        self.name=name
        self.tricks = []

    def add_trick(self,trick):
        self.tricks.append(trick)

pichorrao = Dog('Pichorrao')
pichorrao.add_trick('Cambalhota')
pichorrao.add_trick('Morto')
pichorrao.add_trick('Jump')
pichorrao.add_trick('Mortal')
pichorrao.add_trick('Carinho')
pichorrao.add_trick('Kitchen Tour')

print("Name: ",pichorrao.name)
for trick in pichorrao.tricks:
    print('Trick: ',trick)