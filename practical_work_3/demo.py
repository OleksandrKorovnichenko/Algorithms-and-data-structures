from practical_work_3.structureexamples import StructureExample, ArrayParts, ArrayWithoutListMethods

list1 = StructureExample([1, 2, 3])
print(list1)
list1.append(6)
print(list1)

list2 = ArrayParts([1, 2, 3])
print(list2)
list2.append(6)
print(list2)

list3 = ArrayWithoutListMethods(1, 2, 3)
print(list3)
list1.append(6)
print(list1)
