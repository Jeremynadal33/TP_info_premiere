import streamlit as st
from footer import footer
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

def menu_cours():
    st.title("TP - Listes : Cours")

    st.write("# I - Introduction")
    with st.beta_expander("Afficher/Cacher"):
        st.write('''
        ## 1 - Définition d'une liste
        Une liste en python permet de stocker des données.
        On parle de structure de données ou bien d’objet conteneur, c’est à dire d’un objet qui peut en contenir un autre.
        Une liste est un objet modifiable (mutable) qui peut contenir un ou plusieurs types d'objets différents.

        On note les listes avec des crochets, les valeurs séparées par des virgules : [ valeur1 , valeur2 ,valeur3 ]. Par exemple :
        ''')
        with st.echo():
            liste1 = [1, 2, 3] # Liste d'entiers
            liste2 = [1.0, 2.0, 3.0] # Liste de flottants (nombres à virgules)
            liste3 = [True, True, False] # Liste de booléens

            liste4 = [1, True, 1.0] # Liste de plusieurs types
            liste5 = [[1,2], [1,2,3]] # Liste de listes

        st.write('''
        On appelle le rang de chaque terme de la liste, l'indice (ou index en anglais). L'indice de chaque liste commence à 0. Donc le premier item d'une liste à pour indice 0, le second a pour indice 1 et ainsi de suite.
        \nSouvent, on note l'indice d'une liste _i_ ou _index_.
        ''')
        st.write('''
        ## 2 - Créer une liste
        Pour initialiser une liste, on utilise la syntaxe suivante qui va créer une variable de type list, vide :
        - A l’aide de la fonction :   _list()_
        - A l’aide des crochets :  _[ ]_
        ''')

        with st.echo():
            liste1 = list()
            liste2 = []

        st.write("Rappel : on peut vérifier le type d'une variable en utilisant _type(variable)_ :")
        with st.echo():
            print('Le type de la liste1 est :', type(liste1))


        st.write('''
        ## 3 - Longueur d'une liste
        On peut connaitre la longueur d'une liste en utilisant la fonction _len()_ :
        ''')

        with st.echo():
            print('La longueur de la liste1 est :', len(liste1))

        st.write('''
        ## 4 - Accéder aux valeurs d'une liste
        On peut accéder à un terme d'une liste très facilement quand on connait son indice en écrivant le nom de la liste suivi de l'indice entre crochets.

        Par exemple :
        ''')

        with st.echo():
            liste = [3, 6, -3] # une liste d'entiers
            print(liste[0]) # Affiche le premier élément de la liste : 3
            print(liste[2]) # Affiche le premier élément de la liste : -3
        st.write('''
        Attention, il faut être sûr que l'élément existe. Essayer l'exemple suivant en enlevant le "#" au début de la deuxième ligne.
        ''')

        with st.echo():
            liste = [3, 6, -3]
            #print(liste[3]) # Retournerait une erreur car il n'y a pas d'élément d'indice 3 dans la liste

        st.write('''
        On peut aussi accéder au dernier élément d'une liste en utilisant l'indice "-1" :
        ''')
        with st.echo():
            liste = [3, 6, -3] # une liste d'entiers
            print(liste[-1]) # Affiche le dernier élément de la liste : -3


        st.write('''
        On peut aussi modifier l'élément d'une liste en utilisant l'indice :
        ''')
        with st.echo():
            liste = [3, 6, -3] # une liste d'entiers
            liste[0] = -3
            print(liste) # Affiche la liste modifiée



        st.write('''
        ## 5 - Parcourir une liste
        On peut afficher la liste en utilisant la fonction _print()_ :
        ''')
        with st.echo():
            liste = [3, 6, -3]
            print(liste)
        st.write('''
        On peut aussi afficher tous les éléments un par un avec une boucle for :
        ''')

        with st.echo():
            liste = [3, 6, -3] # une liste d'entiers
            for item in liste : # On accède directement aux items des listes
                print(item)

            for index in range(len(liste)): # On parcourt les indices
                print("La valeur d'indice ", index, "de la liste est :",  liste[index])
        st.write('''
        ## 6 - Retrouver l'indice d'un item
        On peut retrouver l'indice d'un item dans une liste avec la méthode _.index(item)_.

        Attention, si la liste contient plusieurs fois _item_, la méthode retournera l'indice du premier.
        ''')

        with st.echo():
            liste = ["a","b","c","d","e","e"]
            print(liste.index("a")) # on cherche l'index de l'élément 'a'
            print(liste.index("e")) # on cherche l'index de l'élément 'e'

    st.write('# II - Ajouter et enlever des valeurs')
    with st.beta_expander("Afficher/Cacher"):
        st.write('''
        ## 1 - Ajouter des valeurs à la création
        ''')
        with st.echo():
            liste = [3, 6, -3] # On crée une liste avec trois éléments

        st.write('''
        ## 2 - Ajouter des valeurs avec _.append()_
        On peut utiliser la méthode _.append()_ sur une liste après sa création. Ceci ajoute un élément à la fin de la liste.
        ''')

        with st.echo():
            liste = [3, 6, -3] # Liste avec 3 éléments
            liste.append(5)
            print(liste) # [3, 6, -3, 5]

        st.write('''
        ## 3 - Ajouter des valeurs avec _.insert()_
        On peut utliser la méthode _.insert()_ sur une liste pour insérer un nouvel élément à un indice précis et décaler ceux qui suivent :
        ''')
        with st.echo():
            liste = [3, 6, -3]
            indice = 2
            element = 0
            liste.insert(indice, element)
            print(liste) # [3, 6, 0, -3]

        st.write('''
        ## 4 - Supprimer des valeurs avec _del_
        La fonction _del liste[i]_ va supprimer l’item à l'indice i spécifié. On n'a pas besoin de connaitre l'élément, simplement son indice.
        ''')
        with st.echo():
            liste = [3, 6, -3] # On crée une liste avec 3 éléments
            print('On affiche liste avant de supprimer un élément : ', liste)
            del liste[0] # On supprime le premier élément de la liste
            print('On affiche liste après avoir supprimé un élément : ', liste)


        st.write('''
        ## 5 - Supprimer des valeurs avec _.pop()_
        La méthode _liste.pop(i)_ va supprimer l’item à l'indice _i_ spécifié comme _del_ mais en plus il **retourne la valeur supprimée**. Si on ne donne pas _i_, c’est le dernier élément qui est supprimé.
        ''')
        with st.echo():
            import random
            liste = [] # On crée une liste vide
            for i in range(10): # et on va y ajouter 10 éléments
                liste.append(random.randint(0,1)) # on y ajoute aléatoirement un entier entre 0 et 1
            element = liste.pop() # On enlève le dernier élément et on le récupère pour l'afficher

            print('La liste après avoir supprimé un élément : ', liste)
            print("L'élement supprimé est : ", element)


        st.write('''
        ## 6 - Supprimer des valeurs avec _.remove()_
        Il est possible de supprimer un item d'une liste avec sa valeur en utilisant la méthode _.remove(item)_. Cela va supprimer le premier élément de la liste égale à _item_.
        Attention, il faut être sûr que _item_ est contenu dans la liste, sinon il y aura une erreur.
        ''')
        with st.echo():
            liste = [3, 6, -3]
            liste.remove(3) # On enlève l'item 3
            print("Après suppression d'un élément, la liste contient :",liste)
            # liste.remove(3) # Si on essaie à nouveau, il y aura une erreur. Essayer en enlevant le "#" au début de la ligne.

    st.write("# III - Compléments")
    with st.beta_expander("Afficher/Cacher"):
        st.write('''
        ## 1 - Trier une liste
        Lorsque les items d'une liste sont du même type, on peut les trier en utilisant la méthode _.sort()_ :
        - Pour une liste de nombres (entiers ou à virgule), la liste sera triée dans l'ordre croissant
        - Pour une liste de caractères, ce sera par ordre alphabétique
        - Pour une liste de booléens, ce sera les _False_ en premier puis les _True_
        ''')


        with st.echo():
            liste1 = [4, 2, 9, -2] # Une liste de nombres
            liste2 = ['b', 'a', 'x', 'p'] # Une liste de caractères
            liste3 = [True, False, False, True, False] # Une liste de booléens
            # On trie les listes :
            liste1.sort()
            liste2.sort()
            liste3.sort()
            print("La liste1 triée est : ", liste1)
            print("La liste2 triée est : ", liste2)
            print("La liste3 triée est : ", liste3)

        st.write('''
        ## 2 - Concaténer deux listes
        Concaténer deux listes veut dire créer une liste avec tous les élements de la première suivis de ceux de la seconde.
        Il suffit d'utiliser le signe _+_ : liste1 + liste2.
        ''')

        with st.echo():
            liste1 = [4, 2, 9, -2] # Une liste de nombres
            liste2 = ['b', 'a', 'x', 'p'] # Une liste de caractères
            liste3 = liste1 + liste2
            print("La liste3 contient : ", liste3)

        st.write('''
        ## 3 - Les slices
        On peut selectionner une sous partie d'une liste en utilisant le signe _:_. Il veut dire 'tous les indices' mais on peut ajouter des bornes _a_ et _b_ comme : _a:b_ ce qui voudrait dire tous les indices entre _a_ et _b_ avec _b_ exclu.
        ''')

        with st.echo():
            liste = [3, 6, -3, 4, 2, -1]
            print(liste[:]) # On affiche tous les éléments
            print(liste[1:2]) # On affiche seulement les élements d'indice 1 à 2 avec 2 exclu
            print(liste[:3]) # On affiche les 3 premiers éléments
            print(liste[:-1]) # On affiche tous les éléments sauf le dernier
            print(liste[-3:]) # On affiche les 3 derniers éléments


        st.write('''
        ## 4 - Inverser les valeurs d'une liste
        On peut inverser les valeurs d'une liste de deux manières différentes :
        - En utilisant la méthode _.reverse_
        - En utilisant les slices : _[::-1]_
        ''')

        with st.echo():
            liste1 = [3, 6, -3]
            liste2 = [3, 2, -1]

            liste1.reverse() # Ici la liste1 est modifiée
            print("La liste1 renversée : ", liste1)
            print("La liste2 renversée : ", liste2[::-1]) # ici, on affiche juste la liste renversée, la liste2 n'est pas modifée

        st.write('''
        ## 5 - Compter les occurences d'un item
        On peut compter le nombre d'items identiques dans une liste en utilisant la méthode _.count(item)_. Si _item_ n'est pas dans la liste, cela renverra 0.
        ''')

        with st.echo():
            liste = [3, 6, -3, 3, 2, -1]

            print("La liste contient", liste.count(3), "fois le nombre 3")
            print("La liste contient", liste.count(1), "fois le nombre 1")


        st.write('''
        ## 6 - Liste définie par compréhension
        Les listes en compréhension sont une syntaxe présente dans le langage Python (entre autres) permettant de filtrer un itérable (comme une liste).
        En gros, cela permet l’écriture d’une boucle for dont la finalité est de créer une liste. Un exemple sera plus parlant :
        ''')

        with st.echo():
            # On va créer la liste des carrés de 0 à 10
            # D'abord en utilisant une boucle :
            liste_boucle = []
            for i in range(11):
                liste_boucle.append(i*i)

            # Puis par compréhension :
            liste_comprehension = [i**2 for i in range(10)]

            print(liste_boucle)
            print(liste_comprehension)

    st.write('''
    # IV - Résumé
    ''')
    with st.beta_expander('Afficher/Cacher'):

        st.write('''
    - Une liste est un objet conteneur qui est mutable.
    - Pour créer une liste, on utilise la syntaxe :
        - _liste = [valeur1,valeur2,valeur3]_
    - Pour récupérer une valeur dans une liste python :
        - La méthode directe : _liste[index]_ # Attention le 1er élément de la liste L est L[0], le 2e est L[1] ...
        - En utilisant les slices : _liste[i:j]_ # renvoie une sous liste composée des éléments d’indice _i_ à _(j-1)_
    - Remplacer une valeur si l'indice existe::
        - _liste[index] = valeur_ # pour modifier la valeur
    - Ajouter une valeur :
        – _liste.append(valeur)_ # pour ajouter valeur à la fin de la liste
        - _liste.insert(index, valeur)_ # pour ajouter valeur à l'indice _index_
    - Supprimer un item :
        - Avec l'indice : _del_ ou _.pop()_ # pas besoin de connaitre l'item
        - Avec sa valeur : _.remove(x)_ # le premier élément dont la valeur est égale à _x_
    - Parcourir une liste :
        - Par les index : _for index in range(len(liste))_
        - Directement : _for item in liste_
    - Trouver l'indice d'une valeur :
        - _liste.index(item)
    - Trier ou renverser les valeurs d'une liste :
        - _liste.sort()_
        - _liste.reverse()_ # Modifie liste
        - _liste[::-1]_ # Retourne la liste renversée sans la modifier
    - Compter le nombre d'occurences d'une valeur :
        - _liste.count(item)_
        ''')


    st.markdown(footer,unsafe_allow_html=True)

