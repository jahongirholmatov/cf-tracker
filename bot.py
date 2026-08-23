import datetime
import json
import urllib.request

HANDLE = "jahongirholmatov"
LOG_FILE = "daily_progress.txt"


def check_codeforces():
  url = f"https://codeforces.com/api/user.status?handle={HANDLE}&from=1&count=5"
  try:
    with urllib.request.urlopen(url) as response:
      data = json.loads(response.read().decode("utf-8"))
      if data["status"] == "OK":
        today = datetime.date.today()
        solved_today = 0

        for sub in data["result"]:
          sub_date = datetime.date.fromtimestamp(sub["creationTimeSeconds"])
          if sub_date == today and sub["verdict"] == "OK":
            solved_today += 1

        return solved_today
  except Exception as e:
    print(f"API bilan bog'lanishda xatolik: {e}")
  return 0


if __name__ == "__main__":
  print("Codeforces tekshirilmoqda...")
  solved = check_codeforces()
  print(f"Bugun yechilgan to'g'ri masalalar soni: {solved}")

  if solved > 0:
    today_str = str(datetime.date.today())
    with open(LOG_FILE, "a", encoding="utf-8") as f:
      f.write(
          f"Jahongir solved {solved} problems on Codeforces on {today_str}\n"
      )
    print("Log fayl yangilandi!")
  else:
    print("Bugun hali yangi masalalar yechilmagan.")