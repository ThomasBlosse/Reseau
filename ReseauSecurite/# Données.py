# Données
x = [11.3, 11.3, 11.0, 10.8, 11.4, 11.0, 10.8, 11.3, 11.1, 11.6, 11.4]
y = [11.1, 10.9, 11.3, 10.9, 11.0, 10.9, 11.1, 10.8, 11.2, 11.0]

# Calcul des moyennes
x_mean = sum(x) / len(x)
y_mean = sum(y) / len(y)

# Calcul de la somme des carrés des écarts
x_carre = sum((i - x_mean)**2 for i in x)
y_carre = sum((i - y_mean)**2 for i in y)

# Calcul des écarts types
ecart_x = (x_carre / (len(x) )) ** 0.5
ecart_y = (y_carre / (len(y) )) ** 0.5

# Calcul de la covariance
covariance = sum((x[i]*y[i]) - (x_mean * y_mean) for i in range(len(x))) / (len(x))

# Calcul du taux de corrélation
correlation = covariance / (ecart_x * ecart_y)

# Affichage des résultats
print(f"moyenne de x : {x_mean}")
print(f"moyenne de y : {y_mean}")
print(len(x))
print("Écart type de x :", ecart_x)
print("Écart type de y :", ecart_y)
print("Covariance :", covariance)
print("Taux de corrélation :", correlation)
