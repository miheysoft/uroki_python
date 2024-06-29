### Простая настройка логирования:

import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Сообщение уровня DEBUG")
logging.info("Сообщение уровня INFO")
logging.warning("Сообщение уровня WARNING")
logging.error("Сообщение уровня ERROR")
logging.critical("Сообщение уровня CRITICAL")


### Логирование в файл:

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.info("Запись в файл")


### Использование логгера:

import logging

logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Создание файла лога
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

# Формат лога
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)

logger.debug("Debug сообщение")
logger.info("Info сообщение")
