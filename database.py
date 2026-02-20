import json
import os
from datetime import datetime
from config import *

def load_json(file):
    if not os.path.exists(file):
        return {} if file.endswith(".json") else []
    with open(file, "r") as f:
        content = f.read().strip()
        return json.loads(content) if content else ({} if file.endswith(".json") else [])

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)

def add_riwayat(uid, tipe, keterangan, jumlah):
    riwayat = load_json(RIWAYAT_FILE)
    if str(uid) not in riwayat: riwayat[str(uid)] = []
    riwayat[str(uid)].append({
        "tipe": tipe, "keterangan": keterangan, "jumlah": jumlah,
        "waktu": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    })
    save_json(RIWAYAT_FILE, riwayat)
  
