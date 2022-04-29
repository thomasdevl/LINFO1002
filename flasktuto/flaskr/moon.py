# Determine les phases de la lune à un moment donné
# Python code by HAB
#https://www.daniweb.com/programming/software-development/code/216727/moon-phase-calculator (code simplifié et modifié)

def moon_phase(date):    
    sep = date.split("/")
    day = int(sep[0])
    month = int(sep[1])
    year = int(sep[2]) 
    ages = [18, 0, 11, 22, 3, 14, 25, 6, 17, 28, 9, 20, 1, 12, 23, 4, 15, 26, 7]
    offsets = [-1, 1, 0, 1, 2, 3, 4, 5, 7, 7, 9, 9]
    description = ["new",
      "waxing crescent",
      "in its first quarter",
      "waxing gibbous",
      "full",
      "waning gibbous",
      "in its last quarter",
      "waning crescent"]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    if day == 31:
        day = 1
    days_into_phase = ((ages[(year + 1) % 19] + ((day + offsets[month-1]) % 30) + (year < 1900)) % 30)
    index = int((days_into_phase + 2) * 16/59.0)
    if index > 7:
        index = 7
    status = description[index]
    
    return status

def dico_naiss_lune(naiss):

    #return : dictionnaire avec la date en clé et en fct du 
    # jour le nmbr de vache en pleine lune 1 et en période normale 0


    moon = {}
    nbr = ""
    d = {}
    for date in naiss:
        d[date[0]] = ''
    for n in naiss: d[n[0]] += "1" if moon_phase(n[0])=="full" else "0"
    for date in naiss:

        if moon_phase(date[0])=="full": 
            nbr+="1"      
            moon[date[0]]=nbr
        else:       
            nbr += "0"
            moon[date[0]]=nbr

    return d