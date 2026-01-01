print("Calculatrice simple")
operation=["+", "-", "*", "/"]

def calcul():
  while True:
      try:
       num1=float(input("entrez le premier nombre: "))
       num2=float(input("entrez le deuxième nombre: "))
      
      except ValueError:
        print("entrée non valide, veuillez entrer une opération valide")
        continue
      operation= input("entrer l'opération voulue: ")

      if operation == "+":
        print(f"{num1} + {num2}= {num1+num2}")
        
      elif operation == "-":
        print(f"{num1} - {num2}= {num1-num2}")

      elif operation == "*":
        print(f"{num1} * {num2}= {num1*num2}")
    
      elif operation == "/":
        if num2 ==0:
          print("erreur: division par zéro non permise")
          continue
        print(f"{num1} / {num2}= {num1/num2}")
    
      else:
          print("opération non valide")  
          continue
      

      
      rewind= input("voulez-vous réesssayer? (o/n):").lower()
      if rewind =="o":
       continue
      elif rewind !="o":
       print("au revoir!")
      break

  
calcul()
            
     
