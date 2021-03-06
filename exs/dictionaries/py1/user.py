# -*- coding: utf-8 -*-

#### Άσκηση:
####  Γράψτε μια συνάρτηση σε Python
####
####    histogram(L)
####
#### όπου L είναι μια λίστα ακεραίων. Η συνάρτηση θα επιστρέφει ένα λεξικό όπου κλειδιά θα είναι
#### όσοι ακέραιοι εμφανίζονται στην L (μια φορά ο καθένας). Η τιμή του κάθε κλειδιού θα είναι
#### το πόσες φορές εμφανίζεται το κλειδί στην L. Αν η λίστα L είναι κενή θα πρέπει και το λεξικό
#### να είναι κενό.
#### 
#### Για παράδειγμα, αν L = [-1, 1, 0, 1, 2, -1]
#### τότε το αποτέλεσμα είναι το λεξικό {-1: 2, 1: 2, 0: 1, 2: 1}.

L = eval(input("Please give a list of integers (Python style): "))


def histogram(L):
    d = {}
    for x in L:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    return d
    
print(' ')
print(histogram(L))