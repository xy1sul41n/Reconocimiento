# extractPorts

Con esta utilidad, vamos a agilizar el proceso de reconocimiento inicial de una dirección IP. 
Al pasarle un archivo de resultados de un reconocimiento de nmap, nos va mostrar los puertos abiertos y se nos copiará a la clipboard.
Necesitaremos la herramienta xclip:
```
sudo apt install xclip
```
Editaremos el archivo ".bashrc":
```
nano /.bashrc
```
Si tu shell es otra diferente a bash, deberás cambiar el nombre del archivo por el de tu shell.
Para que el resultado de la herramienta quede bonito vamos a incluir una tabla de colores al principio del archivo mencionado anteriormente:
```
#Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"
```

Una vez incluida la tabla de colores y descargada la herramienta xclip, en el mismo archivo bajamos hacia abajo hasta encontrar los alias. Debajo de ellos vamos a incluir nuestra función:
```
function extractPorts(){
    ports="$(cat $1 | grep -oP '\d{1,5}/open' | awk '{print $1}' FS='/' | xargs | tr ' ' ',')"
    ip_address="$(cat $1 | grep -oP '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' | sort -u | head -n 1)"
    echo -e "\n[*] Extracting information...\n" > extractPorts.tmp
    echo -e "\t[*] IP Address: $ip_address"  >> extractPorts.tmp
    echo -e "\t[*] Open ports: $ports\n"  >> extractPorts.tmp
    echo $ports | tr -d '\n' | xclip -sel clip
    echo -e "[*] Ports copied to clipboard\n"  >> extractPorts.tmp
    cat extractPorts.tmp; rm extractPorts.tmp
}
```
#### Hay que tener en cuenta que el resultado de nmap debe ser en formato grepeable. Si no no funcionará la utilidad. 
Para guardar el resultado en este formato debemos añadir la siguiente flag cuando se realice el reconocimiento con nmap:
```
-oG nombre_del_archivo
```
En mi caso los resultados de nmap los guardo con el nombre allPorts. Si le poneis otro nombre al archivo del resultado debes cambiar la primera parte de las variables "ip_address" y "open_ports". 
```
 ip_address=$(cat allPorts)
 open_ports=$(cat allPorts)
 
 ip_address=$(cat nombre_archivo_resultado_nmap)
 open_ports=$(cat nombre_archivo_resultado_nmap)
 ```
Guardamos el archivo... y LISTO!
Para utilizar la función:
```
extractPorts nombre_del_archivo
```


 

