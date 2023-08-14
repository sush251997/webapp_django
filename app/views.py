from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
import psycopg2
from django.http import HttpResponse
from django.core.files.storage import default_storage,FileSystemStorage
import pandas as pd
from django.contrib import messages

global upload_Path
upload_Path = ""
MEDIA_URL = '/media/'


def dbconnection():
    try:
        con = psycopg2.connect(database="catalyst",user="sush",password="sush",host="localhost",port= '5432')
        return con
    except Exception as e:
        print("Exception in Database connection: "+e)



def home(request):
    return render(request,'login.html')


def loginUser(request):
    if request.method == 'POST':
        email = request.POST['emails']
        password = request.POST['password'] 

        print(email,password)

        con = dbconnection()
        cursor = con.cursor()
        cursor.execute('select * FROM app_userlogin WHERE user_email = %s AND user_password = %s', (email, password))
        result = cursor.fetchone()

        print("result in canteen views")
        print(result)

        if len(result)>0:
            print("len of result")
            request.session['uname'] = result[1]
            request.session ['userid'] = result[0]
            return redirect('userIndex')
        else:
            return render(request,'login.html')
    return render(request,'login.html')


def userIndex(request):
    if request.session.get('uname'):
        if request.method=="POST":
            global upload_Path

            uploadedFile = request.FILES['cmpFile']
            fs = FileSystemStorage()
            filepath = fs.save(uploadedFile.name, uploadedFile)
            # filepath = fs.url(filepath)
            # file_name = default_storage.save(filename.name, filename)
            upload_Path += fs.path(filepath)
            print("filename")
            print(filepath)
            print(upload_Path)

            
            if ".csv" in filepath:
                df = pd.read_csv(upload_Path, encoding='ISO-8859-1', error_bad_lines=False)
                df.dropna(inplace=True, axis=0)
                cmp_name = list(df["name"].unique())
                cmp_link = list(df["domain"].unique())
                cmp_year_founded = list(df["year founded"].unique())
                cmp_type = list(df["industry"].unique())
                cmp_Size_range = list(df["size range"].unique())
                cmp_location = list(df["locality"].unique())
                cmp_country = list(df["country"].unique())
                cmp_linkedin = list(df["linkedin url"].unique())
                cmp_emp_estimate = list(df["current employee estimate"].unique())
                total_cmp_emp = list(df["total employee estimate"].unique())

                for name,link,year_founded,type,size,location,country,linkedin,emp_stimate,total_estimate in zip(cmp_name, cmp_link,cmp_year_founded,cmp_type,cmp_Size_range,cmp_location,cmp_country,cmp_linkedin,cmp_emp_estimate,total_cmp_emp):
                    sql = "insert into app_company(cmp_name, cmp_link,cmp_year_founded,cmp_type,comp_size_range,cmp_location,cmp_country,cmp_linkedin,cmp_emp_estimate,total_cmp_emp) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (name,link,year_founded,type,size,location,country,linkedin,emp_stimate,total_estimate)
                    con = dbconnection()
                    cursor = con.cursor()
                    cursor.execute(sql,val)
                    con.commit()

            else:
                df = pd.read_excel(upload_Path, encoding='ISO-8859-1', error_bad_lines=False)
                df.dropna(inplace=True, axis=0)

                cmp_name = list(df["name"])
                cmp_link = list(df["domain"])
                cmp_year_founded = list(df["year founded"])
                cmp_type = list(df["industry"])
                cmp_Size_range = list(df["size range"])
                cmp_location = list(df["locality"])
                cmp_country = list(df["country"])
                cmp_linkedin = list(df["linkedin url"])
                cmp_emp_estimate = list(df["current employee estimate"])
                total_cmp_emp = list(df["total employee estimate"])

                for name,link,year_founded,type,size,location,country,linkedin,emp_stimate,total_estimate in zip(cmp_name, cmp_link,cmp_year_founded,cmp_type,cmp_Size_range,cmp_location,cmp_country,cmp_linkedin,cmp_emp_estimate,total_cmp_emp):
                    sql = "insert into app_company(cmp_name, cmp_link,cmp_year_founded,cmp_type,cmp_Size_range,cmp_location,cmp_country,cmp_linkedin,cmp_emp_estimate,total_cmp_emp) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (name,link,year_founded,type,size,location,country,linkedin,emp_stimate,total_estimate)
                    con = dbconnection()
                    cursor = con.cursor()
                    cursor.execute(sql,val)
                    con.commit()

            print(df)

            messages.success(request, 'Data added successfully!')

            return render(request,'index.html')
        return render(request,'index.html')
    return render(request,'login.html')



