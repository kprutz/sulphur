from django.db import models
from custom_user.models import User


def user_directory_path(instance, filename):
  # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
  return "user_{0}/{1}".format(instance.user.id, filename)


class Transcribe(models.Model):
  user = User()
  request_time = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{} - {}'.format(self.user.name, self.request_time)
