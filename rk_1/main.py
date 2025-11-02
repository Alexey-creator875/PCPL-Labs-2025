class Part():
    def __init__(self, id, name, price, supplierId):
        self.id = id
        self.name = name
        self.price = price
        self.supplierId = supplierId

class Supplier():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PartSupplierM2MRelationship():
    def __init__(self, partId, supplierId):
        self.partId = partId
        self.supplierId = supplierId

def main():
    parts = [
        Part(1, "Болт", 25.50, 1),
        Part(2, "Гайка", 12.00, 2),
        Part(3, "Шайба", 5.30, 1),
        Part(4, "Винт", 18.90, 3),
        Part(5, "Подшипник", 320.00, 4),
        Part(6, "Шпонка", 42.75, 2),
        Part(7, "Заклёпка", 7.80, 5),
        Part(8, "Штифт", 29.40, 3),
        Part(9, "Гвоздь", 3.15, 5),
        Part(10, "Резьба", 55.20, 4)
    ]

    suppliers = [
        Supplier(1, "ООО \"Вектор\""),
        Supplier(2, "АО \"МеталлСервис\""),
        Supplier(3, "ЗАО \"ТехноПром\""),
        Supplier(4, "ИП \"Стальной мир\""),
        Supplier(5, "ООО \"Квант\"")
    ]

    partSupplierM2MRelationships = [
        PartSupplierM2MRelationship(1, 1),
        PartSupplierM2MRelationship(1, 2),
        PartSupplierM2MRelationship(2, 2),
        PartSupplierM2MRelationship(2, 3),
        PartSupplierM2MRelationship(3, 1),
        PartSupplierM2MRelationship(4, 3),
        PartSupplierM2MRelationship(4, 5),
        PartSupplierM2MRelationship(5, 4),
        PartSupplierM2MRelationship(6, 2),
        PartSupplierM2MRelationship(7, 5)
    ]

    one_to_many = [
        (part.name, part.price, supplier.name)
        for supplier in suppliers
        for part in parts
        if part.supplierId == supplier.id
    ]

    many_to_many_temp = [
        (supplier.name, partSuplier.supplierId, partSuplier.partId)
        for supplier in suppliers
        for partSuplier in partSupplierM2MRelationships
        if partSuplier.supplierId == supplier.id
    ]

    many_to_many = [
        (part.name, part.price, supplierName)
        for supplierName, supplierId, partId in many_to_many_temp
        for part in parts
        if part.id == partId
    ]

    '''
    1. «Отдел» и «Сотрудник» связаны соотношением один-ко-многим. Выведите
        список всех связанных сотрудников и отделов, отсортированный по отделам,
        сортировка по сотрудникам произвольная.
    2. «Отдел» и «Сотрудник» связаны соотношением один-ко-многим. Выведите
        список отделов с суммарной зарплатой сотрудников в каждом отделе,
        отсортированный по суммарной зарплате.
    3. «Отдел» и «Сотрудник» связаны соотношением многие-ко-многим. Выведите
        список всех отделов, у которых в названии присутствует слово «отдел», и список
        работающих в них сотрудников.
    '''


    print("Задание А1")
    resA1 = sorted(one_to_many, key=lambda part : part[2])
    print(resA1)

    print('\nЗадание А2')
    resA2Unsorted = []
    
    for supplier in suppliers:
        
        supplierParts = list(filter(lambda i: i[2]==supplier.name, one_to_many))
        
        if len(supplierParts) > 0:
            
            partPrices = [price for _,price,_ in supplierParts]
            
            partPricesSum = sum(partPrices)
            resA2Unsorted.append((supplier.name, partPricesSum))
    
    resA2 = sorted(resA2Unsorted, key=lambda i : i[1], reverse=True)
    print(resA2)

if __name__ == "__main__":
    main()
