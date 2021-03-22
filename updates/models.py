import json
from django.db import models
from django.conf import settings

from django.core.serializers import serialize


def upload_update_image(instance, filename):   # This method is for ImageField() and used for upload_to in ImageField().
    return 'updates/{user}/{filename}'.format(user=instance.user, filename=filename)


# Custom Query Set Manager.
class UpdateQuerySet(models.QuerySet):
    # def serialize(self):
    #     qs = self
    #     return serialize('json', qs, fields=('user', 'content', 'image'))

    # def serialize(self):
    #     qs = self
    #     final_array = []   # Empty list
    #     for obj in qs:
    #         stuct = json.loads(obj.serialize())
    #         final_array.append(stuct)
    #     return json.dumps(final_array)

    def serialize(self):
        list_values = list(self.values("user", "content", "image", "id"))  # Added values method on actual queryset. It will give you list with values.
        print(list_values)
        return json.dumps(list_values)
        

class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)


class Update(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content     = models.TextField(blank=True, null=True)
    image       = models.ImageField(upload_to=upload_update_image, blank=True, null=True)   # upload_to=upload_update_image here upload_update_image from the method.
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ''

    # def serialize(self):
    #     json_data = serialize("json", [self], fields=('user', 'content', 'image'))
    #     stuct = json.loads(json_data) # Opposite of dumps data. It taking json data and turned it into something we can use. loads turns it into list over dictionary [{}].
    #     print(stuct)
    #     data = json.dumps(stuct[0] ['fields'])  # Transform the data to being json. Trying to back in python dictionary or array to print it on what it is exactly.
    #     return data

    def serialize(self):
        try:
            image = self.image.url
        except:
            image = ""            
        data = {
            "id": self.id,
            "content": self.content,
            "user": self.user.id,
            "image": image
        }
        data = json.dumps(data)
        return data
