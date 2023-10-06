from bs4 import BeautifulSoup
import json
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info("Iniciando validações em arquivos...")

def convert_json_to_html(response):
    try:
        # Decodifique a string JSON e obtenha o valor 'html'
        response_html = json.loads(response.text)['html']

        soup = BeautifulSoup(response_html, 'html.parser')
        return soup
    except (json.JSONDecodeError, KeyError) as e:
        logger.error(f"Erro ao decodificar JSON ou encontrar 'html': {str(e)}")
    except Exception as e:
        logger.error(f"Ocorreu um erro inesperado: {str(e)}")
