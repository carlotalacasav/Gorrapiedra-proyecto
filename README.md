# Gorrapiedra-proyecto
Alejandro Jaramillo, Marina Dalmau, Alba Martínez, Carlota Lacasa
Treball final postgrau.

El següent treball té la finalitat de fer una predicció del percentatge de molls per bicicletes donat l'històric recopilat de dades de cadascuna de les estacions. A més dels corresponents casos d'estudi.

# Breu explicació del contingut del repositori

## VISUALITZACIÓ DADES BRUTES
- /analisis_year_by_year: carpeta que conté, any a any, histogramas de cada variable del les dades "raw" del projecte per estudiar comportaments, tendèncias i trobar outliers i NaNs.

## FORMATEIG DE LES DADES RAW
- data_formating.ipynb: notebook en què treballem les dades "raw" per donar-lis el format correcte (amb el valor de la disponibilitat a les 5 hores anteriors a cada valor, fent la mitjana).

## DADES FORMATEJADES:
- /data/formated data: arxius .csv que contenen les dades resultat del punt anterior.

## DADES EXTERNES:
- /data/info bicing: axius que contenen la informació addicional de cada estació de Bicing.
- /data/locations_data: informació geogràfica d'interés relacionada amb la mobilitat, l'oci i els llocs d'interès cultural. Extretes d'[Open Data BCN](https://opendata-ajuntament.barcelona.cat/es/)
    - /data/locations_data/geo_data: arxius amb els polígons dels codis postals de la ciutat de Barcelona i arxius auxiliars per poder graficar-los.
    - /data/locations_data/barna_pics.csv: arxiu amb els llocs d'interès cultural de la ciutat de Barcelona.
    - /data/locations_data/bcn_ocio.csv: arxiu amb els llocs d'oci de la ciutat de Barcelona.
    - /data/locations_data/equipament.csv: arxiu amb informació sobre els equipaments relacionats amb la mobilitat a Barcelona.
- /data/weather_data: informació meterològica (precipitació i temperatura). Extreta de amb la API de Meteocat a través del notebook weather.ipynb
- /festius: arxiu amb la llista de festius a Barcelona entre 2020 i 2024.

## GENERACIÓ DEL DATAFRAME COMPLET:
- process_dataframe.ipynb: notebook que llegeix les dades formatejades i afegeix tota la informació externa, tractant adequadament els NaNs que apareixen. Escriu els arxius amb els dataframes sencers fora del repositori.

## FUNCIONS D'ÚS GENERAL
- utils.py: conté diverses funcions que es fan servir al llarg del procesament i l'entrenament de models.

## MODELS GUARDATS:
- /models: carpeta que conté arxius amb els models entrenats per la seva fàcil recuperació.

# MODELS ESTUDIATS

- evaluate_models.ipynb: diferents models estudiats, entrenats i evaluats.

## MODELS LINEALS:
- Regressor Lineal: estudi bàsic per fer servir com a base del projecte. Retorna uns valors R2 de al voltant de 0.80. Ens permet estudiar el comportament general del model i la importància aproximada de cada feature del model de dades.
- XGBOOST: model lineal més avançat i que dona millors resultats. Valors R2 de entre 0.84 i 0.86.

## XARXES NEURONALS:
- Xarxa neuronal bàsica: amb una arquitectura de 128-64-32-1 neurones. Dóna els millors resultats. Evaluada amb 10 i 100 epochs, valors R2 per sobre de 0.86. Millor resultat amb 10-20 epochs.
- Xarxa neuronal ampliada: amb una capa addicional inicial de 256 neurones. Mostra un overfitting evident, i pitjors resultats que la bàsica.
- Xarxa neuronal amb dropout: una capa de dropout amb paràmetre 0.5 després de cada capa de neurones. Dóna pitjors resultats a les prediccions i pitjors temps d'entrenament.