def menu_ex_listes_1():
    st.title("TP - Listes : Exercices I")

### EXERCICE 1 ###
    st.subheader("Exercice 1 :")
    st.write('''
    1.  Créer une liste _L1_ contenant les valeurs 3, 4, 5.
    3.  Modifier le premier élément de cette liste en lui donnant la valeur 1 puis afficher cette liste pour vérifier.
    4.  Créer une liste _L2_ avec 3 éléments de type différents.
    5.  Afficher le deuxième élément de cette liste ainsi que son type.
    6.  Créer une liste _L3_ avec 6 éléments avec au moins 2 types différents.
    7.  Afficher la longueur de cette liste.
    8.  Parcourir cette liste, et pour chaque élément, afficher son indice, sa valeur et son type.
    ''')

    cols = st.beta_columns([1,1])
    with cols[0]:

        with st.beta_expander("Aide"):
            st.write("Remplacer les '...' en enlevant les mot clefs _try :_ , _except :_  et _pass_ :")
            with st.echo():
                try :
                    L1 = [..., ..., ...]
                    L1[...] = 1
                    ...

                    L2 = [1, 'a', True] # Un entier, un charactère et un booléen
                    print(..., ...)
                    L3 = [1, 'a', 'b', 3, 4, 5]
                    print(...(L3))
                    for index in ... :
                        print(..., ..., ...)
                except:
                    pass

    with cols[1]:
        with st.beta_expander("Solution"):
            st.write("Recopie quand même dans EduPython pour t'assurer que tu comprends")
            with st.echo():
                L1 = [3, 4, 5]
                L1[0] = 1 # Le premier élément à pour indice 0
                print(L1)

                L2 = [1, 'a', True] # Un entier, un charactère et un booléen
                print(L2[1], type(L2[1])) # On donne le type d'un élément en utilisant la fonction type()
                L3 = [1, 'a', 'b', 3, 4, 5]
                print(len(L3)) # on peut avoir la longueur d'une liste en utilisant la fonction len()
                for index in range(len(L3)):
                    print(index, L3[index], type(L3[index]))

