from scholarly import scholarly

if False:
	from scholarly import ProxyGenerator
	# Set up a ProxyGenerator object to use free proxies
	# This needs to be done only once per session
	pg = ProxyGenerator()
	pg.FreeProxies()
	scholarly.use_proxy(pg)

def writecitations(id, filename):
	author = scholarly.search_author_id(id)
	author = scholarly.fill(author, sections=["publications"])
	with open(filename, "w") as o:
		o.write("index,citations,year,title\n")
		for i,x in enumerate(author['publications']):
			try:
				o.write("{},{},{},{}\n".format(
					i+1,
					x["num_citations"],
					x['bib']['pub_year'],
					x['bib']['title'],
					))
			except:
				print ("failed:\n{}".format(x))
writecitations("pZcYYCkAAAAJ", "googlescholar.csv")