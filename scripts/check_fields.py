from bs4 import BeautifulSoup
from utils.file_utils import convert_json_to_html, load_json, save_json


import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info("Iniciando checagem dos campos...")


def check_fields(response):
    soup = convert_json_to_html(response)
    check_type_fields(soup)


def check_type_fields(soup):
    tileDetails = soup.find(id='tileDetails')

    if tileDetails:
        if 'oasis' in tileDetails.get('class', []):
            check_oasis_fields(soup)
        elif 'village' in tileDetails.get('class', []):
            check_village_fields(soup)
        else:
            print("Ambiente selvagem")
    else:
        logger.error(
            "Elemento com ID 'tileDetails' não encontrado no HTML.")


def check_oasis_fields(soup):
    map_details = soup.find(id='map_details')
    if map_details:
        if not check_field_occupied(soup):
            field_values = extract_text_from_element_for_oassis(soup)
            file_name = "oasis_livre.json"
            save_fields(field_values, file_name)
        else: 
            print("Oásis ocupado")


def check_village_fields(soup):
    map_details = soup.find(id='map_details')
    if map_details:
        if check_field_occupied(soup):
            field_values = extract_text_from_element(soup)
            check_and_save_tribe_type(field_values)
        else: 
            print("Vale Abandonado")

def check_and_save_tribe_type(field_values):
    tribe = field_values.get("tribe", "")
    if tribe == "Natarianos":
        file_name = "natarianos_file.json"
        save_fields(field_values, file_name)
    else:
        file_name = "villages_file.json"
        save_fields(field_values, file_name)


def check_field_occupied(soup):
    village_info = soup.find(id='village_info')
    if village_info:
        return True

def extract_text_from_element_for_oassis(soup):
    distance = soup.find(id='distance')
    extracted_data = {
        "title_in_header": soup.find(class_='titleInHeader').get_text(strip=True) if soup.find(class_='titleInHeader') else '',
        "coordinates": soup.find(class_='coordinatesWrapper').get_text(strip=True) if soup.find(class_='coordinatesWrapper') else '',
        "distance": distance.find('td', string='Campos:').get_text(strip=True) if soup.find('td', string='Campos:') else '',
        "troop_info_list": extract_text_from_troop_info_table(soup.find('table', id='troop_info'))
    }
    return extracted_data

def extract_text_from_element(soup):
    extracted_data = {
        "title_in_header": soup.find(class_='titleInHeader').get_text(strip=True) if soup.find(class_='titleInHeader') else '',
        "coordinates": soup.find(class_='coordinatesWrapper').get_text(strip=True) if soup.find(class_='coordinatesWrapper') else '',
        "tribe": soup.find('th', string='Tribo:').find_next('td').get_text(strip=True) if soup.find('th', string='Tribo:') else '',
        "alliance": soup.find('th', string='Aliança:').find_next('td').find('a').get_text(strip=True) if soup.find('th', string='Aliança:') else '',
        "player": soup.find('th', string='Proprietário:').find_next('td').find('a').get_text(strip=True) if soup.find('th', string='Proprietário:') else '',
        "population": soup.find('th', string='População:').find_next('td').get_text(strip=True) if soup.find('th', string='População:') else '',
        "distance": soup.find('th', string='Distância').find_next('td').get_text(strip=True) if soup.find('th', string='Distância') else '',
    }
    return extracted_data


def extract_text_from_troop_info_table(troop_info_table):
    troop_info_list = []
    if troop_info_table:
        # Encontre todas as linhas ('tr') na tabela
        rows = troop_info_table.find_all('tr')

        # Itere sobre as linhas para extrair as informações das tropas
        for row in rows:
            # Encontre todas as colunas ('td') na linha
            columns = row.find_all('td')

            # Verifique se há informações suficientes (pelo menos 3 colunas) para garantir que as informaçõe no 'td' são as de tropas
            if len(columns) >= 3:
                troop_id = columns[0].find('img')['class'][1]
                troop_quantity = columns[1].get_text(strip=True)
                troop_name = columns[2].get_text(strip=True)

                troop_info = {
                    'troop_id': troop_id,
                    'troop_quantity': troop_quantity,
                    'troop_name': troop_name
                }
                troop_info_list.append(troop_info)

    return troop_info_list

def save_fields(field_values, file_name):
    existing_data = load_json(file_name)
    # Crie uma chave única usando as coordenadas como string
    chave = field_values['coordinates']
    existing_data[chave] = field_values
    save_json(existing_data, file_name)
