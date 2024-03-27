from recipe import *
import pprint

def main():
    builder = RecipeBuilder()
    
    x = builder.elem("牛肉細切れ")
    y = builder.elem("にんじん")
    z = builder.elem("じゃがいも")
    
    a = builder.elem("しょうゆ")
    b = builder.elem("砂糖")
    
    y_ = builder.op("ざく切り", (y,), (f"ざく切りにしたもの",))
    z_ = builder.op("ざく切り", (z,), (f"ざく切りにしたもの",))
    ab_ = builder.op("混ぜ合わせる", (a, b,), (f"混ぜ合わせたもの",))
    
    (result,) = builder.op("煮る", (x, *y_, *z_, *ab_), ("肉じゃが",))
    pprint.pprint(result)


if __name__ == "__main__":
    main()
    