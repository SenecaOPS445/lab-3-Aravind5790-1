#!/usr/bin/env python3
#Author ID: Aravi-Kumar

import subprocess

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    result = subprocess.check_output(command, shell=True, text=True)
    return result.strip()

if __name__ == "__main__":
    disk_space = free_space()
    print(f"{disk_space}")
