import matplotlib.pyplot as plt 
import numpy as np 



def Base(salary:int, mode = "yearly", span = 10):
    if mode == "yearly":
        X = np.linspace(0,span,span+1)
        base_deposit = X * salary
        # plt.plot(X,base_deposit)
    return X,base_deposit

def calculate(salary:int, span:int, rate:float, mode="yearly"):
    if mode == "yearly":
        X, base_deposit = Base(salary=salary,span=span,mode=mode)
        profit_deposit = np.empty_like(X)
        tmp=0;
        for x in np.nditer(profit_deposit,op_flags=['readwrite']):
            x[...]=tmp
            tmp=salary+(1+rate)*tmp
    return X, base_deposit, profit_deposit


plt.bar(X,profit,width=0.4,align='')
plt.bar(X,base,width=0.4,align='left')
plt.barbs()
figure = plt.figure(dpi=100,figsize=(10,6))
figure.subplot