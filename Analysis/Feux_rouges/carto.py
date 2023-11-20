import folium


def tracer_carte(Dataframe_trajet,num):
    route=Dataframe_trajet[0]
    ite=len(route['latitude'])
    lat_start=route['latitude'][0]
    lon_start=route['longitude'][0]
    lat_end=route['latitude'][ite-1]
    lon_end=route['longitude'][ite-1]

    center_map=[(lat_start+lat_end)/2,(lon_start+lon_end)/2]

    #Créer une carte centrée sur les coordonnées GPS indiquée
    carte= folium.Map(location=center_map,zoom_start=13)

    feux_rouges=Dataframe_trajet[14]   #feux_rouges concernés par le trajet

    feux_rouge_zone=[[48.6432999, 2.2277113], [48.6440138, 2.229054], [48.6867015, 2.1734666], [48.6848082, 2.1836103], [48.6844659, 2.1861026], [48.7006828, 2.1881442], [48.7002799, 2.188166], [48.6850638, 2.1863024], [48.7036758, 2.1927257], [48.7037897, 2.1924666], [48.7020258, 2.1735926], [48.6954158, 2.1764425], [48.6990236, 2.2082831], [48.6989478, 2.2031618], [48.6964973, 2.1554647], [48.7067205, 2.2105648], [48.704094, 2.2181155], [48.7035555, 2.2242576], [48.6533853, 2.2469109], [48.6716434, 2.2125916], [48.6794994, 2.2006153], [48.6860944, 2.2129053], [48.6755861, 2.2389974], [48.7029587, 2.2432553], [48.7008498, 2.2454688], [48.6891458, 2.2303165], [48.6972338, 2.246695], [48.6850348, 2.2392714], [48.6423356, 2.2329294], [48.6423749, 2.2328152], [48.7007565, 2.2455894], [48.6988143, 2.237854], [48.6987056, 2.2375258], [48.7007248, 2.2337515], [48.7027494, 2.2432614], [48.7013666, 2.2427162], [48.7094683, 2.2384], [48.704045, 2.2329923], [48.6883309, 2.206174], [48.7003171, 2.2209198], [48.6992729, 2.230792], [48.6985732, 2.2266978], [48.6986956, 2.2377046], [48.7097683, 2.2431145], [48.7095451, 2.2461899], [48.7084643, 2.2413054], [48.6839027, 2.2382657], [48.6986822, 2.235123], [48.7010957, 2.2436188], [48.7000001, 2.2140287], [48.6999463, 2.2155464], [48.6846977, 2.1940603], [48.6843441, 2.1995357], [48.6994161, 2.2247226], [48.7062346, 2.2112758], [48.7061499, 2.2107211], [48.5892762, 2.2452618], [48.5914698, 2.2443131], [48.5904803, 2.2447455], [48.6899519, 2.181429], [48.705406, 2.2143595], [48.5855446, 2.2417659], [48.5590052, 2.1553142], [48.7059828, 2.2053023], [48.7062283, 2.2047757], [48.6984906, 2.2302314], [48.7092824, 2.2461516], [48.7087966, 2.187312], [48.5802282, 2.2223227], [48.710671, 2.1589862], [48.6844059, 2.1881345], [48.6842871, 2.1885521], [48.6845491, 2.188873], [48.6963098, 2.1936362], [48.6451548, 2.2318329], [48.6785584, 2.1745738], [48.6964378, 2.1984815], [48.7070645, 2.1903309], [48.698824, 2.1898194], [48.6999391, 2.2153312], [48.6870401, 2.1679196], [48.6944506, 2.1644108], [48.6569806, 2.1999597], [48.557653, 2.1479962], [48.7071651, 2.1901921], [48.7036304, 2.1922985], [48.7034893, 2.1921828], [48.6989745, 2.1877606], [48.7060375, 2.1915345], [48.5577275, 2.1481734], [48.6784361, 2.1749219], [48.6787944, 2.174904], [48.6785255, 2.1747469], [48.5080618, 2.2079452], [48.6849061, 2.1879992], [48.612731, 2.1673899], [48.6126761, 2.167361], [48.6437709, 2.2285612], [48.6398814, 2.2446524], [48.6399929, 2.2450439], [48.6452284, 2.231682], [48.5840437, 2.2374575], [48.6399358, 2.244038], [48.642506, 2.2320202], [48.6920128, 2.2243689], [48.6788019, 2.1747349], [48.6683412, 2.1964748], [48.6683752, 2.196459], [48.691898, 2.159538], [48.6870048, 2.1675602], [48.6868307, 2.1676572], [48.6789998, 2.174564], [48.6784318, 2.1748856], [48.6989752, 2.1879939], [48.6990832, 2.1878882], [48.6989018, 2.1877985], [48.6847957, 2.1887378], [48.6841871, 2.2018689], [48.7060011, 2.1951865], [48.6840082, 2.2381466], [48.6838395, 2.2380996], [48.6837966, 2.2378528], [48.6838201, 2.237716], [48.6840222, 2.2379225], [48.6548156, 2.244572], [48.6546974, 2.2448359], [48.6547036, 2.2446683], [48.6893055, 2.2301003], [48.6892468, 2.2300796], [48.6992903, 2.2399981], [48.6793862, 2.2006816], [48.6801415, 2.2010977], [48.6802212, 2.2008569], [48.6793277, 2.2007966], [48.6848924, 2.1880649], [48.6848092, 2.187958], [48.5633881, 2.1914776], [48.5632917, 2.1918166], [48.563295, 2.1915939], [48.5634743, 2.1917959], [48.6944738, 2.1640315], [48.6944757, 2.1641097], [48.705179, 2.2146832], [48.705374, 2.2141173], [48.6858666, 2.2091659], [48.6857542, 2.2091756], [48.6821659, 2.1449367], [48.6819714, 2.1447839], [48.6888295, 2.154941], [48.6890384, 2.1551616], [48.6890284, 2.1548589], [48.6917071, 2.1593301], [48.6919302, 2.1592996], [48.694329, 2.1639772], [48.7070615, 2.1905484], [48.5649948, 2.1716604], [48.56488, 2.1717753], [48.7001823, 2.2176553], [48.7000876, 2.2176401], [48.7001624, 2.2175883], [48.6992028, 2.2397781], [48.6993, 2.2403493], [48.7006926, 2.1880403], [48.6984749, 2.2298116], [48.7064793, 2.2388467], [48.7066817, 2.2387017], [48.7068758, 2.2390759], [48.7068944, 2.2390434]]

    #on ajoute avec une couleur différente les feux sur la carte selon s'ils sont concernés par le trajet
    for feux in feux_rouge_zone:
        if feux in feux_rouges:
            folium.Marker(feux, popup = "feu rouge",icon=folium.Icon(color="green", icon="info-sign")).add_to(carte)
        else:
            folium.Marker(feux, popup = "feu rouge",icon=folium.Icon(color="red", icon="info-sign")).add_to(carte)

    #on trace chaque segment avec une couleur spécifique (selon le signe qui corrrespond à la position par rapport à un feu rouge, avant ou après)
    points_positive, points_negative= adjust_list_dist_to_trace(Dataframe_trajet)

    for list in points_positive:
        folium.PolyLine(list, color="blue", weight=2.5, opacity=0.8).add_to(carte)
    for list in points_negative:
        folium.PolyLine(list, color="red", weight=2.5, opacity=0.8).add_to(carte)

    #Sauvegarder cette carte dans un fichier HTML
    name=f'Carte_trajet{num}.html'
    carte.save(name)


