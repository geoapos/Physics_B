#!/usr/bin/python3
# filename 2_29.py
"""
Άσκηση 2.29

Λαμπτήρας αντίστασης R1 = 40Ω συνδέε-
ται σε σειρά με αντίσταση R2 = 20Ω και στα
άκρα του συστήματος εφαρμόζεται τάση V =120V.

α) Πόση είναι η ισχύς του λαμπτήρα;
β) Αν παράλληλα με το λαμπτήρα συνδεθεί
αντίσταση R3 = 40Ω, πόση είναι η επί τοις
εκατό (%) μεταβολή της ισχύος του;
"""

# Δεδομένα
R1 = 40  # Αντίσταση λαμπτήρα σε Ω
R2 = 20  # Αντίσταση σε Ω
R3 = 40  # Αντίσταση σε Ω
V = 120  # Τάση σε V

print()
print('Α. Το ρεύμα που διαρέει το κυκλωμα είναι:')
Ι = V / (R1 + R2)
print('Ι=V/(R1+R2)=> I={:.2f} A'.format(Ι))

print('Η ισχύς του Λσμπτήρα είναι Pηλ=Ι²*R1 =>')
Pηλ = (Ι ** 2) * R1
print('Pηλ={:.2f} W'.format(Pηλ))

print()
print('Β. Αν παράλληλα με τον λαμπτήρα συνδεθεί αντίσταση R3, τότε:')
print('η ισοδύναμη αντίσταση γίνεται R13=R1*R3/(R1+R3) =>')
R13 = R1 * R3 / (R1 + R3)
print('R13={:.2f} Ω'.format(R13))
I = V / (R13 + R2)
print('και θα ισχύει V=I*R13+I*R2 => I={:.2f} A'.format(I))
print('Η τάση στα άκρα του λαμπτήρα θα είναι V13 =>')
I1 = I * R13 / R1
print('V13=I*R13 => I*R13=I1*R1 => I1=I*R13/R1 =>I1={:.2f} A'.format(I1))

print()
Pnew = (I1 ** 2) * R1
print('Η νέα ισχύς Pnew=(Ι1**2)*R1 =>Pnew={:.2f} W'.format(Pnew))
print('άρα μεταβολή: (Pnew-Pηλ)/Pηλ = {:.2f} %'.format(100 * (Pnew - Pηλ) / Pηλ))
