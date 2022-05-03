from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=500, blank=True, verbose_name="Название")
    status = models.IntegerField(default=0, blank=True, verbose_name="Статус")

    class Meta:
        verbose_name = "мимика"
        verbose_name_plural = "мимика"

    def __str__(self):
        return self.title


class Category2(models.Model):
    title = models.CharField(max_length=500, blank=True, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    logo = models.ImageField(upload_to='upload', verbose_name="Фото", blank=True)
    status = models.IntegerField(default=0, blank=True, verbose_name="Статус")

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категория"

    def __str__(self):
        return self.title


class Grade(models.Model):
    photo = models.ImageField(upload_to='upload', verbose_name="Фото")
    ball = models.IntegerField(default=0)
    status = models.IntegerField(default=0, blank=True, verbose_name="Статус")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "оценка"
        verbose_name_plural = "оценка"

    def __str__(self):
        return self.category.title


class Video(models.Model):
    title = models.CharField(max_length=500, blank=True, verbose_name="Название")
    link_video = models.CharField(max_length=500, blank=True, verbose_name="Ссылка на видео")
    description = models.TextField(blank=True, verbose_name="Описание", default="")
    status = models.IntegerField(default=0, blank=True, verbose_name="Статус")

    class Meta:
        verbose_name = "видео"
        verbose_name_plural = "видео"

    def __str__(self):
        return self.title


class Info(models.Model):
    adress = models.CharField(max_length=500, blank=True, verbose_name="Адресс")
    phone = models.CharField(max_length=500, blank=True, verbose_name="Телефон")
    email = models.CharField(max_length=500, blank=True, verbose_name="email")
    fax = models.CharField(max_length=500, blank=True, verbose_name="FAX")

    class Meta:
        verbose_name = "инфо"
        verbose_name_plural = "инфо"

    def __str__(self):
        return self.adress


class SendMessage(models.Model):
    name = models.CharField(max_length=500, blank=True, verbose_name="Имя")
    email = models.CharField(max_length=500, blank=True, verbose_name="email")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "ообщение"
        verbose_name_plural = "сообщение"

    def __str__(self):
        return self.name

class Mark(models.Model):
    mark = models.IntegerField(blank=True)

    def __str__(self):
        return self.mark