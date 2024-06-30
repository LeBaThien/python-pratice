from pprint import pprint


user = {
    "first_name": (first_name := "Thien"),
    "last_name": (last_name := "lee"),
    "display_name": f"{first_name} {last_name}",
    "height": (height := 168),
    "weight": (weight := 70),
    "bmi": weight / (height / 100) ** 2,
}

if __name__ == '__main__':
    pprint(user)