def menu_ex_listes_2():
    st.title("TP - Listes : Exercices II")

### EXERCICE 1 ###
    st.subheader("Exercice 1 :")
    st.write('''
    1.  Créer une liste _L1_ contenant les valeurs 3, 4, 5.
    2.  Créer une liste _L2_ vide et ajouter des valeurs pour que _L1=L2_.
    3.  Vérifier que _L1=L2_.
    ''')

    cols = st.beta_columns([1,1])
    with cols[0]:

        with st.beta_expander("Aide"):
            st.write("Remplacer les '...' en enlevant les mots-clefs _try :_ , _except :_  et _pass_ :")
            with st.echo():
                try :
                    L1 = [..., ..., ...]
                    L2 = ...
                    ...
                    ...
                    ...
                    print( ... )
                except:
                    pass

    with cols[1]:
        with st.beta_expander("Solution"):
            st.write("Recopie quand même dans EduPython pour t'assurer que tu comprends")
            with st.echo():
                L1 = [3, 4, 5]
                L2 = []
                L2.append(3)
                L2.append(4)
                L2.append(5)
                print(L1 == L2)

    st.write("#")
    st.write("#")

### EXERCICE 2 ###
    st.subheader("Exercice 2 :")
    st.write('''
    1.  Créer une liste _L_ contenant les jours suivants (sous forme de caractères): Lundi, Mardi, Jeudi, Vendredi, Vendredi.
    2.  Ajouter Mercredi au bon endroit.
    3.  Supprimer un Vendredi et afficher la liste afin de vérifier que nous avons tous les jours ouvrés.
    ''')

    cols = st.beta_columns([1,1])
    with cols[0]:

        with st.beta_expander("Aide"):
            st.write("Remplacer les '...' en enlevant les mots-clefs _try :_ , _except :_  et _pass_ :")
            with st.echo():
                try :
                    L = [..., ..., ..., ..., ...]
                    L.insert(..., ...)
                    L.remove(...)
                    print( ... )
                except:
                    pass

    with cols[1]:
        with st.beta_expander("Solution"):
            st.write("Recopie quand même dans EduPython pour t'assurer que tu comprends")
            with st.echo():
                L = ['Lundi', 'Mardi', 'Jeudi', 'Vendredi', 'Vendredi']
                L.insert(2, 'Mercredi')
                L.remove('Vendredi')
                print( L )

    st.write("#")
    st.write("#")

