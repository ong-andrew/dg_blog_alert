from datetime import date, timedelta, datetime
from urllib import request
from time import sleep
from discord_webhook import DiscordWebhook

translator = {
    'jan': 'januari',
    'feb': 'februari',
    'mar': 'mac',
    'apr': 'april',
    'may': 'mei',
    'jun': 'jun',
    'jul': 'julai',
    'aug': 'ogos',
    'sep': 'september',
    'oct': 'oktober',
    'nov': 'november',
    'dec': 'disember'
}

today = date.today() - timedelta(days = 1)

year = today.strftime("%Y")
month_int = today.strftime("X%m").replace("X0", "X").replace("X", "")
day_pad_zero = today.strftime("%d")
day_no_zero = today.strftime("X%d").replace("X0", "X").replace("X", "")
month_str = today.strftime("%b").lower()
month_bm = translator[month_str]

print(today)
print(year)
print(month_int)
print(day_pad_zero)
print(day_no_zero)
print(month_bm)
url = ("https://kpkesihatan.com/" + year + "/" + month_int + "/" + day_pad_zero + "/kenyataan-akhbar-kpk-" + day_no_zero + "-" + month_bm + "-" + year + "-situasi-semasa-jangkitan-penyakit-coronavirus-2019-covid-19-di-malaysia/")
# print(url)

try:
    resp = request.urlopen(url).getcode()
    if resp == 200:
        msg = f"DG's new post is up. Click {url}"
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/816719001387532318/Id8zK5Mh0i_SUcHvFZgJqqePrKcu97cxDCCVYiK_6yBsVR_o-0fVdaZyQmWBrj-FFcra', content = msg)
        execute = webhook.execute()

except Exception as e:
    print(f'{e} ' + str(datetime.now()))
    sleep(5)
    x -= 1


