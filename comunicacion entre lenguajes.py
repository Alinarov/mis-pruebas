from time import time

import scapy.all as scapy


# Ahora vamos a construir una función que nos ayude a analizar la red wifi a la cual estamos conectados.
def escanear(direccion_ip):
    solicitud_arp = scapy.ARP(pdst=direccion_ip)
    print(solicitud_arp.summary())
escanear("192.168.0.1/24")