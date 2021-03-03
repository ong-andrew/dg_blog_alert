from datetime import date, timedelta
import urllib

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

today = date.today()

year = today.strftime("%Y")
month_int = today.strftime("X%m").replace("X0", "X").replace("X", "")
day_pad_zero = today.strftime("%d")
day_no_zero = today.strftime("X%d").replace("X0", "X").replace("X", "")
month_str = today.strftime("%b").lower()
month_bm = translator[month_str]

print(year)
print(month_int)
print(day_pad_zero)
print(day_no_zero)
print(month_bm)
url = ("https:kpkesihatan.com/" + year + "/" + month_int + "/" + day_pad_zero + "/kenyataan-akhbar-kpk-" + day_no_zero + "-" + month_bm + "-" + year + "-situasi-semasa-jangkitan-penyakit-coronavirus-2019-covid-19-di-malaysia/")

print(url)
