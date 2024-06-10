import tkinter as tk
from tkinter import messagebox

def invert_ul_bit(mac):
    # Convert the first byte to integer, invert the 7th bit, and format it back to hex
    first_byte = int(mac[:2], 16)
    first_byte ^= 0x02
    return "{:02x}".format(first_byte) + mac[2:]

def eui64_process(mac):
    # Insert FFFE in the middle
    return mac[:6] + "fffe" + mac[6:]

def format_mac(mac):
    return mac.lower().replace(":", "").replace("-", "")

def generate_ipv6():
    prefix = prefix_entry.get().strip()
    mac = mac_entry.get().strip()

    if not prefix or not mac:
        messagebox.showerror("Input Error", "Both IPv6 prefix and MAC address are required.")
        return

    mac = format_mac(mac)
    if len(mac) != 12:
        messagebox.showerror("Input Error", "Invalid MAC address format.")
        return

    eui64_mac = eui64_process(mac)
    inverted_mac = invert_ul_bit(eui64_mac)
    
    ipv6_address = prefix + inverted_mac[:4] + ":" + inverted_mac[4:8] + ":" + inverted_mac[8:12] + ":" + inverted_mac[12:16]

    result_label.config(text=f"Full IPv6 Address: {ipv6_address}")
    step1_label.config(text=f"1. Split MAC Address: {mac[:6]} and {mac[6:]}")
    step2_label.config(text=f"2. Insert FFFE: {eui64_mac}")
    step3_label.config(text=f"3. Invert U/L bit: {inverted_mac}")
    step4_label.config(text=f"4. Combine with Prefix: {ipv6_address}")

app = tk.Tk()
app.title("EUI-64 IPv6 Address Generator")

tk.Label(app, text="IPv6 Prefix (e.g., 2001:0db8:85a3::)").grid(row=0, column=0, padx=10, pady=10)
prefix_entry = tk.Entry(app)
prefix_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="MAC Address (e.g., 00:1A:2B:3C:4D:5E)").grid(row=1, column=0, padx=10, pady=10)
mac_entry = tk.Entry(app)
mac_entry.grid(row=1, column=1, padx=10, pady=10)

generate_button = tk.Button(app, text="Generate IPv6 Address", command=generate_ipv6)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(app, text="Full IPv6 Address: ")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

step1_label = tk.Label(app, text="1. Split MAC Address: ")
step1_label.grid(row=4, column=0, columnspan=2, pady=5)

step2_label = tk.Label(app, text="2. Insert FFFE: ")
step2_label.grid(row=5, column=0, columnspan=2, pady=5)

step3_label = tk.Label(app, text="3. Invert U/L bit: ")
step3_label.grid(row=6, column=0, columnspan=2, pady=5)

step4_label = tk.Label(app, text="4. Combine with Prefix: ")
step4_label.grid(row=7, column=0, columnspan=2, pady=5)

app.mainloop()
