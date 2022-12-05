class superhero:
    people = 'people'
    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        print(name)
        double_health = health_points * 2
        print(f'nickname: {nickname}, superpower: {superpower}, health: {double_health}')
        print(len(catchphrase))

class Hero:
    superh = superhero('Killua', 'killer', 'thunder', 100, 'this is my main goal')