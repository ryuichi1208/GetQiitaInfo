# -*- coding: utf-8 -*-
import sys
import time
import os
import re
import requests
import json
import numpy as np
import matplotlib.pyplot as plt

domain = "https://qiita.com"
username = ""
token = ""


def check_domain_valid(domain: str):
    regex = "^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}$"
    return True if re.match(regex, domain) else False


def check_url_valid(url: str):
    regex = "^(http|https)://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$"
    return True if re.match(regex, domain) else False


def exec_http_requrest(url: str, headers={}):
    headers = {'Authorization': "Bearer " + token}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response
    else:
        return response.status_code


def get_user_ingo(username: str):
    if exec_http_requrest(gen_url(domain, "agwagopkewpogkew", 0)) == 404:
        pass


def get_itmes(url: str, js: list, pages: int):
    response = exec_http_requrest(url)
    tmp = json.loads(response.text)
    js.extend(tmp)
    if len(js) % 20 == 0:
        get_itmes(gen_url(domain, username, pages+1), js, pages+1)
    return js


def gen_url(domain: str, username: str, pages: int):
    if pages:
        return f'{domain}/api/v2/users/{username}/items?page={pages}'
    else:
        return f'{domain}/api/v2/users/{username}'


def get_titles(items: list, kind: str):
    if kind is "title":
        return [items[i]['title'] for i in range(len(items))]
    elif kind is "id":
        return [items[i]['id'] for i in range(len(items))]
    elif kind is "views":
        return []


def get_views_count(id_list: list):
    view_list = []
    for i in range(len(id_list)):
        url = "https://qiita.com/api/v2/items/" + id_list[i]
        tmp = json.loads(exec_http_requrest(url).text)
        view_list.append(tmp['page_views_count'])
        time.sleep(3)
    return view_list


def load_config(conf_path: str):
    pass


def data_prot(data: list):
    x_width = 0.5
    x_loc = np.array(range(len(data))) + x_width

    labels = [i for i in range(len(data))]

    plt.figure(figsize=(30, 15), dpi=50, facecolor="azure", edgecolor="coral")
    plt.title(f'view count / Total : [{sum(data)}]', fontsize=30)
    plt.ylabel("count", fontsize=20)
    plt.bar(x_loc, data, color="green", width=x_width)
    plt.xticks(x_loc, labels)
    plt.show()

def main():
    pages = 1
    print(check_domain_valid(domain))
    get_user_ingo(username)
    url = gen_url(domain, username, pages)
    response = get_itmes(url, [], pages)
    id_list = get_titles(response, "id")
    view_list = get_views_count(id_list)
    data_prot(view_list)


if __name__ == "__main__":
    main()

