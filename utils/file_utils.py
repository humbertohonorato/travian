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


def load_json(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}  # Se o arquivo não existir, comece com um dicionário vazio


def save_json(data, file_name):
    try:
        with open(file_name, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f"Dados adicionados/salvos em '{file_name}' com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os dados em JSON: {str(e)}")

