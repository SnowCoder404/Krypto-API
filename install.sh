#
#   Copyright © 2023, SnowCoder404
#
apt update && apt dist-upgrade -y
apt install python3-pip python3-venv -y
apt install libgmp-dev -y
cd /opt/krypto-api/
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirement.txt
python3 main.py &>/dev/null &