# EUI-64 IPv6 Address Generator

## Overview
This project provides a graphical user interface (GUI) tool for generating IPv6 addresses using the EUI-64 process. The tool allows users to input an IPv6 prefix and a MAC address, and it performs the EUI-64 process to produce the full IPv6 address. The GUI also explains the steps involved in the process.

## Features
- Input fields for IPv6 prefix and MAC address
- Step-by-step explanation of the EUI-64 process
- Help button providing detailed instructions
- Generates full IPv6 address based on user input
- Validates MAC address and IPv6 prefix format
- Provides a portable executable version

## Requirements
- Python 3.x
- Tkinter (if running from source)

## Installation

### Running from Source

1. Clone the repository:
    ```sh
    git clone https://github.com/davidgonzalezh/EUI64-IPv6-Generator.git
    ```
2. Navigate to the project directory:
    ```sh
    cd EUI64-IPv6-Generator
    ```

3. Run the Python script:
    ```sh
    python eui64_ipv6_generator_v1.2.1.py
    ```

### Creating the Portable Executable

1. Install PyInstaller:
    ```sh
    pip install pyinstaller
    ```

2. Build the Executable:
    ```sh
    pyinstaller --name EUI64IPv6Generator --onefile eui64_ipv6_generator_v1.2.1.py
    ```

   If `pyinstaller` is not recognized, use:
    ```sh
    python -m PyInstaller --name EUI64IPv6Generator --onefile eui64_ipv6_generator_v1.2.1.py
    ```

3. Find the executable in the `dist/` folder.

## Download Locations
You can download the portable executable directly from the following link:
- [Download EUI64IPv6Generator](https://github.com/davidgonzalezh/EUI64-IPv6-Generator/releases/latest)

## Usage
Run the executable file located in the `dist/` directory:
```sh
./dist/EUI64IPv6Generator
```
## License

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License. See the LICENSE file for details.
Author

- David Gonzalez [LAMBDA Strategies](https://www.lambdastrategies.com)

#### Created in 2024
