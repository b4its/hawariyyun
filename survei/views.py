from django.shortcuts import render,redirect
from .models import jawaban_pilgan,survei
from django.forms import formset_factory
from .forms import jawabanForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from datetime import date, datetime
from account.models import Profile
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def administration(user):
    return user.groups.filter(name='sekretaris').exists()

@login_required(login_url='customerlogin')
def index_survei(request):
    ngecek = survei.objects.filter(user=request.user).exists()
    if ngecek:
        messages.warning(request,'Anda telah mengisi survei, tidak dapat mengisi lagi')
        return redirect('index')
    else:
        if request.method == 'POST':
            form = jawabanForm(request.POST)
            if form.is_valid ():
                user= request.user
                nomor1 = request.POST['nomor1']
                nomor2 = request.POST['nomor2']
                nomor3 = request.POST['nomor3']
                nomor4 = form.cleaned_data['nomor4']
                nomor5 = request.POST['nomor5']
                nomor6 = request.POST['nomor6']
                nomor7 = request.POST['nomor7']
                nomor8 = request.POST['nomor8']
                nomor9 = request.POST['nomor9']
                nomor10 = request.POST['nomor10']

                survei(user = user,nomor1=nomor1,nomor2=nomor2,nomor3=nomor3,nomor4=nomor4,nomor5=nomor5,nomor6=nomor6,
                nomor7=nomor7,nomor8=nomor8,nomor9=nomor9,nomor10=nomor10

                ).save()
                messages.success(request,'Terima kasih telah mengisi survei minat dan bakat :)')
                return redirect('index')
            else:
                messages.error(request,'Proses anda telah gagal')
                return redirect('index')
        context = {
            'form':jawabanForm()
        }

    return render(request, 'index_survei.html', context)

@login_required
@user_passes_test(administration,login_url='index_absensi')
def sekretaris_survei(request):
    pengurus = Profile.objects.get(user = request.user)
    now = datetime.now()
    current_year = now.strftime("%Y")
    current_month = now.strftime("%m")
    current_day = now.strftime("%d")
    tanggal = now.strftime("%A, %d %B %Y")
    saran = survei.objects.all().order_by('-date_posted')
    context = {
        'pengurus':pengurus,
        'day':tanggal,
        'hadir':saran,

    }
    return render(request, 'sekretaris/sekretaris_survei.html',context)

@login_required
@user_passes_test(administration,login_url='index_absensi')
def show_survei(request, id):
  pi = survei.objects.get(pk=id)
  profil = Profile.objects.get(user = pi.user)
  context ={
     'pi':pi,
     'profile':profil
  }
  return render(request, 'sekretaris/show_survei.html',context)

@login_required
@user_passes_test(administration,login_url='index_absensi')
def survei_nama(request):
    pengurus = Profile.objects.get(user = request.user)
    saran = survei.objects.all()
    if request.method == "POST":
        pencarian = request.POST['pencarian']
        hasil = survei.objects.filter(user__first_name__contains=pencarian)
        context = {
            'pengurus':pengurus,
            'saran':saran,
            'hadir':hasil,
            'pencarian':pencarian
        }
        return render(request, 'sekretaris/survei_nama.html',context)
    else:
        return render(request, 'sekretaris/survei_nama.html',{})




