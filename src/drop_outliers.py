import pandas as pd

def drop_outliers(tabla, columna, umbral=1.5):
    q1 = tabla[columna].quantile(0.25) #Primer cuartil
    q3 = tabla[columna].quantile(0.75) #Tercer cuartil
    iqr = q3-q1 #Rango intercuartílico
    lim_inf = q1 - (umbral*iqr) #limite inferior ==> Todo valor que esté por debajo es un outlier
    lim_sup = q3 + (umbral*iqr) #limite superior ==> Todo valor que esté por encima es un outlier
    outliers = tabla[(tabla[columna]<lim_inf)|(tabla[columna]>lim_sup)] #Registros que son outliers
    tabla.drop(outliers.index.to_list(), axis=0, inplace=True) #Borramos outliers
    tabla.reset_index(drop=True, inplace=True) #Reseteamos los índices de la tabla