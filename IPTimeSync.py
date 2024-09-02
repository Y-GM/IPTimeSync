import requests
from datetime import datetime
import pytz
import os
import platform

def read_proxy_file(file_path='proxy.txt'):
    try:
        with open(file_path, 'r') as file:
            proxy_list = [
                line.strip() for line in file.readlines() 
                if line.strip().startswith('http://') or line.strip().startswith('socks5://')
            ]
            return proxy_list
    except Exception as e:
        print(f"Error reading proxy file: {e}")
        return None

def get_location_info(proxy=None):
    try:
        if proxy:
            print(f"Trying with proxy: {proxy}")
            if proxy.startswith('socks5://'):
                proxies = {
                    'http': proxy,
                    'https': proxy,
                }
            else:
                proxies = {
                    'http': proxy,
                    'https': proxy,
                }
        else:
            print("No proxy provided, making direct request")
            proxies = None

        response = requests.get('http://ipinfo.io', proxies=proxies)
        data = response.json()
        return data
    except Exception as e:
        print(f"Error fetching location data: {e}")
        return None

def set_system_time(timezone_str):
    try:
        timezone = pytz.timezone(timezone_str)
        local_time = datetime.now(timezone)
        formatted_time = local_time.strftime('%Y-%m-%d %H:%M:%S')
        print(f"Setting system time to: {formatted_time} ({timezone_str})")
        
        if platform.system() == "Linux":
            os.system(f'sudo date -s "{formatted_time}"')
        elif platform.system() == "Windows":
            os.system(f'date {local_time.strftime("%m-%d-%Y")}')
            os.system(f'time {local_time.strftime("%H:%M:%S")}')
        else:
            print("Unsupported OS for automatic time setting.")
    except Exception as e:
        print(f"Error setting system time: {e}")

def main():
    proxy_list = read_proxy_file()
    if proxy_list:
        for proxy in proxy_list:
            location_info = get_location_info(proxy)
            if location_info:
                timezone = location_info.get('timezone')
                if timezone:
                    set_system_time(timezone)
                    break  # Exit after successfully setting time
                else:
                    print("Could not determine the timezone.")
            else:
                print("Could not fetch location info with proxy.")
    else:
        # If no proxies available, try direct connection
        location_info = get_location_info()
        if location_info:
            timezone = location_info.get('timezone')
            if timezone:
                set_system_time(timezone)
            else:
                print("Could not determine the timezone.")
        else:
            print("Could not fetch location info directly.")

if __name__ == "__main__":
    main()
