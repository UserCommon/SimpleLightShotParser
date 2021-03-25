import requests
import random
import string
import uuid
from bs4 import BeautifulSoup


def generate_code(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


k = 0


while True:
    unique_filename = str(uuid.uuid4())
    try:
        k = k + 1
        generated_code = generate_code()
        url="https://prnt.sc/{}/".format(generated_code)
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'})
        soup = BeautifulSoup(response.text)
        images = soup.findAll('img')

        if len(images)==3:
            src = images[0].get('src')
            r = requests.get(src, stream = True, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'})
            f = open("img/file"+str(k)+"-"+unique_filename+".png",'wb')
            f.write(r.content)
            f.close()
            print('Image sucessfully Downloaded: file'+str(k)+'.png')
        else:
            print("Miss")
        print(src)
    except Exception:
        pass
