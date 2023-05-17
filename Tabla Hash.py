def generar_tabla_hash(texto):
    tabla_hash = {}
    lineas = texto.split('\n')
    
    for i, linea in enumerate(lineas):
        palabras = linea.split()
        for j, palabra in enumerate(palabras):
            clave = f'({i+1},{j+1})'
            tabla_hash[clave] = palabra
    
    return tabla_hash


def main():
    codigo_c = '''
    int suma = 0;
    suma = 54 + 20;
    '''
    
    tabla_hash = generar_tabla_hash(codigo_c)
    
    # Mostrar la tabla hash
    print("Tabla Hash:")
    for clave, valor in tabla_hash.items():
        print(f'{clave}: {valor}')


if __name__ == '__main__':
    main()
