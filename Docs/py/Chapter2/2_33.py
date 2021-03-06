#!/usr/bin/python3
# filename 2_33.py
"""
Άσκηση 2.33

Μια ηλεκτρική θερμάστρα αναγράφει τα στοιχεία «1000W-100V».
Να βρείτε την αντίσταση που πρέπει να συνδέσουμε σε σειρά
με τη θερμάστρα για να λειτουργήσει σε δίκτυο τάσης 220V.
"""

# Δεδομένα
P = 1000  # Ισχύς σε W
Vk = 100  # Τάση σε V
V = 220  # Τάση σε V

print()
R1 = (Vk ** 2) / P
print('Η ένταση που διαρρέει την θερμάστρα στην κανονική της λειτουργίας είναι:')
I = P / Vk
print('I=P/Vk => I={:.2f} A'.format(I))

print('Για να λειτουργεί η θερμάστρα κανονικά θα πρέπει και μετά την προσθήκη, ')
print('αντίστασης σε σειρά να διαρρέεται από το ίδιο ρεύμα, άρα ισχύει:')

print('I*R1+I*R2=V =>(R1+R2)*I=V => (R1+R2)=V/I => R2=(V/I) - R1 =>')
R2 = V / I - R1
print('R2={:.2f} Ω'.format(R2))
