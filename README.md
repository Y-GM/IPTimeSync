```markdown
# IPTimeSync

`IPTimeSync` is a Python-based application that automatically adjusts your system's time based on your geographic location. The program retrieves the geolocation using your IP address and accurately sets the local time according to the corresponding time zone. It supports both HTTP and SOCKS5 proxies and can operate without a proxy if none are available.

## Features

- Retrieve geographic location using the IP address.
- Automatically adjust system time based on the detected time zone.
- Support for both HTTP and SOCKS5 proxies.
- Ability to function without proxies if needed.

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

1. Ensure you have Python installed on your system.
2. If you want to use a proxy, update the `proxy.txt` file with your proxy details.
3. Run the script:

```bash
pip install -r requirements.txt

python IPTImeSync.py
```
