class practice:
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        self.grid = []
        # for item in grid:
        #     one, two = item
        #     self.grid += [one, two]
        self.grid = [item for row in grid for item in row]
        self.no_of_items = len(self.grid)
        self.match_list = [*range(1, self.no_of_items + 1)]
        self.missing_num = None
        self.repeated_num = None
        for item in self.match_list:
            if item in self.grid:
                if self.grid.count(item) > 1:
                    self.repeated_num = item

            else:
                self.missing_num = item
        self.output_list = [self.repeated_num, self.missing_num]
        return self.output_list


obj = practice()
list = [[1,3],[2,2]]
ans = obj.findMissingAndRepeatedValues(list)
print(ans)