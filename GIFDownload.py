import requests
from lxml import etree
from urllib import request
import os
import re
from queue import Queue
import threading



class Producer(threading.Thread):
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

    }
    def __init__(self,page_queue, img_queue,  *args, **kwargs):
        super(Producer,self).__init__(*args, **kwargs)
        self.page_queue=page_queue
        self.img_queue=img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        response = requests.get(url, headers=self.HEADERS)
        text = response.text
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img in imgs:
            img_url = img.get('data-original')
            alt = img.get('alt')
            alt = re.sub(r'[\?？\.，。！|!/<]', '', alt)
            suffix = os.path.splitext(img_url)[1]
            if alt:
                filename = alt + suffix
                self.img_queue.put((img_url,filename))



class Consumer(threading.Thread):
    def __init__(self, page_queue,  img_queue, *args, **kwargs):
        super(Consumer,self).__init__(*args, **kwargs)
        self.page_queue=page_queue
        self.img_queue=img_queue
        self.path = os.path.join(os.path.dirname(__file__),'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url, filename = self.img_queue.get()
            request.urlretrieve(img_url,self.path + '\\' + filename)

def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)

    for x in range(1,101):
        url = "https://www.pkdoutu.com/photo/list/?page={}"
        urls = url.format(x)
        page_queue.put(urls)
        # break
    for x in range(5):
        t = Producer(page_queue,img_queue)
        t.start()
    for x in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()

if __name__ == '__main__':
    main()