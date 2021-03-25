# 1.3 пространство имен

'''
Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку
создания пространств имен и добавление в них переменных.
 '''

namespaces = {'global': {'parent': 'None', 'objects': []}}


def create(namespace, obj):
    namespaces[namespace] = {'parent': obj, 'objects': []}  # example : create foo global


def add(namespace, obj):
    namespaces[namespace]['objects'].append(obj)


def get(namespace, obj):
    if obj in namespaces[namespace]['objects']:
        return print(namespace)
    else:
        try:
            return get(namespaces[namespace]['parent'], obj)
        except KeyError:
            print('None')


n = int(input())

for i in range(n):
    cmd, namespace, obj = input().split()
    if cmd == 'add':
        add(namespace, obj)
    if cmd == 'create':
        create(namespace, obj)
    if cmd == 'get':
        get(namespace, obj)

print(namespaces)
