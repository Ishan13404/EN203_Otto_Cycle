import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



                                                           #COMPUTATIONAL_PART#
######################################################################################################################################

#Defining Some Important Functions to Carry Out Linear Regression
def bar (x) :
 sum = 0
 count = 0
 for i in x :
    sum = sum + i
    count = count + 1
 return sum/count

def avg_of_square(x):
 if len(x) == 0:
    return 0
 square_sum = sum(i ** 2 for i in x)
 count = len(x)
 average = square_sum / count
 return average

def xybar(y, x, index):
 count = 0
 xy = 0
 for i in range(len(y)):
    xy = xy + y[i+index] * x[i+index]
    count += 1
 return xy / count

##############################################################################

#Reading the specific parts of the given data set corresponding to the main otto cycle, complete otto cycle, expansion and compression
Complete_Otto_Cycle = pd.read_csv('Group_5.csv')
Main_Otto_Cycle = pd.read_csv('Group_5.csv')[250:613]
Expansion_Otto_Cycle = pd.read_csv('Group_5.csv')[383:540]
Actual_Expansion = pd.read_csv('Group_5.csv')[360:540]
Extra_Compression = pd.read_csv('Group_5.csv')[540:613]
Compression_Otto_Cycle = pd.read_csv('Group_5.csv')[180:360]
Compression_Otto_Cycle_Regression = pd.read_csv('Group_5.csv')[251:360]

Vvalues = [43.45, 280.57,  213.89, 30.5, 280.57, 30.5]
Pvalues = [2936.65, 215.8, 61.65, 1026.4, 37.7, 7339.21718]
PVIndexes = [383, 540, 251, 360, 180]

##############################################################################

#Finding the Polytropic Index for Expansion

xbar_expansion = bar (np.log(Expansion_Otto_Cycle['vol (cc)']))
ybar_expansion = bar (np.log(Expansion_Otto_Cycle['Avg p (kPa)']))
xybar_expansion = xybar(np.log(Expansion_Otto_Cycle['Avg p (kPa)']), np.log(Expansion_Otto_Cycle['vol (cc)']), 383)
xsqbar_expansion = avg_of_square(np.log(Expansion_Otto_Cycle['vol (cc)']))

a = (xybar_expansion - xbar_expansion*ybar_expansion)/(xsqbar_expansion - xbar_expansion*xbar_expansion)
a0 = (ybar_expansion*xsqbar_expansion - xybar_expansion*xbar_expansion)/(xsqbar_expansion - xbar_expansion*xbar_expansion)
m_AtoB_ = -1*a

##############################################################################

#Finding the Polytropic Index for Compression

xbar_compression = bar (np.log(Compression_Otto_Cycle_Regression['vol (cc)']))
ybar_compression = bar (np.log(Compression_Otto_Cycle_Regression['Avg p (kPa)']))
xybar_compression = xybar(np.log(Compression_Otto_Cycle_Regression['Avg p (kPa)'])
                          , np.log(Compression_Otto_Cycle_Regression['vol (cc)']), 251)
xsqbar_compression = avg_of_square(np.log(Compression_Otto_Cycle_Regression['vol (cc)']))

b = (xybar_compression - xbar_compression*ybar_compression)/(xsqbar_compression - xbar_compression*xbar_compression)
b0 = (ybar_compression*xsqbar_compression - xybar_compression*xbar_compression)/(xsqbar_compression - xbar_compression*xbar_compression)
m_CtoD_ = -1*b

###############################################################################
# Calculating the work of Complete Cycle, Expansion and Compression by calculating area under the curve

area = 0.0
for i in range(len(Main_Otto_Cycle)-1):
    x1 = Main_Otto_Cycle['vol (cc)'][i+250]
    x2 = Main_Otto_Cycle['vol (cc)'][i+251]
    y1 = Main_Otto_Cycle['Avg p (kPa)'][i+250]
    y2 = Main_Otto_Cycle['Avg p (kPa)'][i+251]

    #print(x1, x2, y1, y2, ((x2-x1)*(y1+y2)*0.5))
    area += ((x2-x1)*(y1+y2)*0.5)  #Here, x2-x1 = dx = dV and (y1+y2)/2 = y = P

#Calculating the area of expansion
area_expansion = 0.0
for i in range(len(Expansion_Otto_Cycle)-1):
    x1 = Expansion_Otto_Cycle['vol (cc)'][i+383]
    x2 = Expansion_Otto_Cycle['vol (cc)'][i+384]
    y1 = Expansion_Otto_Cycle['Avg p (kPa)'][i+383]
    y2 = Expansion_Otto_Cycle['Avg p (kPa)'][i+384]

    # print(x1, x2, y1, y2, ((x2-x1)*(y1+y2)*0.5))
    area_expansion += ((x2-x1)*(y1+y2)*0.5)  #Here, x2-x1 = dx = dV and (y1+y2)/2 = y = P

