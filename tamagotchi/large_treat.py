class LargeTreat:
    def __init__(self):
        self.fullness_bonus = 8
        self.current_treat = 1
        
        
    
    def use_treat(self):
        if self.current_treat == 0:
            return 0
        else:
            self.current_treat -= 1
            return self.fullness_bonus