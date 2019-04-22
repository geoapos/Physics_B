#!/usr/bin/python3
# filename 2_27.py
"""
Άσκηση 2.27

Ένας θερμοσίφωνας έχει όγκο 20L  και είναι
γεμάτος με νερό θερμοκρασίας 10°C. Η αντίσταση
του θερμοσίφωνα είναι 10Ω και αυτός
συνδέεται με δίκτυο τάσης 220V. Αν το
20% της παραγόμενης θερμότητας εκλύεται
στο περιβάλλον, vα βρείτε σε πόσο χρόνο
η θερμοκρασία του νερού θα ανέβει στους
80°C και πόσο θα στοιχίσει αυτό. Δίνονται:
Πυκνότητα νερού: d νερ = 1g/cm3 , Ειδική θερ-
μότητα νερού: c νερ = 1cal/g·grad, Κόστος=0,1€/KWh.
"""

# Δεδομένα
Vl = 20 * 10 ** (-3)  # Όγκος σε m3
θ1 = 10  # Θερμοκρασία σε οC
θ2 = 80  # Θερμοκρασία σε οC
R = 10  # Αντίσταση σε Ω
n = 0.8  # Ποσοστό 80%
d = 1 * 10 ** (-3) / (1 * 10 ** (-6))  # Πυκνότητα σε Kg/m3
Cp = 4.18 / (1 * 10 ** (-3))  # Ειδική θερμότητα σε J/Kg·grad
K = 0.1  # Κόστος σε €/KWh
V = 220  # Τάση σε V

print()
print('Η αποροφούμενη ηλεκτρική ενέργεια είναι: E=V²*t/R   (1)')
print('Το 80% αυτής αποδίδεται στο νερό, άρα Q=0.8*E (2)')
ΔΤ = θ2 - θ1
print('Ισχύει όμως Q=m*Cp*ΔΤ  (3) όπου ΔΤ=θ2-θ1')

print('από την (2),(3) έχουμε: 0.8*E=(d*Vl)*Cp*ΔΤ =>')
E = (d * Vl) * Cp * ΔΤ / 0.8  # Ηλεκτρική ενέργεια
print('Ε={:.2f} J'.format(E))

print()
print('από την σχέση (1) => Ε=V²*t/R =>t=(E*R)/V² =>')
t = (E * R) / V ** 2
print('t={:.2f} sec ή t={:.2f} h'.format(t, t / 3600))

print()
print('Όπως είδαμε στην (1) η αποροφούμενη ενέργεια είναι:')
Eap = (E * 10 ** -3) / 3600
print('Ε={:.2f} KWh'.format(Eap))
print()
print('άρα το κόστος είναι: {:.2f}*{:.2f}={:.2f} ΕΥΡΩ'.format(Eap, K, Eap * K))
