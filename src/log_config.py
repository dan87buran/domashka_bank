import logging
import os
from typing import Optional


def setup_logger(name: str) -> Optional[logging.Logger]:
    """Настройка логера для модуля"""
    try:
        os.makedirs('logs', exist_ok=True)
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        if logger.handlers:
            logger.handlers.clear()

        handler = logging.FileHandler(f'logs/{name}.log', mode='w')
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger
    except Exception as e:
        print(f"Ошибка настройки логера: {e}")
        return None