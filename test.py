from recipe import *


def main():
    builder = RecipeBuilder()

    x = builder.material("牛肉細切れ")
    y = builder.material("にんじん")
    z = builder.material("じゃがいも")

    a = builder.material("しょうゆ")
    b = builder.material("砂糖")

    y_ = builder.operation("ざく切り", (y,), (f"ざく切りにしたもの",))
    z_ = builder.operation("ざく切り", (z,), (f"ざく切りにしたもの",))
    ab_ = builder.operation("混ぜ合わせる", (a, b,), (f"混ぜ合わせたもの",))

    recipe = builder.operation("煮る", (x, *y_, *z_, *ab_), ("肉じゃが", "煮汁"))

    descripter = Descripter()
    print(f"# {recipe[0].local_name} の作り方 \n")
    print(descripter.descript_material(recipe[0]) + "\n")
    print(descripter.descript_operation(recipe[0]) + "\n")


if __name__ == "__main__":
    main()
