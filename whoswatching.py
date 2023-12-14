import subprocess
import socket
import tkinter as tk
from tkinter import scrolledtext, messagebox

###   / _ \
### \_\(_)/_/
###  _//o\\_ 
###   /   \


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
                ip, mac, _ = parts  # Extract IP and MAC from the output
                name = get_device_name(ip)
                devices.append({'ip': ip, 'mac': mac, 'name': name})

        return devices

    except Exception as e:
        messagebox.showerror("Error", f"Error retrieving connected devices: {e}")
        return []

def display_result(devices):
    result_text = "[+] Devices connected to the network:\n"
    result_text += "- IP - \t\t - MAC Address -\t\t - Device Name -\n"
    result_text += "---------------------------------------------------------\n"

    for device in devices:
        result_text += f"{device['ip']}\t\t{device['mac']}\t\t{device['name']}\n"

    return result_text

def show_result():
    devices = get_connected_devices()
    result_text = display_result(devices)
    result_text_widget.delete(1.0, tk.END)
    result_text_widget.insert(tk.END, result_text)

# Tkinter setup
root = tk.Tk()
root.title(">k.")

# ASCII Art Label
ascii_art_label = tk.Label(root, text=r'''

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

''', font=("Courier", 10))
ascii_art_label.pack(pady=10)



# Result Text
result_text_widget = scrolledtext.ScrolledText(root, width=60, height=15, wrap=tk.WORD)
result_text_widget.pack(pady=10)

# Refresh Button
refresh_button = tk.Button(root, text="Scan (around 15s)", command=show_result)
refresh_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
