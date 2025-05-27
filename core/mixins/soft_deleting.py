from django.db import models


class SoftDeleteMixinQuerySet(models.QuerySet):
    def undeleted(self):
        """ Отфильтровывает удаленные записи """
        return self.filter(publish=True)


class SoftDeleteMixinManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteMixinQuerySet(self.model, using=self._db)
        
    def undeleted(self):
        """ Отфильтровывает удаленные записи """
        return self.get_queryset().undeleted()


class SoftDeleteMixin(models.Model):
    """
    Позволяет скрыть данные от пользователя без реального удаления данных
    """
    is_delete = models.BooleanField("Помечен на удаление", default=False)
    
    objects = SoftDeleteMixinManager() 

    def soft_delete(self):
        """Помечает как удаленную"""
        self.is_delete = True
        self.save(update_fields=['is_delete'])
        
    def restore(self):
        """Помечает запись как не удаленную. Даже в случае если она и так была помечена как не удаленная."""
        self.is_delete = False
        self.save(update_fields=['is_delete'])

    class Meta:
        abstract = True
        