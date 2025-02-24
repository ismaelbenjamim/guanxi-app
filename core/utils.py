import random

import requests

proxies = ['twiskgiw:x2tmv8dqwjeo@85.198.44.138:6064', 'twiskgiw:x2tmv8dqwjeo@92.113.239.42:5426',
           'twiskgiw:x2tmv8dqwjeo@92.113.239.70:5454', 'twiskgiw:x2tmv8dqwjeo@23.129.255.55:5463',
           'twiskgiw:x2tmv8dqwjeo@23.129.255.156:5564', 'twiskgiw:x2tmv8dqwjeo@85.198.40.118:5753',
           'twiskgiw:x2tmv8dqwjeo@85.198.44.62:5988', 'twiskgiw:x2tmv8dqwjeo@85.198.37.64:5701',
           'twiskgiw:x2tmv8dqwjeo@85.198.33.140:5488', 'twiskgiw:x2tmv8dqwjeo@23.129.255.226:5634',
           'twiskgiw:x2tmv8dqwjeo@85.198.33.33:5381', 'twiskgiw:x2tmv8dqwjeo@85.198.37.197:5834',
           'twiskgiw:x2tmv8dqwjeo@85.198.44.3:5929', 'twiskgiw:x2tmv8dqwjeo@85.198.44.179:6105',
           'twiskgiw:x2tmv8dqwjeo@85.198.40.96:5731', 'twiskgiw:x2tmv8dqwjeo@85.198.37.163:5800',
           'twiskgiw:x2tmv8dqwjeo@85.198.40.192:5827', 'twiskgiw:x2tmv8dqwjeo@85.198.40.242:5877',
           'twiskgiw:x2tmv8dqwjeo@85.198.40.170:5805', 'twiskgiw:x2tmv8dqwjeo@92.113.239.43:5427',
           'twiskgiw:x2tmv8dqwjeo@85.198.33.23:5371', 'twiskgiw:x2tmv8dqwjeo@92.113.239.185:5569',
           'twiskgiw:x2tmv8dqwjeo@92.113.239.84:5468', 'twiskgiw:x2tmv8dqwjeo@92.113.239.202:5586',
           'twiskgiw:x2tmv8dqwjeo@85.198.44.14:5940', 'twiskgiw:x2tmv8dqwjeo@85.198.40.237:5872',
           'twiskgiw:x2tmv8dqwjeo@23.129.255.138:5546', 'twiskgiw:x2tmv8dqwjeo@23.129.255.196:5604',
           'twiskgiw:x2tmv8dqwjeo@85.198.44.250:6176', 'twiskgiw:x2tmv8dqwjeo@85.198.33.39:5387',
           'twiskgiw:x2tmv8dqwjeo@23.129.255.241:5649', 'twiskgiw:x2tmv8dqwjeo@85.198.33.155:5503',
           'twiskgiw:x2tmv8dqwjeo@23.129.255.129:5537', 'twiskgiw:x2tmv8dqwjeo@92.113.240.42:5427',
           'twiskgiw:x2tmv8dqwjeo@85.198.37.185:5822', 'twiskgiw:x2tmv8dqwjeo@85.198.40.196:5831',
           'twiskgiw:x2tmv8dqwjeo@92.113.239.156:5540', 'twiskgiw:x2tmv8dqwjeo@92.113.240.142:5527',
           'twiskgiw:x2tmv8dqwjeo@92.113.239.73:5457', 'twiskgiw:x2tmv8dqwjeo@85.198.44.220:6146',
           'twiskgiw:x2tmv8dqwjeo@85.198.33.97:5445', 'twiskgiw:x2tmv8dqwjeo@85.198.37.162:5799',
           'twiskgiw:x2tmv8dqwjeo@85.198.37.234:5871', 'twiskgiw:x2tmv8dqwjeo@85.198.44.10:5936',
           'twiskgiw:x2tmv8dqwjeo@85.198.40.122:5757', 'twiskgiw:x2tmv8dqwjeo@92.113.240.62:5447',
           'twiskgiw:x2tmv8dqwjeo@85.198.44.193:6119', 'twiskgiw:x2tmv8dqwjeo@85.198.37.225:5862',
           'twiskgiw:x2tmv8dqwjeo@85.198.44.242:6168', 'twiskgiw:x2tmv8dqwjeo@85.198.37.20:5657']


def get_instagram_username(session_id):
    url = "https://i.instagram.com/api/v1/accounts/current_user/"
    headers = {
        "User-Agent": "Instagram 219.0.0.12.117 Android",
        "Referer": "https://www.instagram.com/",
        "X-IG-App-ID": "936619743392459"  # ID do app oficial do Instagram
    }
    cookies = {"sessionid": session_id}

    response = requests.get(url, headers=headers, cookies=cookies)

    if response.status_code == 200:
        data = response.json()
        return data.get("user", {}).get("username")
    else:
        print(f"Erro ao obter username: {response.status_code}, {response.text}")
        return None


def get_random_proxy():
    proxy = random.choice(proxies)
    return {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }

