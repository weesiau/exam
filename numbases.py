hextodec = {'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7', \
            '8':'8','9':'9','A':'10','B':'11','C':'12','D':'13','E':'14','F':'15'}

dectohex = {'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7', \
            '8':'8','9':'9','10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}

def dectobase(decnumber,base):
    if base == 2 or base == 8:
        result = []
        output = ''
        while decnumber > 0:
            rem = decnumber % base
            result.append(rem)
            decnumber = decnumber // base
        for i in range(len(result)-1,-1,-1):
            output += str(result[i])
        return output
    elif base == 16:
        result = []
        output = ''
        while decnumber > 0:
            rem = decnumber % base
            result.append(dectohex[str(rem)])
            decnumber = decnumber // base
        for i in range(len(result)-1,-1,-1):
            output += (result[i])
        return output

def basetodec(number,base):
    if base == 8:
        total = 0
        for i in range(1,len(str(number))+1):
            total += int(str(number)[-i]) * (base**(i-1))
        return total
    elif base == 2:
        number = str(number)
        number = number.lstrip('0')
        total = 0
        for i in range(1,len(str(number))+1):
            total += int(number[-i]) * (base**(i-1))
        return total
    elif base == 16:
        total = 0
        for i in range(1,len(number)+1):
            total += int(hextodec[number[-i]]) * (base**(i-1))
        return total

print(basetodec(101101001,2))
print(basetodec(761527,8))
print(basetodec('C48D',16))
