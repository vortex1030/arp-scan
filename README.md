# ARP Network Scanner

Um scanner de rede simples desenvolvido em Python com a biblioteca **Scapy**, capaz de identificar dispositivos ativos em uma rede local por meio de requisições ARP (Address Resolution Protocol).

## 🚀 Funcionalidades

- Envio de requisições ARP em broadcast Ethernet.
- Identificação de dispositivos que respondem às requisições.
- Exibição dos endereços IP e MAC encontrados.
- Tratamento de interrupção pelo teclado (`Ctrl+C`).

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **Scapy**
- **Ethernet**
- **ARP**

## 📋 Pré-requisitos

- Python 3 instalado.
- Privilégios administrativos para enviar pacotes de rede.
- Biblioteca Scapy instalada.

Instale a dependência com:

```bash
pip install scapy
```

Em distribuições Linux que utilizam ambientes virtuais ou gerenciam pacotes Python pelo sistema, recomenda-se utilizar um ambiente virtual (`venv`).

## 📦 Como utilizar

1. Clone o repositório:

   ```bash
   git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
   ```

2. Entre no diretório:

   ```bash
   cd SEU-REPOSITORIO
   ```

3. Execute o programa com privilégios administrativos:

   ```bash
   sudo python3 scanner.py
   ```

4. Informe a faixa de rede que deseja verificar, por exemplo:

   ```text
   IP: 192.168.1.0/24
   ```

## 💻 Exemplo de saída

```text
IP: 192.168.1.1 | MAC: aa:bb:cc:dd:ee:ff
IP: 192.168.1.5 | MAC: 11:22:33:44:55:66
IP: 192.168.1.10 | MAC: 77:88:99:aa:bb:cc
```

*Os endereços acima são fictícios e servem apenas como exemplo.*

## ⚙️ Como funciona

1. O usuário informa uma rede ou endereço IP.
2. O programa cria um pacote Ethernet destinado ao endereço de broadcast `ff:ff:ff:ff:ff:ff`.
3. O pacote contém uma requisição ARP com o campo `pdst` definido pela entrada do usuário.
4. A função `srp()` envia os pacotes na camada 2 e coleta as respostas dentro do tempo limite configurado.
5. O programa percorre os pacotes respondidos e imprime o IP de origem (`psrc`) e o endereço MAC de origem (`hwsrc`).

## ⚠️ Limitações

- O scanner funciona principalmente em redes locais Ethernet compatíveis com ARP.
- Dispositivos em outras redes ou separados por roteadores normalmente não serão descobertos por esse método.
- Firewalls, isolamento de clientes Wi-Fi e outras configurações podem impedir respostas.
- O tempo limite de dois segundos pode não ser suficiente em todas as redes.

## 🔐 Uso responsável

Utilize esta ferramenta somente em redes próprias ou em ambientes nos quais você tenha autorização para realizar testes.

## 📚 Objetivo do projeto

Projeto de estudo para praticar Python, Scapy, protocolos de rede, Ethernet, ARP e reconhecimento de dispositivos em redes locais.

