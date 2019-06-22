def parse(data):
    return_list = []
    notre_numero = 0
    
    for i in data:
        if  i == "i":
            notre_numero += 1
        elif i == "d":
            notre_numero -= 1
        elif i == "s":
            notre_numero = notre_numero**2
        elif i == "o":
            return_list.append(notre_numero)
            
    return return_list
