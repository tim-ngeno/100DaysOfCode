# User Input
bictionary = {}

bid_is_open = True
while bid_is_open:
    name = input("Type in your name: \n")
    bid = int(input("What is your bid price?\n$ "))
    bictionary[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no':  ")
    if other_bidders == 'no':
        bid_is_open = False
# bid dictionary


bid_price = 0
winner = ""
for bidder in bictionary:
    highest_bid = bictionary[name]
    if highest_bid > bid_price:
        bid_price = highest_bid
        bidder = winner
print(f"{name} is the winner with the highest bid of ${highest_bid}")
print(bictionary)