#Calculating the area of compression
area_compression = 0.0
for i in range(len(Compression_Otto_Cycle_Regression)-1):
    x1 = Compression_Otto_Cycle['vol (cc)'][i+251]
    x2 = Compression_Otto_Cycle['vol (cc)'][i+252]
    y1 = Compression_Otto_Cycle['Avg p (kPa)'][i+251]
    y2 = Compression_Otto_Cycle['Avg p (kPa)'][i+252]

    # print(x1, x2, y1, y2, ((x2-x1)*(y1+y2)*0.5))
    area_compression += ((x2-x1)*(y1+y2)*0.5)  #Here, x2-x1 = dx = dV and (y1+y2)/2 = y = P

#Calculating the actual area of expansion
area_actual_expansion = 0.0
for i in range(len(Actual_Expansion)-1):
    x1 = Actual_Expansion['vol (cc)'][i+360]
    x2 = Actual_Expansion['vol (cc)'][i+361]
    y1 = Actual_Expansion['Avg p (kPa)'][i+360]
    y2 = Actual_Expansion['Avg p (kPa)'][i+361]

    # print(x1, x2, y1, y2, ((x2-x1)*(y1+y2)*0.5))
    area_actual_expansion += ((x2-x1)*(y1+y2)*0.5)  #Here, x2-x1 = dx = dV and (y1+y2)/2 = y = P

#Calculating the actual area of compression
area_extra_compression = 0.0
for i in range(len(Extra_Compression)-1):
    x1 = Extra_Compression['vol (cc)'][i+540]
    x2 = Extra_Compression['vol (cc)'][i+541]
    y1 = Extra_Compression['Avg p (kPa)'][i+540]
    y2 = Extra_Compression['Avg p (kPa)'][i+541]

    # print(x1, x2, y1, y2, ((x2-x1)*(y1+y2)*0.5))
    area_extra_compression += ((x2-x1)*(y1+y2)*0.5)  #Here, x2-x1 = dx = dV and (y1+y2)/2 = y = P

area_actual_compression = area_compression + area_extra_compression

print('\nWork Done during adiabatic compression from C to D (By area under the curve) =', round(area_compression/1000, 2), 'Joules')
print('Work Done during adiabatic expansion from A to B (By area under the curve) =', round(area_expansion/1000, 2), 'Joules')
print('Work Done during actual expansion by considering the expansion from D to A as well (By area under the curve) =',
      round(area_actual_expansion/1000, 2), 'Joules')
print('Work Done during actual compression by considering the compression from B to C as well (By area under the curve) =',
      round(area_actual_compression/1000, 2), 'Joules')
print('Total Work Done (By area under the curve) =', round(area/1000, 2), 'Joules')
print('Total Work Done in expansion and compression by not considering work in D to A and B to C (By area under the curve) ='
      , round((area_expansion + area_compression)/1000, 2), 'Joules') 

                     #ROUGH_WORK#
#########################################################
'''m_AtoB = (np.log(Pvalues[1])-np.log(Pvalues[0])) / \ #
    (np.log(Vvalues[1])-np.log(Vvalues[0]))             #
m_CtoD = (np.log(Pvalues[3])-np.log(Pvalues[4])) / \    #
    (np.log(Vvalues[3])-np.log(Vvalues[4]))'''          #
                                                        #
'''print('Slope of process A-B:', round(m_AtoB, 2))     #
print('Slope of process C-B:', round(m_CtoD, 2))'''     #
##################################################################################################

#Calculating the work done in expansion and compression by using the polytropic indices calculated
print('\nPolytropic Index of Expansion using Regression:', m_AtoB_)
print('Polytropic Index of Compression using Regression:', m_CtoD_)
Work_AtoB = (np.exp(a0 + a*np.log(Vvalues[1]))*Vvalues[1]-np.exp(a0+a*np.log(30.5))*30.5)/(1-m_AtoB_)
Work_CtoD = (np.exp(b0 + b*np.log(Vvalues[3]))*Vvalues[3]-np.exp(b0 + b*np.log(Vvalues[4]))*Vvalues[4])/(1-m_CtoD_)
print('\nWork Done during compression from E to D (By Formula) =', round(Work_CtoD/1000, 2) ,'Joules')
print('Work Done during expansion from F to B (By Formula) =', round(Work_AtoB/1000, 2) ,'Joules')
print('Total Work Done (By formula) =', round(
    (Work_AtoB+Work_CtoD)/1000, 2), 'Joules')
print('\nError in the work done in the ideal case and that in the actual case ='
      , (-area + Work_AtoB + Work_CtoD)*100/(Work_AtoB + Work_CtoD), '%')

###################################################################################################

