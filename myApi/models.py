from django.db import models

# Create your models here.
class textDic(models.Model):
    title = models.CharField(max_length=100, blank=False)  # 标题字段，不可为空
    date = models.DateField(auto_now_add=True)  # 日期字段，默认为当前日期
    message_content = models.TextField(blank=False)  # 留言内容字段，不可为空
    author_name = models.CharField(max_length=50, blank=False)  # 留言人名字字段，不可为空

    # def __str__(self):
    #     return self.title
