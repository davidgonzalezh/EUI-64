import tkinter as tk
from tkinter import messagebox
import re

VERSION = "1.2.1"
AUTHOR = "David Gonzalez"
YEAR = 2024
COMPANY = "LAMBDA Strategies"
WEBSITE = "https://www.lambdastrategies.com"

def invert_ul_bit(mac):
    first_byte = int(mac[:2], 16)
    first_byte_bin = bin(first_byte)[2:].zfill(8)
    flipped_bit_bin = first_byte_bin[:6] + ('1' if first_byte_bin[6] == '0' else '0') + first_byte_bin[7:]
    flipped_bit_bin_segmented = ' '.join([flipped_bit_bin[i:i+4] for i in range(0, 8, 4)])
    first_byte_flipped = int(flipped_bit_bin, 2)
    return "{:02x}".format(first_byte_flipped) + mac[2:], flipped_bit_bin_segmented

def eui64_process(mac):
    return mac[:6] + "fffe" + mac[6:], f"{mac[:4]}:{mac[4:8]}:ff:fe:{mac[8:12]}"

def format_mac(mac):
    return mac.lower().replace(":", "").replace("-", "")

def is_valid_mac(mac):
    mac = format_mac(mac)
    if re.match(r"^[0-9a-f]{12}$", mac):
        return True
    return False

def is_valid_ipv6_prefix(prefix):
    try:
        segments = prefix.split(":")
        if len(segments) > 8:
            return False
        for segment in segments:
            if len(segment) > 4 or not re.match(r"^[0-9a-fA-F]*$", segment):
                return False
        return True
    except:
        return False

def generate_ipv6():
    prefix = prefix_entry.get().strip()
    mac = mac_entry.get().strip()

    if not is_valid_mac(mac):
        messagebox.showerror("Input Error", "Invalid MAC address format. Ensure it is 48 bits (12 hex digits) without any separators.")
        return

    if not is_valid_ipv6_prefix(prefix):
        messagebox.showerror("Input Error", "Invalid IPv6 prefix format. Ensure it follows the standard IPv6 notation.")
        return

    mac = format_mac(mac)
    eui64_mac, eui64_mac_formatted = eui64_process(mac)
    inverted_mac, flipped_bit_bin_segmented = invert_ul_bit(eui64_mac)
    
    ipv6_address = prefix + inverted_mac[:4] + ":" + inverted_mac[4:8] + ":" + inverted_mac[8:12] + ":" + inverted_mac[12:16]

    result_label.config(text=f"Full IPv6 Address: {ipv6_address}", font=("Helvetica", 12, "bold"))
    step1_label.config(text=f"1. Split MAC Address: {mac[:6]} and {mac[6:]}")
    step2_label.config(text=f"2. Insert FFFE: {eui64_mac_formatted}")
    step3_label.config(text=f"3. Invert U/L bit: {inverted_mac[:2]} (Original first byte: {mac[:2]}, Binary: {' '.join([bin(int(mac[:2], 16))[2:].zfill(8)[i:i+4] for i in range(0, 8, 4)])}, Flipped: {flipped_bit_bin_segmented})")
    step4_label.config(text=f"4. Combine with Prefix: {ipv6_address}")

def show_help():
    help_message = (
        "EUI-64 IPv6 Address Generation Process:\n\n"
        "1. Split the MAC Address: The 48-bit MAC address is divided into two 24-bit halves.\n"
        "2. Insert FFFE: Insert the hexadecimal value 'FFFE' in the middle of the two halves to form a 64-bit value.\n"
        "3. Invert the U/L Bit: Convert the first byte of the MAC address to binary, flip the 7th bit, and convert it back to hex:\n"
        "   - Original first byte: Convert the first byte of the MAC address to binary.\n"
        "   - Flip the 7th bit: Change the 7th bit (from the left) from 0 to 1, or from 1 to 0.\n"
        "   - Convert back to hex: Convert the modified binary value back to hexadecimal.\n"
        "4. Combine with Prefix: Combine the 64-bit network prefix with the modified MAC address to form the full 128-bit IPv6 address.\n\n"
        f"Author: {AUTHOR}\nVersion: {VERSION}\nCompany: {COMPANY}\nWebsite: {WEBSITE}"
    )
    messagebox.showinfo("Help - EUI-64 Process", help_message)

app = tk.Tk()
app.title("EUI-64 IPv6 Address Generator")
app.attributes('-topmost', True)
app.iconbitmap('icon.ico')

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

help_button = tk.Button(app, text="Help", command=show_help)
help_button.grid(row=8, column=0, columnspan=2, pady=10)

info_label = tk.Label(app, text=f"Author: {AUTHOR} | Version: {VERSION} | Company: {COMPANY} | Website: {WEBSITE}")
info_label.grid(row=9, column=0, columnspan=2, pady=10)

app.mainloop()
