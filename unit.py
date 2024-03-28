from dataclasses import dataclass


@dataclass
class Weight:
    value_g: float
    
    def g(self):
        return self.value_g
    def kg(self):
        return self.g() / 1000

@dataclass
class Count:
    value: int
    
    def c(self):
        return self.value


@dataclass
class Volume:
    value_ml: float
    
    def ml(self) -> float:
        return self.value_ml
    
    def l(self) -> float:
        return self.ml() / 1000

Amount = Weight | Count | Volume

@dataclass
class Timespan:
    time_s: float
    
    def s(self) -> float:
        return self.time_s
    
    def m(self) -> float:
        return self.s() / 60
    
    def h(self) -> float:
        return self.m() / 60