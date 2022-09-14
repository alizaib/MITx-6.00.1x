animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    largest = 0
    resultkey = list(aDict.keys())[0]
    for key in aDict.keys():
        if len(aDict[key]) > largest:
            resultkey = key
            largest = len(aDict[key])
    
    return resultkey

print(biggest(animals))
print(list(animals.keys())[0])


