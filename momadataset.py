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
    
    
    
    
    
    
 #Stripping Data#
test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

cleaned_data = []
for s in test_data:
    s = strip_characters(s)
    cleaned_data.append(s)
print(cleaned_data)
stripped_test_data = cleaned_data

