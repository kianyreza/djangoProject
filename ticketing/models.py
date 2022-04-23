from django.db import models

# Create your models here.
class Movie (models.Model):
    """
    Represents a movie
    """
    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم'
    name = models.CharField('عنوان', max_length=100)
    director = models.CharField('کارگردان', max_length=50)
    year = models.IntegerField('سال تولید')
    length = models.IntegerField('مدت زمان')
    description = models.TextField('توضیحات')

    def __str__(self):
        return self.name


class Cinema(models.Model):
    """
    fefeffefefefef
    """
    class Meta:
        verbose_name = 'سینما'
        verbose_name_plural = 'سینما'
    cinema_code = models.IntegerField('کد سینما', primary_key=True)
    name = models.CharField('نام', max_length=50)
    city = models.CharField('شهر', max_length=30, default='تهران')
    capacity = models.IntegerField('ظرفیت')
    phone = models.CharField('تلفن', max_length=20, null=True)
    address = models.TextField('آدرس')

    def __str__(self):
        return self.name


class ShowTime(models.Model):
    """
    gegggggegeg
    """
    class Meta:
        verbose_name = 'نمایش'
        verbose_name_plural = 'نمایش'
    movie = models.ForeignKey('Movie', on_delete=models.PROTECT, verbose_name='عنوان فیلم')
    cinema = models.ForeignKey('Cinema', on_delete=models.PROTECT, verbose_name='سینما')
    start_time = models.DateTimeField('تاریخ نمایش')
    price = models.IntegerField('قیمت')
    salable_seats = models.IntegerField('تعداد صندلی های قابل فروش')
    free_seats = models.IntegerField('تعداد صندلی های باقیمانده')
    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKETS_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6
    status_choices = (
        (SALE_NOT_STARTED, 'فروش آغاز نشده است.'),
        (SALE_OPEN, 'در حال فروش بلیت'),
        (TICKETS_SOLD, 'بلیت ها تمام شد'),
        (SALE_CLOSED, 'فروش بلیت بسته شد.'),
        (MOVIE_PLAYED, 'فیلم پخش شد. '),
        (SHOW_CANCELED, 'سانس لغو شد.'),
    )

    status = models.IntegerField('وضعیت', choices=status_choices)

    def __str__(self):
        return '{} - {} - {}'.format(self.movie, self.cinema, self.start_time)
