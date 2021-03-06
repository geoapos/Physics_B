#!/usr/bin/python3
# filename 2_40.py
"""
Άσκηση 2.40

Σε ένα κύκλωμα συνδέονται κατά σειρά πηγή
ηλεκτρικού ρεύματος, διακόπτης, αμπερό-
μετρο και ωμική αντίσταση R. Στους πόλους
της πηγής συνδέεται βολτόμετρο. Όταν ο δι-
ακόπτης είναι ανοιχτός, η ένδειξη του βολ-
τομέτρου είναι 24V. Όταν ο διακόπτης είναι
κλειστός, η ένδειξη του βολτομέτρου είναι
20V και του αμπερομέτρου 2Α. Να βρεθεί η
ΗΕΔ και η εσωτερική αντίσταση της πηγής.
Τα όργανα να θεωρηθούν ιδανικά.

"""

# Δεδομένα
V1 = 24  # Τάση σε V
V2 = 20  # Τάση σε V
I = 2  # Ένταση ρεύματος σε Α

print()

# ---------------------------------
print('Όταν ο διακόπτης είναι ανοιχτός τότε το κύκλωμα δεν διαρρέεται')
print('από ρεύμα, συνεπώς η ένδειξη του βολτομέτρου V1 δείχνει την ΗΕΔ, άρα:')
E = V1
print('E={:.2f} V'.format(E))

print('Όταν ο διακόπτης κλείνει τότε το κύκλωμα διαρρέεται από ρεύμα Ι={}A'.format(I))
R = V2 / I
print('και η ένδειξη του βολτομέτρου V2=I*R => R={} Ω'.format(R))

print('και ισχύει αν εφαρμόσουμε τον νόμο του Ohm:')
print('E=I*R+I*r => r= (E-I*R) / I =>', end='')
r = (E - I * R) / I
print('r={:.2f} Ω'.format(r))
