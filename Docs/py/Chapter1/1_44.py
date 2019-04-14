#!/usr/bin/python3
#Filename: 1_44.py
'''Άσκηση 44:

Οι οπλισμοί Α και Β του πυκνωτή του σχήματος απέχουν απόστα-
ση 100cm και η διαφορά δυναμικού μεταξύ των δύο οπλισμών
είναι 2.000V. Σημειακό φορτίο +1μC τοποθετείται στη θέση «Κ»
που απέχει απόσταση 20cm από τον οπλισμό (Α). Να βρείτε το
έργο της δύναμης του πεδίου για τη μετακίνηση του φορτίου:
A. WK→Λ
B. WΜ→Κ
Γ. WK→Λ→Μ→Κ
'''

#Δεδομένα

l=1                    #απόσταση οπλισμών σε m
V=2000                 #Η διαφορά δυναμικού των οπλισμών σε V
q=1*10**(-6)           #φορτίο σε class
KA=20*10**(-2)         #απόσταση ΚΑ σε m
ΚΛ=60*10**(-2)         #απόσταση ΚΛ σε m
print()

print('Α. Το έργο της δύναμης του πεδίου δινεται από την σχέση W=ΔV*q')
print('όπου ΔV είναι η διαφορά δυναμικού μεταξύ Κ και Λ')
print('Ισχύει ότι Ε=ΔV/KΛ (1), επίσης')
print('Ε=V/l (2)')
ΔV=V*ΚΛ/l
print('Από (1) και (2) έχουμε: ΔV=V*KΛ/l => ΔV={:.2f}'.format(ΔV))
W1=q*ΔV
print('Επομένως το έργο της δύναμης από το Κ στο Λ είναι WK→Λ=q*ΔV => WK→Λ={:.2e} J'.format(W1))