#Calculating the IMEP for Expansion and Compression
Displacement_Volume = Vvalues[4] - Vvalues[3]
IMEP_Compression = -area_actual_compression/Displacement_Volume
print('\nIMEP for compression process is', IMEP_Compression, 'kPa')
IMEP_Expansion = area_actual_expansion/Displacement_Volume
print('IMEP for expansion process is', IMEP_Expansion, 'kPa')


####################################################################################################






                                                       #PLOTTING_PART#
######################################################################################################################################
V_AtoB = np.linspace(
    Complete_Otto_Cycle['vol (cc)'][PVIndexes[3]], Complete_Otto_Cycle['vol (cc)'][PVIndexes[1]], 10000)
P_AtoB = Pvalues[0]*pow((Vvalues[0]/V_AtoB),m_AtoB_)

P_BtoC = np.linspace(
    Complete_Otto_Cycle['Avg p (kPa)'][PVIndexes[1]], Complete_Otto_Cycle['Avg p (kPa)'][PVIndexes[4]], 10000)
V_BtoC = (Vvalues[1]+Vvalues[1])*0.5*P_BtoC/P_BtoC

V_CtoD = np.linspace(
    Complete_Otto_Cycle['vol (cc)'][PVIndexes[4]], Complete_Otto_Cycle['vol (cc)'][PVIndexes[3]], 10000)
P_CtoD = Pvalues[4]*((Vvalues[4]/V_CtoD)**(m_CtoD_))

P_DtoA = np.linspace(
    Complete_Otto_Cycle['Avg p (kPa)'][PVIndexes[3]], np.exp(a0 + a*np.log(30.5)), 10000)
V_DtoA = (Vvalues[3]+Vvalues[3])*0.5*P_DtoA/P_DtoA

######################################################################################
point_names = ['A', 'B', 'C', 'D','E','F']
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

ax1.plot(Complete_Otto_Cycle['vol (cc)'], Complete_Otto_Cycle['Avg p (kPa)'])
ax1.plot(Main_Otto_Cycle['vol (cc)'], Main_Otto_Cycle['Avg p (kPa)'])
ax1.scatter(Vvalues, Pvalues, c=['brown', 'green', 'black', 'purple', 'blue', 'magenta'], label='Data Points', s=100)
ax1.set_title('PV Curve of Otto Cycle from the given data')
ax1.plot(V_AtoB, np.exp(a0 + a*np.log(V_AtoB)), 'r--')
ax1.plot(V_BtoC, P_BtoC, 'r--')
ax1.plot(V_CtoD, np.exp(b0 + b*np.log(V_CtoD)), 'r--')
ax1.plot(V_DtoA, P_DtoA, 'r--')

ax1.scatter(Vvalues, Pvalues, c=['brown', 'green', 'black', 'purple', 'blue', 'magenta'], label='Data Points', s=100)

ax1.legend(['Otto Cycle including Inlet and Exhaust',
           'Otto Cycle excluding Inlet and Exhaust', 'Constructed Curve'])
ax1.set_xlabel('Volume (in cc)')
ax1.set_ylabel('Pressure (in kPa)')

###############################

ax2.plot(np.log(Complete_Otto_Cycle['vol (cc)']), np.log(
    Complete_Otto_Cycle['Avg p (kPa)']))
ax2.plot(np.log(Main_Otto_Cycle['vol (cc)']),
         np.log(Main_Otto_Cycle['Avg p (kPa)']))
ax2.plot(np.log(V_AtoB), a0 + a*np.log(V_AtoB), 'r--')
ax2.plot(np.log(V_BtoC), np.log(P_BtoC), 'r--')
ax2.plot(np.log(V_CtoD), b0 + b*np.log(V_CtoD), 'r--')
ax2.plot(np.log(V_DtoA), np.log(P_DtoA), 'r--')
ax2.scatter(np.log(Vvalues), np.log(Pvalues), c=['brown', 'green', 'black', 'purple','blue','magenta'], label='Data Points', s=100)
ax2.set_title('LogP-LogV Curve of Otto Cycle from the given data')
ax2.legend(['Otto Cycle including Inlet and Exhaust',
           'Otto Cycle excluding Inlet and Exhaust', 'Constructed Curve'])
ax2.set_xlabel('LogV')
ax2.set_ylabel('LogP')

##########################################

# add annotations for each point
for i, j, name, color in zip(Vvalues, Pvalues, point_names, ['brown', 'green', 'black', 'purple','blue','magenta']):
    ax1.annotate('{} ({:.2f}, {:.2f})'.format(name, i, j), xy=(i, j),
                 textcoords='offset points', xytext=(0, 10), ha='center', color=color)
    ax2.annotate('{} ({:.2f}, {:.2f})'.format(name, np.log(i), np.log(j)), xy=(np.log(i), np.log(j)),
                 textcoords='offset points', xytext=(0, 10), ha='center', color=color)


plt.show()
