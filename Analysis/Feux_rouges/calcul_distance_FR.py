from numpy import sin, cos, arccos, pi, round
import overpy
import pandas as pd
import math

api = overpy.Overpass()

'''# récupération des noeuds qui nous intéressent dans la zone sélectionnée
result = api.query("""
    node(48.5026320, 2.1447839, 48.7107057, 2.2502904)
    [highway=traffic_signals];
    out;
    """)

feux_rouges_zone=[]     #création de la liste contenant les coordonées des feux rouges

for node in result.nodes:

    node.lat, node.lon=float(node.lat), float(node.lon)      #on passe en flottant

    coords_fr=[node.lat,node.lon]
    feux_rouges_zone.append(coords_fr)     #on ajoute les coords à la liste'''

feux_rouges_zone=[[48.6432999, 2.2277113], [48.6440138, 2.229054], [48.6867015, 2.1734666], [48.6848082, 2.1836103], [48.6844659, 2.1861026], [48.7006828, 2.1881442], [48.7002799, 2.188166], [48.6850638, 2.1863024], [48.7036758, 2.1927257], [48.7037897, 2.1924666], [48.7020258, 2.1735926], [48.6954158, 2.1764425], [48.6990236, 2.2082831], [48.6989478, 2.2031618], [48.6964973, 2.1554647], [48.7067205, 2.2105648], [48.704094, 2.2181155], [48.7035555, 2.2242576], [48.6533853, 2.2469109], [48.6716434, 2.2125916], [48.6794994, 2.2006153], [48.6860944, 2.2129053], [48.6755861, 2.2389974], [48.7029587, 2.2432553], [48.7008498, 2.2454688], [48.6891458, 2.2303165], [48.6972338, 2.246695], [48.6850348, 2.2392714], [48.6423356, 2.2329294], [48.6423749, 2.2328152], [48.7007565, 2.2455894], [48.6988143, 2.237854], [48.6987056, 2.2375258], [48.7007248, 2.2337515], [48.7027494, 2.2432614], [48.7013666, 2.2427162], [48.7094683, 2.2384], [48.704045, 2.2329923], [48.6883309, 2.206174], [48.7003171, 2.2209198], [48.6992729, 2.230792], [48.6985732, 2.2266978], [48.6986956, 2.2377046], [48.7097683, 2.2431145], [48.7095451, 2.2461899], [48.7084643, 2.2413054], [48.6839027, 2.2382657], [48.6986822, 2.235123], [48.7010957, 2.2436188], [48.7000001, 2.2140287], [48.6999463, 2.2155464], [48.6846977, 2.1940603], [48.6843441, 2.1995357], [48.6994161, 2.2247226], [48.7062346, 2.2112758], [48.7061499, 2.2107211], [48.5892762, 2.2452618], [48.5914698, 2.2443131], [48.5904803, 2.2447455], [48.6899519, 2.181429], [48.705406, 2.2143595], [48.5855446, 2.2417659], [48.5590052, 2.1553142], [48.7059828, 2.2053023], [48.7062283, 2.2047757], [48.6984906, 2.2302314], [48.7092824, 2.2461516], [48.7087966, 2.187312], [48.5802282, 2.2223227], [48.710671, 2.1589862], [48.6844059, 2.1881345], [48.6842871, 2.1885521], [48.6845491, 2.188873], [48.6963098, 2.1936362], [48.6451548, 2.2318329], [48.6785584, 2.1745738], [48.6964378, 2.1984815], [48.7070645, 2.1903309], [48.698824, 2.1898194], [48.6999391, 2.2153312], [48.6870401, 2.1679196], [48.6944506, 2.1644108], [48.6569806, 2.1999597], [48.557653, 2.1479962], [48.7071651, 2.1901921], [48.7036304, 2.1922985], [48.7034893, 2.1921828], [48.6989745, 2.1877606], [48.7060375, 2.1915345], [48.5577275, 2.1481734], [48.6784361, 2.1749219], [48.6787944, 2.174904], [48.6785255, 2.1747469], [48.5080618, 2.2079452], [48.6849061, 2.1879992], [48.612731, 2.1673899], [48.6126761, 2.167361], [48.6437709, 2.2285612], [48.6398814, 2.2446524], [48.6399929, 2.2450439], [48.6452284, 2.231682], [48.5840437, 2.2374575], [48.6399358, 2.244038], [48.642506, 2.2320202], [48.6920128, 2.2243689], [48.6788019, 2.1747349], [48.6683412, 2.1964748], [48.6683752, 2.196459], [48.691898, 2.159538], [48.6870048, 2.1675602], [48.6868307, 2.1676572], [48.6789998, 2.174564], [48.6784318, 2.1748856], [48.6989752, 2.1879939], [48.6990832, 2.1878882], [48.6989018, 2.1877985], [48.6847957, 2.1887378], [48.6841871, 2.2018689], [48.7060011, 2.1951865], [48.6840082, 2.2381466], [48.6838395, 2.2380996], [48.6837966, 2.2378528], [48.6838201, 2.237716], [48.6840222, 2.2379225], [48.6548156, 2.244572], [48.6546974, 2.2448359], [48.6547036, 2.2446683], [48.6893055, 2.2301003], [48.6892468, 2.2300796], [48.6992903, 2.2399981], [48.6793862, 2.2006816], [48.6801415, 2.2010977], [48.6802212, 2.2008569], [48.6793277, 2.2007966], [48.6848924, 2.1880649], [48.6848092, 2.187958], [48.5633881, 2.1914776], [48.5632917, 2.1918166], [48.563295, 2.1915939], [48.5634743, 2.1917959], [48.6944738, 2.1640315], [48.6944757, 2.1641097], [48.705179, 2.2146832], [48.705374, 2.2141173], [48.6858666, 2.2091659], [48.6857542, 2.2091756], [48.6821659, 2.1449367], [48.6819714, 2.1447839], [48.6888295, 2.154941], [48.6890384, 2.1551616], [48.6890284, 2.1548589], [48.6917071, 2.1593301], [48.6919302, 2.1592996], [48.694329, 2.1639772], [48.7070615, 2.1905484], [48.5649948, 2.1716604], [48.56488, 2.1717753], [48.7001823, 2.2176553], [48.7000876, 2.2176401], [48.7001624, 2.2175883], [48.6992028, 2.2397781], [48.6993, 2.2403493], [48.7006926, 2.1880403], [48.6984749, 2.2298116], [48.7064793, 2.2388467], [48.7066817, 2.2387017], [48.7068758, 2.2390759], [48.7068944, 2.2390434]]
#si pas de connexion voici les coords de feux rouges de la zone

