#!/bin/bash

cd "${0%/*}"
open ./Install/AddDW1820A.app
sudo rm -r /System/Library/Extensions/IO80211Family.kext
sudo rm -r /System/Library/Extensions/IOBluetoothFamily.kext
sudo cp -r IO80211Family.kext /System/Library/Extensions
sudo cp -r IOBluetoothFamily.kext /System/Library/Extensions
sudo rm /System/Library/PrelinkedKernels/prelinkedkernel
sudo rm /System/Library/Caches/com.apple.kext.caches/Startup/kernelcache
sudo chmod -R 755 /System/Library/Extensions
sudo chmod -R 755 /Library/Extensions
sudo chown -R root:wheel /System/Library/Extensions
sudo chown -R root:wheel /Library/Extensions
sudo touch /System/Library/Extensions
sudo touch /Library/Extensions
sudo kextcache -i /