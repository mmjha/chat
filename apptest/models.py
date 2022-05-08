from django.db import models
from apptest.managers import TestCustomManager


class Test(models.Model):
    """
    Model Description
    """
    objects = models.Manager()  # default manager
    custom_objects = TestCustomManager()  # custom manager
    code = models.CharField(max_length=255, null=True, help_text="ex)일련번호")
    date = models.DateField(null=True)
    count = models.IntegerField(null=True)
    before_date = models.DateField(null=True)

    class Meta:
        db_table = "test"
