import subprocess
import socket
import sys 
import time 


###   / _ \
### \_\(_)/_/
###  _//o\\_ 
###   /   \

kira = '''

                                .--..     
                              .' ..   `.   
     .     .--.              /    \   \    `. 
   .|     |__|              \    '   |     | 
 .  |     .--..-,.--.        `--'   /     /  
<    |     |  ||  .-. |    __      .  ,-  
 |   | ____|  || |  | | .:--..    |  /       
 |   | \ .'|  || |  | |/ |   \ |   | '        
 |   |/  . |  || | '- `" __ | |   '-'        
 |    /\  \|__|| |      .'.''| |  .--.        
 |   |  \  \   | |     / /   | |_/    \       
     \  \  \  |_|     \ \._,\ '/\    /       
------  ---         `--  `"  `--        


'''



def animated_wait_message():
    message = "Please wait"
    while True:
        sys.stdout.write("\r" + message)
        sys.stdout.flush()
        time.sleep(0.5)  # Réglage de la vitesse de l'animation
        message += "."
        if len(message) > 15:  # Limiter le nombre de points pour éviter une surcharge visuelle
            message = "Please wait"

try:
    animated_wait_message()
except KeyboardInterrupt:
    print("\nProcessus annulé.")


print(animated_wait_message)

def get_device_name(ip):
    try:
        host_name, _, _ = socket.gethostbyaddr(ip)
        return host_name
    except (socket.herror, socket.gaierror):
        return "N/A"

def get_connected_devices():
    try:
        result = subprocess.check_output("arp -a", shell=True, text=True)
        lines = result.splitlines()
        devices = []

        for line in lines[3:]:
            parts = line.split()
            if len(parts) == 3:
                ip, _, mac = parts
                name = get_device_name(ip)
                devices.append({'ip': ip, 'mac': mac, 'name': name})

        return devices

    except Exception as e:
        print(f"[!] Erreur lors de la récupération des appareils connectés : {e}")
        return []

def display_result(devices):
    print(kira)
    print("[+] Appareils connectés à la box :")
    print("- IP - \t\t\t- MAC Address -\t\t - Nom de l'appareil -")
    print("---------------------------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}\t\t{device['name']}")

if __name__ == "__main__":
    # Analyse du réseau et affichage des résultats
    devices = get_connected_devices()
    display_result(devices)
