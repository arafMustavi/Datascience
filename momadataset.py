def replace_paranthesis(word):
    word = word.replace("(" , "")
    word = word.replace(")" , "")
    return word

#### Removes the () from the strings

for entry in moma:
    entry[2] = replace_paranthesis(entry[2])
    entry[5] = replace_paranthesis(entry[5])
