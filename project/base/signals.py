import os
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import Lagu, Album, Genre

@receiver(pre_save, sender=Lagu)
def delete_old_lagu_files(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Lagu.objects.get(pk=instance.pk)
        if 'audio_file' in instance.__dict__ and instance.audio_file != old_instance.audio_file:
            if old_instance.audio_file:
                old_file_path = old_instance.audio_file.path
                if os.path.isfile(old_file_path):
                    os.remove(old_file_path)
        if 'audio_img' in instance.__dict__ and instance.audio_img != old_instance.audio_img:
            if old_instance.audio_img:
                old_image_path = old_instance.audio_img.path
                if os.path.isfile(old_image_path):
                    os.remove(old_image_path)

@receiver(post_delete, sender=Lagu)
def delete_lagu_files(sender, instance, **kwargs):
    if instance.audio_file:
        old_file_path = instance.audio_file.path
        if os.path.isfile(old_file_path):
            os.remove(old_file_path)
    if instance.audio_img:
        old_image_path = instance.audio_img.path
        if os.path.isfile(old_image_path):
            os.remove(old_image_path)

@receiver(pre_save, sender=Album)
def delete_old_album_files(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Album.objects.get(pk=instance.pk)
        if 'album_img' in instance.__dict__ and instance.album_img != old_instance.album_img:
            if old_instance.album_img:
                old_image_path = old_instance.album_img.path
                if os.path.isfile(old_image_path):
                    os.remove(old_image_path)

@receiver(post_delete, sender=Album)
def delete_album_files(sender, instance, **kwargs):
    if instance.album_img:
        old_image_path = instance.album_img.path
        if os.path.isfile(old_image_path):
            os.remove(old_image_path)

@receiver(pre_save, sender=Genre)
def delete_old_genre_files(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Genre.objects.get(pk=instance.pk)
        if 'image' in instance.__dict__ and instance.image != old_instance.image:
            if old_instance.image:
                old_image_path = old_instance.image.path
                if os.path.isfile(old_image_path):
                    os.remove(old_image_path)

@receiver(post_delete, sender=Genre)
def delete_genre_files(sender, instance, **kwargs):
    if instance.image:
        old_image_path = instance.image.path
        if os.path.isfile(old_image_path):
            os.remove(old_image_path)
