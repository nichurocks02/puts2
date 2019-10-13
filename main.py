from flask import Flask, request
from fractions import Fraction 

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
  



if __name__ == "__main__":
    app.run(debug=True)
