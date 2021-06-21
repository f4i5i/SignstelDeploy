from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from PIL import Image



class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, phone,password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        user = self.model( phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.IntegerField(unique=True, null=True)
    email = models.EmailField(_('email address'), null=True,unique=True)
    phone = models.CharField(_('phone'), max_length=100 ,unique=True, null=False)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()




class Profile(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    CITIES = (
        ('Wah', 'Wah'),('Taxila', 'Taxila'),('Kohat','Kohat'),('Vehari','Vehari'),
        ('Chakwal','Chakwal'),('Kalar Kahar','Kalar Kahar'), ('Sangla Hill','Sangla Hill'),
        ('Shah Kot','Shah Kot'),('Gojra','Gojra'),('Toba Tek Singh','Toba Tek Singh'),('Multan','Multan'),
        )

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    cnic = models.CharField(max_length=100 ,unique=True, null=True)
    dob = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add= True, null=True )
    gender = models.CharField(max_length=100, null=True, choices=GENDER )
    city = models.CharField(max_length=500, null=True, choices=CITIES )
    area = models.CharField(max_length=500, null=True)
    postalCode = models.IntegerField(null=True)
    aboutMe= models.TextField(max_length=2000, null=True)
    address= models.TextField(max_length=2000, null=True)
    image = models.ImageField(default ='PP.jpg', upload_to ='profile_pics')

    def __str__(self):
        return f'{self.user.first_name} Profile'
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (128, 128)
            img.thumbnail(output_size)
            img.save(self.image.path)