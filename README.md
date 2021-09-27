# detecteur-de-Moravec (IUT:S3)
objectif: générer une heatMap des changement au seins d'une image

 - Langage utilisé : Python 
 - Résultat attendu : heatMap des points d'interet.
 
# Comment l'utiliser
##installation des dépendances pip (cocher la case "installer pip" à l'installation de python)
 - pip install imageio

## Parametres
 - image entrée: ligne 10 dans main.py
 - image de sortie: ligne 56 dans main.py
 - definition de la fenêtre: ligne 26 dans Intensite.py 
   la variable rayonVoisinageStatic correspond à rayon autour du pixels qui sera considèré comme étant dans la fenêtre.

## résolution de problèmes
 - les contours sont affiché mais n'apparaissent que très faiblement. <br>
    **solution:** augmenter la valeur du contraste ligne 46 de main.py
# Créateurs du projet
3 étudiants de 2A DUT informatique :
- **HOLAY Jérémy**
- **CHARLOT Valentin**
- [***RIVAT Matthis***](https://github.com/MattRvt)

## FAIT A  
**I.U.T. de Caen,
CAMPUS 3,
14123 Ifs,
Département Informatique**