### EXERCICE 3 ###
    st.subheader("Exercice 3 : Tri sélection")
    st.write('''
    1.  Expliquer ce que fait la fonction suivante en la testant sur une liste _L = [3, 4, 1, -1]_ :
    ''')
    with st.echo():
        def ppe(L):
            resultat = L[0]
            for item in L:
                if item < resultat:
                    resultat = item
            return resultat

    cols = st.beta_columns([1,1,1])
    with cols[0]:
        with st.beta_expander("Solution"):
            st.write("La fonction permet de trouver le plus petit élément d'une liste _L_.")
    with cols[1]:
        with st.beta_expander('Définir L'):
            L = [st.number_input("L[0]", -10, 10, 3), st.number_input("L[1]", -10, 10, 4), st.number_input("L[2]", -10, 10, 1), st.number_input("L[3]", -10, 10, -1)]
    with cols[2]:
        if st.button("Tester"):
            #L = [3, 4, 1, -1]
            st.write("ppe([{},{},{},{}]) : {}".format(L[0],L[1],L[2],L[3],ppe(L)))

    st.write("##")

    st.write('''
    2.  Le principe du tri sélection est le suivant :

    À chaque passage, tant que la liste _L_ n'est pas vide, on retire la plus petite valeur trouvée dans la liste _L_ et on la stocke dans une nouvelle liste _L\_ordre_, initiallement vide. Cette liste contiendra donc la liste _L_ triée par ordre croissant.
    Essayer d'effectuer cet algorithme à la main en utilisant la liste suivante : _L = [ 3, -1, 0, 2 ]_.

    3.  Utiliser la fonction _ppe_ précédente afin de compléter la fonction suivante :
    ''')

    with st.echo():
        def tri_selection(L):
            L_ordre = []
            for i in range(...):
                min = ...
                L.remove(...)
                L_ordre.append(...)

            return L_ordre

    cols = st.beta_columns([1,1,1])
    with cols[0]:
        with st.beta_expander("Solution"):
            st.write("Recopie quand même dans EduPython pour t'assurer que tu comprends")
            with st.echo():
                def tri_selection(L):
                    L_ordre = []
                    for i in range(len(L)):
                        min = ppe(L)
                        L.remove(min)
                        L_ordre.append(min)

                    return L_ordre
    with cols[1]:
        with st.beta_expander('Définir L'):
            L = [st.number_input("L[0] ", -10, 10, 3), st.number_input("L[1] ", -10, 10, 4), st.number_input("L[2] ", -10, 10, 1), st.number_input("L[3] ", -10, 10, -1)]
    with cols[2]:
        if st.button("Tester tri"):
            L_ordre = tri_selection(L.copy())
            st.write("tri_selection([{}, {}, {}, {}]) : \n\n [{}, {}, {}, {}]".format(L[0],L[1],L[2],L[3],L_ordre[0], L_ordre[1], L_ordre[2], L_ordre[3]))

        st.write("#")
        st.write("#")


