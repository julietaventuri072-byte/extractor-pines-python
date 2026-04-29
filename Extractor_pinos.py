def pin_extractor(poems):
    # Paso 18: Lista para almacenar todos los PINs generados
    secret_codes = []
    
    # Paso 17: Bucle para procesar cada poema recibido en la lista
    for poem in poems:
        secret_code = ""
        # Dividimos el poema actual en líneas
        lines = poem.split("\n")
        
        # Recorremos cada línea con su índice
        for line_index, line in enumerate(lines):
            words = line.split()
            
            # Paso 14 y 15: Validación y manejo de errores (else)
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                # Si la línea es muy corta, añadimos un '0'
                secret_code += '0'
        
        # Paso 18: Agregamos el PIN del poema actual a la lista general
        secret_codes.append(secret_code)
    
    # Paso 19: Devolvemos la lista con todos los resultados
    return secret_codes

# --- Ámbito Global ---

# Paso 3: Primer poema
poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

# Paso 16: Poemas adicionales
poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

# Paso 19: Llamada final con la lista de poemas y print descomentado
print(pin_extractor([poem, poem2, poem3]))