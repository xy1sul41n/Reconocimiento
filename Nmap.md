# Nmap
### Reconocimiento inicial.

Para realizar un reconocimiento inicial de la dirección IP en la cual nos proporcionará todos los puertos abiertos que tiene la maquina utilizaremos:
```
nmap -p- --open -T5 -v -n -oG allPorts 10.10.10.10
```
* **-p-** Todos los puertos
* **--open** Solo mostrará los puertos abiertos
* **-T5** Escaneo rápido. Escala de 1-5, siendo 5 el más rápido y ruidoso (recomendado para entornos controlados)
* **-v** Modo verbose. Para que nos indique lo que vaya descubriendo.
* **-n** El escaneo se demora mucho menos.
* **-oG allPorts** Exportar resultado a formato grepeable en un archivo llamado allPorts.
Con la utilidad extractPorts sacamos los puertos abiertos del archivo allPorts y se copian en la clipboard:
```
extractPorts allPorts
```
### Reconocimiento rápido. TCP SYN Scan.
Este tipo de reconocimiento agiliza el escaneo y tarda menos:
```
nmap -sS --min-rate 5000 --open -vvv -Pn -p- 10.10.10.10
```
* **-sS** TCP SYN Scan.
* ** --min-rate 5000** Envíar 5000 paquetes/segundo.
* **-vvv** Muestra la información 
* **-Pn** No aplicar descubrimiento de hosts a través del protocolo de resolucion de direcciones ARP.


### Reconocimiento de Servicios y Versiones.

Una vez tenemos los puertos abiertos pasamos a un escaneo más profundo. Reconocimiento de servicios y versiones.
Para realizar un escaneo de los servicios y versiones que están corriendo en estos puertos utilizamos:
```
nmap -p21,80,1443,49150 -sC -sV -oN targeted
```
* **-sC** Scripts básicos de enumeración
* **-sV** Versiones y servicios que corren en los puertos indicados.
* **-oN targeted** Exportar en formato de nmap al archivo llamado targeted
