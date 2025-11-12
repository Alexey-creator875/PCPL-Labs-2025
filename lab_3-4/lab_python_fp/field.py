def field(items, *args):
    assert len(args) > 0
    
    if len(args) == 1:
        for item in items:
            key = args[0]
            value = item.get(key)
            if value is not None:
                yield value
    else:
        for item in items:
            dictResult = {}

            for key in args:
                value = item.get(key)
                if value is not None:
                    dictResult[key] = value
            
            if dictResult:
                yield dictResult


goods = [
   {'title': 'Ковер', 'price': 2000, 'color': 'green'},
   {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

def test_field():
    print("Test1")
    resultTest1 = list(field(goods, 'title'))
    print(resultTest1)

    print('\nTest2')
    resultTest2 = list(field(goods, 'title', 'price'))
    print(resultTest2)

if __name__ == "__main__":
    test_field()
