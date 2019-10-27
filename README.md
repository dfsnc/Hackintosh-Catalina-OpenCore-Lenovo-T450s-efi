# Thinkpad T450s Catalina

## Notice: If you need to edit config.plist, don't use OpenCore configurator, use PlistEdit pro or Xcode instead.

## Introduction

efi for Thinkpad T450s (20BXCT01WW) Hackintosh Catalina.

![About](Images/About.jpg)

CPU: i5-5200U

Integrated Graphics: HD Graphics 5500

Sound Card: ALC292

Wireless Card: **BCM94360CD 4 antennas.**

## Bios

- `Security -> Security` Chip: **Disabled**;
- `Memory Protection -> Execution Prevention`: **Enabled**;
- `Virtualization -> Intel Virtualization Technology`: **Disabled**;
- `Internal Device Access -> Bottom Cover Tamper Detection`: must be **Disabled**;
- `Anti-Theft -> Current Setting`: **Disabled**;
- `Anti-Theft -> Computrace -> Current Setting`: **Disabled**;
- `Secure Boot -> Secure Boot`: **Disabled**;
- `UEFI/Legacy Boot`: **UEFI Only**;
- `CSM Support`: **Yes**.

## What works

- Sleep / Wake
- Wifi and Bluetooth (BCM94360CD)
- Handoff, Continuity, AirDrop
- iMessage, FaceTime, App Store, iTunes Store (Change Config.plist -> PlatformInfo -> Generic -> MLB and SystemSerialNumber)
- Ethernet
- Onboard audio (Using VoodooHDA. For AppleALC, layout-id: 32, Use [ALCPlugFix](https://github.com/daliansky/XiaoMi-Pro-Hackintosh/blob/master/ALCPlugFix) to fix unworking jack after replug )
- TRIM
- USB 2.0 / USB 3.0
- Battery
- Touchpad:
    Default ApplePS2Controller is the one from [Rehabman](https://github.com/RehabMan/OS-X-Voodoo-PS2-Controller), it support those three buttons on the touchpad, but doesn't support three finger gestures.
    If you wanna use three finger gesture, and you don't care about those buttons, you can replace ApplePS2Controller with this one from [acidanthera](https://github.com/acidanthera/VoodooPS2).
- Redpoint
- Use [one-key-hidpi](https://github.com/daliansky/XiaoMi-Pro-Hackintosh/blob/master/one-key-hidpi) to enable HiDPI
- If you are using a usb mouse with side buttons, you can spoof apple usb mouse by change the pid and vid in AnyAppleUSBMouse.kext/Info.plist and enable it in config.plist.

## What doesn't work

- Sidecar (Broadwell doesn't support sidecar)
- SD Card Reader
- VGA (Untested)
- miniDP (Untested)
