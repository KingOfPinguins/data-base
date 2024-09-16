from time import sleep
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

alberta = ['alberta', 'Airdrie', 'Beaumont', 'Brooks', 'Calgary', 'Camrose', 'Chestermere', 'Cold Lake', 'Edmonton',
'Fort Saskatchewan', 'Grande Prairie', 'Lacombe', 'Leduc', 'Lethbridge', 'Lloydminster', 'Medicine Hat',
'Red Deer', 'Spruce Grove', 'St. Albert', 'Wetaskiwin']


british_columbia = ['british columbia', 'Abbotsford', 'Armstrong', 'Burnaby', 'Campbell River', 'Castlegar', 'Chilliwack',
'Colwood', 'Coquitlam', 'Courtenay', 'Cranbrook', 'Dawson Creek', 'Delta', 'Duncan', 'Enderby', 'Fernie',
'Fort St. John', 'Grand Forks', 'Greenwood', 'Kamloops', 'Kelowna', 'Kimberley', 'Langford', 'Langley',
'Maple Ridge', 'Merritt', 'Mission', 'Nanaimo', 'Nelson', 'New Westminster', 'North Vancouver', 'Parksville',
'Penticton', 'Pitt Meadows', 'Port Alberni', 'Port Coquitlam', 'Port Moody', 'Powell River', 'Prince George',
'Prince Rupert', 'Quesnel', 'Revelstoke', 'Richmond', 'Rossland', 'Salmon Arm', 'Surrey', 'Terrace',
'Trail', 'Vancouver', 'Vernon', 'Victoria', 'West Kelowna', 'White Rock', 'Williams Lake']

manitoba = ['manitoba', 'Brandon', 'Dauphin', 'Flin Flon', 'Morden', 'Portage la Prairie', 'Selkirk', 'Steinbach', 'Thompson', 'Winkler', 'Winnipeg']


new_brunswick = ['new brunswick', 'Bathurst', 'Campbellton', 'Dieppe', 'Edmundston', 'Fredericton', 'Miramichi', 'Moncton', 'Saint John']


newfoundland_and_labrador = ['newfoundland and labrador', 'Corner Brook', 'Mount Pearl', "St. John's"]


northwest_territories = ['northwest territories', 'Yellowknife']


ontario = ['ontario', 'Barrie', 'Belleville', 'Brampton', 'Brant', 'Brantford', 'Brockville', 'Burlington', 'Cambridge',
'Clarence-Rockland', 'Cornwall', 'Dryden', 'Elliot Lake', 'Greater Sudbury', 'Guelph', 'Haldimand County',
'Hamilton', 'Kawartha Lakes', 'Kenora', 'Kingston', 'Kitchener', 'London', 'Markham', 'Mississauga',
'Niagara Falls', 'Norfolk County', 'North Bay', 'Orillia', 'Oshawa', 'Ottawa', 'Owen Sound', 'Pembroke',
'Peterborough', 'Pickering', 'Port Colborne', 'Prince Edward County', 'Quinte West', 'Richmond Hill',
'Sarnia', 'Sault Ste. Marie', 'St. Catharines', 'St. Thomas', 'Stratford', 'Temiskaming Shores', 'Thorold',
'Thunder Bay', 'Timmins', 'Toronto', 'Vaughan', 'Waterloo', 'Welland', 'Windsor', 'Woodstock']


prince_edward_island = ['prince edward island', 'Charlottetown', 'Summerside']


