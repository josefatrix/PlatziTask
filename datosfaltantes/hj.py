import os

# Ruta correcta del archivo usando un string raw
notebook_path = r'C:\Users\josed\Documents\platzi_task\datosfaltantes\datosfaltantes.ipynb'
output_path = r'C:\Users\josed\Documents\platzi_task\datosfaltantes\output_content.txt'

# Verifica si el archivo existe
if os.path.exists(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as file:
        notebook_content = file.read()
    # Guarda los primeros 1000 caracteres en un nuevo archivo
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(notebook_content[:1000])
    print(f"Contenido guardado en: {output_path}")
else:
    print(f"Archivo no encontrado: {notebook_path}")
