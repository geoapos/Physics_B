#!/usr/bin/python3
# filename 4_5.py
"""
Άσκηση 4.5

Το άτομο του υδρογόνου βρίσκεται στη θεμελιώδη κατάσταση στην οποία η
ολική ενέργεια είναι –13,6eV:
α. Ποια ελάχιστη ενέργεια απαιτείται, για να ιονιστεί το άτομο;
β. Ποια ενέργεια απαιτείται, για να διεγερθεί το άτομο στην πρώτη διεγερμένη
κατάσταση (n=2);
γ. Το άτομο του υδρογόνου απορροφά, λόγω κρούσης, ενέργεια 15eV και
ιονίζεται. Ποια κινητική ενέργεια αποκτά τελικά το ηλεκτρόνιο, αν η κινητική
ενέργεια του ατόμου δε μεταβάλλεται κατά την κρούση;

"""


# Δεδομένα
E1 = -13.6    # Ενέργεια 1ης στάθμης σε eV
n2 = 2        # Κβαντικός αριθμός 2ης στάθμης
En = 15       # Ενέργεια  σε eV

print()
print('α) Η ενέργεια που απαιτείται για να ιονιστεί το άτομο είναι η ενέργεια\n'
      '   για να απομακρυνθεί το ηλεκτρόνιο σε ∞ απόσταση τότε:\n'
     f'   Eιον= E∞ - E1 = 0 - ({E1}) = {0-E1:.2f} eV, ')
print()

print('β) Η ενέργεια που απαιτείται, για να διεγερθεί το άτομο στην πρώτη διεγερμένη \n'
      '   κατάσταση (n=2) είναι: Ειον = E2 - Ε1 = (Ε1 / n2²) -Ε1 , έτσι:\n'
      '   Eιον=', end='')

Eιον = (E1 / n2**2) -E1
print(f'  {Eιον} eV')
print()

print('γ) Η κινητική ενέργεια που αποκτά τελικά το ηλεκτρόνιο είναι ίση με τη \n'
      f'   διαφορά της ενέργειας που απορροφά το άτομο ({En}) και της ενέργειας \n'
      f'   που απαιτείται, για να ιονιστεί το άτομο ({Eιον}eV):')
print(f'   Ek={En}-{-E1}={(En+E1):.2f} eV')
