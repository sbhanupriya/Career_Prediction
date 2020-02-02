from django.shortcuts import render
from django.http import HttpResponse
from .models  import dataset
from .models import page
from .ml import model
import pandas as pd
import pickle
from .models import page
from django.shortcuts import redirect
# Create your views here.

def login(request):
    if request.method=='POST':
        user1=request.POST.get("username")
        pass1=request.POST.get("password")
        from django.contrib import auth
        x=auth.authenticate(username=user1,password=pass1)
        if x is None:
            return redirect('start/home/')
        else:
            return redirect('start/form/')
def login2(request):
    print("false")
    x1=request.POST.get("name")
    x3=request.POST.get("emailid")
    x2=request.POST.get("password")
    obj1=page(username=x1,emailid=x3,password=x2)
    obj1.save()
    print("trur")
    return redirect('start/form/')

def home(request):
    return render(request, 'app1/index.html')

def  form(request):
    return render(request, 'app1/a.html')

def  signup(request):
    return render(request, 'app1/signuppage.html')
def mod(request):
    model()
    return HttpResponse('model trained')

def final(request):
    osmarks=request.POST.get("osmarks")
    algomarks = request.POST.get("algomarks")
    progmarks = request.POST.get("progmarks")
    softmarks=request.POST.get("softmarks")
    cnmarks=request.POST.get("cnmarks")
    electromarks=request.POST.get("electromarks")
    coamarks=request.POST.get("coamarks")
    mamarks=request.POST.get("mamarks")
    commmarks=request.POST.get("commmarks")
    workcap=request.POST.get("workcap")
    logical=request.POST.get("logical")
    hackathon=request.POST.get("hackathon")
    coding = request.POST.get("coding")
    pubspeaking = request.POST.get("pubspeaking")
    canwork = request.POST.get("canwork")
    selflearn = request.POST.get("selflearn")
    extracurr = request.POST.get("extracurr")
    certificates = request.POST.get("certificates")
    workshop=request.POST.get("workshop")
    talent = request.POST.get("talent")
    olympiad = request.POST.get("olympiad")
    readwrite = request.POST.get("readwrite")
    retention = request.POST.get("retention")
    interestsub = request.POST.get("interestsub")
    interestca = request.POST.get("interestca")
    jobstudy = request.POST.get("jobstudy")
    company = request.POST.get("company")
    seniorhelp = request.POST.get("seniorhelp")
    games = request.POST.get("games")
    print(games)
    prefsalarywork = request.POST.get("prefsalarywork")
    singlemingle = request.POST.get("singlemingle")
    gentlestubborn = request.POST.get("gentlestubborn")
    managetech = request.POST.get("managetech")
    hardsmart =request.POST.get("hardsmart")
    teamplayer = request.POST.get("teamplayer")
    introvert = request.POST.get("introvert")
    with open('model_pickel.bin','rb') as f:
        mp=pickle.load(f)
    print('first')
    print(hardsmart)
    print('123')

    #with open('labelencoder.bin', 'rb') as ff:
     #   le = pickle.load(ff)
    #l=pd.DataFrame(l)
    import os
    import pandas as pd
    import numpy as np
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(BASE_DIR, "app1")
    file2 = os.path.join(filepath, "roo_data.csv")
    dataset = pd.read_csv(file2)
    data = dataset.iloc[:, :-1].values
    label = dataset.iloc[:, -1].values
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    le = LabelEncoder()


    data[:,14] = le.fit(data[:,14])
    canwork= le.transform([canwork])
    data[:, 15] = le.fit(data[:, 15])
    selflearn = le.transform([selflearn])
    data[:, 16] = le.fit(data[:, 16])
    extracurr = le.transform([extracurr])
    data[:, 17] = le.fit(data[:, 17])
    certificates = le.transform([certificates])
    data[:,18] = le.fit(data[:,18])
    workshop= le.transform([workshop])
    data[:, 19] = le.fit(data[:, 19])
    talent = le.transform([talent])
    data[:, 20] = le.fit(data[:, 20])
    olympiad = le.transform([olympiad])
    data[:, 21] = le.fit(data[:, 21])
    readwrite = le.transform([readwrite])
    data[:, 22] = le.fit(data[:, 22])
    retention = le.transform([retention])
    data[:, 23] = le.fit(data[:, 23])
    interestsub = le.transform([interestsub])
    data[:, 24] = le.fit(data[:, 24])
    interestca = le.transform([interestca])
    data[:, 25] = le.fit(data[:, 25])
    jobstudy = le.transform([jobstudy])
    data[:, 26] = le.fit(data[:, 26])
    company = le.transform([company])
    data[:, 27] = le.fit(data[:, 27])
    seniorhelp = le.transform([seniorhelp])
    data[:, 28] = le.fit(data[:, 28])
    games = le.transform([games])
    data[:, 29] = le.fit(data[:, 29])
    prefsalarywork = le.transform([prefsalarywork])
    data[:, 30] = le.fit(data[:, 30])
    singlemingle = le.transform([singlemingle])
    data[:, 31] = le.fit(data[:, 31])
    gentlestubborn = le.transform([gentlestubborn])
    data[:, 32] = le.fit(data[:, 32])
    managetech = le.transform([managetech])
    data[:, 33] = le.fit(data[:, 33])
    hardsmart = le.transform([hardsmart])

    data[:, 34] = le.fit(data[:, 34])
    teamplayer = le.transform([teamplayer])
    data[:, 35] = le.fit(data[:, 35])
    introvert = le.transform([introvert])
    label=le.fit(label)
    print('second')
    print(hardsmart)
    listm = [int(osmarks), int(algomarks), int(progmarks), int(softmarks), int(cnmarks), int(electromarks), int(coamarks), int(mamarks), int(commmarks), workcap,
             int(logical), int(hackathon), int(coding), int(pubspeaking), canwork[0]
        , selflearn[0],
             extracurr[0], certificates[0], workshop[0], talent[0], olympiad[0], readwrite[0], retention[0], interestsub[0], interestca[0],
             jobstudy[0], company[0]
        , seniorhelp[0], games[0], prefsalarywork[0], singlemingle[0], gentlestubborn[0], managetech[0], hardsmart[0], teamplayer[0], introvert[0]]
    listm=np.array(listm).reshape(1,-1)
    career_pred=mp.predict(listm)
    print(type(career_pred))
    print(career_pred)
    career_pred=le.inverse_transform([career_pred[0]])
    print(career_pred)
    res=str(career_pred[0])
    res=[res]
    print(type(res))
    """obj1=dataset(osmarks=osmarks,algomarks=algomarks,progmarks=progmarks,softmarks=softmarks,cnmarks=cnmarks,electromarks=electromarks,coamarks=coamarks,
                 mamarks=mamarks,commmarks=commmarks,workcap=workcap,logical=logical,hackathon=hackathon,coding=coding,pubspeaking=pubspeaking,canwork=canwork,
                 selflearn=selflearn,extracurr=extracurr,certificates=certificates,workshop=workshop,talent=talent,olympiad=olympiad,readwrite=readwrite,
                 retention=retention,interestsub=interestsub,interestca=interestca,jobstudy=jobstudy,
                 company=company,seniorhelp=seniorhelp,games=games,prefsalarywork=prefsalarywork,singlemingle=singlemingle,
                 gentlestubborn=gentlestubborn,managetech=managetech,hardsmart=hardsmart,teamplayer=teamplayer,introvert=introvert,
                 result=res)
    obj1.save()
    print('345')
    xyz = dataset.objects.all()"""
    my_dict={'career':res}
    print('678')
    return render(request,'app1/output.html',context=my_dict)
