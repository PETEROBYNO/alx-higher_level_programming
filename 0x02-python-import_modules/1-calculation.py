#!/usr/bin/python3

if __name__ == "__main__":

    a = 10
    b = 5

    from calculator_1 import add, sub, mul, div

    sum_ = add(a, b)
    minu_ = sub(a, b)
    time_ = mul(a, b)
    diff_ = div(a, b)

    print("{:d} + {:d} = {:d}" .format(a, b, sum_))
    print("{:d} - {:d} = {:d}" .format(a, b, minu_))
    print("{:d} * {:d} = {:d}" .format(a, b, time_))
    print("{:d} / {:d} = {:d}" .format(a, b, diff_))
