from flask import Flask,request
import turicreate as tc
import json
app = Flask(__name__)

model1 = tc.load_model("popular_deals")
model2 = tc.load_model("popular_deals1")

@app.route('/rec/<int:num>',  methods=['GET'])
def predict(num):

        if request.method == 'GET':

        		rec_list=[]
                data=model1.recommend([num])
                for i in range(0,9):
                	values='exclusivedeal_'+str(data[i]['dealId'])
                	rec_list.append(values)
                return json.dumps({'deal':rec_list})

@app.route('/recomend/<int:num>',  methods=['GET'])
def prediction(num):

        if request.method == 'GET':

				rec_list=[]
                data=model2.recommend([num])
                for i in range(0,9):
                	values='exclusivedeal_'+str(data[i]['dealId'])
                	rec_list.append(values)
                return json.dumps({'deal':rec_list})


if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0')
