class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable
    def find(self, iterable, callback):
        for i in range(len(iterable)):
            if callback(iterable[i]) == True:
                return iterable[i]
    def filter(self, iterable, callback):
        myList = []
        for i in range(len(iterable)):
            if callback(iterable[i]) == True:
                myList.append(iterable[i])
        return(myList)
    def reject(self, iterable, callback):
        myList = []
        for i in range(len(iterable)):
            if callback(iterable[i]) == False:
                myList.append(iterable[i])
        return(myList)
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
print(evens)
notEvens = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(notEvens)
iterateMyShit = _.map([1, 2, 3, 4, 5, 6], lambda x: x % 2)
print(iterateMyShit)
firstEven = _.find([1, 3, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(firstEven)