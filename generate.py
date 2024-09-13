from models.object import *
from models.paint import *
from models.color import *
from models.style import *

a = Object.get_random(object=Curio, color=Green, style=Modern)
print(a)

b = Paint.get_random()
print(b)