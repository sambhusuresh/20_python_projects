import webbrowser as wb

def webauto():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    #path to the chrome.exe
    URLS = (
        "google.com",
        "facebook.com"
    )
    for url in URLS:
        print("opening " + url)
        wb.get(chrome_path).open(url)
webauto()