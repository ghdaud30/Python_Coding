seoul = ["Jane", "Kim"]

def solution(seoul):
    location = 0
    
    for idx , name in enumerate(seoul):
        if(name == 'Kim'):
            location = idx

    return f'김서방은 {location}에 있다' 