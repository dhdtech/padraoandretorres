from django.dispatch import receiver
from django.utils import timezone

from model_clone.signals import post_clone_save, pre_clone_save

from users import models as user_models


@receiver(pre_clone_save, sender=user_models.StudentDefaultSchedule)
def increase_seq(sender, instance, **kwargs):
    pass
