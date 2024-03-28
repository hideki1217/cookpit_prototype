from dataclasses import dataclass
from collections import defaultdict


@dataclass(frozen=True)
class Node:
    global_name: str
    elements: tuple["Edible"]
    output_names: tuple[str]

    @property
    def outputs(self) -> tuple["Edible"]:
        return tuple(Edible(name, self) for name in self.output_names)

    def is_material(self) -> bool:
        return (len(self.elements) == 0) and (len(self.output_names) == 1)

    def is_operation(self) -> bool:
        return not self.is_material()


@dataclass(frozen=True)
class Edible:
    local_name: str
    recipe: Node


class RecipeBuilder:
    def __init__(self) -> None:
        pass

    def material(self, name: str) -> Edible:
        return Node(name, tuple(), (name, )).outputs[0]

    def operation(self, name: str, elements: tuple[Edible], outputs: tuple[str]) -> tuple[Edible]:
        return Node(name, elements, outputs).outputs


class Descripter:
    def __init__(self) -> None:
        pass

    def descript_material(self, edible: Edible) -> str:
        def find_all_material(node: Node) -> tuple[Node]:
            if node.is_material():
                return (node, )

            result = tuple()
            for elem in node.elements:
                result += find_all_material(elem.recipe)

            return result

        materials = find_all_material(edible.recipe)
        mtrls_description = "## 材料\n" + \
            "\n".join([f"- {elem.global_name}"for elem in materials])
        return mtrls_description

    def descript_operation(self, edible: Edible) -> str:
        def topological_sort(node: Node) -> tuple[Node]:
            # assume: nodeが唯一の出力のないNode

            def refcount_op_dict(node: Node) -> dict[Node, int]:
                res = defaultdict(int)

                def f(node: Node):
                    if node.is_material():
                        return

                    res[node] += 1
                    for elem in node.elements:
                        f(elem.recipe)

                f(node)
                return res

            refcount = refcount_op_dict(node)

            tpl_sorted = []
            frontier = [node]
            while len(frontier) != 0:
                front = frontier.pop()
                tpl_sorted.append(front)

                for elem in front.elements:
                    if elem.recipe in refcount:
                        refcount[elem.recipe] -= 1

                        if refcount[elem.recipe] == 0:
                            frontier.append(elem.recipe)

            return list(reversed(tpl_sorted))

        index2op = topological_sort(edible.recipe)
        op2index = {op: index + 1 for index, op in enumerate(index2op)}

        def descript(op: Node):
            elems = [elem.local_name if elem.recipe.is_material() else str(
                op2index[elem.recipe]) for elem in op.elements]
            return f"{'と'.join(elems)}を{op.global_name}"

        op_description = "## 手順\n" + \
            "\n".join([f"{index+1}. {descript(op)}" for index,
                      op in enumerate(index2op)])

        return op_description
