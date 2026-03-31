# argv = información extra/adicional que se puede incluir al ejecutar un archivo/script 
import sys
#import openpyxl
import json

archivo_xlsx = sys.argv[1]
#wb= openpyxl.load_workbook(archivo_xlsx)

#hoja = wb.active

datos = []

#print(list(hoja.iter_rows))