import requests


def IsInternet():
    '''
    Check if you are connected to internet
    '''

    try:
        requests.get("https://www.google.com")
        return True

    except requests.ConnectionError:
        return False


if IsInternet():
    print('Internet Access')

else:
    print('No Internet')
