from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# Create your models here.

class OnlineAccountModel(models.Model):
    account_url = models.URLField(blank=True,null=True);
    account_name = models.CharField(max_length=255, blank=False, null=False);
    account_type = models.CharField(max_length=128, blank=False, null=False);
    account_email = models.EmailField(max_length=255, blank=True, null=True);
    account_id = models.CharField(max_length=128, blank=True, null=True);
    account_link = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True);
    account_passwd = models.CharField(max_length=128, blank=True, null=True);
    account_passwd_chgDate = models.DateTimeField(blank=True, null=True);
    account_subscription_type = models.CharField(max_length=128, blank=True, null=True);
    account_subscription_payDate = models.DateTimeField(blank=True, null=True);
    account_2fa = models.CharField(max_length=255, blank=True, null=True);
    account_notes = models.TextField(blank=True, null=True);
    def __str__(self):
        return '%s' % (self.account_name)
    class Meta:
        unique_together = ('account_url', 'account_name')

class OnlineAccountForm(ModelForm):
    class Meta:
        model = OnlineAccountModel;
        fields = [ 
            'account_url',
            'account_name',
            'account_type',
            'account_email',
            'account_id',
            'account_link',
            'account_passwd',
            'account_passwd_chgDate',
            'account_subscription_type',
            'account_subscription_payDate',
            'account_2fa',
            'account_notes',
            ];
        labels = {
            'account_url': _('Account URL'),
            'account_link': _('Linked Authentication'),
            'account_passwd': _('Password Hint'),
            'account_passwd_chgDate': _('Next Password Change Date'),
            'account_subscription_type': _('Subscription Type'),
            'account_subscription_payDate': _('Next Subscription Payment'),
            'account_2fa': _('2FA Device'),
            'account_notes': _('Notes'),
            };
