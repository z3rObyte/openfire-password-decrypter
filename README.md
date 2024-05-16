# openfire-password-decrypter
Small tool for decrypting openfire passwords using the key

### Setup
```bash
sudo apt update
sudo apt install python3-venv -y
git clone https://github.com/z3rObyte/openfire-password-decrypter
cd openfire-password-decrypter
python3 -m venv .env
source ./.env/bin/activate
pip install -r requirements.txt
```
### Usage
```bash
python3 decrypter.py encryptedPassword PasswordKey
```
