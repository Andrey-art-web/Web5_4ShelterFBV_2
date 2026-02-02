from django.core.management import BaseCommand
import pyodbc
from config.settings import USER, PASSWORD, HOST, DRIVER, PAD_DATABASE, DATABASE


class Command(BaseCommand):

    def handle(self, *args, **options):
        connection_string = (
            f"DRIVER={DRIVER};"
            f"SERVER={HOST};"
            f"DATABASE={PAD_DATABASE};"
            f"UID={USER};"
            f"PWD={PASSWORD}"

        )

        try:
            conn = pyodbc.connect(connection_string)
            conn.autocommit = True
            conn.execute(fr'CREATE DATABASE {DATABASE};')
        except pyodbc.Error as err:
            print(err)
        else:
            print(f'База данных {DATABASE} успешно создана')
