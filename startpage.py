import requests
from bs4 import BeautifulSoup

def startpage(query, needed):
    link = "https://www.startpage.com/do/search?hmb=1&cat=web&cmd=process_search&language=english_uk&engine0=v1all&query={0}&abp=1&t=night&nj=0&pg=0".format(query)
    source_code = requests.get(link, 'html')
    plain_txt = source_code.text
    lst = []
    s = BeautifulSoup(plain_txt, "lxml")
    for text in s.find_all('h3', {'class': 'clk'}):
        for lin in text.find_all('a'):
            for itmes in s.find_all('input', {'name': 'qid', 'type': 'hidden'}):
                href = lin.get('href')
                qid = itmes.get('value')
                break
            for action in s.find_all('form'):
                lst.append(action.get('action'))
                break
            break
        host = lst[-1]
        jobs = []
        for txt in s.find_all('h3', {'class': 'clk'}):
            for lin in txt.find_all('a'):
                ref = lin.get('href')
                jobs.append(ref)
                break
            value = 10
            while True:
                link2 = '{0}?cmd=process_search&startat={1}&language=english_uk&qid={2}&rcount=&rl=NONE&abp=1&nj=0&t=night&cpg=0&query={3}&cat=web&engine0=v1all&hmb=1'.format(host, value, qid, query)
                value += 10
                next_pages = requests.get(link2, 'html')
                p_text = next_pages.text
                s1 = BeautifulSoup(p_text, 'lxml')
                for text in s1.find_all('h3', {'class': 'clk'}):
                    for lin in text.find_all('a'):
                        href = lin.get('href')
                        jobs.append(href)
                        if len(jobs) == needed:
                            break
                            for job in jobs:
                                print(job)
