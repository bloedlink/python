import requests
import hashlib
#1 test api request

def api_communicate(value):
    url = 'https://api.pwnedpasswords.com/range/' + value
    res = requests.get(url)
    if res.status_code != '200':
        print(res)
        #raise RuntimeError('Something is wrong, try again.')
    return res

def api_password_leaks_count(hashes, hash_to_check ):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hash,count in hashes:
        if hash == hash_to_check:
            return count
    return 0
        
        
    
    
    
#2 functie die ons paswoord hasht

def api_hash_value(password):
    secret = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    five,tail = secret[:5],secret[5:]
    answer = api_communicate(five)
    return api_password_leaks_count(answer, tail)

api_hash_value('password')



#4 door de responses loopen en zorgen dat deze opgedeeld worden eerste 5 waarden en de rest. 

#5 onze waarden, matchen met de waarden die we terug krijgen en printen als ons paswoord nog veilig is, of niet. 
