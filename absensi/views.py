from django.shortcuts import render,redirect,HttpResponse
from .models import absensi_kehadiran,kegiatan
from account.models import Profile
from .forms import absensiForm,dateForm,rincianForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from datetime import date, datetime


# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def administration(user):
    return user.groups.filter(name='sekretaris').exists()

def index_absensi(request):
    return render(request, 'index_absensi.html')

@login_required(login_url='customerlogin')
def absensi(request):
   profil = Profile.objects.get(user = request.user)
   cek = profil.role == 2 or profil.role == 3 or profil.role == 1
   if request.method == 'POST':
        form = absensiForm(request.POST, request.FILES)
        print(form.as_p)
        if form.is_valid():
            user = request.user
            kegiatan = form.cleaned_data['kegiatan']
            keterangan = form.cleaned_data['keterangan']
            status = form.cleaned_data['status']
            absensi_kehadiran(user = user, kegiatan=kegiatan,keterangan=keterangan, status=status).save()
            if status == 1:
             messages.success(request,'Absensi kehadiran kamu sudah berhasil terdata !')
            if status == 2:
             messages.success(request,'Absensi izin kamu sudah berhasil terdata !')
            else:
             messages.success(request,'Absensi ke tidakhadiran kamu sudah berhasil terdata !')
            return redirect('index_absensi')
        else:
            messages.error(request,'Mohon maaf proses absensi kamu gagal!')
            return redirect('index_absensi')
   else:
        context = {
            'form':absensiForm(),
            'cek':cek
        }
   return render(request, 'absensi.html',context)

@login_required
@user_passes_test(administration,login_url='index_absensi')
def list_kehadiran(request):
    pengurus = Profile.objects.get(user = request.user)
    now = datetime.now()
    current_year = now.strftime("%Y")
    current_month = now.strftime("%m")
    current_day = now.strftime("%d")
    tanggal = now.strftime("%A, %d %B %Y")
    saran = absensi_kehadiran.objects.filter(
        date_posted__year = current_year,
        date_posted__month = current_month,
        date_posted__day = current_day
        ).order_by('-date_posted')

    context = {
        'pengurus':pengurus,
        'day':tanggal,
        'hadir':saran,

    }
    return render(request, 'sekretaris/list_kehadiran.html',context)


@login_required
@user_passes_test(administration,login_url='index_absensi')
def search_rinci(request):
    pengurus = Profile.objects.get(user = request.user)

    if request.method == 'POST':
        form = rincianForm(request.POST)
        datee = request.POST['tanggal']
        print(datee)
        if form.is_valid():
            kegi = form.cleaned_data['kegiatan']
            sta = form.cleaned_data['status']
            dateba = absensi_kehadiran.objects.filter(kegiatan__nama_kegiatan__contains = kegi,status__contains=sta,date_posted__contains=datee)

            context = {
                'pengurus':pengurus,
                'hadir':dateba,
                'tanggal':datee,
                'form':rincianForm()
            }
            return render(request, 'sekretaris/search_rinci.html',context)
    else:
        context = {
                'pengurus':pengurus,
                'form':rincianForm()
            }
        return render(request, 'sekretaris/search_rinci.html', context)

@login_required(login_url='customerlogin')
@user_passes_test(administration,login_url='index_absensi')
def show_kehadiran(request, id):
  pi = absensi_kehadiran.objects.get(pk=id)
  context ={
     'pi':pi
  }
  return render(request, 'sekretaris/show_kehadiran.html',context)

@login_required(login_url='customerlogin')
@user_passes_test(administration,login_url='index_absensi')
def show_anggota(request, id):
  pi = Profile.objects.get(pk=id)
  context ={
     'pi':pi
  }
  return render(request, 'sekretaris/show_anggota.html',context)

