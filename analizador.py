def contar_palabras(texto):
	texto=texto.lower()
	texto=texto.replace(".","")
	texto=texto.replace("!","")
	texto=texto.replace("¡","")
	texto=texto.replace("?","")
	texto=texto.replace("¿","")
	lista=texto.split()
	return len(lista)
    # TODO: Retornar el número total de palabras

def contar_oraciones(texto):
    oraciones= texto.count(".") + texto.count("!") + texto.count("?") 
    return oraciones
    # TODO: Contar oraciones (terminan en '.', '!' o '?')

def palabra_mas_frecuente(texto):
	frecuencia = {}
	texto=texto.lower()
	texto=texto.replace(".","")
	texto=texto.replace("!","")
	texto=texto.replace("¡","")
	texto=texto.replace("?","")
	texto=texto.replace("¿","")
	lista=texto.split()
	for palabra in lista:
		if palabra not in frecuencia:
			frecuencia[palabra] = 1
		else:
			frecuencia[palabra] +=1
	frecuente=max(frecuencia, key=frecuencia.get)
	return frecuente
    # TODO: Retornar la palabra que más se repite (ignorar mayúsculas)
    # Pista: usa un diccionario para contar frecuencias

def palabras_unicas(texto):
	unicas= set()
	resultado=[]
	texto=texto.lower()
	texto=texto.replace(".","")
	texto=texto.replace("!","")
	texto=texto.replace("¡","")
	texto=texto.replace("?","")
	texto=texto.replace("¿","")
	lista=texto.split()
	for palabra in lista:
		if palabra not in unicas:
			resultado.append(palabra)
			unicas.add(palabra)
	return resultado
    # TODO: Retornar un conjunto (set) de palabras únicas

def longitud_promedio_palabras(texto):
	texto=texto.lower()
	texto=texto.replace(".","")
	texto=texto.replace("!","")
	texto=texto.replace("¡","")
	texto=texto.replace("?","")
	texto=texto.replace("¿","")
	lista=texto.split()
	suma=0
	for palabra in lista:
		suma += len(palabra)
	promedio= suma / len(lista)
	return promedio
    # TODO: Retornar la longitud promedio de las palabras

def buscar_palabra(texto, palabra):
	palabra=palabra.lower()
	texto=texto.lower()
	texto=texto.replace(".","")
	texto=texto.replace("!","")
	texto=texto.replace("¡","")
	texto=texto.replace("?","")
	texto=texto.replace("¿","")
	lista=texto.split()
	total=lista.count(palabra)
	return total
    # TODO: Retornar cuántas veces aparece la palabra en el texto

def reemplazar_palabra(texto, vieja, nueva):
	texto=texto.replace(vieja, nueva)
	return texto
    # TODO: Retornar el texto con la palabra vieja reemplazada por la nueva

# Texto de ejemplo para analizar
texto_ejemplo = """
Python es un lenguaje de programación muy popular. Python es fácil de aprender.
Muchos programadores usan Python para ciencia de datos y para desarrollo web.
Python tiene una gran comunidad. La comunidad de Python es muy activa y amigable.
¿Te gusta programar? ¡Python es una excelente opción para empezar!
""" 

print("=== ANALIZADOR DE TEXTO ===")
print(f"Total de palabras: {contar_palabras(texto_ejemplo)}")
print(f"Total de oraciones: {contar_oraciones(texto_ejemplo)}")
print(f"Palabra más frecuente: {palabra_mas_frecuente(texto_ejemplo)}")
print(f"Palabras únicas: {len(palabras_unicas(texto_ejemplo))}")
print(f"Longitud promedio: {longitud_promedio_palabras(texto_ejemplo):.1f}")
print(f"Veces que aparece 'Python': {buscar_palabra(texto_ejemplo, 'Python')}")

nuevo = reemplazar_palabra(texto_ejemplo, "Python", "Java")
print(f"\nTexto modificado (primeras 100 letras):\n{nuevo[:100]}...")
