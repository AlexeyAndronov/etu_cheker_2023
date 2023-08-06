import requests

import db.dbworks
from db.dbworks import storeAbitur, storePriority, getAllAbitur, getSpecPlaces, getPriorityBy
from  db.dbworks import createSuperRecord, cleatSuperlist, clearAbiturs, clearPriority
from processing import normalizeCode

def download(url):
    t = requests.get(url.url)
    if t.status_code == 200:
        result = t.json()
        print(result["data"]["competition"]["name"])
    for item in result["data"]["list"]:
        code = item["code"]
        points = int(item["total_points"])
        original = bool(item["has_original"])
        conditions = item["enroll_condition"]
        payed_contract = bool(item["has_paid_contract"])
        if original == True and conditions == 'ОМ' :
            code = normalizeCode(code)
            storeAbitur(code, points)
    #        print (url.code)
            storePriority(url.code, code, int(item["priority"]))


if __name__ == "__main__":

    clearPriority()
    clearAbiturs()

    all_urls = db.dbworks.getSpecialitys()
    for url in all_urls:
        print(url.url)
        download(url)


    cleatSuperlist()

    people = getAllAbitur(minPoint = 180)
    spec = getSpecPlaces()
    print(len(spec))
    currentValues = {}
    for item in spec:
        currentValues[item[0]] = item[1]

    print (len(people))

    for item in people:
        print(f"Расчет для - {item}")
        priority = getPriorityBy(item[0])
        for p_num in priority:
            spec_code = p_num[1]
            cv = currentValues[spec_code]
            if cv > 0:
                createSuperRecord(p_num[1], item[0], item[1], cv)
                currentValues[spec_code] -= 1
                print(f"{item[0]} - поступил на {spec_code} - {cv}")
                break
            else:
                print (f"Специальность {spec_code} заполнена: {cv}")
                continue




