"""
For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided 2 dimensional array (x)
 for good ideas 'good' and bad ideas 'bad'.
 If there are one or two good ideas, return 'Publish!',
 if there are more than 2 return 'I smell a series!'.
  If there are no good ideas, as is often the case,
  return 'Fail!'.

The sub arrays may not be the same length.

The solution should be case insensitive (ie good, GOOD and gOOd
 all count as a good idea). All inputs may not be strings.
"""


def well(arr):
    res = 0
    for ar in arr:
        for word in ar:
            if word.lower()== "good":
                res+=1

    if res==0:
        return "Fail!"
    if res <=2:
        return "Publish!"
    else:
        return "I smell a series!"


#second var
def well_v2(arr):
    res = str(arr).lower().count('good')
    return 'I smell a series!' if (res > 2) else 'Fail!' if not(res) else 'Publish!'

arr = [['bad', 'bAd', 'bad'], ['bad', 'GooD', 'bad'], ['bad', 'bAd', 'bad']]
print(well(arr))
print(well_v2(arr))
