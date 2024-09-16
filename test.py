import yaml




with open('city_locations.yaml', 'r') as file_y:
        LOCATION_ALL = yaml.safe_load(file_y)
        



CITYs = LOCATION_ALL['USA']['Florida']

for i in CITYs:
    print(i)