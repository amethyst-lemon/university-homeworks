import numpy as np
import matplotlib.pyplot as plot
import pandas as pd
import statistics as st

xls = pd.ExcelFile("autodati.xls")
df1 = pd.read_excel(xls, "Sheet1", usecols=['Gads', 'Automašīnu skaits uz 1 000 iedzīvotājiem'])
df2 = pd.read_excel(xls, "Sheet2", usecols=['Gads', 'Ceļu satiksmes negadījumi'])


#statistika 1 - par automašīnu skaitu
statistics1 = df1['Automašīnu skaits uz 1 000 iedzīvotājiem'].describe(include='all')
print("Aprakstošā statistika par automašīnu skaitu")
print(statistics1)
print(' ')

#average / videjais aritmetiskais
vidart1 = df1['Automašīnu skaits uz 1 000 iedzīvotājiem'].mean()
print('Vidējais aritmētiskais: ' + str(vidart1))
print(' ')

#moda
moda1 = df1['Automašīnu skaits uz 1 000 iedzīvotājiem'].mode()
print('Moda: ' + str(moda1))
print(' ')

#median / mediana
mediana1 = df1['Automašīnu skaits uz 1 000 iedzīvotājiem'].median()
print('Mediāna: ' + str(mediana1))
print(' ')

#range / amplitūda
ampl1 = df1.max()-df1.min()
print('Amplitūda:' + str(ampl1))
print(' ')

#variance / dispersija
variance1 = df1['Automašīnu skaits uz 1 000 iedzīvotājiem'].var()
print('Dispersija: ' + str(variance1))
print(' ')

#standard deviation / Standartnovirze
start1 = df1['Automašīnu skaits uz 1 000 iedzīvotājiem'].std()
print('Standartnovirze: ' + str(start1))
print(' ')

#skew / Asimetrijas koeficients
asik1 = df1['Automašīnu skaits uz 1 000 iedzīvotājiem'].skew()
print('Asimetrijas koeficients: ' + str(asik1))
print(' ')

#kurtosis / Ekscesa koeficients
ekstkoe1 = df1['Automašīnu skaits uz 1 000 iedzīvotājiem'].kurt()
print('Ekscesa koeficients: ' + str(ekstkoe1))
print(' ')


#statistika 2 - par ceļu satiksmes negadījumiem
statistics2 = df2['Ceļu satiksmes negadījumi'].describe(include='all')
print("Aprakstošā statistika par ceļu satiksmes negadījumi")
print(statistics1)
print(' ')

#average / videjais aritmetiskais
vidart2 = df2['Ceļu satiksmes negadījumi'].mean()
print('Vidējais aritmētiskais: ' + str(vidart2))
print(' ')

#moda
moda2 = df2['Ceļu satiksmes negadījumi'].mode()
print('Moda: ' + str(moda2))
print(' ')

#median / mediana
mediana2 = df2['Ceļu satiksmes negadījumi'].median()
print('Mediāna: ' + str(mediana2))
print(' ')

#range / amplitūda
ampl2 = df2.max()-df2.min()
print('Amplitūda:' + str(ampl2))
print(' ')

#variance / dispersija
variance2 = df2['Ceļu satiksmes negadījumi'].var()
print('Dispersija: ' + str(variance2))
print(' ')

#standard deviation / Standartnovirze
start2 = df2['Ceļu satiksmes negadījumi'].std()
print('Standartnovirze: ' + str(start2))
print(' ')

#skew / Asimetrijas koeficients
asik2 = df2['Ceļu satiksmes negadījumi'].skew()
print('Asimetrijas koeficients: ' + str(asik2))
print(' ')

#kurtosis / Ekscesa koeficients
ekstkoe2 = df2['Ceļu satiksmes negadījumi'].kurt()
print('Ekscesa koeficients: ' + str(ekstkoe2))
print(' ')

def corr(df1, df2):
    n = len(df1)
    v1, v2 = df1.values, df2.values
    sums = np.multiply.outer(v2.sum(0), v1.sum(0))
    stds = np.multiply.outer(v2.std(0), v1.std(0))
    return pd.DataFrame((v2.T.dot(v1) - sums / n) / stds / n,
                        df2.columns, df1.columns)

#korelācijas koeficients
kor = corr(df1, df2)
print('Korelācijas koeficients' + str(kor))
print(' ')


#diagrammas kaste ar ūsa 
a_plot = df1.boxplot(column='Automašīnu skaits uz 1 000 iedzīvotājiem')
a_plot.plot()
plot.show()

b_plot = df2.boxplot(column='Ceļu satiksmes negadījumi')
b_plot.plot()
plot.show()

#diagrammas punktveida
c_plot = df1.plot.scatter(x = 'Gads', y = 'Automašīnu skaits uz 1 000 iedzīvotājiem')
c_plot.plot()
plot.show()

d_plot = df2.plot.scatter(x = 'Gads', y = 'Ceļu satiksmes negadījumi')
d_plot.plot()
plot.show()