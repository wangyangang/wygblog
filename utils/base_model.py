from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)