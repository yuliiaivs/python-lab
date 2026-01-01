import requests
import matplotlib.pyplot as plt

days = ["20251225", "20251226", "20251227", "20251228", "20251229", "20251230", "20251231"]
labels = ["25.12", "26.12", "27.12", "28.12", "29.12", "30.12", "31.12"]

rates = []
print("Getting currency rates from NBU...")
for day in days:
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date=" + day + "&json"
    response = requests.get(url)
    data = response.json()

    if data:
        current_rate = data[0]['rate']
        rates.append(current_rate)
        print("Date " + day + ":rate is " + str(current_rate))

plt.figure(figsize=(9,  5))
plt.plot(labels, rates, marker='o' , color='grey' , label='USD rate')

plt.title("NBU Exchange Rates (USD/UAH)")
plt.xlabel("Day")
plt.ylabel("Rate (UAH)")
plt.grid(True)
plt.legend()

plt.show()
