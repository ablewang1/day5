from sklearn import datasets
from matplotlib import pyplot as plt

# digits = datasets.load_digits()
# # print(digits.data[0,:])
# # print(digits.images[0,:,:])
# # plt.imshow(digits.images[0,:,:],cmap='gray')
#
# for image_index in range(10):
#     subplot_index = image_index + 1
#     plt.subplot(2,5,subplot_index)
#     plt.imshow(digits.images[image_index,:,:],cmap='gray')
# plt.show()

class Animal(object):
    def __init__(self,name):
        self.name = name
    def say(self):
        print("what is your name?%s" % self.name)
class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        # Animal.__init__(self,name)
        self.age = age
        self.name = name
    def say(self):
        print("My name is %s ,my age is %d" % (self.name,self.age))
    # def computer(self,other):
    #     other.say()
    def __add__(self,other):
        return self.age + other.age
    def __del__(self):
        if __name__ == '__main__':
            print("我还会回来的！")
        else:
            print("我回来了")
class Body():
    def __init__(self):
        self.name = "Body is hard!"
    def computer(self,other):
        print("Body is you %s" % other)

dog1 = Dog("小白狗",1)
dog1.say()
body = Body()
dog2 = Dog("大白",1)
body.computer(dog2.name)
print(dog1 + dog2)

class Matrix():
    def __init__(self,data):
        self.data = data

    def __add__(self, other):
        a_row = len(self.data)
        a_col = len(self.data[0])

        b_row = len(other.data)
        b_col = len(other.data)

        if a_row != b_row or a_col != b_col:
            return "形状不同"
        for row in range(a_row):
            for col in range(a_col):
                self.data[row][col] += other.data[row][col]
        return self
    def __str__(self):
        return str(self.data)

if __name__ == '__main__':
    a = Matrix([[1,2],[3,4]])
    b = Matrix([[4,3],[2,1]])
    print(a+b)