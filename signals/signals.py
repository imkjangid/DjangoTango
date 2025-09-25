from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Users
import logging
logger = logging.getLogger('save_logger')

@receiver(post_save, sender=Users)
def user_add(sender, instance, created, **kwargs):
    if created:
        print(f"Users instance created with id: {instance.id}")
        logger.info(f"Users instance created with id: {instance.id}")
    else:
        logger.info(f"Users instance updated with id: {instance.id}")

def user_delete(sender, instance, **kwargs):
    print(f"Users instance deleted with id: {instance.id}")
    logger.info(f"Users instance deleted with id: {instance.id}")    