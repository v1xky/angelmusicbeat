from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "8913469"))
API_HASH = getenv("API_HASH", "b3f7cb5deefe1cf33bebee944915061b")
BOT_TOKEN = getenv("BOT_TOKEN","2124064704:AAG-_oWI2-08SAgg1GbrU45OayzAHepIdAk")
BOT_NAME = getenv("BOT_NAME","⛧𓆩🖤 Aɴɢᴇʟ Mᴜsɪᴄ 🖤𓆪⛧")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "BQBfC3QCMB4gRIbLYq8GF0H8c3MWwjUFq6NCTEDuWtYYMu_gfmQXyyTtl3r39BF091z0rkPVo4h3wsCCGifBY5uM0xaKMI2mBgALa2yvrbSb1_ncV59ZV-4202Kbi1r5-lB2lNTUTRGKD5u_81tSMijSAo_nArk_iOqOnNi3f4GgEf_qRlb8WBnC1th-BK4NFreREgRnYGmi7_KdsjFDoBulOd53eDemWFBqR2IAfihl1rIrdW9LRNhpQtsxn1yf8eBfo6o6uasmaR4zExQYZyn-W02khrDxZVpgqS9gODR9b5tZPrri4TOK5WKdaSYLEE3NsjDKsNH1XUVZsgFdhuDWeArx6QA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "DISABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5486269467").split()))
