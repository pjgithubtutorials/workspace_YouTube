
print("Hello world!, this is Pedram")

def add(x,y):
    return x+y

print(add(10,15))


x = 1



even_number = [x for x in range(11) if x%2==0]
print(even_number)




import random
import matplotlib.pyplot as plt

plt.plot([random.randint(0,100) for _ in range(100) ])
plt.show()


