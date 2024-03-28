from pprint import pprint
from recipe import *
from unit import Weight, Count, Volume

def main():
    builder = RecipeBuilder()

    x = builder.material("牛肉細切れ", Weight(120, "g"))
    y = builder.material("にんじん", Count(1))
    z = builder.material("じゃがいも", Count(3))

    a = builder.material("しょうゆ", Volume(1, "tbsp"))
    b = builder.material("砂糖", Volume(2, "tsp"))

    y_ = builder.operation("ざく切りにする", (y,), (f"ざく切りにしたもの",))
    z_ = builder.operation("ざく切りにする", (z,), (f"ざく切りにしたもの",))
    ab_ = builder.operation("混ぜ合わせる", (a, b,), (f"混ぜ合わせたもの",))

    recipe = builder.operation("煮る", (x, *y_, *z_, *ab_), ("肉じゃが", "煮汁"))
    pprint(recipe)


if __name__ == "__main__":
    main()
