from scapy.all import IP,ICMP,send

# ip destino del ping
ip = IP(dst="www.esiiab.uclm.es")
icmp = ICMP()

# creacion del paquete
ping = ip/icmp

ping.show()

send(ping)
