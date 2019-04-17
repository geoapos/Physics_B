#!/usr/bin/python3
#filename 2_20.py
'''
Άσκηση 2.20

Θεωρούμε ένα ισοπαχύ και ομογενή κυκλικό αγωγό κέντρου Κ
και τέσσερα σημεία του Α, Β, Γ, Δ τέτοια ώστε, ΑΒ = ΒΓ = ΓΔ = ΔΑ = 90°.
Τα σημεία Α και Β συνδέονται με τάση VAB = 60V.

α) Να βρείτε τη διαφορά δυναμικού VΑΓ .
β) Αν γειώσουμε το Δ, να βρείτε το δυναμικό του σημείου Γ.
'''


#Δεδομένα
R1=10                   #Αντίσταση σε Ω
R2=20                   #Αντίσταση σε Ω
V=10                    #Τάση σε V
R3=20                   #Αντίσταση σε Ω

print()
print('Στην περίπτωση αυτή η αντίσταση R2 είναι βραχυκυκλωμένη,')
print('άρα δεν διαρέεται από ρεύμα, που σημαίνει ότι:')
I1=V/R1
print('I1=V/R1 => I1={:.2f} A'.format(I1))
print()

print('Στην περίπτωση που συνδέσουμε αντίσταση R3, τότε αυτή είναι παράλληλη με την R2')
R=R2*R3/(R2+R3)
print('Άρα η ισοδύναμη αντίσταση του κλάδου είναι R=R2*R3/(R2+R3) => R={:.2f} Ω'.format(R))
I1=V/(R1+R)
print('Τότε ισχύει V=I1*R1+I1*R => I1=V/(R1+R) => I1={:.2f} Ω'.format(I1))
I3=(V-I1*R1)/R3
print('Επίσης V=I1*R1+I3*R3 => I3=(V-I1*R1)/R3 => I3={:.2f} Ω'.format(I3))
I2=I1-I3
print('Σύμφωνα με τον νόμο του Kirchof I1=I2+I3=> I2={:.2f} Ω'.format(I2))
