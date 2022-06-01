from django.db import models


class Home(models.Model):
    title = models.CharField('Титул', max_length=255)
    address = models.CharField('Адрес', max_length=255)
    description = models.TextField('Сипаттама')
    price = models.IntegerField('Бағасы', blank=True, null=True)
    slug = models.SlugField()
    image = models.ImageField('Сурет', upload_to='receive_housing/')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'homes'
        verbose_name = "Үй туралы мәлімет"
        verbose_name_plural = "Үй туралы мәліметтер"


class HomeShots(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Изображение", upload_to="Home_shots/")
    vehicle = models.ForeignKey(Home, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'images_home'
        verbose_name = "Сурет"
        verbose_name_plural = "Суреттер"


class Jer(models.Model):
    name = models.CharField('Аты', max_length=255)
    rayon = models.CharField('Аудан', max_length=255)
    village = models.CharField('Ауыл', max_length=255)
    description = models.TextField('Сипаттама')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'zher'
        verbose_name = "Жер туралы мәлімет"
        verbose_name_plural = "Жер туралы мәліметер"


class Data(models.Model):
    title = models.CharField('Титул', max_length=255)
    description = models.TextField('Сипаттама')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'datasmodel'
        verbose_name = "Жалпы мәлімет"
        verbose_name_plural = "Жалпы мәліметер"


class CategoryNews(models.Model):
    name = models.CharField('Категория аты', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categorynews'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категориялар'


class News(models.Model):
    title = models.CharField('Тақырыбы', max_length=255)
    description = models.TextField('Мәтіні')
    image = models.ImageField('Сурет', upload_to='news/')
    slug = models.SlugField()
    yout = models.CharField('Жаңалыққа сілтеме', max_length=2000, null=True, blank=True)
    category = models.ForeignKey(CategoryNews, verbose_name='Категория', on_delete=models.CASCADE)
    created_at = models.DateTimeField('Жарияланған күні', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news'
        verbose_name = "Жаңалық"
        verbose_name_plural = "Жаңалықтар"


class Vakancia(models.Model):
    region = models.CharField('Аймақ', max_length=500)
    qyzmet = models.TextField('Қызмет')

    def __str__(self):
        return f"{self.region} - {self.qyzmet}"

    class Meta:
        db_table = 'vakancia'
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансиялар"


class RequestHelp(models.Model):
    ch = [
        ('Ақшалай', 'Ақшалай'),
        ('Жұмыс', 'Жұмыс'),
        ('Үй', 'Үй'),
        ('Гуманитарлық', 'Гуманитарлық'),
    ]
    name = models.CharField("Есіміңіз", max_length=100)
    surname = models.CharField("Тегіңіз", max_length=100)
    nomer = models.CharField("Телефон номер", max_length=11)
    req = models.CharField("Көмек түрі", choices=ch, max_length=100)
    email = models.EmailField()
    publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.name} - {self.email}"

    class Meta:
        db_table = 'requesthelp'
        verbose_name = "Әлеуметтік көмек"
        verbose_name_plural = "Әлеуметтік көмектер"


class OtinishVak(models.Model):
    name = models.CharField("Есіміңіз", max_length=100)
    surname = models.CharField("Тегіңіз", max_length=100)
    nomer = models.CharField("Телефон номер", max_length=11)
    vakancia = models.ForeignKey(Vakancia, verbose_name='Вакансия', on_delete=models.CASCADE)
    email = models.EmailField()
    publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.surname} - {self.email}"

    class Meta:
        db_table = 'otinishvak'
        verbose_name = "Бос жұмыс орындарына өтініш"
        verbose_name_plural = "Бос жұмыс орындарына өтініштер"


class Questions(models.Model):
    name = models.CharField("Есімі", max_length=100)
    text = models.TextField("Хабарлама", max_length=5000)

    email = models.EmailField()
    publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        db_table = 'questions'
        verbose_name = "Сұрақ"
        verbose_name_plural = "Сұрақтар"


class Reviews(models.Model):
    name = models.CharField("Есімі", max_length=100)
    surname = models.CharField("Тегі", max_length=100)
    email = models.EmailField()
    text = models.TextField("Хабарлама", max_length=5000)
    image = models.ImageField('Суреті', upload_to='reviews/', blank=True)
    publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.surname} -{self.email}"

    class Meta:
        db_table = 'reviews'
        verbose_name = "Пікір"
        verbose_name_plural = "Пікірлер"