### EXERCICE 4 ###
    st.subheader("Exercice 4 :")
    st.write('''
    1.  Créer une liste _L1_ de longueur 10 contenant aléatoirement des 1 ou des 0 en utilisant :
    ''')
    with st.echo():
        import random
        L1 = []
        for _ in range(10):
            L1.append(random.randint(0,1))
    st.write('''
    2.  Créer une liste _L2_ vide et la remplir avec les indices des items égaux à 1 dans _L1_.
    3.  Supprimer tous les 1 de la liste L1 de deux méthodes différentes (une en utilisant seulement _L1_ et une boucle _while_ et l'autre en utilisant _L2_ : attention au sens de parcours de la liste, pourquoi faut il la parcourir du dernier élément au premier et pas l'inverse ?) et afficher _L1_ pour vérifier.
    ''')

    cols = st.beta_columns([1,1])
    with cols[0]:

        with st.beta_expander("Aide"):
            st.write("Remplacer les '...' en enlevant les mots-clefs _try :_ , _except :_  et _pass_ :")
            with st.echo():
                try :
                    L2 = []
                    for index in range(...):
                        if ... :
                            L2.append(...)
                    L1_copy = L1.copy() # Pour que l'on puisse faire les deux méthodes
                    #Méthode 1 : on enlève directement les 1 dans L1
                    while 1 in ... : # On boucle tant que L1 contient un 1
                        L1.remove(...) # Et on enlève le premier à chaque fois
                    print(L1)

                    #Méthode 2 : on utilise les indices récupérés dans L2
                    for index in ... :  # Attention, il faut parcourir L2 à l'envers
                        L1_copy.pop(...)
                    print(...)
                except:
                    pass

    with cols[1]:
        with st.beta_expander("Solution"):
            st.write("Recopie quand même dans EduPython pour t'assurer que tu comprends")
            with st.echo():
                L2 = []
                for index in range(len(L1)):
                    if L1[index]==1 :
                        L2.append(index)
                L1_copy = L1.copy() # Pour que l'on puisse faire les deux méthodes
                #Méthode 1 : on enlève directement les 1 dans L1
                while 1 in L1 : # On boucle tant que L1 contient un 1
                    L1.remove(1) # Et on enlève le premier à chaque fois
                print(L1)

                #Méthode 2 : on utilise les indices récupérés dans L2
                for index in L2[::-1] :  # Attention, il faut parcourir L2 à l'envers
                    L1_copy.pop(index)
                print(L1_copy)
def menu_ex_listes_3():
    st.title("TP - Listes : Exercices III")

