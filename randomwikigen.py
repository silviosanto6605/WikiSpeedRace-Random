def randomwikigen():
	import requests
	response = requests.get('https://it.wikipedia.org/wiki/Speciale:PaginaCasuale')
	return("\n"+response.url)
