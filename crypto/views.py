from django.shortcuts import render
import requests
import json

def home(request):
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,DOGE,ADA,BNB,LTC,EOS,BUSD,BCH&tsyms=USD")
	price = json.loads(price_request.content)
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'home.html', {'api':api, 'price': price})

def prices(request):
	if request.method == 'POST':
		quote = request.POST['quote']
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {'quote':quote, 'crypto':crypto})

	else:
		return render(request, 'prices.html', {})
