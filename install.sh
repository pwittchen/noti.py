#!/usr/bin/env bash
set -e
wget -O noti.py https://raw.githubusercontent.com/pwittchen/noti.py/master/noti.py
chmod +x noti.py
sudo mv noti.py /usr/local/bin/noti.py
