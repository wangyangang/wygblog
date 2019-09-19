from django.db import models

from utils.base_model import BaseModel
from blog.models import Post


class Comment(BaseModel):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    target = models.ForeignKey(Post, verbose_name='评论目标', on_delete=None)
    content = models.CharField('内容', max_length=2000)
    nickname = models.CharField('昵称', max_length=50)
    website = models.URLField('网站')
    email = models.EmailField('邮箱')
    status = models.PositiveIntegerField('状态', choices=STATUS_ITEMS, default=1)

    class Meta:
        verbose_name_plural = verbose_name = '评论'

    def __str__(self):
        return '{}在{}中说:{}'.format(self.nickname,
                                   self.target,
                                   self.content[:50] if len(self.content) > 50 else self.content)