#fonction qui met bien en forme la liste des distances afin de faciliter l'implémentation avec folium
def adjust_list_dist_to_trace(Dataframe_trajet):
    route_Df=Dataframe_trajet[0]
    lat=route_Df['latitude']
    lon=route_Df['longitude']

    iteration=len(lat)

    points_positive=[]
    points_negative=[]


    sign_ref='negative'
    new_list=[]

    for i in range(iteration):     #on décompose notre trajet selon les différentes parcelles (avant ou après le feu rouge)

        dist=route_Df['distance_traffic'][i]

        if dist>=0:
            sign='positive'
        else:
            sign='negative'

        if sign!=sign_ref:      #si on change de signe alors on crée une nouvelle liste
            if sign=='negative':
                points_positive.append(new_list)
            elif sign=='positive':
                points_negative.append(new_list)
            sign_ref=sign
            new_list=[]

        new_list.append([dist,i])

        if i==iteration-1:      #cas particulier pour le dernier élement
            if sign=='positive':
                points_positive.append(new_list)
            elif sign=='negative':
                points_negative.append(new_list)

    #récupération des coordonnées des points pour chaque distance :

    for k,list in enumerate(points_positive):
        for j, couple in enumerate(list):
            points_positive[k][j]=(lat[couple[1]],lon[couple[1]])

    for k,list in enumerate(points_negative):
        for j,couple in enumerate(list):
            points_negative[k][j]=(lat[couple[1]],lon[couple[1]])

    return points_positive, points_negative






