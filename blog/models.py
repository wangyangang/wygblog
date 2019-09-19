from django.db import models

from utils.base_model import BaseModel
from django.contrib.auth.models import User


class Category(BaseModel):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    name = models.CharField('名称', max_length=50)
    status = models.IntegerField('状态', choices=STATUS_ITEMS, default=STATUS_NORMAL)
    is_nav = models.BooleanField('是否为导航', default=False)
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=None)

    class Meta:
        verbose_name = verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Tag(BaseModel):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    name = models.CharField('名称', max_length=10)
    status = models.PositiveIntegerField('状态', choices=STATUS_ITEMS, default=STATUS_NORMAL)
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=None)

    class Meta:
        verbose_name = verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Post(BaseModel):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿'),
    )
    title = models.CharField('标题', max_length=255)
    desc = models.CharField('摘要', max_length=1024, blank=True)
    context = models.TextField('正文', help_text='正文必须为MarkDown格式')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=None)
    tag = models.ForeignKey(Tag, verbose_name='标签', on_delete=None)
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=None)

    class Meta:
        verbose_name_plural = verbose_name = '文章'
        ordering = ['-created_time']

    def __str__(self):
        return self.title
