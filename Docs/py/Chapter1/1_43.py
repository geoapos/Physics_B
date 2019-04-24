#!/usr/bin/python3
# Filename: 1_43.py
'''Άσκηση 43:

Δίνονται δύο σημεία Κ και Λ ενός ομογενούς ηλεκτρικού πεδίου.
Η διαφορά δυναμικού VΚΛ = 1000V. Εάν η απόσταση των ΚΛ είναι 50cm,
να υπολογισθούν:
A. Η ένταση του ηλεκτρικού πεδίου.
B. Το δυναμικό σημείο «Λ», εάν το δυναμικό στο «Κ» είναι +200V.
'''

# Δεδομένα
VΚΛ = 1000  # Δυαναμικό μεταξύ των σημείων ΚΛ σε V
ΚΛ = 50 * 10 ** (-2)  # απόσταση οπλισμών σε m
VK = 200  # Το δυναμικό στο σημείο Κ σε V

print()
E = VΚΛ / ΚΛ
print('Α. Ισχύει ότι Ε=V/ΚΛ οπότε, Ε={:.2f} V/m'.format(E))
print()
print('B. VΚΛ=VΚ-VΛ => VΛ=VK-VΚΛ => VΛ={:.2f} V'.format(VK - VΚΛ))
