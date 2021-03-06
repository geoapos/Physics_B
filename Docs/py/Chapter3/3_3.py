#!/usr/bin/python3
# filename 3_3.py
"""
Άσκηση 3.3

Μονοχρωματική ακτίνα φωτός ορισμένης συχνότητας έχει μήκος κύματος
500nm, όταν διαδίδεται στο νερό. Να υπολογιστεί, το μήκος κύματος αυτού του
φωτός, όταν διαδίδεται στο βενζόλιο. Οι δείκτες διάθλασης του νερού και του
βενζολίου είναι αντίστοιχα 1,333 και 1,501.
"""

# Δεδομένα
λν = 500 * 10**(-9)      # Μήκος κύματος στο νερό σε m
nν = 1.333               # Δείκτης διάθλασης νερού
nβ = 1.501               # Δείκτης διάθλασης βενζολίου
Co = 3 * 10**8           # Ταχύτητα σε m/sec


print()
print('Ο δείκτης  διάθλασης  στο  νερό  είναι:\tnν = λο / λν \t(1) ,όπου λο το μήκος κύματος στο κενό.'
      'ο δείκτης διάθλασης στο βενζόλιο είναι:\tnβ = λο / λβ \t(2)')
λβ = nν * (λν / nβ)
print(f'Από (1) και (2) => λβ = nν * (λν / nβ) => λβ ={λβ:.2e} m')