#on souhaite pour un point GPS donnée déterminé la distance avec le feu rouge le plus proche, on considérera
# qu'il n'y a pas d'influence d'un feu rouge au delà de 100 mètres


def rad2deg(radians):     #fonction de conversion
    degrees = radians * 180 / pi
    return degrees

def deg2rad(degrees):
    radians = degrees * pi / 180
    return radians

def getDistanceBetweenPoints(latitude1, longitude1, latitude2, longitude2): #fonction pour obtenir la distance entre deux points dont on connaît la longitude et la latitude

    theta = longitude1 - longitude2

    distance = 60 * 1.1515 * rad2deg(
        arccos(
            (sin(deg2rad(latitude1)) * sin(deg2rad(latitude2))) +
            (cos(deg2rad(latitude1)) * cos(deg2rad(latitude2)) * cos(deg2rad(theta)))
        )
    )
    return (distance * 1.609344)*1000       #rendu de la donnée en mètre


def Feu_rouge_proche(coords, feux_rouges_zone):
    rayon_action=math.inf    #définition de du rayon autour de la position GPS afin de détécter un feu rouge, ici on prend toutes les distances
    distance_feu_rouge=rayon_action
    lat_gps=coords[0]
    long_gps=coords[1]

    for feu_rouge in feux_rouges_zone :      #on regarde pour chaque feu rouge de la zone si il est proche de la coordonnée GPS
        lat_fr=feu_rouge[0]
        long_fr=feu_rouge[1]
        distance = getDistanceBetweenPoints(lat_gps,long_gps,lat_fr,long_fr)
        if distance < distance_feu_rouge :       #On cherche le plus proche
            distance_feu_rouge=distance
    return distance_feu_rouge


def Feu_rouge_crossed(coords, feux_rouges_trajet):
    rayon_action=20   #définition de du rayon autour de la position GPS afin de détécter si un feu rouge est effectivmeent croisé, à réfinir, il ne faut pas passer à coté de feux
    lat_gps=coords[0]
    long_gps=coords[1]

    for feu_rouge in feux_rouges_zone :      #on regarde pour chaque feu rouge de la zone si il est au moins proche du rayon de la coord GPS
        lat_fr=feu_rouge[0]
        long_fr=feu_rouge[1]
        distance = getDistanceBetweenPoints(lat_gps,long_gps,lat_fr,long_fr)
        if distance < rayon_action :
            feux_rouges_trajet.append([lat_fr, long_fr])  #s'il est assez proche on peut l'ajouter au dataframe


def ajout_feux(Dataframe_trajet):

    traffic_crossed=[]      #ajout des feux rouges pour ce trajet précis
    route_Df=Dataframe_trajet[0]
    lat=route_Df['latitude']
    lon=route_Df['longitude']
    iteration=len(lat)
    for i in range(iteration):       #on calcule la distance par rapport au feu rouge à tous les feux rouges pour chaque point GPS et on garde celui qui est en dessous du rayon
        coords=[lat[i],lon[i]]
        Feu_rouge_crossed(coords, traffic_crossed)

    #maintenant on a les feux rouges présents sur le trajet, on souhaite donc récupérer pour chaque position, la distance par rapport au feu rouge le plus proche
    #et afficher si c'est avant ou après le feu rouge (distance négative signifie avant, distance positive signifie après)

    number=len(traffic_crossed)    #nombre de feux comptés sur le trajet
    distance_traffic=[]            #création de la liste comprenant les distances par rapport au feu le plus proche
    for i in range(iteration):
        coords=[lat[i],lon[i]]
        dist = Feu_rouge_proche(coords, traffic_crossed)
        distance_traffic.append(dist)

    dist0=distance_traffic[0]  #on souhaite maintenant regarder le sens de parcours des feux et donc donner une info en plus sur la distance
    pos_ref=-1
    distance_traffic[0]=-round(dist0, 2)

    for indice, dist1 in enumerate(distance_traffic[1:]):
        ecart=abs(dist1-dist0)      #cela permet de s'affranchir des bruits potentiels
        if ecart<8.5:
            pos=pos_ref
        elif dist0>=dist1:         #on compte négativement si on se rapproche d'un feu plus proche ou positivement si on s'éloigne d'un feu plus proche
            pos=-1                 #l'ajout de 4 permet de s'affranchir de certains problèmes de bruit
        elif dist0<=dist1:
            pos=1
        pos_ref=pos
        dist0=dist1
        dist1 = round(pos*dist1,2)
        distance_traffic[indice+1]=dist1  #on récupère une liste avec l'indication sur le sens, arrondi au centième

    return distance_traffic, traffic_crossed    #on récupère les distances et la liste des feux







