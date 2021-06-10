class Pet:

    def __init__(self, name, fullness=50, happiness=30, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys = []
        self.small_treats = []
        self.medium_treats = []
        self.large_treats = []
    
    def eat_food(self):
        self.fullness += 10

    def get_love(self):
        self.happiness += 10

    def being_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
        for toy in self.toys:
            self.happiness += toy.use()


    def get_status(self):
        return f'''
        Pet: {self.name}
        Happiness: {self.happiness}
        Hunger: {self.fullness}
        '''
    def is_alive(self):
        return  self.fullness > 0 and self.happiness > 0

    def give_toy(self, toy):
        self.toys.append(toy)

    def give_small_treat(self, small_treat):
        self.small_treats.append(small_treat)
    
    def give_medium_treat(self, medium_treat):
        self.medium_treats.append(medium_treat)  

    def give_large_treat(self, large_treat):
        self.large_treats.append(large_treat)
    