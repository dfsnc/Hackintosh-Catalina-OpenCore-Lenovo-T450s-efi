import os
from biplist import *

airports = bts = None
try:
    data = readPlist("./Data.plist")
    airports = data["Airport"]
    bts = data["Bluetooth"]
except InvalidPlistException as e:
    print("Error:", e)

os.chdir("../../../")

os.system("cp -r /System/Library/Extensions/IO80211Family.kext ./")
os.system("cp -r /System/Library/Extensions/IOBluetoothFamily.kext ./")
os.system("cp -r ./IO80211Family.kext ./IO80211Family_Backup.kext")
os.system("cp -r ./IOBluetoothFamily.kext ./IOBluetoothFamily_Backup.kext")

airport_plist = "./IO80211Family.kext/Contents/PlugIns/AirPortBrcm4360.kext/Contents/Info.plist"
bt_plist = "./IOBluetoothFamily.kext/Contents/PlugIns/BroadcomBluetoothHostControllerUSBTransport.kext/Contents/Info.plist"

try:
    # add wifi info
    airport = readPlist(airport_plist)
    for data in airports:
        airport["IOKitPersonalities"]["Broadcom 802.11 PCI"]["IONameMatch"].append(f"pci{data}")

    writePlist(airport, airport_plist)

    # add bt info
    bluetooth = readPlist(bt_plist)
    for bt in bts:
        vid_hex_str, pid_hex_str = bt.split(',')
        vid = int(vid_hex_str, 16)
        pid = int(pid_hex_str, 16)
        vid_hex = ("%#X" % vid)[2:]
        pid_hex = ("%#X" % pid)[2:]

        bluetooth["IOKitPersonalities"][f"PID {pid} 0x{pid_hex} VID {vid} 0x{vid_hex}"] = \
            {'CFBundleIdentifier': 'com.apple.iokit.BroadcomBluetoothHostControllerUSBTransport',
             'IOClass': 'BroadcomBluetoothHostControllerUSBTransport',
             'IOProviderClass': 'IOUSBHostDevice',
             'LMPLoggingEnabled': True,
             'idProduct': pid,
             'idVendor': vid}

    writePlist(bluetooth, bt_plist)
except (InvalidPlistException, NotBinaryPlistException) as e:
    print("Error:", e)
