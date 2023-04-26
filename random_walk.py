from random import choice

class RandomWalk:

    def __init__(self, num_of_points = 5000):
        self.num_of_points = num_of_points

        #walk starts at 0,0
        self.xvalues = [0]
        self.yvalues = [0]
    
    def gen_step(self):
        direction = choice([1,-1])
        distance = choice([1,2,3,4])
        step =direction * distance
        return step
    
    def fill_walk(self):
        while len(self.xvalues) < self.num_of_points:
            x_step = self.gen_step()
            y_step = self.gen_step()
            if x_step == 0 and y_step == 0:
                continue
            x = self.xvalues[-1] + x_step
            y = self.yvalues[-1] + y_step
            self.xvalues.append(x)
            self.yvalues.append(y)



