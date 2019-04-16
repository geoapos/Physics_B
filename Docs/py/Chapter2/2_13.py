#!/usr/bin/python3
#filename 2_13.py
'''
Άσκηση 2.13

Στο παρακάτω κύκλωμα δίνονται:
R1 = 3Ω, R2 = 6Ω, R3 = 8Ω, R4 = 7Ω, R5 = 3Ω, V = 60V.
Να βρείτε:
α) την ολική αντίσταση του συστήματος,
β) την τάση στα άκρα κάθε αντίστασης,
γ) την ένταση του ρεύματος, που διαρρέει
κάθε αντίσταση.
'''

#Δεδομένα
R1=3                            #Αντίσταση σε Ω
R2=6                            #Αντίσταση σε Ω
R3=8                            #Αντίσταση σε Ω
R4=7                            #Αντίσταση σε Ω
R5=3                            #Αντίσταση σε Ω
V=60                            #Τάση σε V


print()

RΑΓ=(R1*R2)/(R1+R2)
print('H Αντίσταση RAΓ=(R1*R2)/(R1+R2) => RΑΓ={:.2f} Ω'.format(RΑΓ))

RAΓΒ=RΑΓ+R3
print('H Αντίσταση RAΓΒ=RAΓ+R3 => RAΓΒ={:.2f} Ω'.format(RAΓΒ))

RAΔΒ=R4+R5
print('H Αντίσταση RAΔΒ=R4+R5 => RAΔΒ={:.2f} Ω'.format(RAΔΒ))

RAΒ=(RAΓΒ*RAΔΒ)/(RAΓΒ+RAΔΒ)
print('H Αντίσταση RAΒ=(RAΓΒ*RAΔΒ)/(RAΓΒ+RAΔΒ) => RAΒ={:.2f} Ω'.format(RAΔΒ))
print()

V4=V*(R4/RAΔΒ)
print('V=IΑΔΒ*RΑΔΒ επίσης V4=VΑΔ=IΑΔΒ*R4 =>V4=V*(R4/RΑΔΒ) => V4={:.2f} V'.format(V4))

V5=V*(R5/RAΔΒ)
print('V=IΑΔΒ*RΑΔΒ επίσης V5=VΔΒ=IΑΔΒ*R5 =>V5=V*(R5/RΑΔΒ) => V5={:.2f} V'.format(V5))

V3=V*(R3/RAΓΒ)
print('V=IΑΓΒ*RΑΓΒ επίσης V3=VΓΒ=IΑΓΒ*R3 =>V3=V*(R3/RΑΓΒ) => V3={:.2f} V'.format(V3))

VΑΓ=V1=V2=(V-V3)
print('VΑΓ=V1=V2=(V-V3) => V1=V2={:.2f} V'.format(V1))



print()
I1=V1/R1
I2=V2/R2
I3=V3/R3
I4=V4/R4
I5=V5/R5
print('I1=V1/R1 => I1={:.2f}'.format(I1))
print('I2=V2/R2 => I2={:.2f}'.format(I2))
print('I3=V3/R3 => I3={:.2f}'.format(I3))
print('I4=V4/R4 => I4={:.2f}'.format(I4))
print('I5=V5/R5 => I5={:.2f}'.format(I5))
