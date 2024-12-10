from django.core.management.base import BaseCommand
from blog.models import Article,Category
import os,random

class Command(BaseCommand):
    def handle(self,*args,**options):
        os.chdir('/home/pi/wen/收藏')
        book_names = os.listdir()
        for book_name in book_names:
            os.chdir('/home/pi/wen/收藏/{}'.format(book_name))
            pgnames = os.listdir()
            for pgname in pgnames:
                with open(pgname,'r',encoding='gbk') as f:
                    a = f.read()
                Article.objects.create(
                  title = pgname,
                  excerpt = '无',
                  category = Category.objects.filter(id=5),
                  tags = '小说',
                  img = '插_图/{}'.format(random.choice(os.listdir('/home/pi/下载/壁纸'))),
                  body = a,
                  user = 'yc',
                  tui = '热门推荐'
                )
                print('创建成功',book_name,pgname)
                #os.chdir('/home/pi/myblog/blog')
            
