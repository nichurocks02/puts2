from flask import Flask, request
from fractions import Fraction 
import statistics 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/add', methods=['GET','POST'])
def addition():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('B',default = 0, type = Fraction)
    C=value1+value2
    D=str(C).split('/')
    if len(D) == 2:
        E=float(D[0])/float(D[1])
        F=str(E).split(".")
        if F[1] == '0':
            return " %s\n" % F[0]
        else:
            return  " %s\n" %E
    else:
        G=str(C).split(".") 
        return " %s \n" % G[0]  
  

@app.route('/sub', methods=['GET','POST'])
def sub():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('B',default = 0, type = Fraction)
    C=value1-value2
    D=str(C).split('/')
    if len(D) == 2:
        E=float(D[0])/float(D[1])
        F=str(E).split(".")
        if F[1] == '0':
            return " %s\n" % F[0]
        else:
            return  " %s\n" %E
    else:
        G=str(C).split(".") 
        return "%s \n" % G[0]   

@app.route('/mul', methods=['GET','POST'])
def mul():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('B',default = 0, type = Fraction)
    C=value1*value2
    D=str(C).split('/')
    if len(D) == 2:
        E=float(D[0])/float(D[1])
        F=str(E).split(".")
        if F[1] == '0':
            return "%s\n" % F[0]
        else:
            return  "%s\n" %E
    else:
        G=str(C).split(".") 
        return "%s \n" % G[0]   
  
@app.route('/div', methods=['GET','POST'])
def div():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('B',default = 0, type = Fraction)
    C=value1/value2
    D=str(C).split('/')
    if len(D) == 2:
        E=float(D[0])/float(D[1])
        F=str(E).split(".")
        if F[1] == '0':
            return " %s\n" % F[0]
        else:
            return  " %s\n" %E
    else:
        G=str(C).split(".") 
        return " %s \n" % G[0]  


@app.route('/average', methods=['GET','POST'])
def average():
    value1=request.args.get('X' )
    sum=0

    count=0
    a=value1.split(',')
    for i in a:
        print(i)

        match = re.search('/',i)
        if match:
            x=[]
            n=i.split('/')
            print(n)
            for j in n :
                print(j)
                if j!='/':
                    j= int(j)
                    x.append(j)
            div=x[0]/x[1]
            sum=sum+div
            count = count +1
        else:
            i=float(i)
            sum=sum+i
            count=count+1
    avg = sum/count
    D=str(avg).split('.')
    if len(D) == 2:
        if D[1]!=0:
            return " %s\n" % avg
        elif D[1]==0:
            return " %s\n" % D[0]

@app.route('/avg', methods=['GET','POST'])
def avg():
    value1=request.args.get('X' )
    sum=0

    count=0
    a=value1.split(',')
    for i in a:
        print(i)

        match = re.search('/',i)
        if match:
            x=[]
            n=i.split('/')
            print(n)
            for j in n :
                print(j)
                if j!='/':
                    j= int(j)
                    x.append(j)
            div=x[0]/x[1]
            sum=sum+div
            count = count +1
        else:
            i=float(i)
            sum=sum+i
            count=count+1
    avg = sum/count
    D=str(avg).split('.')
    if len(D) == 2:
        if D[1]!=0:
            return " %s\n" % avg
        elif D[1]==0:
            return " %s\n" % D[0]

@app.route('/mean', methods=['GET','POST'])
def mean():
        value1=request.args.get('X' )
        sum=0

        count=0
        a=value1.split(',')
        for i in a:
            print(i)

            match = re.search('/',i)
            if match:
                x=[]
                n=i.split('/')
                print(n)
                for j in n :
                    print(j)
                    if j!='/':
                        j= int(j)
                        x.append(j)
                div=x[0]/x[1]
                sum=sum+div
                count = count +1
            else:
                i=float(i)
                sum=sum+i
                count=count+1
        avg = sum/count
        D=str(avg).split('.')
        if len(D) == 2:
            if D[1]!=0:
                return " %s\n" % avg
            elif D[1]==0:
                return " %s\n" % D[0]

@app.route('/max', methods=['GET','POST'])
def max():
    value1=request.args.get('X' , type = str)
    a=value1.split(',')
    print(a)
    y=[]
    for i in a:
        match = re.search('/',i)
        if i!=',' :
            if not match:
                y.append(float(i))



            if match:
                x=[]
                n=i.split('/')
                for j in n:
                    if j!='/':
                        j= int(j)
                        x.append(j)
                div=x[0]/x[1]
                y.append(div)

    y.sort()
    return " %s\n" % y[-1]

@app.route('/min', methods=['GET','POST'])
def min():
    value1=request.args.get('X' , type = str)
    a=value1.split(',')
    print(a)
    y=[]
    for i in a:
        match = re.search('/',i)
        if i!=',' :
            if not match:
                y.append(float(i))



            if match:
                x=[]
                n=i.split('/')
                for j in n:
                    if j!='/':
                        j= int(j)
                        x.append(j)
                div=x[0]/x[1]
                y.append(div)

    y.sort()
    return " %s\n" % y[0]

@app.route('/median', methods=['GET','POST'])
def median():
    value1=request.args.get('X' , type = str)
    a=value1.split(',')
    print(a)
    y=[]
    for i in a:
        match = re.search('/',i)
        if i!=',' :
            if not match:
                y.append(float(i))

            if match:
                x=[]
                n=i.split('/')
                for j in n:
                    if j!='/':
                        j= int(j)
                        x.append(j)
                div=x[0]/x[1]
                y.append(div)
    med=statistics.median(y)

    return " %s\n" % med


if __name__ == "__main__":
    app.run(debug=True)
