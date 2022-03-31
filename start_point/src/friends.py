# 1. For a given person, return their name
from optparse import AmbiguousOptionError


def get_name (person):
    return (person["name"])

# 2. For a given person, return their favourite tv show
  # (e.g. the function favourite_tv_show(self.person2) should return the string "Baywatch")
def get_favourite_tv_show (person):
    return (person["favourites"]["tv_show"])

# 3. For a given person, check if they like a particular food
  # (e.g. the function likes_to_eat(self.person2, "bread") should return True, likes_to_eat(self.person3, "spinach") should return False)
def likes_to_eat(person, food):
    snacks = person["favourites"]["snacks"]
    for snack in snacks:
        if snack == food:
            return True
    return False

 # 4. For a given person, add a new name to their list of friends
  # (e.g. the function add_friend(self.person2, "Scrappy-Doo") should add Scrappy-Doo to the friends.)
  # (hint: This function should not return anything. After the function call, check for the length of the friends array to test it!)

def add_friend(person, pals):
      person ["friends"].append(pals)
      return len(person["friends"])

# 5. For a given person, remove a specific name from their list of friends
  # (hint: Same as above, testing for the length of the array should be sufficient)

def remove_friend(person, pals):
      person ["friends"].remove(pals)
      return len(person["friends"])
    
# 6. Find the total of everyone's money
  # (hint: use the self.people array, remember how we checked the total number of eggs yesterday?)

def total_money(person):
    total_amount = 0
    for per in person:
        total_amount += per["monies"]
    return total_amount

# 7. For two given people, allow the first person to loan a given value of money to the other
  # (hint: our function will probably need 3 arguments passed to it... the lender, the lendee, and the amount for this function)

def lend_money (creditor, debtor, amount):
    amount = creditor["monies"]
    creditor["monies"] =creditor["monies"] - (amount)
    debtor ["monies"] = debtor ["monies"] + (amount)

# 8. Find the set of everyone's favourite food joined together
  # (hint: concatenate the favourites/snack arrays together)

def all_favourite_foods (persons_list):
    all_fav_foods = []

    for person in persons_list:
       for snack in person["favourites"]["snacks"]:
           all_fav_foods.append(snack)
    return all_fav_foods

# 9. Find people with no friends
  # (hint: return an list, there might be more people in the future with no friends!)

# def find_no_friends (person):
#     amount_of_friends =  len(person["friends"])
#     #print (amount_of_friends)
#     for per in person ["friends"]:
#         if amount_of_friends == 0:
#             return person


amount_of_friends =  len(person["friends"])
print (amount_of_friends)   