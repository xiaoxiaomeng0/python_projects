student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     # new_student_dict = {key:value for (key, value) in s}
#     pass
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas

new_list = {}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
for (index, row) in data.iterrows():
    new_list[row.letter] = row.code

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_on = True
while is_on:
    user_name = input("What is your name?").upper()
    name_list = {item: new_list[item] for item in user_name}
    print(name_list)
