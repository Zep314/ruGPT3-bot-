import requests

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json',
    'Server': 'istio-envoy',
    'Accept-encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.43',
    'Content-Type': 'application/json',
    'Origin': 'https://russiannlp.github.io',
    'Referer': 'https://russiannlp.github.io/',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7',
    }
def generate_ruGPT3(text):
    response = requests.post("https://api.aicloud.sbercloud.ru/public/v1/public_inference/gpt3/predict",
                         json={"text": text}, headers=headers)
    if response.status_code == 200:
        return response.json()['predictions']
    else:
        return 'Ошибка связи с высшим разумом...'
