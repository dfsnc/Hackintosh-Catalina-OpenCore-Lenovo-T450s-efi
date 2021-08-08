#!/bin/bash

# Mount point
MNT="/Volumes/EFITest"

dot_clean .
rm -rf "${MNT}/EFI"
cp -r ./EFI $MNT
