# # 2․ Գրել ծրագիր, որը․
# #    - հետևյալ dict_1-ից կստանա նոր dict_2 այնպես, որ dict_2-ի key-երը լինեն dict_1-ի value-ները,
# #      իսկ value-ները՝ dict_1-ի value-ների երկարությունները,
# #    օրինակ՝ dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'},
# #    պետք է ստացվի՝ dict_2 = {'red': 3, 'green': 5, 'black': 5, 'white': 5}:
#
# dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# dict_2={}
# for i,v in dict_1.items():
#     dict_2[v]= len(v)
# print(dict_2)
# # 3. Գրել ֆունկցիա, որը․
# #    - կֆիլտրի տրված dictionary-ի value-ները, թողնելով միայն կենտ թվերը,
# #    - կվերադարձնի ստացված dictionary-ն,
# #    օրինակ՝ {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]},
# #    պետք է ստացվի՝ {'a': [1, 3, 7], 'b': [], 'c': [9, 9, 5]}:
# d1={'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
# d2={}
# for i, v in d1.items():
#     d2[i] = list(filter(lambda x : x%2!=0 , v))
# print(d2)
# import time
# list1=[]
