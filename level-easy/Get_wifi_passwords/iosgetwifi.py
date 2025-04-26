# Source Code of Getting WiFi Passwords using Python in MAC OS

import subprocess

def get_wifi_interface():
    try:
        result = subprocess.check_output(["networksetup", "-listallhardwareports"]).decode()
        lines = result.splitlines()
        for i in range(len(lines)):
            if "Wi-Fi" in lines[i] or "AirPort" in lines[i]:
                if "Device" in lines[i + 1]:
                    return lines[i + 1].split(": ")[1]
    except Exception as e:
        print("Error getting Wi-Fi interface:", e)
    return None

def get_saved_wifi_names(interface):
    try:
        output = subprocess.check_output(
            ["/usr/sbin/networksetup", "-listpreferredwirelessnetworks", interface]
        ).decode()
        networks = []
        for line in output.splitlines()[1:]:  # Skip the header line
            name = line.strip()
            if name:
                networks.append(name)
        return networks
    except Exception as e:
        print("Error getting saved Wi-Fi names:", e)
        return []

def get_wifi_password(ssid):
    try:
        password = subprocess.check_output(
            ["security", "find-generic-password", "-D", "AirPort network password", "-ga", ssid],
            stderr=subprocess.STDOUT
        ).decode()
        # Password appears after: password: "yourpassword"
        for line in password.splitlines():
            if "password:" in line:
                return line.split("password: ")[1].strip().strip('"')
    except subprocess.CalledProcessError as e:
        return "Password not found or permission denied"
    return "Unknown error"

if __name__ == "__main__":
    interface = get_wifi_interface()
    if interface:
        print(f"Wi-Fi Interface: {interface}\n")
        ssids = get_saved_wifi_names(interface)
        for ssid in ssids:
            print(f"SSID: {ssid}")
            pwd = get_wifi_password(ssid)
            print(f"Password: {pwd}\n")
    else:
        print("Could not detect a Wi-Fi interface.")