### EXERCICE 1 ###
    st.subheader("Exercice 1 :")
    st.write('''
    1.  Écrire une fonction _create\_list_ prenant en argument un nombre entier positif _n_ et deux nombres _a_ et _b_ **avec _a_ < _b_** et qui renvoie une liste _L_ de nombres aléatoires entre _a_ et _b_ de longueur _n_.
    ''')

    cols = st.beta_columns([1,1])
    with cols[0]:
        with st.beta_expander("Aide"):
            st.write("Remplacer les '...' en enlevant les mots-clefs _try :_ , _except :_  et _pass_ :")
            with st.echo():
                import random
                def create_list(n, a, b):
                    L = ...
                    for i in range(...):
                        ...
                    return L

    with cols[1]:
        with st.beta_expander("Solution"):
            st.write("Recopie quand même dans EduPython pour t'assurer que tu comprends")
            with st.echo():
                import random
                def create_list(n, a, b):
                    L = []
                    for i in range(n):
                        L.append(random.randint(a, b))
                    return L
    st.write("##")
    st.write('''
    2.  Écrire une fonction _moyenne_ prenant en argument une liste _L_ et retournant la moyenne des éléments de la liste.
    ''')
    cols = st.beta_columns([1,1])
    with cols[0]:
        with st.beta_expander("Aide"):
            st.write("Remplacer les '...' en enlevant les mots-clefs _try :_ , _except :_  et _pass_ :")
            with st.echo():
                def moyenne(L):
                    sum = ...
                    for i in range(...):
                        sum += ...
                    return ...

    with cols[1]:
        with st.beta_expander("Solution"):
            st.write("Recopie quand même dans EduPython pour t'assurer que tu comprends")
            with st.echo():
                def moyenne(L):
                    sum = 0
                    for i in range(len(L)):
                        sum += L[i]
                    return sum/len(L)
    st.write("##")
    st.write('''
    3.  Écrire une fonction _mediane_ prenant en argument une liste _L_ et retournant la médiane des éléments de la liste. (on peut utiliser int() pour s'assurer que l'on a un chiffre entier)
    ''')
    cols = st.beta_columns([1,1])
    with cols[0]:
        with st.beta_expander("Aide"):
            st.write("Remplacer les '...' en enlevant les mots-clefs _try :_ , _except :_  et _pass_ :")
            with st.echo():
                def mediane(L):
                    L.sort()           # On trie L
                    milieu = int(...)  # On cherche l'indice du milieu de la liste
                    if len(L) % 2 == 0: # On regarde si la liste contient un nombre pair ou impair de valeurs
                        ...
                    else :
                        ...
    with cols[1]:
        with st.beta_expander("Solution"):
            st.write("Recopie quand même dans EduPython pour t'assurer que tu comprends")
            with st.echo():
                def mediane(L):
                    L.sort()
                    milieu = int(len(L)/2)
                    if len(L) % 2 == 0:
                        return (L[ milieu - 1] + L[milieu])/2
                    else :
                        return L[milieu]

    st.write("#")
    st.write("#")


### EXERCICE 2 ###
    st.subheader("Exercice 2 :")
    st.write('''
    1.  Écrire une fonction _suite_ prenant en argument un nombre entier positif _n_ et un flottant _q_ et qui renvoie une liste _L_ des _n_ premiers termes de la suite (Un) définie par U0 = 1 et Un+1 = q*Un
    ''')

    cols = st.beta_columns([1,1,1])
    with cols[2]:
        with st.beta_expander("Aide"):
            st.write("Remplacer les '...' ")
            with st.echo():
                def suite(n, q):
                    U = 1
                    L = ... # on inialise L
                    for i in range(...): # attention, on veut les n premiers termes
                        U = ... # formule de récurrence
                        ...
                    return ...

    with cols[1]:
        with st.beta_expander("Solution"):
            st.write("Recopie quand même dans EduPython pour t'assurer que tu comprends")
            with st.echo():
                def suite(n, q):
                    U = 1
                    L = [U]
                    for i in range(1,n):
                        U = q*U
                        L.append(U)
                    return L
    with cols[0]:
        with st.beta_expander("Définir n et q : "):
            n = st.number_input("n = ", 0, 20, 10)
            q = st.number_input("q = ", -5.0, 5.0, 2.0)
        if st.button("Tester"):
            st.markdown(suite(n, q))


    st.write("##")
    st.write('''
    2.  Nous allons maintenant apprendre à tracer des points sur une courbe en traçant les _n_ premiers termes de la suite _(Un)_.
    \nPour cela, utilise le bout de code ci dessous :
    ''')

    cols = st.beta_columns([1,1])
    with cols[0]:
        with st.echo():
            import matplotlib.pyplot as plt # Librairie pour faire des graphiques
            q = 1/2
            n = 15
            L = suite(n, q)
            fig, ax = plt.subplots()
            ax.scatter( range(len(L)), L )
            plt.show()
    with cols[1] :
        with st.beta_expander("Définir n et q : "):
            n = st.number_input("n =", 0, 20, 10)
            q = st.number_input("q =", -5.0, 5.0, 2.0)
        if st.button("Tester "):
            L = suite(n, q)
            fig, ax = plt.subplots()
            ax.scatter( range(len(L)),L )
            st.pyplot(fig)
    st.write('''
    Essayer avec plusieurs valeurs de _q_ positives. Que remarque t on ?
    ''')


def menu_ex_proba():
    st.title("TP - Variables aléatoires : Exercices")

