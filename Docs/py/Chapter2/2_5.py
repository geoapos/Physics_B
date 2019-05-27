#!/usr/bin/python3
# filename 2_5.py
"""
Άσκηση 2.5

Να κάνετε τη γραφική παράσταση της αντίστασης ενός αγωγού σε συνάρτηση με:
α) το μήκος του
β) το εμβαδό διατομής τους
γ) την τάση στα άκρα του
δ) την ένταση του ρεύματος που τον διαρρέει.

"""
import matplotlib.pyplot as plt
import numpy as np


def RI(l):  # Συνάρτηση που υπολογίζει την αντίσταση ενός αγωγού συναρτήση του μήκους l
    ρ = 1.7 * 10 ** (-8)  # Ειδική αντίσταση χαλκού σε Ωm.
    S = 2 * 10 ** (-4)  # Διατομή Χαλκού σε m2self
    R = ρ * l / S
    return R


def RS(S): # Συνάρτηση που υπολογίζει την αντίσταση ενός αγωγού συναρτήση της διατομής του S
    ρ = 1.7 * 10 ** (-8)  # Ειδική αντίσταση χαλκού σε Ωm.
    l = 2  # Μηκος αγωγού σε m
    R = ρ * l / S
    return R


l = np.linspace(0, 30, 1000)  # Εύρος του l από 0-30 με 1000 τιμές δειγματοληψία
plt.title('Αντίσταση ενός αγωγού σε συνάρτηση με το μήκος του', fontsize=10, color='green')  # τίτλος γραφήματος
plt.xlabel('Μήκος l (m)', fontsize=10, color='green')  # x label
plt.ylabel('Αντίσταση (Ω)', fontsize=10, color='green')  # x label
plt.plot(l, RI(l), 'g-', linewidth=2.0)
plt.show()

S = np.linspace(1, 30, 1000)  # Εύρος του S από 1-30 με 1000 τιμές δειγματοληψία
plt.title('Αντίσταση ενός αγωγού σε συνάρτηση με την διατομή του', fontsize=10, color='red')  # τίτλος γραφήματος
plt.xlabel('Διατομή (m2)', fontsize=10, color='red')  # x label
plt.ylabel('Αντίσταση (Ω)', fontsize=10, color='red')  # x label
plt.plot(S, RS(S), 'r-', linewidth=2.0)
plt.show()
