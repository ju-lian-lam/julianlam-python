days = [
    "first", "second", "third", "fourth", "fifth", "sixth",
    "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
]

quantities = [
    "A", "Two", "Three", "Four", "Five", "Six",
    "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve"
]

items = [
    "partridge in a pear tree.", 
    "turtle doves,",
    "French hens,",
    "calling birds,",
    "gold rings,",
    "geese a-laying,",
    "swans a-swimming,",
    "maids a-milking,",
    "ladies dancing,",
    "lords a-leaping,",
    "pipers piping,",
    "drummers drumming,"
]

def list_gifts(n):
    if n == 0:
        print(f"{quantities[0]} {items[0]}")
    else:
        print(f"{quantities[n]} {items[n]}")
        list_gifts(n - 1)

def sing(day):
    if day == len(days):
        return 
    print(f"On the {days[day]} day of Christmas my true love sent to me:")
    list_gifts(day)
    print()
    sing(day + 1)

sing(0)
