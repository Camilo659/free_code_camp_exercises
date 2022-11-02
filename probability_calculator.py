import random

class Hat:
    
    def __init__(self, **contents):
        self.contents = []
        for k, v in contents.items():
            self.contents.append((k+' ') * v)
        self.contents = ''.join(self.contents)
        self.contents = self.contents.split()


    def draw(self, balls_for_draw):
        self.balls_for_draw = balls_for_draw
        self.chosen = []

        if self.balls_for_draw > len(self.contents):  return self.contents 

        else:
            while self.balls_for_draw > 0 and len(self.contents) > 0:
                self.r = random.choice(self.contents)
                self.chosen.append(self.r)
                self.contents.remove(self.r)
                self.balls_for_draw -= 1

            for i in self.chosen:    self.contents.append(i)

            return self.chosen
            

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    n = num_experiments
    expected_balls_list= []
    check_list = []

    if num_balls_drawn < sum(expected_balls.values()):  print('Error')

    else:
        for k, v in expected_balls.items():     expected_balls_list.append((k + ' ') * v)
        expected_balls_list =                   ''.join(expected_balls_list)
        expected_balls_list =                   expected_balls_list.split()

        while num_experiments > 0:
            exp = hat.draw(num_balls_drawn)

            for i in range(len(expected_balls_list)):
                try:
                    e = exp.index(expected_balls_list[i])
                    check_list.append(exp[e])
                    exp.remove(exp[e])
                except:pass 

            if check_list == expected_balls_list:   m += 1 
            else:pass

            exp = []
            check_list = []
            num_experiments -= 1
        print((m / n) * 100)
       
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat, {"black":4,"red":3, "green":1}, 10, 20000)

