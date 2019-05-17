from django.shortcuts import render, redirect, get_object_or_404

from django.forms import modelformset_factory
from .models import OnlineAccountForm
from .models import OnlineAccountModel

from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

import time
import datetime

fieldToNameMap = {
    'account_url': 'URL',
    'account_name': 'Name',
    'account_type': 'Type',
    'account_id': 'User Id',
    'account_email': 'Email',
    'account_passwd': 'Secret',
    'account_link': 'Auth Acct',
    };

visibleFields = {
    'account_url',
    'account_name',
    'account_type',
    'account_id',
    'account_passwd',
};

printFields = {
    'account_url',
    'account_name',
    'account_type',
    'account_id',
    'account_email',
    'account_passwd',
    'account_link',
};

urlFields = {
    'account_url',
};

def fieldsToNames(fieldList):
    returnList = [];
    for field in fieldList:
        if fieldToNameMap.get(field) is None:
            returnList.append(field);
        else:
            returnList.append(fieldToNameMap[field]);
    return returnList;

def fieldsToVisible(fieldList):
    returnList = [];
    for field in fieldList:
        if field in visibleFields:
            returnList.append(1);
        else:
            returnList.append(0);
    return returnList;

def getUrlFields(fieldList):
    returnList = [];
    idx = 0;
    for field in fieldList:
        if field in urlFields:
            returnList.append(idx);
        idx += 1;
    return returnList;

def replaceNone(data):
    for record in data:
        for idx in range(len(record)):
            if record[idx] == None:
                record[idx] = 'None';

def replaceDates(data):
    for record in data:
        for idx in range(len(record)):
            if type(record[idx]) is datetime.datetime:
                record[idx] = str(record[idx]);

# Create your views here.

class MainView(TemplateView):
    template_name = 'main.html';
    def get(self, request, *args, **kwargs):
        context = {};
        num_records = OnlineAccountModel.objects.all().count();
        context['numRecs'] = num_records;
        return render(request, 'account_tool/main.html', context);

class SecureView(LoginRequiredMixin, TemplateView):
    template_name = 'secure.html';
    login_url = '/login/';

    def get(self, request, *args, **kwargs):
        context = {};
        queryset = OnlineAccountModel.objects.all();
        num_records = queryset.count();
        context['numRecs'] = num_records;

        # The first element from _meta.get_fields() is the name of the model. That's cut.
        fields = [f.name for f in OnlineAccountModel._meta.get_fields()][1:]
        resultsList = [];
        if queryset.count() > 0:
            resultsList = [list(item) for item in
                           queryset.values_list(*fields)];
            replaceNone(resultsList);
            replaceDates(resultsList);

        context['results'] = resultsList;
        context['header'] = fieldsToNames(fields);
        context['visible'] = fieldsToVisible(fields);
        context['toPrint'] = fieldsToNames(printFields);
        context['urlFieldIndices'] = getUrlFields(fields);
        return render(request, 'account_tool/secure.html', context);

class InputFormView(LoginRequiredMixin, TemplateView):
    template_name = "input_form.html";
    login_url = '/login/';
    def get(self, request, *args, **kwargs):
        context = {};
        formset = OnlineAccountForm();
        context['formset'] = formset;
        return render(request, 'account_tool/input_form.html', context);
    def post(self, request, *args, **kwargs):
        context = {};
        formset = OnlineAccountForm(request.POST, request.FILES);
        # This form will report errors reported at formset.save()
        if formset.is_valid():
            formset.save();
            return redirect('secure');
        context['formset'] = formset;
        return render(request, 'account_tool/input_form.html', context);

class UpdateRecordView(LoginRequiredMixin, TemplateView):
    login_url = '/login/';
    def get(self, request, *args, **kwargs):
        context = {};
        context['input_id'] = 'None';
        if request.GET.get('record'):
            input_id = request.GET['record'];
            try:
                rec_instance = OnlineAccountModel.objects.get(id=input_id);
                formset = OnlineAccountForm(instance=rec_instance);
                context['input_id'] = input_id;
                context['formset'] = formset;
            except OnlineAccountModel.DoesNotExist:
                context['input_id'] = input_id;
        return render(request, 'account_tool/update_rec.html', context);
    def post(self, request, *args, **kwargs):
        context = {};
        rec_instance = None;
        try:
            rec_instance = OnlineAccountModel.objects.get(id=request.POST['input_id']);
                                                          
        except OnlineAccountModel.DoesNotExist:
            rec_instance = None;
        formset = OnlineAccountForm(request.POST, instance=rec_instance);
        if formset.is_valid():
            formset.save();
            return redirect('secure');
        context['formset'] = formset;
        return render(request, 'account_tool/update_rec.html', context);
