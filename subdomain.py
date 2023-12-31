import requests

target_url = "du.ac.in"

def request(url):
    try:
      return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
      pass

with open("/home/kali/Downloads/Subdomain.txt","r") as wordlist_file:
 for line in wordlist_file:
  word = line.strip()
  test_url = word + "." + target_url
  response = request(test_url)
  if response:
    print("[+] Discovered subdomain --->" + test_url)