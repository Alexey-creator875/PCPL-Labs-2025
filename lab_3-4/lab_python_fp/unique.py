from gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.seen = set()

    def __next__(self):
        while True:
            item = next(self.items)

            if self.ignore_case and isinstance(item, str):
                key = item.lower()
            else:
                key = item

            if key not in self.seen:
                self.seen.add(key)
                return item

    def __iter__(self):
        return self
    
def test_unique():
    print('Test 1')
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    result1 = list(Unique(data1))
    print(f"Input:  {data1}")
    print(f"Output: {result1}")
    
    print('\nTest 2')
    data2 = list(gen_random(10, 1, 3))
    result2 = list(Unique(data2))
    print(f"Input:  {data2}")
    print(f"Output: {result2}")

    data34 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

    print('\nTest 3')
    result3 = list(Unique(data34))
    print(f"Input:  {data34}")
    print(f"Output: {result3}")
    
    print('\nTest 4')
    result4 = list(Unique(data34, ignore_case=True))
    print(f"Input:  {data34}")
    print(f"Output: {result4}")

if __name__ == "__main__":
    test_unique()