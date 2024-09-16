import requests


line = 'https://www.google.com/maps/search/car/@43.7173166,-79.7076942,10z/data=!4m2!2m1!6e6?entry=ttu'


get_data = requests.get(line)

fi = open("data.txt", '+w', encoding='ascii', errors='ignore')

fi.write(get_data.text)

print(get_data.text)