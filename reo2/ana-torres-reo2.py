import sys

filePath = sys.argv[1]

try:
    file = open(filePath, 'r', encoding='utf8')
    fileLines = file.readlines()
    lines = float(len(fileLines))
except:
    print('Erro ao abrir o arquivo')
    sys.exit()

if lines == 0:
  print('Arquivo vazio')
  sys.exit()  

xs = []
ys = []
sumx = 0
sumy = 0

for line in fileLines:
    a, b = line.split(',')
    x = float(a)
    y = float(b)   
    
    if ((type(x) or type(y)) is not float):
        print('Valor não é float')
        sys.exit()

    xs.append(x)
    ys.append(y)
    sumx += x
    sumy += y

xbar = sumx / lines
ybar = sumy / lines

sumDividend = 0.0
sumDividerX = 0.0
sumDividerY = 0.0

for i in range (int(lines)):
    sumDividend += (xs[i] - xbar) * (ys[i] - ybar)
    sumDividerX += ((xs[i] - xbar) ** 2)
    sumDividerY += ((ys[i] - ybar) ** 2)

cp = sumDividend / ((sumDividerX * sumDividerY) ** (1/2))
print (cp)