#cara mengimport module ke-1

import Matematika
Matematika.kali(2,3)
Matematika.bagi(4,2)
print(50*'=')

#cara mengimport module ke-2
import Matematika as math
math.kali(1,2)
math.bagi(6,3)
print(50*'=')

#cara mengimport module ke-3
from Matematika import kali, bagi
kali(2,2)
bagi(2,2)
print(50*'=')

#cara mengimport module ke-4
from Matematika import *
kali(2,3)
bagi(4,2)
print(50*'=')

#cara mengimport module ke-5
from Matematika import kali as X
X(2,3)
from Matematika import bagi as B
B(4,2)
print(50*'=')
