import random
# Tehtävä1
print('Hello world!')

# Tehtävä2,3 
a = random.randint(0, 100)
b = random.randint(0, 100)

if a > b:
    print(f"{a} on suurempi kuin {b}")
elif b > a :
    print(f"{b} on suurempi kuin {a}")
    
else:
    print(f"{a} on yhtä suuri kuin {b}")
    

# Tehtävä4
c = random.randint(0, 11)
d = random.randint(0, 11)

def my_function(c, d):
  return c + d


print(f"lukujen {c} ja {d} summa on:",  my_function(c, d))

# Tehtävä5

def kertoLasku():
    print("Laske kertolaskut:")
    
    num = []
    num2 = []

    for x in range(5):
        satunnainenn_numero1 = random.randint(0, 10)
        satunnainenn_numero2 = random.randint(0, 10)
        num.append(satunnainenn_numero1)
        num2.append(satunnainenn_numero2)
        
    oikeaVastaus = []
    kVastaus = []

    for y in range(len(num)):
        
        tulo = num[y] * num2[y]
        oikeaVastaus.append(tulo)
      
        kVastaus = input(f"{num[y]} * {num2[y]} = ")
        if kVastaus.isdigit():
            kVastaus = int(kVastaus)
            if kVastaus == tulo:
                print(f"Oikein: {tulo}")
            else:
                print(f"Väärin: {tulo} ")
            
kertoLasku()


# Tehtävä7





   
        

            
     
        
        
        
        





       
       
      
   
   

    
    
    




    
    
    
    
    
    
  