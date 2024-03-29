from dataclasses import dataclass, asdict
from typing import Any, Literal, Sequence
from unit import Amount, Timespan


@dataclass
class Attribute:
    _id: int
    name: str
    kind: Literal["material", "operation"]

    def __eq__(self, __value: "Attribute") -> bool:
        return self.kind == __value.kind and self._id == __value._id


@dataclass
class Material(Attribute):
    pass

    @classmethod
    def from_name(cls, name: str) -> "Material":
        # TODO: hard code
        name2id = {
            "にんじん": 0,
            "じゃがいも": 1,
            "牛肉細切れ": 2,
            "しょうゆ": 3,
            "砂糖": 4,
        }
        return Material(name2id[name], name, "material")


@dataclass
class Operation(Attribute):
    pass

    @classmethod
    def from_name(cls, name: str) -> "Operation":
        # TODO: hard code
        name2id = {
            "蒸す": 0,
            "焼く": 1,
            "炒める": 2,
            "茹でる": 3,
            "混ぜる": 4,
            "ざく切りにする": 5,
            "混ぜる": 6,
            "煮る": 7,
        }
        return Operation(name2id[name], name, 'operation')


# Constant function
MaterialMap = tuple[Material, Amount]
OperationMap = tuple[Operation, Any]


@dataclass
class Recipe:
    mapper: MaterialMap | OperationMap
    inputs: tuple["Edible"]
    output_details: tuple["Output"]

    @property
    def outputs(self) -> tuple["Edible"]:
        return tuple(
            Edible(recipe=self, **asdict(details)) for details in self.output_details)

    def materials(self) -> tuple[MaterialMap]:
        res = []

        def f(recipe: Recipe):
            if recipe.mapper.kind == "material":
                res.append(recipe.mapper)

            for input in recipe.inputs:
                f(input.recipe)

        f(self)
        return tuple(res)


@dataclass
class Output:
    name: str
    expiration_time: Timespan | None = None


@dataclass
class Edible:
    # NOTE: Edible must has Output's fields, hard coded.
    name: str
    expiration_time: Timespan | None
    recipe: Recipe


class RecipeBuilder:
    def __init__(self) -> None:
        pass

    def material(self, material: Material, amount: Amount) -> Edible:
        return Recipe((material, amount), [], (Output(material.name), )).outputs[0]

    def operation(self, op: Operation, inputs: Sequence[Edible], outputs: Sequence[Output], option=None) -> tuple[Edible]:
        return Recipe((op, option), tuple(inputs), tuple(outputs)).outputs
