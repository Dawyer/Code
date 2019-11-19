def convert(s,numRows):
    if numRows == 1:
        return s

    rows = ['\n']*min(numRows,len(s))
    godown=False
    currow=0
    for c in s:
        rows[currow] += c
        if currow == 0 or currow == numRows-1:
            godown = not godown
        if godown:
            currow += 1
        else:
            currow -= 1
    return ''.join(rows)

print(convert('PAYPALISHIRING',3))