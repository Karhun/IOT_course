
#!/usr/bin/python
# -*- coding: utf-8 -*-
#MQTT publish koodi.

import paho.mqtt.client as mqtt

# COnnecting to pblic tv on the class.
broker_ip = "192.168.2.12"
topiikki = "testitopic"
viesti = "Karhun rasp"

client = mqtt.Client()
client.connect(broker_ip)
client.publish(topiikki, viesti)
client.disconnect()
