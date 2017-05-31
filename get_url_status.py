import requests
import time


def main():
    # get filename
    file = input('Enter file path: ')
    valid = False
    while not valid:
        try:
            with open(file, 'r' ) as url_file:
              urls = url_file.read().split(',')
              results = ""
              #timeout after 30 minutes
              timeout = time.time() + 60*30
            #   print("Starting to ping urls: " + time.ctime())
              while time.time() < timeout:
                #ping URL and save response to a string.
                results = ping_urls(urls, results)
                #sleep 5 minutes
                time.sleep(300)
            # print("Done pinging urls: " + time.ctime())
            print(results)
            valid = True
        except:
            file = input('Incorrect file, please try again: ')

def ping_urls(urls, results):
    for url in urls:
        try:
            r = requests.get(url)
            results += url + "'s status: " + str(r.status_code) + "\n"
        except Exception as e:
            print("Error occurred while requesting the url " + url + "\n")
            print(e)
    return results

if __name__ == "__main__":
    main()
