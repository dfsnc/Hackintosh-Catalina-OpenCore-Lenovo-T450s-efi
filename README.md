# Thinkpad T450s Catalina

## 

## Introduction

efi for Thinkpad T450s Hackintosh Catalina.

![pic.jpg](/Users/echo/Desktop/Hackintosh-Catalina-OpenCore-Lenovo-T450s-efi/pic.jpg)

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
- Touchpad
- Use [one-key-hidpi](https://github.com/daliansky/XiaoMi-Pro-Hackintosh/blob/master/one-key-hidpi) to enable HiDPI

## What doesn't work

- Sidecar (Broadwell doesn't support sidecar)
- Redpoint (I never use this...)
- SD Card Reader
- DV (Untested)
- miniDP (Untested)
