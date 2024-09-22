
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        # self.pet_type = pet_type

        if pet_type.lower() not in self.PET_TYPES:
            raise Exception(f"Invalid pet type.")

        self.pet_type = pet_type.lower()
        self.owner = owner
        self.__class__.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [Pet for Pet in Pet.all if Pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise ValueError ("invalid pet type!")
        
    def get_sorted_pets(self):
        owner_pets = self.pets()
        sorted_pets = sorted(owner_pets, key=lambda x: x.name)
        return sorted_pets
