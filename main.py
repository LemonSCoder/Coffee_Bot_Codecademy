#sys is imported in order to terminate the loop later with sys.exit().
import sys
from utils import print_message, get_size, order_latte, extra_toppings
def coffee_bot():
  print('Welcome to the cafe!')
  #These responses aren't necessary to complete the project
  positive_responses = ["yes", "sure", "good", "yee", "y", "ye"]
  negative_responses = ["no", 'n', "nah"]
  exit_words = ["stop", "bye"]
  order_drink = 'y'
  drinks = []
  while order_drink != 'n':
    size = get_size()  
    drink_type = get_drink_type()
    toppings = extra_toppings()
    drink = '{} {} with {}'.format(size, drink_type, toppings)
    #Append the drink ordered after drink is declared.
    drinks.append(drink)
    print('Alright, that\'s a {}!'.format(drink))
    order_drink = input("Would you like to order another drink? (y/n) \n>")
    #I wanted to minimalize the amount of code needed to check if the response is 'yes' or 'no' to order another drink, so I used a loop to check. Again, this part of the code is not necessary.
    for word in positive_responses:
      if word == order_drink:
        order_drink = 'y'
    for word in negative_responses:
      if word == order_drink:
        order_drink = 'n'
    for word in exit_words:
      if word == order_drink:
        #Terminates the code
        sys.exit("TERMINATED")
    if order_drink != 'y' or order_drink != 'n':
        print_message()
  print("Okay, so I have:")
  for drink in drinks:
    print("A " + drink)
  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your order will be ready shortly.'.format(name))

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n[d] Frappuccino \n> ')

  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  #frappuccino was added
  elif res == 'd':
    return 'frappuccino'
  else:
    print_message()
    return get_drink_type()
  
# Define new functions here!
def order_mocha():
  res=input("Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n>")
  while res == True:
    if res == 'a':
      return 'peppermint mocha'
    elif res == 'b':
      return 'mocha'
    else:
      return print_message()
order_mocha()
coffee_bot()