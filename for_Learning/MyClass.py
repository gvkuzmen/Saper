'''
Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет,
которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке,
предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то
количество монет, не превышая ее вместимость.



'''


class MoneyBox():
    def __init__(self, capacity):
        self.capacity = capacity
        self.ammount = 0

    def can_add(self, v):
        if (self.ammount + v) <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.ammount += v
        else:
            return print(self.capacity - self.ammount)


box1 = MoneyBox(10)
box1.add(5)
box1.add(9)
box1.add(3)

'''
Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки 
чисел из этой последовательности, затем сумму второй пятерки, и т. д.

Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части. 
Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.

Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок 
последовательных элементов по мере их накопления.

Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно 
необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма.

'''


class Buffer:
    def __init__(self):
        self.total_lst = []

    def add(self, *a):
        self.summa = 0
        lst = list(a)
        self.total_lst += lst
        while len(self.total_lst) >= 5:
            for i in range(5):
                self.summa += self.total_lst[i]
            self.total_lst = self.total_lst[5:]
            print(self.summa)
            self.summa = 0
        # return print(self.total_lst)

    def get_current_part(self):
        return self.total_lst


buf = Buffer()
buf.add(1,2,3)
buf.get_current_part()
buf.add(4,5,6)
buf.get_current_part()
buf.add(7,8,9,10)
buf.get_current_part()
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buf.get_current_part()


#Второй вариант решения
#Второй вариант решения
#Второй вариант решения
#Второй вариант решения