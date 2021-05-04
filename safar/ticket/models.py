from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from uuslug import uuslug 
from phonenumber_field.modelfields import PhoneNumberField


class City(models.Model):

    name = models.CharField(max_length=20, unique=True)


    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("city_detail", kwargs={"pk": self.pk})


class Agency(models.Model):

    TYPE_CHOICES = [
        ('FL', 'Flight'),
        ('TR', 'Train'),
        ('BU', 'Bus'),
    ]

    name = models.CharField(max_length=35)
    slug = models.CharField(max_length=200, blank=True, unique=True)
    phone = PhoneNumberField(_("Phone Number"))
    email = models.EmailField(_("Email"), max_length=50)
    logo = models.ImageField(upload_to='logos/', default='logos/default.jpeg')
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
    )

    class Meta:
        verbose_name = "Agency"
        verbose_name_plural = "Agencies"

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("ticket:agency", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
         self.slug = uuslug(self.name, instance=self)
         super(Agency, self).save(*args, **kwargs)


class Ticket(models.Model):

    title = models.CharField(_("Title"), max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    agency = models.ForeignKey(Agency, related_name="%(class)s_tickets", on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField(_("Capacity"))
    origin = models.ForeignKey(City, verbose_name=_("Origin"), related_name="%(class)s_origins", on_delete=models.CASCADE)
    destination = models.ForeignKey(City, verbose_name=_("Destination"), related_name="%(class)s_destinations", on_delete=models.CASCADE)
    starts = models.DateTimeField(_("Starts at"))
    arrives = models.DateTimeField(_("Arrives at"))
    
    class Meta:
        abstract = True
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")

    def __str__(self):
        return "{} : {}".format(self.title, self.starts)

    def get_minimum_by_date(self, date):
        objects = Ticket.objects.filter(starts=date)


class Flight(Ticket):

    CLASS_CHOICES = [
        ('EC', 'Economy'),
        ('BS', 'Business'),
    ]

    flight_class = models.CharField(
        max_length=2,
        choices=CLASS_CHOICES,
    )


    class Meta:

        verbose_name = _("Flight")
        verbose_name_plural = _("Flights")

    def __str__(self):
        return "{} : {}".format(self.title, self.starts)

    def get_absolute_url(self):
        return reverse("ticket:flight_detail", kwargs={"id": self.id})


class Bus(Ticket):


    BUS_TYPE_CHOICES = [
        ('VIP', 'VIP'),
        ('CLS', 'Classic'),
    ]

    bus_type = models.CharField(
        max_length=3,
        choices=BUS_TYPE_CHOICES,
    )


    class Meta:
        verbose_name = _("Bus")
        verbose_name_plural = _("Buses")


    def get_absolute_url(self):
        return reverse("ticket:bus_detail", kwargs={"id": self.id})



class Train(models.Model):

    train_type = models.CharField(_("Train Type"), max_length=20)

    class Meta:
        verbose_name = _("Train")
        verbose_name_plural = _("Trains")


    def get_absolute_url(self):
        return reverse("ticket:train_detail", kwargs={"id": self.id})


class MiddleWayStaion(models.Model):

    city = models.ForeignKey(City, verbose_name=_("City"), on_delete=models.CASCADE)
    train = models.ForeignKey(Train, verbose_name=_(""), related_name="middle_ways", on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("MiddleWayStaion")
        verbose_name_plural = _("MiddleWayStaions")


    def get_absolute_url(self):
        return reverse("MiddleWayStaion_detail", kwargs={"pk": self.pk})


