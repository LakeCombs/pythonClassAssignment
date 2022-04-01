
class User():
    first_name = ""
    last_name = ""
    email_address = ""
    phone_number = ""
    alergies = ""
    food_diet = ""
    user_type = ""

    def get_full_name(self):

        return f"{self.first_name} {self.last_name}"


class Father():
    name = ""
    company = ""
    __wife__ = ""


class Son(Father):
    first_name = ""


class MenuItem():
    name = ""
    description = ""
    service_size = ""
    allergens = ""


class Order():
    orderId = ""
    user = ""
    menu = ""


class Price():
    pass


class KitcheanStaff:
    pass


user = User()

user.first_name = "lake combs"
user.last_name = "Trapping"
user.email_address = "adesolaolamilekan2@gmail.com"
user.alergies = "none"

# print(f"My name is {user.first_name}")

print(user.get_full_name())


son1 = Son()
