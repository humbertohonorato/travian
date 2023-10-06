from configs.constants import *
from libs.http_client import HttpClient

import logging
import sys

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def post_map_tile_details_data(coord_x=COORD_X, coord_y=COORD_Y):
    try:
        headers = {"User-Agent": USER_AGENT,
                   "Content-Type": CONTENT_TYPE,
                   "Accept": ACCECPT,
                   "Authorization": BEARER_TOKEN,
                   "Cookie": COOKIE}

        client = HttpClient(URL_BASE_SERVER, headers=headers)

        login_route = f"{API_VERSION}/{API_TILE_DETAILS_PATH}"

        data = {
            "x": f"{coord_x}",
            "y": f"{coord_y}"
        }

        response = client.post(login_route, data=data)

        if response.status_code != 200:
            logger.error(
                f"Erro na requisição http. Código de status: {response.status_code}")
            sys.exit(1)  # Use 1 para indicar um erro

        return response
    except Exception as e:
        logger.error(f"Ocorreu um erro ao fazer a requisição : {str(e)}")
        sys.exit(1)