


from flask import Flask,jsonify,request
import turicreate as tc

app = Flask(__name__)

model = tc.load_model("popular_deals")


@app.route('/recomend/<int:num>',  methods=['GET'])
def prediction(num):

        if request.method == 'GET':

                return jsonify(list(model.recommend([num])))


if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')