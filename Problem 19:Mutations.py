def mutate_string(string, position, character):
    s = string[position:].replace(string[position], character , 1)
    string =  string[:position]+ s
    return string
