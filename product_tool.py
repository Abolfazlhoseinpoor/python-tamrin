# tamrin 1 module 
def add_dicount (price,percent):
    return price * ( 1 - percent / 100)
def format_price (price):
    return f"{price:,} toman"
def is_in_stock (kala):
    if kala > 0:
        return "kala az 0 bishtar ast"
    elif kala < 0 :
        return "tedad kala manfi ast"
    else:
        return "tedad kala 0 ast"

        