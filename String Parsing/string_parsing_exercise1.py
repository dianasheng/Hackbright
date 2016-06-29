str = "item:apples,quantity:4,price:1.50\n"
split_str = str.split(",")
price_list = split_str[2].split(":")
price = price_list[1]

print split_str
print price_list
print price