@login_required
@user_passes_test(administration,login_url='index_absensi')
def list_nama(request):
    pengurus = Profile.objects.get(user = request.user)
    saran = absensi_kehadiran.objects.all()
    if request.method == "POST":
        pencarian = request.POST['pencarian']
        hasil = absensi_kehadiran.objects.filter(user__first_name__contains=pencarian)
        context = {
            'pengurus':pengurus,
            'saran':saran,
            'hadir':hasil,
            'pencarian':pencarian
        }
        return render(request, 'sekretaris/list_nama.html',context)
    else:
        return render(request, 'sekretaris/list_nama.html',{})

@login_required
@user_passes_test(administration,login_url='index_absensi')
def list_hadir(request):
    pengurus = Profile.objects.get(user = request.user)
    saran = absensi_kehadiran.objects.filter(status = 1).order_by('-date_posted')
    context = {
        'pengurus':pengurus,
        'hadir':saran,
    }
    return render(request, 'sekretaris/list_hadir.html',context)

@login_required
@user_passes_test(administration,login_url='index_absensi')
def list_izin(request):
    pengurus = Profile.objects.get(user = request.user)
    saran = absensi_kehadiran.objects.filter(status = 2).order_by('-date_posted')
    context = {
        'pengurus':pengurus,
        'hadir':saran,
    }
    return render(request, 'sekretaris/list_izin.html',context)

@login_required
@user_passes_test(administration,login_url='index_absensi')
def list_thadir(request):
    pengurus = Profile.objects.get(user = request.user)
    saran = absensi_kehadiran.objects.filter(status = 3).order_by('-date_posted')
    context = {
        'pengurus':pengurus,
        'hadir':saran,
    }
    return render(request, 'sekretaris/list_thadir.html',context)


@login_required
@user_passes_test(administration,login_url='index_absensi')
def list_pengurus(request):
    nama = Profile.objects.get(user = request.user)
    pengurus = Profile.objects.all()
    context = {
        'pengurus':pengurus,
        'nama':nama,
    }
    return render(request, 'sekretaris/list_pengurus.html',context)

@login_required
@user_passes_test(administration,login_url='index_absensi')
def list_petinggi(request):
    nama = Profile.objects.get(user = request.user)
    pengurus = Profile.objects.filter(role = 2)
    context = {
        'pengurus':pengurus,
        'nama':nama,
    }
    return render(request, 'pengurus/list_petinggi.html',context)
@login_required
@user_passes_test(administration,login_url='index_absensi')
def list_psdm(request):
    nama = Profile.objects.get(user = request.user)
    pengurus = Profile.objects.filter(role = 5)
    context = {
        'pengurus':pengurus,
        'nama':nama,
    }
    return render(request, 'pengurus/list_psdm.html',context)
@login_required
@user_passes_test(administration,login_url='index_absensi')
def list_sekretaris(request):
    nama = Profile.objects.get(user = request.user)
    pengurus = Profile.objects.filter(role = 3)
    context = {
        'pengurus':pengurus,
        'nama':nama,
    }
    return render(request, 'pengurus/list_sekretaris.html',context)
@login_required
@user_passes_test(administration,login_url='index_absensi')
def list_bendahara(request):
    nama = Profile.objects.get(user = request.user)
    pengurus = Profile.objects.filter(role = 4)
    context = {
        'pengurus':pengurus,
        'nama':nama,
    }
    return render(request, 'pengurus/list_bendahara.html',context)
@login_required
@user_passes_test(administration,login_url='index_absensi')
def list_medkom(request):
    nama = Profile.objects.get(user = request.user)
    pengurus = Profile.objects.filter(role = 6)
    context = {
        'pengurus':pengurus,
        'nama':nama,
    }
    return render(request, 'pengurus/list_medkom.html',context)

@login_required
@user_passes_test(administration,login_url='index_absensi')
def list_anggota(request):
    nama = Profile.objects.get(user = request.user)
    pengurus = Profile.objects.filter(role = 7)
    context = {
        'pengurus':pengurus,
        'nama':nama,
    }
    return render(request, 'pengurus/list_anggota.html',context)