# From_Id3_to_C4.5

## Présentation du projet

L’objectif du projet est de comprendre et d’implémenter l’algorithme Id3 puis de l’enrichir à travers 
différentes extensions proposées dans l’algorithme C4.5.

## Explication de l'algorithme

L’algorithme ID3 se base sur le concept d’attributs et de classe de l’apprentissage automatique (sur classification discrète3). Cet algorithme recherche l’attribut le plus pertinent à tester pour que l’arbre soit le plus court et optimisé possible.

Le principe de l’algorithme Id3 qui réalise la construction de l’arbre à partir de S est le suivant :

1- Sélectionner le « meilleur » attribut Ai pour faire croître l’arbre :
* Le « meilleur » attribut est celui qui possède le gain d’information le plus élevé pour S.
* Un nouveau nœud n(Ai) est ajouté à l’arbre et des branches sont créées pour chaque valeur 
possible de l’attribut Ai, i.e. vi1, vi2, …, viK.

2- Partitionner l’ensemble d’apprentissage « local » S en K sous-ensembles S1, S2, …, SK, chaque 
sous-ensemble regroupant les données satisfaisant au test Ai = vik, k= 1, ..., K.

3- Le processus de construction continue (étapes 1 et 2) jusqu’à satisfaire une des conditions 
d’arrêt suivantes :
* L’ensemble d’exemples associés au nœud courant est vide.
* Tous les exemples d’apprentissage associés au nœud courant ont la même valeur de classe, 
auquel cas une feuille avec cette valeur de classe est retournée.
* Tous les attributs ont été utilisés sur la branche en cours de développement, auquel cas une 
feuille est retournée avec la classe majoritaire parmi les exemples associés au nœud courant.


## Installation & Environnement
Telecharger le dossier depuis github:<br>
$ git clone https://github.com/RICHARD-90/From_Id3_to_C4.5.git <br>
Il n'y a pas de contrainte concernant l'environnement de programation.<br>
Ce programme est ecrit selon les normes [peip8](https://pep8.org/).
## Resultat

![image](https://user-images.githubusercontent.com/72502866/121279364-bd54b800-c8d4-11eb-996e-8d7543f1ff38.png)
![image](https://user-images.githubusercontent.com/72502866/121279404-cba2d400-c8d4-11eb-8085-c9480c536b1e.png)

