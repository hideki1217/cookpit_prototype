from abc import ABC
from typing import NewType
from dataclasses import dataclass

    
@dataclass(frozen=True)
class Node:
    global_name: str
    elements: tuple["Edible"]
    output_names: tuple[str]
    
    @property
    def outputs(self) -> tuple["Edible"]:
        return tuple(Edible(name, self) for name in self.output_names)
    
    
@dataclass(frozen=True)
class Edible:
    local_name: str
    recipe: Node
    
    @property
    def _id(self) -> str:
        return hash(self)
    

class RecipeBuilder:
    def __init__(self) -> None:
        pass
    
    def elem(self, name: str) -> Edible:
        return Node(name, tuple(), (name, )).outputs[0]
    
    def op(self, name: str, elements: tuple[Edible], outputs: tuple[str]) -> tuple[Edible]:
        return Node(name, elements, outputs).outputs