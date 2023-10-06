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
            print("village")
    else:
        logger.error(
            "Elemento com ID 'tileDetails' não encontrado no HTML.")