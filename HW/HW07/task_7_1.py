# Написать 12 функций по переводу:

# Дюймы в сантиметры
def InchToCentimetr(inch):
    centimetr = inch * 2.54
    return(centimetr)

# Сантиметры в дюймы
def CentimetrToInch(centimetr):
    inch = centimetr * 0.393701
    return(inch)

# Мили в километры
def MileToKilometer(mile):
    kilometer = mile * 0.621371
    return(kilometer)

# Километры в мили
def KilometerToMile(kilometer):
    mile = kilometer * 1.60934
    return(mile)

# Фунты в килограммы
def PoundToKilogram(pound):
    kilogram = pound * 0.453592
    return(kilogram)

# Килограммы в фунты
def KilogramToPound(kilogram):
    pound = kilogram * 2.20462
    return(pound)

# Унции в граммы
def OunceToGram(ounce):
    gram = ounce * 28.3495
    return(gram)

# Граммы в унции
def GramToOunce(gram):
    ounce = gram * 0.03574
    return(ounce)

# Галлон в литры
def GallonToLiter(gallon):
    liter = gallon * 3.78541
    return(liter)

# Литры в галлоны
def LiterToGallon(liter):
    gallon = liter / 3.78541
    return(gallon)

# Пинты в литры
def PintToLiter(pint):
    liter = pint * 0.473176
    return(liter)

# Литры в пинты
def LiterToPint(liter):
    pint = liter / 0.473176
    return(pint)