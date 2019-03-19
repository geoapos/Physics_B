x1=int(input('1ος αριθμός: '))
x2=int(input('2ος αριθμός: '))
x3=int(input('3ος αριθμός: '))
import statistics as et
	print('Μέσος όρος:', (x1+x2+x3)/3)
	print('Μέσος όρος:', et.mean([x1,x2,x3]))
