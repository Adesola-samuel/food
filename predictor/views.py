from django.shortcuts import render, redirect
import pandas as pd
from joblib import load
from .forms import PredictionForm, ReserveForm
from .variables import y_var
from .models import Prediction, Reservation


algorithm = load(open('./algols/DecisionTreeClassifier.joblib','rb'))

def index(request):
    context = {}
    if request.POST:
        form = ReserveForm(request.POST)
        if form.is_valid:
            res = Reservation(
                first_name = request.POST.get('first_name'),
                last_name = request.POST.get('last_name'),
                email = request.POST.get('email'),
                phone = request.POST.get('phone'),
                reserv_date = request.POST.get('reserv_date'),
                numb_guests = request.POST.get('numb_guests'),
                alt_reserv_date = request.POST.get('alt_reserv_date'),
                time = request.POST.get('time'),
            )
            res.save()
            context['msg']='Reservation Successful'
    else:
        pass
    return render(request, 'index.html', context)

def predictor(request):
    context = {}
    if request.POST:
        form = PredictionForm(request.POST)
        if form.is_valid:
            rice = request.POST.get('rice')
            pounded_yam = request.POST.get('pounded_yam')
            fresh_juice = request.POST.get('fresh_juice')
            do_you_have_a_meal_time_table = request.POST.get('do_you_have_a_meal_time_table')
            fufu = request.POST.get('fufu')
            red_meat = request.POST.get('red_meat')
            do_you_avoid_any_kind_of_food = request.POST.get('do_you_avoid_any_kind_of_food')
            soft_juice = request.POST.get('soft_juice')
            milk = request.POST.get('milk')
            coffee = request.POST.get('coffee')
            educational_level = request.POST.get('educational_level')
            gender = request.POST.get('gender')
            beans = request.POST.get('beans')
            vegetables = request.POST.get('vegetables')
            maize = request.POST.get('maize')
            yam = request.POST.get('yam')
            source_of_income = request.POST.get('source_of_income')
            elubo = request.POST.get('elubo')
            chicken = request.POST.get('chicken')
            egg = request.POST.get('egg')
            bread = request.POST.get('bread')
            eba = request.POST.get('eba')
            legumes = request.POST.get('legumes')
            dairy_product = request.POST.get('dairy_product')
            fruits = request.POST.get('fruits')
            fish = request.POST.get('fish')
            garri = request.POST.get('garri')
            tea = request.POST.get('tea')

            temp = {
                'gender': gender,
                'beans': beans,
                'milk': milk,
                'fresh_juice': fresh_juice,
                'garri': garri,
                'source_of_income': source_of_income,
                'chicken': chicken,
                'bread': bread,
                'coffee': coffee,
                'fish': fish,
                'fruits': fruits,
                'do_you_avoid_any_kind_of_food': do_you_avoid_any_kind_of_food,
                'soft_juice': soft_juice,
                'legumes': legumes,
                'do_you_have_a_meal_time_table': do_you_have_a_meal_time_table,
                'dairy_product': dairy_product,
                'tea': tea,
                'rice': rice,
                'yam': yam,
                'egg': egg,
                'maize': maize,
                'vegetables': vegetables,
                'pounded_yam': pounded_yam,
                'elubo': elubo,
                'educational_level': educational_level,
                'fufu': fufu,
                'red_meat': red_meat,
                'eba': eba
            }
            x = pd.DataFrame(temp, index=[0])
            y = algorithm.predict(x)
            menu = pd.DataFrame(y, columns=y_var)

            record = Prediction(
                user = request.user,
                beans = beans,
                educational_level = educational_level,
                rice = rice,
                vegetables = vegetables,
                source_of_income = source_of_income,
                dairy_product = dairy_product,
                coffee = coffee,
                do_you_have_a_meal_time_table = do_you_have_a_meal_time_table,
                soft_juice = soft_juice,
                tea = tea,
                chicken = chicken,
                maize = maize,
                milk = milk,
                fish = fish,
                do_you_avoid_any_kind_of_food = do_you_avoid_any_kind_of_food,
                garri = garri,
                eba = eba,
                red_meat = red_meat,
                fufu = fufu,
                fresh_juice = fresh_juice,
                elubo = elubo,
                pounded_yam = pounded_yam,
                legumes = legumes,
                gender = gender,
                egg = egg,
                bread = bread,
                yam = yam,
                fruits = fruits,
                monday_BF = menu['Monday B/F'][0],
                monday_LH = menu['Monday LH'][0],
                monday_DN = menu['Monday DN'][0],
                tuesday_BF = menu['Tuesday B/F'][0],
                tuesday_LH = menu['Tuesday LH'][0],
                tuesday_DN = menu['Tuesday DN'][0],
                wednesday_BF = menu['Wednesday B/F'][0],
                wednesday_LH = menu['Wednesday LH'][0],
                wednesday_DN = menu['Wednesday DN'][0],
                thursday_BF = menu['Thursday B/F'][0],
                thursday_LH = menu['Thursday LH'][0],
                thursday_DN = menu['Thursday DN'][0],
                friday_BF = menu['Friday B/F'][0],
                friday_LH = menu['Friday LH'][0],
                friday_DN = menu['Friday DN'][0],
                saturday_BF = menu['Saturday B/F'][0],
                saturday_LH = menu['Saturday LH'][0],
                saturday_DN = menu['Saturday DN'][0],
                sunday_BF = menu['Sunday B/F'][0],
                sunday_LH = menu['Sunday LH'][0],
                sunday_DN = menu['Sunday DN'][0],
            )
            record.save()

            context['monday_BF'] = record.monday_BF
            context['monday_LH'] = record.monday_LH
            context['monday_DN'] = record.monday_DN
            context['tuesday_BF'] = record.tuesday_BF
            context['tuesday_LH'] = record.tuesday_LH
            context['tuesday_DN'] = record.tuesday_DN
            context['wednesday_BF'] = record.wednesday_BF
            context['wednesday_LH'] = record.wednesday_LH
            context['wednesday_DN'] = record.wednesday_DN
            context['thursday_BF'] = record.thursday_BF
            context['thursday_LH'] = record.thursday_LH
            context['thursday_DN'] = record.thursday_DN
            context['friday_BF'] = record.friday_BF
            context['friday_LH'] = record.friday_LH
            context['friday_DN'] = record.friday_DN
            context['saturday_BF'] = record.saturday_BF
            context['saturday_LH'] = record.saturday_LH
            context['saturday_DN'] = record.saturday_DN
            context['sunday_BF'] = record.sunday_LH
            context['sunday_LH'] = record.sunday_LH
            context['sunday_DN'] = record.sunday_DN

            return render(request, 'menu.html', context)
        else:
            context['error']='User input error! please ensure to correctly fill the test form'
            return render(request, 'prediction.html', context)
    else:
        form = PredictionForm()
    context['form'] = form
    return render(request, 'prediction.html', context)