quebec = ["quebec", "Acton Vale", "Alma", "Amos", "Amqui", "Baie-Comeau", "Baie-D'Urfé", "Baie-Saint-Paul", "Barkmere",
"Beaconsfield", "Beauceville", "Beauharnois", "Beaupré", "Bécancour", "Bedford", "Belleterre", "Beloeil",
"Berthierville", "Blainville", "Boisbriand", "Bois-des-Filion", "Bonaventure", "Boucherville", "Lac-Brome", "Bromont",
"Brossard", "Brownsburg-Chatham", "Candiac", "Cap-Chat", "Cap-Santé", "Carignan", "Carleton-sur-Mer", "Causapscal",
"Chambly", "Chandler", "Chapais", "Charlemagne", "Châteauguay", "Château-Richer", "Chibougamau", "Clermont",
"Coaticook", "Contrecoeur", "Cookshire-Eaton", "Côte Saint-Luc", "Coteau-du-Lac", "Cowansville", "Danville", "Daveluyville",
"Dégelis", "Delson", "Desbiens", "Deux-Montagnes", "Disraeli", "Dolbeau-Mistassini", "Dollard-des-Ormeaux", "Donnacona",
"Dorval", "Drummondville", "Dunham", "Duparquet", "East Angus",
"Estérel", "Farnham", "Fermont", "Forestville", "Fossambault-sur-le-Lac", "Gaspé", "Gatineau",
"Gracefield", "Granby", "Grande-Rivière", "Hampstead", "Hudson", "Huntingdon", "Joliette", "Kingsey Falls",
"Kirkland", "La Malbaie", "La Pocatière", "La Prairie", "La Sarre", "La Tuque", "Lac-Delage", "Lachute",
"Lac-Mégantic", "Lac-Saint-Joseph", "Lac-Sergent", "L'Ancienne-Lorette", "L'Assomption", "Laval", "Lavaltrie", "Lebel-sur-Quévillon",
"L'Épiphanie", "Léry", "Lévis", "L'ele-Cadieux", "L'ele-Dorval", "L'ele-Perrot", "Longueuil", "Lorraine",
"Louiseville", "Macamic", "Magog", "Malartic", "Maniwaki", "Marieville", "Mascouche", "Matagami",
"Matane", "Mercier", "Métabetchouan-Lac-à-la-Croix", "Métis-sur-Mer", "Mirabel", "Mont-Joli", "Mont-Laurier",
"Montmagny", "Montreal", "Montreal West", "Montréal-Est", "Mont-Saint-Hilaire", "Mont-Tremblant", "Mount Royal", "Murdochville",
"Neuville", "New Richmond", "Nicolet", "Normandin", "Notre-Dame-de-l'ele-Perrot", "Notre-Dame-des-Prairies",
"Otterburn Park", "Paspébiac", "Percé", "Pincourt", "Plessisville", "Pohénégamook", "Pointe-Claire", "Pont-Rouge", "Port-Cartier",
"Portneuf", "Prévost", "Princeville", "Québec", "Repentigny", "Richelieu", "Richmond", "Rigaud",
"Rimouski", "Rivière-du-Loup", "Rivière-Rouge", "Roberval", "Rosemère", "Rouyn-Noranda", "Saguenay", "Saint-Amable",
"Saint-Augustin-de-Desmaures", "Saint-Basile", "Saint-Basile-le-Grand",
"Saint-Bruno-de-Montarville", "Saint-Césaire", "Saint-Charles-Borromée", "Saint-Colomban",
"Saint-Constant", "Sainte-Adèle", "Sainte-Agathe-des-Monts", "Sainte-Anne-de-Beaupré",
"Sainte-Anne-de-Bellevue", "Sainte-Anne-des-Monts", "Sainte-Anne-des-Plaines", "Sainte-Catherine",
"Sainte-Catherine-de-la-Jacques-Cartier", "Sainte-Julie", "Sainte-Marguerite-du-Lac-Masson",
"Sainte-Marie", "Sainte-Marthe-sur-le-Lac", "Sainte-Thérèse", "Saint-Eustache", "Saint-Félicien", "Saint-Gabriel",
"Saint-Georges", "Saint-Hyacinthe", "Saint-Jean-sur-Richelieu", "Saint-Jérôme",
"Saint-Joseph-de-Beauce", "Saint-Joseph-de-Sorel", "Saint-Lambert", "Saint-Lazare", "Saint-Lin-Laurentides", "Saint-Marc-des-Carrières",
"Saint-Ours", "Saint-Pamphile", "Saint-Pascal", "Saint-Philippe", "Saint-Pie", "Saint-Raymond", "Saint-Rémi", "Saint-Sauveur",
"Saint-Tite", "Salaberry-de-Valleyfield", "Schefferville", "Scotstown", "Senneterre", "Sept-eles",
"Shannon", "Shawinigan", "Sherbrooke", "Sorel-Tracy", "Stanstead", "Sutton", "Témiscaming", "Témiscouata-sur-le-Lac",
"Terrebonne", "Thetford Mines", "Thurso", "Trois-Pistoles", "Trois-Rivières", "Valcourt", "Val-d'Or", "Val-des-Sources",
"Varennes", "Vaudreuil-Dorion", "Victoriaville", "Ville-Marie",
"Warwick", "Waterloo", "Waterville", "Westmount", "Windsor"]


saskatchewan = ['saskatchewan', 'Estevan', 'Flin Flon', 'Humboldt', 'Lloydminster', 'Martensville', 'Meadow Lake', 'Melfort',
'Melville', 'Moose Jaw', 'North Battleford', 'Prince Albert', 'Regina', 'Saskatoon', 'Swift Current',
'Warman', 'Weyburn', 'Yorkton']


yukon = ['yukon', 'Whitehorse']

list_of_states = [alberta, british_columbia, manitoba, new_brunswick, newfoundland_and_labrador, northwest_territories, ontario, prince_edward_island, quebec, saskatchewan, yukon]


def search_location(state, city):
    print(state, city)
    driver = webdriver.Firefox()
    driver.implicitly_wait(5) # wait 10 sec if needed

    driver.get("https://www.google.com/maps/")

    element = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
    element.send_keys(city + ", " + state)
    check = driver.find_element(By.XPATH, '//*[@id="cell0x0"]')
    check.click()
    driver.implicitly_wait(10)
    sleep(4)
    get_url = driver.current_url
      
    print(get_url)
    
    line = get_url.split('/@')[1].split('/data')
    formated_line = '  ' + str(city) + ': ' + str(line[0])
    sleep(2)
    
    driver.close()
    
    return formated_line


def get_locations(state):
    new_yaml_data_dict = """
  """ + state[0] + """:
"""
    
    for city in state:
        if city == state[0]:
            continue
        line = search_location(state[0], city)
        new_yaml_data_dict = new_yaml_data_dict + line + '\n'

    data_file = open('city_locations.yaml', 'a')
    data_file.write(new_yaml_data_dict + '\n')

    data_file.close()

#for state in list_of_states:
#    get_locations(state)

global varr

with open('city_locations.yaml', 'r') as yaml_file:
    varr = yaml.safe_load(yaml_file)


print(varr['canada']['alberta']['Airdrie'])
print(varr['test']['town']['some town'])

#canada:
#  alberta:
#    Airdrie: