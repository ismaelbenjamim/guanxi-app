import re
import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from guanxi_app.utils import generate_security_code


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class ComissionType(models.TextChoices):
    PERCENTAGE = "PERCENTAGE"
    FIXED = "FIXED"


class UserType:
    ADMIN = "ADMIN"
    SUPPORT = "SUPPORT"
    MANAGER = "MANAGER"
    OPERATOR = "OPERATOR"
    CUSTOMER = "CUSTOMER"

    TYPES = (
        (ADMIN, "ADMIN"),
        (SUPPORT, "SUPPORT"),
        (MANAGER, "MANAGER"),
        (OPERATOR, "OPERATOR"),
        (CUSTOMER, "CUSTOMER"),
    )


class UserStatus(models.TextChoices):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REPROVED = "REPROVED"
    BANNED = "BANNED"


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=10, choices=UserStatus.choices, default=UserStatus.PENDING)
    type = models.CharField(
        max_length=20,
        choices=UserType.TYPES,
        default=UserType.CUSTOMER
    )
    email_verified = models.BooleanField(default=False)
    is_fist_access = models.BooleanField(default=True)
    birthday = models.DateField(null=True, blank=True)
    security_code = models.CharField(max_length=6, default=generate_security_code)
    mother_name = models.CharField(max_length=150, null=True, blank=True)

    comission_type = models.CharField(max_length=10, choices=ComissionType.choices, default=ComissionType.PERCENTAGE)
    comission_value = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    manager_star = models.IntegerField(default=0)

    address_street = models.CharField(max_length=150, null=True, blank=True)
    address_number = models.IntegerField(null=True, blank=True)
    address_complement = models.CharField(max_length=150, null=True, blank=True)
    address_district = models.CharField(max_length=150, null=True, blank=True)
    address_city = models.CharField(max_length=150, null=True, blank=True)
    address_state = models.CharField(max_length=150, null=True, blank=True)
    address_country = models.CharField(max_length=150, null=True, blank=True)
    address_postal_code = models.IntegerField(null=True, blank=True)

    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'

    @property
    def cpf_with_mask(self):
        if self.cpf and len(self.cpf) == 11:
            return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
        return self.cpf

    def generate_security_code(self):
        self.security_code = generate_security_code()
        self.save()
        return self.security_code

    def save(self, *args, **kwargs):
        if self.status == UserStatus.BANNED:
            self.is_active = False
        if self.cpf:
            self.cpf = re.sub(r'\D', '', self.cpf)
        if self.contact:
            self.contact = re.sub(r'\D', '', self.contact)

        super().save(*args, **kwargs)


class Account(models.Model):
    class AccountStatus(models.TextChoices):
        PENDING = "PENDING", "Pendente"
        PROCESSING_ERROR = "PROCESSING_ERROR", "Falha no processamento"
        PROCESSING = "PROCESSING", "Processando"
        WAITING_CODE = "WAITING_CODE", "Aguardando código de autenticação"
        CONFIRMED = "CONFIRMED", "Conta Confirmada"


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, unique=True)
    session_user_id = models.CharField(max_length=200, null=True, blank=True)
    session_id = models.CharField(max_length=200, null=True, blank=True)
    session_data = models.FileField(upload_to='sessions/', null=True, blank=True)
    temp_code = models.CharField(max_length=10, null=True, blank=True)
    status = models.CharField(max_length=20, choices=AccountStatus.choices, default=AccountStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}'


class Follower(models.Model):
    """
    Armazena os seguidores baixados de uma determinada conta, permitindo retomar o processamento.
    """
    class Status:
        PENDING = 'pending'
        PROCESSED = 'processed'
        ERROR = 'error'

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    follower_id = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20,
        choices=[
            (Status.PENDING, 'Pendente'),
            (Status.PROCESSED, 'Processado'),
            (Status.ERROR, 'Erro')
        ],
        default=Status.PENDING
    )
    last_error = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account.username} - {self.follower_id}"

    class Meta:
        unique_together = ('account', 'follower_id')
