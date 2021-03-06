#!/usr/bin/python3
# filename 2_1.py
"""
Άσκηση 2.1

Ένας πυκνωτής χωρητικότητας C = 20μF συνδέεται με πηγή τάσης V = 24V.
Αποσυνδέουμε την πηγή και συνδέουμε τους οπλισμούς με σύρμα,
οπότε ο πυκνωτής εκφορτίζεται σε χρόνο Δt = 0,02s.
Να βρείτε τον αριθμό των ηλεκτρονίων, που περνάνε από μια διατομή
του αγωγού και τη μέση ένταση του ηλεκτρικού ρεύματος.
Δίνεται: qe= -1,6·10-19 C.
"""

# Δεδομένα
C = 20 * 10 ** (-6)  # χωρητικότητα πυκνωτή σε C
V = 24  # Τάση σε V
Δt = 0.02  # Χρόνος εκφόρτισης σε sec
qe = -1.6 * 10 ** (-19)  # Φορτίο ηλεκτρονίου σε C

print()
Q = C * V
print('Η χωρητικότητα  C είναι C=Q/V => Q=C*V => Q={:.2e}'.format(Q))
print()
print('Ισχύει ότι Q=n*qe, όπου n ο αριθμός των ηλεκτρονίων, άρα:')
n = Q / abs(qe)
print('n=Q/qe => n={:.2e} ηλεκτρόνια'.format(n))
I = Q / Δt
print('Από την σχέση I=Q/Δt => I={:.3f} A'.format(I))