### EXERCICE 1 ###
    st.subheader("Exercice 1 : Loi uniforme")
    st.write('''
    La roulette française possède 37 cases numérotées de _0_ à _36_. La case _0_ est verte et les autres sont alternativement rouges et noires.

    Le jeu consiste à faire tourner la roulette afin qu'une bille tombe dans l'une des cases sachant qu'elle a autant de chances de tomber dans chacune des cases. On va s'intéresser à deux types de pari.

    1.  Un joueur mise sur son numéro fétiche. Si ce numéro sort, il reçoit _35_ fois sa mise et récupère sa mise sinon il la perd. Quelle est l'espérence du gain de ce joueur lorsque sa mise est de _37€_ ?
    2.  Nous allons essayer d'approcher empiriquement ce résultat :

    2.1  - Écrire une fonction _mise\_numero_ prenant en argument _num_ le numéro fétiche d'un joueur et _mise_ sa mise et simule une partie de ce jeu (on retournera le gain).

    _Rappel : pour faire de l'aléatoire, il faut mettre *import random* et la fonction *random.randint(a,b)* renvoie un nombre entier entre a et b._
    ''')

    cols = st.beta_columns([1,1,1])
    with cols[0]:
        with st.beta_expander("Aide"):
            st.write("Remplacer les '...' ")
            with st.echo():
                import random
                def mise_numero(num, mise):
                    alea = ...
                    if ... :
                        gain = ...
                    else :
                        gain = ...
                    return gain

    with cols[1]:
        with st.beta_expander("Solution"):
            st.write("Recopie quand même dans EduPython pour t'assurer que tu comprends")
            with st.echo():
                import random
                def mise_numero(num, mise):
                    alea = random.randint(0, 36)
                    if num == alea :
                        gain = 35 * mise
                    else :
                        gain = -mise
                    return gain
    with cols[2]:
        with st.beta_expander("Définir num et mise : "):
            num = st.number_input("num = ", 0, 37, 7)
            mise = st.number_input("mise = ", 0, 50, 37)
        if st.button("Tester"):
            st.markdown('Le gain est : '+str(mise_numero(num, mise))+'€')


    st.write("##")
    st.write('''
    2.2 -  Écrire une fonction _esperance\_mise\_numero_ permettant de jouer _n_ parties. Elle prendra en argument _num_, _mise_ et _n_ le nombre de parties à effectuer. Cette fonction retournera le gain moyen.

    Essayer avec des valeurs de _n_ croissantes de _10_ à _10000000_ (pour _n_ très grand, cela peut prendre du temps). Que remarque t on ?
    ''')

    cols = st.beta_columns([1,1])
    with cols[0]:
        with st.beta_expander("Aide : "):
            with st.echo():
                def esperance_mise_numero(num, mise, n):
                    gain = ...
                    for i in range(...):
                        gain += ...
                    return ...
    with cols[1] :
        with st.beta_expander("Solution : "):
            with st.echo():
                def esperance_mise_numero(num, mise, n):
                    gain = 0
                    for i in range(n):
                        gain += mise_numero(num, mise)
                    return gain/n


    st.write("##")
    st.write('''
    3.  Intéressons nous maintenant à l'autre type de mise : le joueur mise _37€_ sur la couleur _Rouge_:
        - Si un numéro rouge sort, il reçoit _37€_ plus sa mise
        - Si un numéro noir sort, il perd sa mise
        - Si le numéro _0_ sort, le joueur relance une fois la roulette :
            - Lors du deuxième lancer, un numéro rouge sort, le joueur ne gagne rien mais récupère sa mise
            - Sinon, le joueur perd sa mise.

    Quelle est l'espérence de gain du joueur avec ce pari ?

    ##
    4.  Écrire une fonction _mise\_couleur_ prenant en argument _couleur_ ('rouge' ou 'noir') et _mise_ permettant de simuler une partie de ce jeu.

    _AIDE : Pour simplifier les choses, on va partir du principe que les nombres pairs sont noirs et les nombres impairs sont rouges._

    _Rappel : *a%b* renvoie le reste de la division eucidienne de *a* par *b*._
    ''')

    cols = st.beta_columns([1,1])
    with cols[0]:
        with st.beta_expander("Aide : "):
            with st.echo():
                import random
                def mise_couleur(couleur, mise):
                    assert couleur == 'noir' or couleur == 'rouge', "L'argument couleur doit être soit 'rouge' soit 'noir'."
                    alea = ...
                    if ... : # vert
                        couleur_alea = ...
                    elif ... : # noir
                        couleur_alea = ...
                    else :
                        couleur_alea = ...

                    if ... : # couleur identique
                        gain = mise
                    elif ... : # couleurs differentes et couleur autre que verte
                        gain = -mise
                    else : # vert
                        alea = ...
                        if ... : # vert
                            couleur_alea = ...
                        elif ... : # noir
                            couleur_alea = ...
                        else :
                            couleur_alea = ...

                        if ... : #
                            gain = 0
                        else :
                            gain = -mise
                    return gain
    with cols[1] :
        with st.beta_expander("Solution : "):
            with st.echo():
                import random
                def mise_couleur(couleur, mise):
                    assert couleur == 'noir' or couleur == 'rouge', "L'argument couleur doit être soit 'rouge' soit 'noir'."
                    alea = random.randint(0,36)
                    if alea == 0 : # vert
                        couleur_alea = 'vert'
                    elif alea%2 == 0 : # noir
                        couleur_alea = 'noir'
                    else :
                        couleur_alea = 'rouge'

                    if couleur == couleur_alea : # couleur identique
                        gain = mise
                    elif couleur_alea != 'vert' : # couleurs differentes et couleur autre que verte
                        gain = -mise
                    else : # vert
                        alea = random.randint(0, 36)
                        if alea == 0 : # vert
                            couleur_alea = 'vert'
                        elif alea%2 == 0 : # noir
                            couleur_alea = 'noir'
                        else :
                            couleur_alea = 'rouge'

                        if couleur == couleur_alea : #
                            gain = 0
                        else :
                            gain = -mise
                    return gain


    st.write("##")
    st.write('''
    5.  On peut aussi estimer la loi de probabilité empirique à l'aide d'un [histogramme](https://fr.wikipedia.org/wiki/Histogramme).
    Ce dernier va compter le nombre de fois où chacune des issues de l'expérience aléatoire est apparue puis le diviser par le nombre total d'issues, ce qui donne une approximation de la loi de probabilité.

    Pour ce faire, nous avons besoin de récuperer dans une liste, toutes les issues d'une expérience aléatoire. Quel est, dans le premier exemple, l'ensemble des issues possibles ?
    Écrire une fonction _lancers\_roulettes_ prenant en argument _n_ le nombre de lancers à effectuer et retourner la liste des nombres issus des lancers.
    ''')

    cols = st.beta_columns([1,1])
    with cols[0]:
        with st.beta_expander("Aide : "):
            with st.echo():
                import random
                def lancers_roulettes(n):
                    lancers = ... # initialisation d'une liste vide
                    for i in ... :
                        alea = ...
                        ... # Mettre à jour la liste
                    return ...
    with cols[1] :
        with st.beta_expander("Solution : "):
            with st.echo():
                import random
                def lancers_roulettes(n):
                    lancers = []
                    for i in range(n):
                        alea = random.randint(0, 36)
                        lancers.append(alea)
                    return lancers
    st.write("##")
    st.write('''
    Le bout de code suivant permet de générer l'histogramme à partir de la liste générée avec la fonction _lancers\_roulettes_ :
    ''')
    with st.echo():
        import matplotlib.pyplot as plt
        n = 10
        lancers = lancers_roulettes(n)
        fig, ax = plt.subplots()
        ax.hist(lancers, density = True, bins = 37)
        plt.show()

    st.write('''
    Essayer cette fonction avec différentes valeurs de _n_ de _10_ à _100000_.

    On appelle cette loi, la *_loi uniforme_*. Avez vous une idée de la raison ?

    Sauriez vous dire vers quel nombre chacune des barres verticales de l'histogramme, tend ?
    ''')
    st.write("#")

