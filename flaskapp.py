import sys
sys.setrecursionlimit(10000)
from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def index():
  return render_template('sum.html')
@app.route('/sum',methods=['POST'])
def sum():
    n=int(request.form['num'])
    ans=sumofn(n)
    return render_template('sum.html',value=ans)
def sumofn(n):
    if n<0:
        return "Not a natural number"
    elif n==0 or n==1:
        return n
    elif n>1000000:
        return "Limit Exceeded"
    else:
        val=(n*(n+1)/2)
        return int(val)
if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True,port=80)
