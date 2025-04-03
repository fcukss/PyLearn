#===========================namedtuple==============================
# from collections import namedtuple

# #define (определили) именнованый кортеж
# Point = namedtuple("Point", ['x', 'y'])
#
# # Create new point
# p = Point(10, 20)
# print(p.x)      # 10
# print(p.y)      # 20
# print(p)        # Point(x=10, y=20)
# p.x = 15        # AttributeError: can't set attribute (immutable type)

#============================deque===============================
# from collections import deque
# #create deque
# d = deque([1,2,3])
# print(d)          #deque([1, 2, 3])
#
# #Append to both ends
# d.append(4)
# print(d)          #deque([1, 2, 3, 4])
# d.appendleft(7)
# print(d)          #deque([7, 1, 2, 3, 4])
#
# #Pop from both ends
# d.pop()
# num = d.popleft()
# print(d)          #deque([1, 2, 3])
# print(num)        # 7

#============================COUNTER===============================
# from collections import Counter
#
# word_lst = ['apple', 'banana', 'apple', 'kiwi']
# counter = Counter(word_lst)
# print(counter)  # Counter({'apple': 2, 'banana': 1, 'kiwi': 1})
# print(counter.most_common(2))   #[('apple', 2), ('banana', 1)]
# print(counter['apple'])   #2

# #============================DefaultDictionary===============================
# from collections import defaultdict
#
# dd = defaultdict(list)
#
# dd['names'].append('Tom')
# dd['names'].append('Anna')
# dd['last_names'].append('Soyer')
#
# print(dd)    #defaultdict(<class 'list'>, {'names': ['Tom', 'Anna'], 'last_names': ['Soyer']})
# print(dd['names'])   #['Tom', 'Anna']
# print(dd['ages'])   #[]   Create an empty list by default

# #============================OrderDictionary===============================
# from collections import OrderedDict
#
# od = OrderedDict()
# od['apple'] = 3
# od['banana'] = 5
# od['orange'] = 3
# print(od)  #OrderedDict({'apple': 3, 'banana': 5, 'orange': 3})
#
# od.move_to_end('banana')
# print(od)  #OrderedDict({'apple': 3, 'orange': 3, 'banana': 5})
