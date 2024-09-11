from django.db                   import models
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not email:
            raise ValueError('Users must have an email')
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id       = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length = 30, unique=True)
    lastname   = models.CharField('Lastname', max_length = 30)
    email    = models.EmailField('Email',   max_length = 100, unique=True)
    password = models.CharField('Password', max_length = 256)
    lastChangeDate  = models.DateTimeField(auto_now=True) 
    firstQuestion   = models.CharField(max_length=100 )
    secondQuestion  = models.CharField(max_length=100)
    thirdQuestion   = models.CharField(max_length=100)
    isActivate      = models.BooleanField(default=True)
    image           = models.CharField()



    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'email'