### EXERCICE 2 ###
    st.subheader("Exercice 2 : Loi normale")
    st.write('''
    Les [_lois normales_](https://fr.wikipedia.org/wiki/Loi_normale) ou _lois gaussiennes_ sont parmi les lois de probabilité les plus utilisées pour modéliser des phénomènes naturels issus de phénomènes aléatoires.
    Nous verrons dans cet exercice, un exemple très simple.

    Considérons la variable aléatoire _X_ qui associe à chaque lancer la somme de _2_ dès cubiques équilibrés.

    1.  Déterminer l'ensemble issues possibles de l'expérience aléatoire.
    2.  Déterminer la loi de probabilité de la variable _X_.
    3.  Écrire une fonction _un\_lancer_ qui simule un lancer de dès et qui retourne la valeur de la variable _X_.
    ''')

    cols = st.beta_columns([1,1])
    with cols[0]:
        with st.beta_expander("Aide : "):
            with st.echo():
                import random
                def un_lancer():
                    des_1 = ...
                    des_2 = ...
                    return ...

    with cols[1] :
        with st.beta_expander("Solution : "):
            with st.echo():
                import random
                def un_lancer():
                    des_1 = random.randint(1,6)
                    des_2 = random.randint(1,6)
                    return des_1 + des_2

    st.write('''
    4.  En vous aidant de l'exercice précédent, proposer un bout de code permettant de calculer l'espérance de _X_.
    5.  En vous aidant de l'exercice précédent, proposer un bout de code permettant d'afficher la loi de probabilité empirique de _X_.
    ''')



############### MAIN #########
def main():
    possibilities = ["Cours", "Exercices listes I", "Exercices listes II", "Exercices listes III", "Exercices variables aléatoires"]
    choice = st.sidebar.selectbox("Menu",possibilities)



    if choice == 'Cours':
        menu_cours()
    elif choice == 'Exercices listes I':
        menu_ex_listes_1()
    elif choice == 'Exercices listes II':
        menu_ex_listes_2()
    elif choice == 'Exercices listes III':
        menu_ex_listes_3()
    elif choice == 'Exercices variables aléatoires':
        menu_ex_proba()



if __name__ == "__main__":
    main()
