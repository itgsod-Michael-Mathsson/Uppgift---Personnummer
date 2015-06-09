#encoding: utf-8
import random



def format_person_nummer(person_nummer):
    """
    tar ett person nummer och formaterar om det så att det ska funka att användas i funktionen valid_pnr
    desseutom så testas om nummret har rätt längd feor att faktiskt vara ett person nummer
    :param person_nummer: ett person nummer:
    :returns: formaterat person nummer

    """

    if "-" in person_nummer:
        first_numbers, last_numbers = person_nummer.split("-")
        person_nummer = first_numbers + last_numbers
    for number in person_nummer:
        if not number.isdigit():
            return False
    if len(person_nummer) == 12:
        person_nummer = person_nummer[2:]
        return person_nummer
    elif len(person_nummer) == 10:
        return person_nummer
    else:
        return False



def valid_pnr(person_nummer):
    """
    Den tar ett person nummer och kollar om numrer är legit eller inte baserat dels på om datumen finns på riktigt
    och dels på algoritmen som bestämmer vad den sista siffran blir.

    :param person_nummer: ett person nummer:
    :return: True or False:
    """
    person_nummer = format_person_nummer(person_nummer)
    if not person_nummer:
        return False
    if int(person_nummer[2] + person_nummer[3]) > 12 or int(person_nummer[4] + person_nummer[5]) > 31:
        return False
    sum = 0
    for position in xrange(len(person_nummer)):
        if (position+2) % 2 == 0:
            temp = int(person_nummer[position]) * 2
            if len(str(temp)) == 2:
                temp = int(str(temp)[0]) + int(str(temp)[1])
            sum += temp
        else:
            sum += int(person_nummer[position])
    if sum % 10 == 0:
        return True
    else:
        return False



def generate_pnr(birth_year, gender, ort):
    """
    Den genererar ett trovärdigt personnummer utifrån insatt data.
    :param birth_year: Önskat födelseår.
    :param gender: Önskat kön.
    :param ort: Önskat födelse ort.
    :return: Trovärdigt person nummer.
    """
    birth_year = str(birth_year)
    ort = ort.capitalize()
    if len(birth_year) == 4:
        birth_year = birth_year[2:]
    elif len(birth_year) != 2:
        return "invalid birth_year"
    person_nummer = birth_year
    month = "0" + str(random.randrange(1, 12))
    if len(month) == 3:
        month = month.lstrip("0")
    day = "0" + str(random.randrange(1, 28))
    if len(day) == 3:
        day = day.lstrip("0")
    person_nummer += month + day
    numbers = {"Stockholm": "0013", "Kristianstad": "3538", "Kopparberg": "7173",
    "Uppsala": "1415",         "Malmöhus": "3945",            "Gävleborg": "7577",
    "Södermanland": "1618",     "Halland": "4647",             "Västernorrland": "7881",
    "Östergötland": "1923",     "Västra_Götaland": "4854",     "Jämtland": "8284",
    "Jönköping": "2426",        "Älvsborg": "5558",            "Västerbotten":  "8588",
    "Kronoberg": "2728",        "Skaraborg": "5961",           "Norrbotten": "8992",
    "Kalmar": "2931",           "Värmland": "6264",
    "Gotland": "32",             "Örebro": "6668",
    "Blekinge": "3334",         "Västmanland": "6970"}
    if not ort in numbers:
        return "invalid ort"
    if len(numbers[ort.capitalize()]) == 4:
        temp = str(random.randrange(int(numbers[ort][0] + numbers[ort][1]), int(numbers[ort][2] + numbers[ort][3]) + 1))
        if len(temp) == 1:
            person_nummer += "0" + temp
        else:
            person_nummer += temp
    else:
        person_nummer += numbers[ort]
    if gender == "male":
        person_nummer += str((random.randrange(1, 6) * 2) - 1)
    elif gender == "female":
        person_nummer += str(random.randrange(5) * 2)
    else:
        return "invalid gender"
    for last_number in range(10):
        if valid_pnr(person_nummer + str(last_number)):
            return person_nummer + str(last_number)


print generate_pnr(1997, "male", "Stockholm")
valid_pnr()

