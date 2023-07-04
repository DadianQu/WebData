# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from BMW import settings


class BmwPipeline:
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        if not os.path.exists(self.path):
            os.makedirs(self.path)


    def process_item(self, item, spider):
        category = item['category']
        urls = item['urls']

        category_path = os.path.join(self.path,category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
        for url in urls:
            image_name = url.split(r'/')[-1]
            request.urlretrieve(url,os.path.join(category_path,image_name ))
        return item


class BMWImagesPipelines(ImagesPipeline):
    def get_media_requests(self, item, info):
        request_objs = super(BMWImagesPipelines,self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs


    def file_path(self, request, response=None, info=None, *, item=None):
        path = super(BMWImagesPipelines,self).file_path(request, response, info)
        category = request.item.get('category')
        image_store = settings.IMAGES_STORE
        category_path = os.path.join(image_store,category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
        image_name = path.replace("full/", "")
        image_path = os.path.join(category_path,image_name)
        return image_path