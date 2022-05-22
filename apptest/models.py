from django.db import models
from apptest.managers import TestCustomManager, TestInfoCustomManager


class Test(models.Model):
    """
    Model Description
    """
    objects = models.Manager()  # default manager
    custom_objects = TestCustomManager()  # custom manager
    code = models.CharField(max_length=255, null=True, help_text="ex)일련번호")
    date = models.DateField(null=True)
    count = models.IntegerField(null=True)

    class Meta:
        db_table = "test"


class TestInfo(models.Model):
    objects = models.Manager()
    custom_objects = TestInfoCustomManager()
    test = models.ForeignKey("Test", on_delete=models.CASCADE)