def buildQuery(request):
    if request.session.get('uname'):
        sql = "select * from app_company"
        con = dbconnection()
        cursor = con.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        result = list(res)

        cmp_year_founded = [i[3] for i in result]
        cmp_type = [i[4] for i in result]
        cmp_location = [i[6] for i in result]
        cmp_city = []
        cmp_state = []
        cmp_country = []

        for i in cmp_location:
            try:
                loc = str(i).split(',')
                cmp_city.append(loc[0])
                cmp_state.append(loc[1])
                cmp_country.append(loc[2])
            except:
                print("NaN row founded")

        context = {
            "cmp_year_founded" : cmp_year_founded,
            "industry" : cmp_type,
            "cmp_city" : cmp_city,
            "cmp_state" : cmp_state,
            "cmp_country" : cmp_country,
            "fromEmployees" : cmp_year_founded,
            "toEmployees" : cmp_year_founded
        }


        if request.method=="POST":
            cmp_names = request.POST['keywords'] #cmp_name
            industry = request.POST['industry'] #cmp_type
            cmp_year_founded = request.POST['foundedYear'] #cmp_year_founded
            state = request.POST['state'] #cmp_location
            city = request.POST['city'] #cmp_location
            country = request.POST['country'] #cmp_country
            fromEmployees = request.POST['fromEmployees'] #cmp_year_founded
            toEmployees = request.POST['toEmployees'] #cmp_year_founded
            
            # sql = f"select * from app_company where cmp_type='%{industry}%' and cmp_year_founded='%{cmp_year_founded}%' and cmp_location='%{str(city)+str(state)+str(country)}%' and EXTRACT(YEAR FROM cmp_year_founded) BETWEEN {'%{fromEmployees}%'} AND {'%{toEmployees}%'} and cmp_name LIKE '%{cmp_name}%'"
            sql = "select * from app_company where cmp_name LIKE %s and cmp_type=%s and cmp_year_founded=%s and cmp_location=%s and cmp_year_founded BETWEEN %s AND %s"
            val = (cmp_names+"%",industry,cmp_year_founded,city+","+state+","+country,fromEmployees,toEmployees)
            con = dbconnection()
            cursor = con.cursor()
            print()
            print(sql,val)
            print()
            cursor.execute(sql,val)
            res = cursor.fetchall()
            result = len(list(res))

            messages.success(request, str(result)+' records found for the query')

            return render(request,'build_query.html')
        return render(request,'build_query.html', context)
    return render(request,'login.html')


def addUser(request):
    if request.session.get('uname'):
        con = dbconnection()
        cursor = con.cursor()

        sql = "select user_name,user_email from app_userlogin"
        cursor.execute(sql)
        res = cursor.fetchall()
        result = list(res)
        All_uNames = [i[0] for i in result]
        All_uEmails = [i[1] for i in result]

        context = {
            "All_unames":zip(All_uNames,All_uEmails)
        }

        

        if request.method=="POST":
            uName = request.POST['Uname']
            uEmail = request.POST['Uemail']
            uPass = request.POST['Upass']

            con = dbconnection()
            cursor = con.cursor()

            sql1 = "insert into app_userlogin(user_id,user_name,user_email,user_password) values(%s,%s,%s,%s)"
            val1 = (len(result)+1,uName,uEmail,uPass)
            cursor.execute(sql1,val1)
            con.commit()


            sql2 = "select user_name,user_email from app_userlogin"
            cursor.execute(sql2)
            res = cursor.fetchall()
            result = list(res)

            All_uNames = [i[0] for i in result]
            All_uEmails = [i[1] for i in result]

            context = {
                "All_unames":zip(All_uNames,All_uEmails)
            }

            messages.success(request, 'User added successfully!')

            return render(request,'add_user.html', context)
        return render(request,'add_user.html', context)
    return render(request,'login.html')

def logout(request):    
    del request.session['uname']
    del request.session['userid']
    return redirect('home')