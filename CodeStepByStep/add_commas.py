
def add_commas(string):
    out = ''
    i = 1
    while i <= len(string):
        out += string[-i]
        if (i % 3) == 0 and i != len(string):     
            out += ','
        i += 1
    return out[::-1]
 
if __name__ == '__main__':
	print add_commas('123456')
