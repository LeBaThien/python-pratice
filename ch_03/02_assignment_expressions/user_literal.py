from pprint import pprint


first_name = "thien"
lat_name = "lee"
height = 168
weight = 70


user = {
    "first_name": first_name,
    "last_name": lat_name,
    "display_name": f"{first_name} {lat_name}",
    "height": height,
    "weight": weight,
    "bmi": weight / (height / 100) ** 2,
}

if __name__ == '__main__':
    print(user)

