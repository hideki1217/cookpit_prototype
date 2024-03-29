from dataclasses import dataclass, asdict
from typing import Literal, Sequence
from unit import Amount, Timespan


@dataclass
class Attribute:
    _id: int
    name: str
    kind: Literal["material", "operation"]


@dataclass
class Material(Attribute):
    amount: Amount


@dataclass
class Operation(Attribute):
    pass


@dataclass
class Recipe:
    detail: Material | Operation
    inputs: tuple["Edible"]
    output_details: tuple["Output"]

    @property
    def outputs(self) -> tuple["Edible"]:
        return tuple(
            Edible(recipe=self, **asdict(details)) for details in self.output_details)

    def materials(self) -> tuple[Material]:
        res = []

        def f(recipe: Recipe):
            if recipe.detail.kind == "material":
                res.append(recipe.detail)

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

    def material(self, name: str, amount: Amount) -> Edible:
        # TODO: hard code
        name2id = {
            "にんじん": 0,
            "じゃがいも": 1,
            "牛肉細切れ": 2,
            "しょうゆ": 3,
            "砂糖": 4,
        }
        material = Material(name2id[name], name, "material", amount)
        return Recipe(material, [], (Output(name), )).outputs[0]

    def operation(self, name: str, inputs: Sequence[Edible], outputs: Sequence[Output]) -> tuple[Edible]:
        # TODO: hard code
        name2id = {
            "蒸す": 0,
            "焼く": 1,
            "炒める": 2,
            "茹でる": 3,
            "混ぜる": 4,
            "ざく切りにする": 5,
            "混ぜ合わせる": 6,
            "煮る": 7,
        }
        op = Operation(name2id[name], name, 'operation')
        return Recipe(op, tuple(inputs), tuple(outputs)).outputs
