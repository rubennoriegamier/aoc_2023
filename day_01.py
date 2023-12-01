import fileinput
import re


def main():
    cal_vals: list[str] = list(map(str.rstrip, fileinput.input()))

    print(part_1(cal_vals))
    print(part_2(cal_vals))


def part_1(cal_vals: list[str]) -> int:
    return sum(int(next(char for char in cal_val if '1' <= char <= '9') +
                   next(char for char in cal_val[::-1] if '1' <= char <= '9'))
               for cal_val in cal_vals)


def part_2(cal_vals: list[str]) -> int:
    ltrs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    dgt_re = re.compile(fr'\d|{'|'.join(ltrs)}')
    rev_dgt_re = re.compile(fr'\d|{'|'.join(ltrs)[::-1]}')
    to_dgt = {ltr: str(dgt) for dgt, ltr in enumerate(ltrs, 1)}

    sum_ = 0

    for cal_val in cal_vals:
        first_dgt = dgt_re.search(cal_val).group()
        last_dgt = rev_dgt_re.search(cal_val[::-1]).group()[::-1]

        sum_ += int(to_dgt.get(first_dgt, first_dgt) +
                    to_dgt.get(last_dgt, last_dgt))

    return sum_


if __name__ == '__main__':
    main()
