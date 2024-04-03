import openai

# Establece tu clave de API de OpenAI


# Variable para almacenar la última consulta realizada
ultima_consulta = ""

# Buffer para almacenar consultas y respuestas
buffer_conversacion = []

# Función para realizar una consulta a OpenAI y procesar la respuesta
def consultar_chat_gpt(consulta):  # Corrección: cambiar nombre de función a snake_case
    global ultima_consulta
    try:
        # Imprime la consulta del usuario
        print("You:", consulta)

        # Invoca el API de chatGPT con la consulta del usuario
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {
                    "role": "user",
                    "content": consulta
                }
            ],
            temperature=1,
            max_tokens=150,
            stop=None
        )

        # Imprime la respuesta de chatGPT
        respuesta = response.choices[0].message.content
        print("chatGPT:", respuesta)

        # Agrega la consulta y respuesta al buffer
        buffer_conversacion.append((consulta, respuesta))

        # Actualiza la última consulta realizada
        ultima_consulta = consulta

    except Exception as e:
        # Imprime el error en caso de que ocurra
        print("Se produjo un error al procesar la consulta:", str(e))

# Función para manejar la entrada del usuario y realizar la conversación
def manejar_entrada_usuario():
    global ultima_consulta
    while True:
        try:
            # Solicitar al usuario una consulta
            consulta = input("Ingrese su consulta (o escriba 'salir' para terminar): ")
            if consulta.lower() == 'salir':
                break
            if consulta.strip() == "":
                print("Por favor, ingrese una consulta válida.")
                continue
            if consulta == "\033[A":  # Si se presiona la tecla "cursor Up"
                consulta = ultima_consulta  # Recupera la última consulta realizada
                print("You:", consulta)  # Imprime la consulta recuperada
            else:
                ultima_consulta = consulta  # Almacena la nueva consulta como la última
            consultar_chat_gpt(consulta)  # Corrección: llamada a función con nombre en snake_case
        except KeyboardInterrupt:
            print("\nSe interrumpió la ejecución del programa.")
            break

# Punto de entrada del programa
if __name__ == "__main__":
    manejar_entrada_usuario()
