from bs4 import BeautifulSoup
from utils.file_utils import convert_json_to_html

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
            print("oasis")
        elif 'village' in tileDetails.get('class', []):
            check_village_fields(soup)
    else:
        logger.error(
            "Elemento com ID 'tileDetails' não encontrado no HTML.")


def check_village_fields(soup):
    map_details = soup.find(id='map_details')
    if map_details:
        if check_field_occupied(soup):
            field_values = extract_text_from_element(soup)
            print(field_values)

def check_field_occupied(soup):
    village_info = soup.find(id='village_info')
    if village_info: return True
        


def extract_text_from_element(soup):
    extracted_data = {
        "title_in_header": soup.find(class_='titleInHeader').get_text(strip=True) if soup.find(class_='titleInHeader') else '',
        "coordinates": soup.find(class_='coordinatesWrapper').get_text(strip=True) if soup.find(class_='coordinatesWrapper') else '',
        "tribe": soup.find('th', text='Tribo:').find_next('td').get_text(strip=True) if soup.find('th', text='Tribo:') else "",
        "alliance": soup.find('th', text='Aliança:').find_next('td').find('a').get_text(strip=True) if soup.find('th', text='Aliança:') else "",
        "player": soup.find('th', text='Proprietário:').find_next('td').find('a').get_text(strip=True) if soup.find('th', text='Proprietário:') else "111",
        "population": soup.find('th', text='População:').find_next('td').get_text(strip=True) if soup.find('th', text='População:') else "",
        "distance": soup.find('th', text='Distância').find_next('td').get_text(strip=True) if soup.find('th', text='Distância') else "",
        # "troop_info_list": extract_text_from_troop_info_table(soup.find('table', id='troop_info'))
    }
    return extracted_data
