from django.urls import path,include
from . import views
urlpatterns=[
    path('workapp',views.wrkfn,name='workapp'),
    path('emea',views.emeafn,name='emea'),
    path('home',views.homefn,name='home'),
    path('institution',views.instifn,name='institution'),
    path('studentszone',views.stdzfn,name='studentszone'),
    path('department',views.deptfn,name='department'),
    path('acadamics',views.acadfn,name='acadamics'),
    path('product',views.pfn,name='product'),
    path('baabtra',views.bfn,name='baabtra'),
    path('courses',views.cfn,name='courses'),
    path('contact',views.confn,name='contact'),
    path('facebook',views.fbfn,name='facebook'),
    path('about',views.abfn,name='about'),
    path('master',views.mfn,name='master'),
    path('delim',views.defn,name='delim'),
    path('if',views.iffn,name='if'),
    path('formjinja',views.formfn,name='formjinja'),
    path('tribute',views.tributefn,name='tribute'),


    
    path('signup',views.signupfn,name='signup'),
    path('login',views.loginfn,name='login'),
    path('binary',views.binaryfn,name='binary'),
    path('delete_user',views.deletefn,name='delete_user'),
    path('new',views.newfn,name='new'),
    path('logout',views.logoutfn,name='logout'),
    path('addpro',views.addprofn,name='addpro'),
    path('displaypro',views.disprofn,name='displaypro'),
    path('api',views.apifn,name='api'),

    # ajax
    path('check',views.checkfn,name='check'),
    path('adduser',views.adduserfn,name='adduser'),
    path('ajax',views.ajaxfn,name='ajax')
    
]