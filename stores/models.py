from django.db import models

class Store(models.Model):
    store_id = models.CharField(max_length=32)
    name = models.CharField(max_length=80)
    user_id = models.PositiveIntegerField()
    store_method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True,max_length=6)
    category_one_id = models.CharField(max_length=32)
    category_url = models.CharField(max_length=1000)
    platform_id = models.CharField(max_length=32)
    pagination_type = models.CharField(max_length=50)
    website_url = models.CharField(max_length=1000)
    status = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        ordering = ['-created_at']

# Create your models here.
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.FloatField()
#     description = models.CharField(max_length=1000)
#     creation_date = models.DateTimeField(auto_now_add=True)
#     store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="product_store")

#     def __str__(self):
#         return "%s" % (self.name)


# class Team(models.Model):
#     name = models.CharField(max_length=255)
#     logo = models.ImageField(upload_to="photos/team/")

#     def __str__(self):
#         return self.name

# class Player(models.Model):
#     common_name = models.CharField(max_length=255)
#     firstname = models.CharField(max_length=255)
#     lastname = models.CharField(max_length=255)
#     team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="player_team")
#     photo = models.ImageField(upload_to="photos/player/")
#     nationality = models.CharField(max_length=255)
#     age = models.PositiveIntegerField(max_length=255)

#     def __str__(self):
#         return self.name  


