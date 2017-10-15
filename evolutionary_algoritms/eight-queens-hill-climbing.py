import random

class EightQueens():

    def __init__(self):
        pass

    def create_random_element(self):
        queens = list(range(1,9))
        random.shuffle(queens)
        return queens
    
    def mutation(self, queens):
        queens.append(queens.pop(random.randint(0,7)))
        return queens
     
    def check_attack(self, queens):
        attacked_queens = 0
        for i, queen in enumerate(queens):
            for j, element in enumerate(queens):
                if i == j:
                    continue
                if abs(i-j) == abs(queen - element):
                    attacked_queens += 1
                    break
        return attacked_queens 
        
    def calculate(self):
        queens = self.create_random_element()
        result = self.check_attack(queens)
        number_of_loops = 0
        while result != 0:
            queens_new = self.mutation(queens)
            result_new = self.check_attack(queens_new)
            number_of_loops += 1
            if result_new <= result:
                queens, result = queens_new, result_new
        return queens, number_of_loops
        
    def get_result_only(self):
        return self.calculate()[0]
        
    def avg_loop(self, number_of_calculations):
        loops = []
        for i in range(number_of_calculations):
            loops.append(self.calculate()[1])
        return sum(loops)/len(loops)
        
o = EightQueens()
print(o.get_result_only())
