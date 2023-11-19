from django.db import models



class Home(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='home/image', blank=True)
    slide = models.ImageField(upload_to='home/slide', blank=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'


class Service(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    icons = models.ImageField(upload_to='service/image', blank=True)
    icons_title = models.CharField(max_length=255, blank=True)
    icons_sub_title = models.CharField(max_length=255, blank=True)
    

    def __str__(self) -> str:
        return self.title
    


    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class About(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='about/image', blank=True)
    slide = models.ImageField(upload_to='about/slide', blank=True)
    text_title = models.CharField(max_length=255, blank=True)
    text_sub_title = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'



class WhyChoose(models.Model):
    title = models.CharField(max_length=255, blank=True)
    icons = models.ImageField(upload_to='why/image', blank=True)
    icons_title = models.CharField(max_length=255, blank=True)
    icons_sub_title = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'WhyChoose'
        verbose_name_plural = 'WhyChooses'


class Team(models.Model):
    title = models.CharField(max_length=255, blank=True)
    person_photo = models.ImageField(upload_to='team/photos', blank=True)
    person_name = models.CharField(max_length=255, blank=True)
    person_business = models.CharField(max_length=255, blank=True)
    

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'    



class Customer(models.Model):
    title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='customer/image', blank=True)
    name = models.CharField(max_length=255, blank=True)
    about = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

        