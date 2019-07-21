import sys
import os
import requests
import json

domain = "https://qiita.com"
username = ""


def exec_http_requrest(url: str):
    response = requests.get(url)

    print(response.status_code)
    if response.status_code == 200:
        return response
    else:
        return ""


def get_user_ingo(username: str):
    exec_http_requrest(gen_url(domain, "agwagopkewpogkew", 0))


def get_itmes(url: str, js: list, pages: int):
    response = exec_http_requrest(url)
    tmp = json.loads(response.text)
    js.extend(tmp)
    if len(js) % 20 == 0:
        pass
        get_itmes(gen_url(domain, username, pages+1), js, pages+1)
    return js


def gen_url(domain: str, username: str, pages: int):
    if pages:
        return f'{domain}/api/v2/users/{username}/items?page={pages}'
    else:
        return f'{domain}/api/v2/users/{username}'


def get_titles(items: list):
    return [items[i]['title'] for i in range(len(items))]


def load_config(conf_path: str):
    pass


def main():
    pages = 1
    get_user_ingo("aaa")
    url = gen_url(domain, username, pages)
    response = get_itmes(url, [], pages)
    print(get_titles(response))


if __name__ == "__main__":
    main()

