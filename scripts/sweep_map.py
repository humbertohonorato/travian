from configs.constants import *
from apis.api_tile_details import post_map_tile_details_data
from scripts.check_fields import check_fields

import time
import random
import logging
from tqdm import tqdm

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info("Iniciando busca no mapa...")

def search_fields():
    try:
        total_iterations = (2 * DISTACIA_MAX_X + 1) * (2 * DISTACIA_MAX_Y + 1)
        progress_bar = tqdm(total=total_iterations, desc='Progresso')

        for dx in range(-DISTACIA_MAX_X, DISTACIA_MAX_X + 1):
            for dy in range(-DISTACIA_MAX_Y, DISTACIA_MAX_Y + 1):
                x = COORD_X + dx
                y = COORD_Y + dy

                delay = random.randint(DELAY_MIN, DELAY_MAX) / 1000.0
                time.sleep(delay)

                response = post_map_tile_details_data(x, y)

                if response is not None:
                    logger.info(f"Coordenadas: ({x}, {y}), Delay: ({delay})")
                    check_fields(response)

            progress_bar.update(1)

        progress_bar.close()
    except KeyboardInterrupt:
        logger.warn("Operação interrompida pelo usuário.")
    except Exception as e:
        logger.error(f"Ocorreu um erro: {str(e)}")
