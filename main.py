import webbrowser

# using webbrowser module
url_list = ["https://techcrunch.com/", "https://www.theverge.com/", "https://www.zdnet.com/#google_vignette", "https://medium.com/"]

for i in url_list:
    webbrowser.open_new(i)
