import configparser

config = configparser.ConfigParser()
config.read("config.ini")  # читаем конфигурационный файл
db_name = config.get("database", "db_name")
config.set("database", "db_name", "new_db_name")
with open("config.ini", "w") as configfile:
    config.write(configfile)
