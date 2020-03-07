def randomwikigen():
	import requests
	i = 0
	how_many_links = 2
	while i < how_many_links:

		response = requests.get('https://it.wikipedia.org/wiki/Speciale:PaginaCasuale')
		return("\n"+response.url)
		i = i+1

	if i>= how_many_links:
		exit(2)