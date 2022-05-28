#Pizzeria

#creating a class Pizzeria
class Pizzeria:
  #total amount counter
  total_amt=0
  total_qty=0
  qty_pizza=0
  qty_pasta=0
  pizza_amount=0
  pasta_amount=0
  free_colddrink=0
  bruschetta=0
  chocco_brownies=0

  def menu():
    food_menu="""
1 large pizza = 10.99 AUD 

2 large Pizzas = 20.99 AUD 

3 Large Pizzas = 29.99 AUD

***Buy 4 or more pizza and get 1.5lt of soft drink free***


1 large pasta = 9.5 AUD 

2 large pastas = 17.00 AUD 

3 large pastas = 27.50 AUD

***Buy 4 or more pastas and get 2 bruschetta free.***

***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free.
-----------------------------------------------------
"""
    print(food_menu)

  #this is billing function
  def c_bill(self):
    #individual customer amount counter is c_amount
    c_amount=0
    #Asking user for customer's name
    c_name=input("\nEnter Your Name:- ")
    print("\nWelcome, ",c_name)

    #Asking to user for buying qty of pizza
    input_pizza=int(input("\nEnter number or pizza order you want : "))
    if input_pizza==1:
      print("\tYour pizza order amount is : ",10.99,"AUD\n")
      pizza_amt=10.99
      self.qty_pizza+=1
      self.total_qty+=1
      self.pizza_amount+=10.99
    elif input_pizza==2:
      print("\tYour pizza order amount is : ",20.99,"AUD\n")
      pizza_amt=20.99
      self.qty_pizza+=2
      self.total_qty+=2
      self.pizza_amount+=20.99
    elif input_pizza==3:
      print("\tYour pizza order amount is : ",29.99,"AUD\n")
      pizza_amt=29.99
      self.qty_pizza+=3
      self.total_qty+=3
      self.pizza_amount+=29.99
    elif input_pizza>=4:
      pizza_amt=10.99*input_pizza
      self.qty_pizza+=input_pizza
      self.total_qty+=input_pizza
      self.pizza_amount+=pizza_amt
      self.free_colddrink+=1
      print("\t\t*** Congratulations !! 1.5lt softdrink free ***")
      print("\tYour pizza order amount is : ",float(pizza_amt),"AUD\n")
    else:
      print("\nEnter invalid input...!")

    c_amount+=pizza_amt
      
    #Asking to user for buying qty of pasta
    input_pasta=int(input("\nEnter number or pasta order you want : "))
    if input_pasta==1:
      print("\tYour pizza order amount is : ",9.50,"AUD\n")
      pasta_amt=9.50
      self.qty_pasta+=1
      self.total_qty+=1
      self.pasta_amount+=9.5
    elif input_pasta==2:
      print("\tYour pizza order amount is : ",17.00,"AUD\n")
      pasta_amt=17.00
      self.qty_pasta+=2
      self.total_qty+=2
      self.pasta_amount+=17.00
    elif input_pasta==3:
      print("\tYour pizza order amount is : ",27.50,"AUD\n")
      pasta_amt=27.50
      self.qty_pasta+=3
      self.total_qty+=3
      self.pasta_amount+=27.50
    elif input_pasta>=4:
      pasta_amt=9.5*input_pasta
      self.qty_pasta+=input_pasta
      self.total_qty+=input_pasta
      self.pasta_amount+=pasta_amt
      self.bruschetta+=2
      #self.chocco_brownies+=2
      print("\t\t*** Congratulations !! get 2 bruschetta free ***\n")
      #print("\t\t*** Congratulations !! get 2 chocco brownies ice cream free ***\n")
      print("\tYour pasta order amount is : ","{:.2f}".format(pasta_amt),"AUD\n")
    else:
      print("\nEnter invalid input...!")

    #this if condition for only customer's who ordered 4 or mor pizza and also 4 or mor pasta.
    if input_pizza>=4 and input_pasta>=4:
      self.chocco_brownies+=2
      print("\t\t*** Congratulations !! get 2 chocco brownies ice cream free ***\n")
    
    #increamented individual customer's amount by pasta_amt
    c_amount+=pasta_amt
    print("your billing amount is, ","{:.2f}".format(c_amount),"AUD.")

    #total_amt increamented by individual customer's amount
    self.total_amt+=c_amount
    print("\n\n-----> your Net order amount of the day is : ","{:.2f}".format(self.total_amt),"AUD.")

    user_input=input("\nis there any customer else\n(type 'y' or 'Y' to new Customer) OR (type any button instead of 'y' or 'Y' to Exit.) :- ")

    if user_input.startswith("y") or user_input.startswith("Y"):
      print("Okay..., Give Detials...!")
      client.c_bill()
    else:
      print("\n----------- Pizza and pasta Bill --------------")
      print("payment received from pizza :","{:.2f}".format(self.pizza_amount),"AUD.")
      print("payment received from pasta :","{:.2f}".format(self.pasta_amount),"AUD.")
      print("payment received today :","{:.2f}".format(self.total_amt),"AUD.")
      print("Number of pizza and pasta sold in one shift :",self.qty_pizza+self.qty_pasta)
      print("Number of 1.5lt soft drink bottles given :",self.free_colddrink)
      print("Number of bruschetta given to customer :",self.bruschetta)
      print("Number of chocco brownies ice cream given to customer :",self.chocco_brownies)
      print("\nGood Bye....!")



client=Pizzeria()
def start():
  print("\nPress 1 for Order Menu\nPress 2 for Exit")
  opt=int(input("\nChoose Option from above:- "))

  if opt==1:
        #if user opted 1 menu is Showing
        Pizzeria.menu()
        #Calling billing function after showing menu
        client.c_bill()

  elif opt==2:
    pass
  else:
    print("\ninvalid input...!")
    

start()
