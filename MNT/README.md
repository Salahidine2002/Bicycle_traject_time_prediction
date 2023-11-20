
# MNT

## Données exemples

* Le fichier `moulon.tif` contient le MNT de la zone du Moulon (2 km x 2 km). Il est le résultat du merge de 4 fichiers issus du MNT de l'IGN. Le système de coordonnées dans le quel il est enregistré est l'UTM 31N (à la différence des données initiales qui sont en RGF93)


## Quelques liens utiles

### Liens de référence pour les MNT France par l'IGN

 * https://geoservices.ign.fr/rgealti#telechargement1m
 * https://geoservices.ign.fr/documentation/donnees/alti

Les données sont des dalles de 1000 points x 1000 points. Pour la précision à 1 mètre cela correspond à des carrés de 1km x 1km.

### Exemple de superposition de MNT avec Leaflet 

 * https://rallydatajunkie.com/visualising-rally-stages/accessing-and-working-with-elevation-data-raster-files.html

 (le livre en ligne "Visualising WRC Rally Stages With rayshader and R - A RallyDataJunkie Adventure" par Tony Hirst semble être une lecture intéressante... à voir)

### Paquet pour exploiter les MNT sous python

 * https://rasterio.readthedocs.io/en/latest/installation.html
 Ce paquet permet de lire les fichiers de MNT dans la pluspart des formats, notemment le format .asc dans le quel sont fournies les données IGN 


