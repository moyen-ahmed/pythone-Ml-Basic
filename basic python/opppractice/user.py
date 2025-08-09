class Resturent:
    def __init__(self,restaurent_name,cuisine_name):
        self.restaturent_name=restaurent_name
        self.cuisine_type=cuisine_name
def describe_resturent(self):
    print(f"The restuernt is called{self.resturet_name}")
    print(f"The cuisine type is{self.cuisine_type}.")
def open_resturant(self):
    print(f"The resturent{self.resturet_name}")
    print()
resturent=Resturent('KFC','Bangladesh')
print(f"Resturent name:{resturent.restaurent_name}")
print(f"Resturent cusine :{resturent.cuisine_type}")
resturent.describe_resturent()
resturent.open_resturant()

class IceCreamStand(Resturent):
    def __init__(self,restaurent_name,cuisine_type,*flavors):
        super().__init__(restaurent_name,cuisine_type)
        self.flavors=flavors
    def describe_flavors(self):
        print(f"The resturent{self.restaurent_name} have {len(self.flavors)} flavors")
        print(f"The flavors are {', '.join(self.flavors)}")
ice_cream=IceCreamStand('KFC','Bangladesh','choclate','vanila','strawberry')
ice_cream.describe_resturent()
ice_cream.describe_flavors()
