import wmi
import win32com.client
from colorama import Fore, Style

def get_computer_system():
    c = wmi.WMI()
    computer_system = c.Win32_ComputerSystem()[0]
    return computer_system

def get_installed_drivers():
    installed_drivers = []
    wmi_service = win32com.client.Dispatch('WbemScripting.SWbemLocator')
    c = wmi_service.ConnectServer('.', 'root\cimv2')
    drivers = c.ExecQuery('SELECT * FROM Win32_PnPSignedDriver WHERE DeviceName IS NOT NULL')
    for driver in drivers:
        installed_drivers.append(driver.DeviceName)
    return installed_drivers

def check_driver_updates():
    computer_system = get_computer_system()
    print(f"Computer Manufacturer: {computer_system.Manufacturer}")
    print(f"Computer Model: {computer_system.Model}\n")

    installed_drivers = get_installed_drivers()
    print("Installed Drivers:")
    for driver in installed_drivers:
        if has_update(driver):
            print(f"{Fore.RED}{driver}{Style.RESET_ALL}")
        else:
            print(driver)

def has_update(driver_name):
    # Replace this logic with your own driver update check mechanism
    # Here, we assume that all drivers have available updates
    return True

if __name__ == "__main__":
    check_driver_updates()
