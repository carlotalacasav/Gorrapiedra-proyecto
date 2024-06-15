# Gorrapiedra-proyecto
Alejandro, Marina, Alba, Carlota 
Treball final postgrau.

El següent treball té la finalitat de fer una predicció del percentatge de molls per bicicletes donat l'històric recopilat de dades de cadascuna de les estacions. A més dels corresponents casos d'estudi.

Aquest, està basat en 3 sets de dades:
1. Informació de les bicicletes: Conté informació interessant per utilitzar a l'hora de predir.
2. Github Gist: Dades per a predir. Conté el registre per a cadascuna de les estacions per mes.
3. Kaggle: Mostra de com ha de ser la tramesa.

A continuació, es mostra una breu explicació de cadascun dels notebooks d'aquest treball

## VISUALITZACIÓ DADES BRUTES



## NETEJA DE DADES
En aquest fitxer s'ha desenvolupat un codi amb la finalitat de preprocessar les dades i deixar-les en el format adequat. En aquest s'eliminen columnes, valors nan, es formategen les dates i es creen noves columnes com per exemple el percentatge de disponibilitat de les bicicletes.

## FITXERS DIVIDITS EN ANYS
Aquests fitxers són extrets d'haver fet un previ codi de preprocessat de les dades, explicat prèviament.

## FITXER D'INFORMACIÓ EXTRA AFEGIDA
Per a poder millorar els models, hem decidit utilitzar més dades com és el cas del temps meteorològic i les diferents zones de Barcelona, a partir dels codis postals, és a dir, per polígons.

## VISUALITZACIÓ DE DADES NETES EN EL CORRESPONDENT FORMAT



## FITXER DE PREDICCIONS
Per a dur a terme les nostres prediccions, hem optat per utilitzar una combinació de models lineals i no lineals. En concret, hem implementat dos models lineals, un model de regressió lineal i un XGBoost Regressor (XGBRegressor), així com una xarxa neuronal senzilla. Aquesta elecció ens permet comparar els resultats obtinguts per cadascun d'aquests models i avaluar quin ofereix les millors prediccions.
