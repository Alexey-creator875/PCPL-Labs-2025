import random


def gen_random(numbersCount, begin, end):
    for _ in range(numbersCount):
        yield random.randint(begin, end)

def test_gen_random():
    print('Test1')
    resultTest1 = list(gen_random(5, 1, 3))
    print(*resultTest1)

if __name__ == "__main__":
    test_gen_random()
