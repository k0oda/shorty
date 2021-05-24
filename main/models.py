from django.db import models


class Link(models.Model):
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
        ordering = ['date_of_creation',]

    original_url = models.URLField()
    code = models.CharField(max_length=6)
    date_of_creation = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.shortened_url


class Connection(models.Model):
    class Meta:
        verbose_name = 'Connection'
        verbose_name_plural = 'Connections'
        ordering = ['-date', '-time',]
    
    address = models.GenericIPAddressField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    link = models.ForeignKey('Link', on_delete=models.CASCADE)

    def __str__(self):
        return self.address
