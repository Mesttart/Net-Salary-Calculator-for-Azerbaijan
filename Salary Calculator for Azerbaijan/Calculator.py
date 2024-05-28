salary = int(input ("Maasiniz? "))
a = input("sahe (qeyri-dovlet -QD, Dovlet -D): ")

if (a =='QD'):
    DSMF = ((salary - 200 ) * 0.1) + 6
    IssizlikSigortasi= (salary * 0.005)
    if (salary <= 8000):
        Sigorta = salary *0.02
    elif (salary > 8000):
        Sigorta = ((salary - 8000) * 0.005) + 160

    Result = ((salary -DSMF) - IssizlikSigortasi) - Sigorta

    print ('sizin net Maasiniz: ' , Result )
    
if (a =='D'):
    B = salary * 0.03
    C = salary * 0.005
    if (salary <= 2500):
        V = (salary -200)*0.14
    elif (salary > 2500):
        V = ((salary-2500)*0.25)+350

    if (salary <= 8000):
        DSMF = salary *0.02
    elif (salary>8000):
        DSMF =(salary-8000) * 0.005 + 160

    Result = (((salary -DSMF) - B) - C) - V

    print ('sizin net Maasiniz: ' , Result )

    

    
