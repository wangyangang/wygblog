from django.db import models


class Student(models.Model):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (0, '未知'),
    ]
    STATUS_ITEMS = [
        (0, '申请'),
        (1, '通过'),
        (2, '拒接'),
    ]
    name = models.CharField('姓名', max_length=128)
    sex = models.IntegerField('性别', choices=SEX_ITEMS)
    profession = models.CharField('职业', max_length=128)
    email = models.EmailField('Email')
    qq = models.CharField('QQ', max_length=128)
    phone = models.CharField('电话', max_length=128)
    status = models.IntegerField('审核状态', choices=STATUS_ITEMS, default=0)
    created_time = models.DateTimeField('创建时间', auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        verbose_name = verbose_name_plural = '学员信息'
