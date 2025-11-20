d={
    'name':'Nikhil Patel',
    'course':'B.Tech',
    'fees':20000
}
# for i in d.keys():
#     print(i)
#
# for v in d.values():
#     print(v)

# for k,v in d.items():
#     print(k,":",v)

# print(d['course'])
# print(d.get('course'))

# print(d)
# del d['name']
# d.pop('course')
# print(d)

d2=dict(name='Nikhil', age='22', course='python')
print(d2)
d2.update({'name':'Nikhil Patel'})
d2['age']=24
print(d2)
d2.clear()
print(d2)