# coding: utf-8


def init_set():
    print("===== init_set =====")
    s = set()
    print(s)
    s2 = set([])
    print(s2)
    s3 = set([1])
    print(s3)


def union_update_and_intersection():
    print("===== union_update_and_intersection =====")
    s = set([1, 2, 3])
    s2 = set([2, 3, 4])
    print(s.intersection(s2))
    print(s)
    print(s.union(s2))
    print(s)
    print(s.update(s2))
    print(s)


def add_remove():
    print("===== set_add_remove =====")
    s = set([1, 2, 3])
    s.add(4)
    s.remove(1)
    # s.remove(11)    # KeyError: 11
    if 11 in s:
        s.remove(11)
    print(s)
    print(s.pop())
    print(s)


def main():
    init_set()
    union_update_and_intersection()
    add_remove()


if __name__ == '__main__':
    main()
