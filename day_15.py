from functools import reduce


def main():
    steps = input().split(',')

    print(part_1(steps))
    print(part_2(steps))


def hash_algo(s: str) -> int:
    return reduce(lambda a, b: (a + b) * 17 % 256, map(ord, s), 0)


def part_1(steps: list[str]) -> int:
    return sum(map(hash_algo, steps))


def part_2(steps: list[str]) -> int:
    boxes = [[] for _ in range(256)]

    for step in steps:
        if step[-1] == '-':
            label = step[:-1]
            label_hash = hash_algo(label)
            box = boxes[label_hash]

            for i in range(len(box)):
                if box[i][0] == label:
                    del box[i]
                    break
        else:
            label = step[:-2]
            label_hash = hash_algo(label)
            box = boxes[label_hash]
            focal_len = int(step[-1])

            for i in range(len(box)):
                if box[i][0] == label:
                    box[i] = label, focal_len
                    break
            else:
                box.append((label, focal_len))

    return sum(box_number * lens_number * focal_len
               for box_number, box in enumerate(boxes, 1)
               for lens_number, (_, focal_len) in enumerate(box, 1))


if __name__ == '__main__':
    main()
