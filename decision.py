# my_list = ['lake combs', 'bright', 'fumi']

# my_list.insert(1, "talk")
# my_list.extend(["olu", "tolu"])
# # my_list.pop()

# print(my_list[len(my_list) - 1])

my_dict = {
    "id": 1,
    "name": "lake combs",
    "is_programmer": True,
    "salary": "1.2",
    "loans": [
        {"package": "student loan", "amount": 5666},
        {"package": "car loan", "amount": 3838}
    ],
    "languages": [
        {"lang": "french", "proficiency": 100},
        {"lang": "english", "proficiency": 96}
    ]
}


print(my_dict.get("loans")[0].get("amount"))
