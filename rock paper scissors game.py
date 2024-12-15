import random

ifadeler=["Taş","Kağıt","Makas"]
ifadeseçme=random.choice(ifadeler)

 
while True:
        oyuncu_ifadesi=input("Taş, Kağıt veya Makas girin: ")
        print("Yapay Zeka Tarafından Seçilen İfade:", ifadeseçme)
            

        if ifadeseçme=="Taş" and oyuncu_ifadesi=="Taş":
            print("Berabere!")
           


        if ifadeseçme=="Kağıt" and oyuncu_ifadesi=="Kağıt":
            print("Berabere!") 
             

        if ifadeseçme=="Makas" and oyuncu_ifadesi=="Makas":
            print("Berabere!")   
            

        if ifadeseçme=="Taş" and oyuncu_ifadesi=="Kağıt"  :
            print("Yapay Zeka Yendi")
            

        if ifadeseçme=="Taş" and oyuncu_ifadesi=="Makas":
            print("Oyuncu Yendi") 
              

        if ifadeseçme=="Kağıt" and oyuncu_ifadesi=="Taş":
            print("Yapaz Zeka Yendi")  
             

        if ifadeseçme=="Kağıt" and oyuncu_ifadesi=="Makas":
            print("Oyuncu yendi")  
             

        if ifadeseçme=="Makas" and oyuncu_ifadesi=="Taş":
            print("Oyuncu Yendi")    
           
            
        if ifadeseçme=="Makas" and oyuncu_ifadesi=="Kağıt":
            print("Yapaz Zeka Yendi")
             
        

        
