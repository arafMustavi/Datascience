def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

def replace_paranthesis(word):
    word = word.replace("(" , "")
    word = word.replace(")" , "")
    return word


for entry in moma:
    entry[3] = replace_paranthesis(entry[2])
    entry[4] = replace_paranthesis(entry[5])

    entry[5] = entry[5].title()
    if entry[5] == "":
        entry[5] = "Gender Unknown/Other"
    
    entry[2] = entry[2].title()
    if entry[2] == "":
        entry[2] = "Nationality Unknown"
        
    entry[3] = clean_and_convert(entry[3])
    entry[4] = clean_and_convert(entry[4])
