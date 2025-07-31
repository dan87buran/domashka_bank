import json
from typing import List, Dict, Union
from src.log_config import setup_logger

logger = setup_logger('utils')



def load_transactions(file_path: str) -> List[Dict[str, Union[str, float]]]:
    """
    Загружает транзакции из JSON-файла с логированием.
    """
    try:
        logger.debug(f"Попытка загрузить файл: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if not isinstance(data, list):
            logger.warning("Файл не содержит список транзакций")
            return []

        logger.info(f"Успешно загружено {len(data)} транзакций")
        return data

    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON: {file_path}")
    except Exception as e:
        logger.critical(f"Неожиданная ошибка: {e}", exc_info=True)

    return []