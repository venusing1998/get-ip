import requests
from lxml import etree


def get_ip():
    url = "http://ip.chinaz.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }
    proxies = {"https": "1.119.129.2:8080"}
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        if response.status_code == 200:
            result = etree.HTML(response.text).xpath(
                '//*[@id="rightinfo"]/dl//text()')
            return result
    except requests.ConnectionError as e:
        print(e)
        return None


if __name__ == "__main__":
    # print(get_ip())
    # ip address
    print(get_ip()[1], ": ", get_ip()[3])
    # address
    print(get_ip()[5], ": ", get_ip()[7])
    # os
    # print(get_ip()[10], ": ", get_ip()[12])
    # User-Agent
    # print(get_ip()[20], ": ", get_ip()[22], get_ip()[23])
