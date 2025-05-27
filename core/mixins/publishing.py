from django.db import models


class PublishingMixinQuerySet(models.QuerySet):
    def published(self):
        """ Отфильтровывает неопубликованные записи """
        return self.filter(publish=True)


class PublishingMixinManager(models.Manager):
    def get_queryset(self):
        return PublishingMixinQuerySet(self.model, using=self._db)
        
    def published(self):
        """ Отфильтровывает неопубликованные записи """
        return self.get_queryset().published()


class PublishingMixin(models.Model):
    """
    Миксин, позволяющий иметь в базе данных "заготовки", оставляя их невидимыми для пользователей
    """
    
    publish  = models.BooleanField("Опубликован", default=True)

    class Meta:
        abstract = True