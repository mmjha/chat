from django.db import models
from django.db.models.functions import Coalesce


class TestCustomManager(models.Manager):
    """
    Test Custom manager Description
    https://docs.djangoproject.com/en/3.1/topics/db/managers/
    """

    def test_counts(self):
        return self.annotate(
            num_responses=Coalesce(models.Count("count"), 0)
        )

class TestInfoCustomManager(models.Manager):
    """
    TestInfo Custom manager Description
    """
    pass