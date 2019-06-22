def abbrevName(name):
    x = name.index(" ")
    return (name[0] + "." + name[x+1]).upper()