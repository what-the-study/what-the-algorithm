def solution(today, terms, privacies):
    today = number_of_days(today)
        
    answer = []
    terms_dict = {}
    for item in terms:
        term, expiration = item.split(" ")
        terms_dict[term] = int(expiration) * 28
    
    for i in range (len(privacies)):
        date, term = privacies[i].split(" ")
        expiration_date = number_of_days(date) + terms_dict[term]
        
        if today >= expiration_date:
            answer.append(i+1)
    
    return answer


def number_of_days(date):
    year, month, day = date.split(".")
    return int(year)*12*28 + int(month)*28 + int(day)