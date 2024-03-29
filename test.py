from pprint import pprint
from recipe import *
from unit import Weight, Count, Volume


def main():
    builder = RecipeBuilder()

    meat = builder.material(Material.from_name("牛肉細切れ"), Weight(120, "g"))
    carrot = builder.material(Material.from_name("にんじん"), Count(1))
    potato = builder.material(Material.from_name("じゃがいも"), Count(3))

    soy_sauce = builder.material(Material.from_name("しょうゆ"), Volume(1, "tbsp"))
    suger = builder.material(Material.from_name("砂糖"), Volume(2, "tsp"))

    cutted_carrot = builder.operation(
        Operation.from_name("ざく切りにする"), (carrot,), (Output("ざく切りにしたもの"),))
    catted_potato = builder.operation(
        Operation.from_name("ざく切りにする"), (potato,), (Output("ざく切りにしたもの"),))
    mixed_sauce = builder.operation(
        Operation.from_name("混ぜる"), (soy_sauce, suger,), (Output("混ぜたもの"),))

    nikujaga = builder.operation(
        Operation.from_name("煮る"),
        (meat, *cutted_carrot, *catted_potato, *mixed_sauce),
        (Output("肉じゃが", Timespan(12, "h")), Output("煮汁")))

    pprint(nikujaga)


if __name__ == "__main__":
    main()
