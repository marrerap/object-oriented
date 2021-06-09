from pet import Pet

class CuddlyPet(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.hunger += 2

    
    
    def cuddle(self, other_pet):
        other_pet.get_love()

    def being_alive(self):
        super().being_alive()
        self.happiness += self.mopiness/2
        
    
    def get_status(self):
        return f'''
        Pet: {self.name}
        Happiness: {self.happiness}
        Hunger: {self.fullness}
        Extra Cuddly!!!!!!!!!
        '''