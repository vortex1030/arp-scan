from scapy.all import *

rede = input('IP:')

"""
Envia ARP em broadcast na faixa de ip especificada
Exemplo /24 -> 192.168.1.0 até 192.168.1.225
"""
try:
    pkt = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=rede) 

    answered, unanswered = srp(pkt, timeout=2, verbose=0)#Separa os pacotes respondidos e os nao respondidos

    for env, rec in answered:
        print(f'IP: {rec.psrc} | MAC: {rec.hwsrc}')

except KeyboardInterrupt:
    print('Programa finalizado pelo Usuario! [KeyboardInterrupt]')