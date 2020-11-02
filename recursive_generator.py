import json


def branch(accum, root, tree):
    accum[tree["name"]] = root
    if tree.get("children"):
        for item in tree.get("children"):
            next_step = branch(accum, tree["name"], item)
            yield from next_step


if __name__ == "__main__":
    with open('input.json', 'r') as ij:
        data1 = json.loads(ij.read())
    result = dict()
    try:
        next(branch(result, "root", data1))
    except StopIteration:
        pass
    print(result)


