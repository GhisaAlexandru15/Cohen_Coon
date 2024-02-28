import numpy as np

class Stationar:
    #împart y în mai multe secțiuni și calculez empn pe fiecare
    #dacă e sub o anumită valoare regiunea e staționară
    def metoda2(vector):
        eroare=0.003
        eroare2=0.25
        medie=[]
        zonaStationara=[]
        sampleSize=len(vector)//15
        for i in range(0, len(vector)//sampleSize):
            medie.append(np.mean(vector[i*sampleSize:i*sampleSize+sampleSize]))
        derivata=np.zeros(len(medie))
        for i in range(0, len(medie)):
            medie[i]=Erori.empn0(vector[i*sampleSize:i*sampleSize+sampleSize], max(vector)-min(vector))
            derivata[i]=Stationar.derivata(vector[i*sampleSize:i*sampleSize+sampleSize], max(vector)-min(vector))
            if medie[i]<eroare and derivata[i]<eroare2:
                zonaStationara.append((i*sampleSize,i*sampleSize+sampleSize))
        return zonaStationara

    #calculez valorile de minim/maxim pe ficare interval staționar    
    def valoriStationare(vs,vector):
        maxim=[]
        minim=[]
        medie=np.mean(vector)
        for interval in vs:
            if(np.mean(vector[interval[0]:interval[1]])>medie):
                maxim.append(np.mean(vector[interval[0]:interval[1]]))
            else:
                minim.append(np.mean(vector[interval[0]:interval[1]]))
        if(len(maxim)):
            return (np.mean(minim),np.mean(maxim))
        else: 
            return (np.mean(minim), None)
        
    #extind zona staționară +-10%
    def zonaStationara(vector, v0):
        vmin=[]
        k=1
        procent=10/100
        for i in range(0, len(vector)):
            if(vector[i]>(1-procent)*v0 and vector[i]<(1+procent)*v0 or (vector[i]<(1-procent)*v0 and vector[i]>(1+procent)*v0)):
                k+=1
            else:
                if k>20:
                    vmin.append((i-k+1, i))
                k=0
        if k>20:
            vmin.append((i-k+1, i))
        for i in range(1,len(vmin)):
            if(vmin[i][0]-vmin[i-1][1]<10):
                del vmin[i-1]
        return vmin
    
    #calculez dacă o zonă care pare staționară nu are o pantă
    def derivata(vector,amplitudine):
        sum=0
        for i in range(0, len(vector)//2):
            sum+=(vector[i+len(vector)//2]-vector[i])
        return abs(sum/amplitudine)

class Erori:
    #eroare pătratică
    def empn0(vector, amplitudine):
        sum=0
        medie=np.mean(vector)
        for i in range(0, len(vector)):
            sum+=(vector[i]-medie)**2
        return abs(sum/amplitudine/len(vector))
    
class Semnal:
    #analizez doar o perioada din semnal
    def perioada(vector):
        for k in range(len(vector)//10, 9*len(vector)//10):
            sum=0
            for i in range(0, len(vector)-k):
                sum+=(vector[i]-vector[i+k])**2
            sum=sum/abs(max(vector)-min(vector))
            if sum<1:
                return int(1.1*k)    
class Timp:
    #timp front cazator, timp front crescator, timp de raspuns
    def timp(u0_, ust_, yst_):
        tx=[]
        tx.append(ust_[0][1])
        tx.append(u0_[0][1])
        for i in yst_:
            if(i[0]>tx[1]):
                tx.append(i[0])
                break
        return tx
