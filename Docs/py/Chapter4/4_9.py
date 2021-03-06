#!/usr/bin/python3
# filename 4_9.py
"""
Άσκηση 4.9

Σε μια ακτινογραφία απαιτούνται ακτίνες X μήκους κύματος λ=10^-10m. Η ένταση
του ρεύματος της δέσμης των ηλεκτρονίων είναι 40mA και ο χρόνος λήψης
της ακτινογραφίας είναι 0,1s. Θεωρούμε ότι όλη η κινητική ενέργεια κάθε
ηλεκτρονίου μετατρέπεται σε ενέργεια ενός φωτονίου:

α. Ποια τάση εφαρμόζεται στο σωλήνα παραγωγής ακτίνων X;
β. Πόση ισχύ και πόση ενέργεια μεταφέρει η ηλεκτρονική δέσμη;
γ. Ποια είναι η ταχύτητα των ηλεκτρονίων τη στιγμή που προσπίπτουν στην άνοδο;
δ. Πόσα ηλεκτρόνια σε κάθε δευτερόλεπτο προσπίπτουν στην άνοδο;
"""

import math
from const import h			# σταθερά του Planck
from const import Qe		# φορτίο ηλεκτρονίου
from const import c			# ταχύτητα του φωτός
from const import Me		# μάζα ηλεκτρονίου

# Δεδομένα
I = 40*10**(-3)		# Ένταση ρεύματος σε A
t = 0.1				# Χρόνος σε sec
λ = 10**(-10)		# Μήκος κύματος σε m
t2 = 1				# Χρόνος σε sec


print()
print(f'α) 	Η ενέργεια που αποκτούν τα ηλεκτρόνια υπό τάση V είναι:')
print( '	E = V * Qe\t(1)\tόπου Qe φορτίο ηλεκρονίου, επίσης \n'
	   '	E = h * f \t(2)\tόπου f η συχνότητα εκπομπης φωτονίων και\n'
	   '	f = c / λ \t(3), άρα:\n'
	   '	από (1), (2) και (3) => V = h * c / ( λ * Qe) => V = ', end='')
V = h * c / ( λ * abs(Qe))
print(f'{V:.2f} V')

print('\n\n')
print(f'β) 	Η ισχύς δίνεται από την σχέση P = V * I άρα: P = ', end='')
P = V * I
print(f'{P:.2f} W')
print(f'	Η ενεργεια Ε είναι E = P * t => 			 E = ', end='')
E = P * t
print(f'{E:.2f} J')

print('\n\n')
print( 'γ)  Η ενέργεια που αποκτούν τα ηλεκτρόνια μετατρέπεται σε κινητική, άρα \n'
	   '	E = Ek => Qe * V =1/2 * Me * u² => u = √ (2*Qe*V)/Me) => u = ', end='')
u = math.sqrt(2 * abs(Qe) * V / Me )
print(f'{u:.2e} m/sec')

print('\n\n')
print(f'δ)  Ο αριθμός των ηλεκτρονίων που προσπίπτουν στην άνοδο σε {t2} δευτερόλεπτα\n'
	   '	είναι: t * N= q / t2 => N = I * t2 / Qe * t  => N = ', end='')
N = (I * t2) / (t * abs(Qe))
print(f'{N} ηλεκτρόνια')