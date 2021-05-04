from django.db import models
from django.db.models.fields import DecimalField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Ticket(models.Model):

    Title = models.CharField(_("Title"), max_length=50)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Capacity = models.IntegerField(_("Capacity"))
    Origin = models.ForeignKey(City, verbose_name=_("Origin"), on_delete=models.CASCADE)
    Destination = models.ForeignKey(City, verbose_name=_("Destination"), on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Ticket_detail", kwargs={"id": self.id})
