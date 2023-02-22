def split_and_join(line):
    #write your code here
    hasilA = line.split()
    hasilB = "-".join(hasilA)
    return hasilB

if __name__ == '__main__':
    line(input())
    result = split_and_join(line)
    print(result)