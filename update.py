import requests
import re

USERNAME = "sakaYq4875"

# =========================
# データ取得
# =========================

# AC数・提出数
ac_rank_url = f"https://kenkoooo.com/atcoder/atcoder-api/v3/user/ac_rank?user={USERNAME}"
ac_data = requests.get(ac_rank_url).json()
ac_count = ac_data.get("count", 0)

# レート履歴
history_url = f"https://atcoder.jp/users/{USERNAME}/history/json"
history = requests.get(history_url).json()

current_rating = history[-1]["NewRating"] if history else "None"
performance = history[-1]["Performance"] if history else "None"

# =========================
# README更新
# =========================

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

def replace(tag, value):
    return re.sub(f"(<!-- {tag} -->).*", f"<!-- {tag} --> {value}", content)

content = re.sub(r"(<!-- AC_COUNT -->).*", f"<!-- AC_COUNT --> {ac_count}", content)
content = re.sub(r"(<!-- CURRENT_RATING -->).*", f"<!-- CURRENT_RATING --> {current_rating}", content)
content = re.sub(r"(<!-- PERFORMANCE -->).*", f"<!-- PERFORMANCE --> {performance}", content)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated README!")