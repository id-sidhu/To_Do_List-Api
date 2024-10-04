from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Task

@receiver(post_save, sender=Task)
def task_created(sender, instance, created, **kwargs):
    if created:
        print(f"Task '{instance.task}' has been created.")
        
    # send_mail(
    #     subject=f"New Task Created: {instance.title}",
    #     message = f"A new task has been added: {instance.title}\nDescription: {instance.description}\nDue: {instance.due_date}",
    #     from_email='@gmail.com'
    #     recipient_list=[instance.user.email],
    #     fail_silently=False
    # )