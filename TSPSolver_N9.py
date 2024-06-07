class Backtrack:
    def __init__(self, locations): 
        self.locations = locations
        self.num_locations = len(locations)
        self.paths = []
        self.answer = [] 
    def tsp(self, locations, v, currPos, starPos, n, count, cost, paths):
        # v: visited, n: number of locations
        if count == n and locations[currPos][starPos]:
            self.answer.append(cost + locations[currPos][starPos])
            self.paths.append(paths + [starPos]) 
        else:
            for i in range(n):
                if not v[i] and locations[currPos][i]:
                    v[i] = True
                    self.tsp(locations, v, i,starPos,n, count + 1, cost + locations[currPos][i], paths + [i])
                    v[i] = False # Cái này mang ý nghĩa là return
class BackTrackUp1:
    def __init__(self, locations): 
        self.locations = locations
        self.num_locations = len(locations)
        self.paths = []
        self.answer = [] 
        self.min_cost = float('inf')
        self.min_path = []

    def reset(self):
        self.min_cost = float('inf')
        self.min_path = []
        self.paths = []
        self.answer = []

    def tspu(self, locations, v, currPos, starPos, n, count, cost, paths):
        # v: visited, n: number of locations
        if count == n and locations[currPos][starPos]:
            self.answer.append(cost + locations[currPos][starPos])
            self.paths.append(paths + [starPos]) 
            if (cost + locations[currPos][starPos]<self.min_cost):
                self.min_cost = cost + locations[currPos][starPos]
                self.min_path = paths + [starPos]
        else:
            for i in range(n):
                if not v[i] and locations[currPos][i]:
                    new_cost = cost + locations[currPos][i]
                    if new_cost  < self.min_cost:
                        v[i] = True
                        self.tspu(locations, v, i, starPos, n, count + 1, new_cost, paths + [i])
                        v[i] = False # Cái này mang ý nghĩa là return