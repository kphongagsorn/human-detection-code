from flask import Flask, render_template, request
import time
import reset_cameras, iteration_whole_process

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		if request.form['start'] == 'start':
			iteration_whole_process.main()
		elif request.form['reset'] == 'reset':
			reset_cameras.main()
		else:
			print ""
	else:
		print ""
	
	return render_template('index.html')

@app.route('/start/')
def start():
	iteration_whole_process.main()
	#time.sleep(3)
	return render_template('index.html')

@app.route('/reset/')
def reset():
	reset_cameras.main()
	return render_template('index.html')

@app.route('/feeds')
def feeds():
	return render_template('feeds.html')
	#cam1='http://un:pw@172.16.1.130/mjpg/video.mjpg'
	#cam2='http://un:pw@172.16.1.3/mjpg/video.mjpg'
        #return render_template('feeds.html', cam1, cam2)


def action():
	if request.method == 'POST':
		if request.form['submit'] == 'start':
			iteration_whole_process.main()
		else:
			reset_cameras.main()
		return render_template('index.html')

if __name__=='__main__':
	app.run(debug=True)
