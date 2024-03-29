
from recipe import Recipe, RecipeStep
from unit import Timespan
from user import User
from dataclasses import dataclass


@dataclass
class PlanSummary:
    total_time: Timespan
    # TODO: need more information


class Planner:
    def __init__(self, user: User) -> None:
        self.user = user

    def planning(self, recipe: Recipe) -> tuple[list[RecipeStep], PlanSummary] | None:
        # assume that user cook alone
        # when this function return None, user cannot cook according to the recipe.
        # TODO: must
        pass
