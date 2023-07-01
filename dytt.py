import requests
from lxml import etree


HEADER = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Referer":"https://dytt8.net/index1.htm"
}

BASE_DOMAIN = "https://dytt8.net/"

def get_details(url):
    response = requests.get(url, headers=HEADER)
    text = response.content.decode("gbk")
    html = etree.HTML(text)
    detail_url = html.xpath("//table[@class='tbspan']//a/@href")
    detail_url = map(lambda x: BASE_DOMAIN+x,detail_url )
    return detail_url


def replace(info,name):
    return info.replace(name,"").strip()

def parse_detail(url):
    movie= {}
    response = requests.get(url,headers=HEADER)
    text = response.content.decode("gbk")
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//h1//text()")[0]
    # time = html.xpath("//div[@class='co_content8']//ul//text()")[0]
    poster = html.xpath("//div[@class='co_content8']//img//@src")
    tem = html.xpath("//div[@id='Zoom']//text()")
    for index, info in enumerate(tem):
        if info.startswith("◎片　　名"):
            info = replace(info, "◎片　　名")
            movie["name"] = info
        elif info.startswith("◎年　　代"):
            info = replace(info, "◎年　　代")
            movie["time"] = info
        elif info.startswith("◎类　　别"):
            info = replace(info, "◎类　　别")
            movie["category"] = info
        elif info.startswith("◎主　　演"):
            info = replace(info, "◎主　　演")
            actors = [info]
            for x in range(index + 1, len(tem)):
                actor = tem[x].strip()
                # print (actor)
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie["actor"] = actors
    return movie

        # print (info)
        # print (index)
        # print ("***"*10)
    # print (tem)

def spider():
    url = "https://dytt8.net/html/gndy/dyzz/list_23_{}.html"
    movies = []
    for i in range(1,9):
        urls = url.format(i)
        # print (urls)
        url_details = get_details(urls)
        for j in url_details:
            movie = parse_detail(j)
            movies.append(movie)
    print (movies)




if __name__ == "__main__":
    spider()