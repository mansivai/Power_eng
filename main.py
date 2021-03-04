import math 
import matplotlib.pyplot as plt  
UPF=[]
LAG = []
LEAD = []
I=[]

# TERMINAL VAOLTAGE VS LOAD CURRENT
for i in range(0,101,5):
	I.append(i)
	delta = math.asin( 0.0084*i)
	TV = (3**0.5)*((239.6*math.cos(delta)) - i*0.25)
	UPF.append(TV)
	delta1 = math.asin( 0.0066*i)
	TV1 = (3**0.5)*((239.6*math.cos(delta1)) + i*1.26)
	LAG.append(TV1)
	delta2 = math.asin( 0.0051*i)
	TV2 = (3**0.5)*((239.6*math.cos(delta2)) - i*0.133)
	LEAD.append(TV2)
plt.plot(I, UPF, color = 'red', marker = "o")  
plt.plot(I, LAG, color = 'green', marker = "x") 
plt.plot(I, LEAD, color = 'blue', marker = "+") 
plt.title("Terminal Voltage  vs load current")  
plt.xlabel("Load current")  
plt.ylabel("Terminal Voltage") 
plt.show()


# Voltage regulation

# for i in range(0,101,5):
# 	I.append(i)
# 	delta = math.asin( 0.0084*i)
# 	TV = (3**0.5)*((239.6*math.cos(delta)) - i*0.25)
# 	VF = ((415 - TV)/TV)*100
# 	UPF.append(VF)

# 	delta1 = math.asin( 0.0066*i)
# 	TV1 = (3**0.5)*((239.6*math.cos(delta1)) + i*1.26)
# 	VF1 = ((415 - TV1)/TV1)*100
# 	LAG.append(VF1)

# 	delta2 = math.asin( 0.0051*i)
# 	TV2 = (3**0.5)*((239.6*math.cos(delta2)) - i*0.133)
# 	VF2 = ((415 - TV2)/TV2)*100
# 	LEAD.append(VF2)
# plt.plot(I, UPF, color = 'red', marker = "o")  
# plt.plot(I, LAG, color = 'green', marker = "x")
# plt.plot(I, LEAD, color = 'blue', marker = "+") 
# plt.xlabel("Load current")
# plt.title("Voltage regulation vs load current")  
# plt.xlabel("Load current")  
# plt.ylabel("Voltage regulation")  
# plt.show()



# for i in range(0,100,5):
# 	I.append(i)
# 	delta1 = math.asin( 0.0066*i)
# 	TV1 = ((239.6*math.cos(delta1)) + i*1.26)
# 	POUT = 3*TV1*i*0.7
# 	eff = (POUT/(POUT + 5000))*100
# 	LAG.append(eff)
# plt.plot(I, LAG, color = 'green', marker = "x")
# plt.xlabel("Load current")  
# plt.title("Efficiency vs load current") 
# plt.ylabel("Efficiency")  
# plt.show()

