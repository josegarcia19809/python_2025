# List to Dictionary Exercise
# Given a person variable:
#
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
#
# Create a dictionary called answer , that makes each first item in each list a key and the second item a
# corresponding value.  That's a terrible explanation.  I think it'll be easier if you just look at the end goal:
#
# {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}
#
# There are many potential solutions for this.

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer

answer = {}

for data_person in person:
    answer[data_person[0]] = data_person[1]



answer = {data_person[0]: data_person[1] for data_person in person}
print("-"*100)

answer ={k: v for k,v in person}

answer = dict(person)
print(answer)
