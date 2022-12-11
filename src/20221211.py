import re
from math import prod


def monkey_in_the_middle():
    with open("data/11.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    for star_two in [False, True]:
        monkeys = []
        for line in lines:
            line = line.split()
            match line:
                case ["Monkey", _]:
                    continue
                case ["Starting", "items:", *items]:
                    starting_items = re.findall(r"\d+", "".join([*items]))
                    starting_items = [int(item) for item in starting_items]
                case ["Operation:", *operation]:
                    operation = [*operation]
                    operation = operation[-3:]
                case ["Test:", *test]:
                    divisor = int(re.findall(r"\d+", "".join([*test]))[0])
                case ["If", "true:", *action]:
                    true_reciever = int(re.findall(r"\d+", "".join([*action]))[0])
                case ["If", "false:", *action]:
                    false_reciever = int(re.findall(r"\d+", "".join([*action]))[0])
                    monkeys.append(
                        Monkey(
                            starting_items,
                            operation,
                            divisor,
                            true_reciever,
                            false_reciever,
                            star_two=star_two,
                        )
                    )

        global MODERATOR
        MODERATOR = prod([m.divisor for m in monkeys])

        n_rounds = 20 if not star_two else 10000
        for _ in range(n_rounds):
            for monkey in monkeys:
                monkey.inspect()
                loop_items = [*monkey.items]
                for item in loop_items:
                    monkey.throw_item(item)
                    if item % monkey.divisor == 0:
                        monkeys[monkey.true_reciever].add_item(item)
                    else:
                        monkeys[monkey.false_reciever].add_item(item)

        inspection_counts = sorted([monkey.inspection_count for monkey in monkeys])
        monkey_business = inspection_counts[-2] * inspection_counts[-1]
        print(f"Star 1/2: {monkey_business}")


class Monkey:
    def __init__(
        self,
        starting_items,
        operation,
        divisor,
        true_reciever,
        false_reciever,
        star_two=False,
    ):
        self.items = starting_items
        self.operation = operation
        self.divisor = divisor
        self.true_reciever = true_reciever
        self.false_reciever = false_reciever
        self.inspection_count = 0
        self.star_two = star_two

    def inspect(self):
        tmp_items = []
        for item in self.items:
            match self.operation:
                case ["old", "+", num] if num.isdigit():
                    tmp_item = item + int(num)
                case ["old", "*", num] if num.isdigit():
                    tmp_item = item * int(num)
                case ["old", "*", "old"]:
                    tmp_item = item * item
            if self.star_two:
                tmp_item = tmp_item % MODERATOR
            else:
                tmp_item = tmp_item // 3
            tmp_items.append(tmp_item)
            self.inspection_count += 1
        self.items = tmp_items

    def add_item(self, item):
        self.items.append(item)

    def throw_item(self, item):
        self.items.remove(item)


if __name__ == "__main__":
    monkey_in_the_middle()
