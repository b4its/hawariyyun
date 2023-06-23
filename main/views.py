from django.shortcuts import render
from survei.models import survei
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from account.models import Profile
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def administration(user):
    return user.groups.filter(name='sekretaris').exists()

@login_required(login_url='customerlogin')
def index(request):
    pengguna = request.user
    cek = survei.objects.filter(user = pengguna).exists()
    sekretaris = Profile.objects.filter(user = request.user ,role = 3) or Profile.objects.filter(user=request.user, role=1)
    medkom = Profile.objects.filter(user=request.user, role = 6 )
    context = {
        'cek':cek,
        'sekretaris':sekretaris
    }
    return render(request, 'index.html',context)

@login_required
@user_passes_test(administration,login_url='index_absensi')
def sekretaris(request):
    pengguna = request.user
    cek = Profile.objects.filter(user = request.user ,role = 4)
    nama = Profile.objects.get(user = request.user)
    pengurus = Profile.objects.get(user = request.user)

    context = {
        'cek':cek,
        'pengurus':pengurus,
        'nama':nama,
    }


    return render(request, 'sekretaris/sekretaris.html',context)
