from recipe import RecipeStep
from unit import Timespan

class User:
    def __init__(self, time_m = 10) -> None:
        self.time_m = time_m
    
    def estimated_time(self, step: RecipeStep) -> Timespan:
        # TODO: hard coded
        
        return Timespan(self.time_m, 'm')
        
