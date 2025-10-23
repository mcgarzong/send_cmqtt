import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform
from PIL import Image

# Mostrar la versión de Python
st.write("Versión de Python:", platform.python_version())

# Mostrar imagen principal (botón decorativo)
image = Image.open("boton.jpeg")
st.image(image, caption="Controlador principal", use_container_width=True)

values = 0.0
act1 = "OFF"

def on_publish(client, userdata, result):
    print("El dato ha sido publicado\n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)

broker = "broker.mqttdashboard.com"
port = 1883
client1 = paho.Client("GIT-HUB")
client1.on_message = on_message

st.title("CONTROL POR BOTÓN 💥")

# Botón ON
if st.button('🔴 ENCENDER'):
    act1 = "ON"
    client1 = paho.Client("Camilag")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Act1": act1})
    ret = client1.publish("cmqtt_camilag", message)
else:
    st.write('')

# Botón OFF
if st.button('⚪ APAGAR'):
    act1 = "OFF"
    client1 = paho.Client("Camilag")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Act1": act1})
    ret = client1.publish("cmqtt_camilag", message)
else:
    st.write('')

# Slider de valores
values = st.slider('Selecciona el rango de valores', 0.0, 100.0)
st.write('Valor seleccionado:', values)

# Botón para enviar valor analógico
if st.button('📡 Enviar valor analógico'):
    client1 = paho.Client("Camilag")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Analog": float(values)})
    ret = client1.publish("cmqtt_cami", message)
else:
    st.write('')
