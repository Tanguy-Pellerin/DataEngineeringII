import unittest
import os
import requests

class FlaskTests(unittest.TestCase):

	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		pass
		
	def tearDown(self):
		pass

	def test_a_index(self):
		responce = requests.get('http://localhost:5000')
		self.assertEqual(responce.status_code, 200)

	def test_b_classify_negative(self):
		params = {
			"sentence" : "Strange and bad movie",
			"form_type": "classify"
		}
		responce = requests.post('http://localhost:5000', data=params)
		self.assertEqual(responce.status_code, 200)
		self.assertEqual(responce.content, '''<HTML>
<head>
    <style> 
        .EmbedModel-module--embedContainer--1-R1j {

            margin: 2rem 0;
            box-shadow: 0 0 2px 0 rgba(119,135,147,.1),0 10px 30px 0 rgba(119,135,147,.1);
            border-radius: 6px;
            } 
    </style>

</head>
<BODY>
        <center>
<div class="EmbedModel-module--embedContainer--1-R1j">

    <div>
        <form method="POST" action="" >
            <center>
            <H1> Test you text </H1> <br>
            <span>Put your text to see the sentiment analysis</span><br>
            <input type = "text" name = "sentence" style="height:200px;width:500px;font-size:14pt;"/> <br>
            <input type="hidden" name="form_type" value="classify"/>
            <input type = "submit">
            </center>
        </form>
    </div>
    <div>
        <h3>Results</h3>
        <div>
            <div>
                <span>Negative</span>
            </div>
        </div>
    </div>
</div>
</BODY>
</HTML>'''.encode())


	def test_c_classify_neutral(self):
		params = {
			"sentence" : "flavors good however don't see difference oaker oats",
			"form_type": "classify"
		}
		responce = requests.post('http://localhost:5000', data=params)
		self.assertEqual(responce.status_code, 200)
		self.assertEqual(responce.content, '''<HTML>
<head>
    <style> 
        .EmbedModel-module--embedContainer--1-R1j {

            margin: 2rem 0;
            box-shadow: 0 0 2px 0 rgba(119,135,147,.1),0 10px 30px 0 rgba(119,135,147,.1);
            border-radius: 6px;
            } 
    </style>

</head>
<BODY>
        <center>
<div class="EmbedModel-module--embedContainer--1-R1j">

    <div>
        <form method="POST" action="" >
            <center>
            <H1> Test you text </H1> <br>
            <span>Put your text to see the sentiment analysis</span><br>
            <input type = "text" name = "sentence" style="height:200px;width:500px;font-size:14pt;"/> <br>
            <input type="hidden" name="form_type" value="classify"/>
            <input type = "submit">
            </center>
        </form>
    </div>
    <div>
        <h3>Results</h3>
        <div>
            <div>
                <span>Neutral</span>
            </div>
        </div>
    </div>
</div>
</BODY>
</HTML>'''.encode())


	def test_d_classify_positive(self):
		params = {
			"sentence" : "It's a sad movie but very good",
			"form_type": "classify"
		}
		responce = requests.post('http://localhost:5000', data=params)
		self.assertEqual(responce.status_code, 200)
		self.assertEqual(responce.content, '''<HTML>
<head>
    <style> 
        .EmbedModel-module--embedContainer--1-R1j {

            margin: 2rem 0;
            box-shadow: 0 0 2px 0 rgba(119,135,147,.1),0 10px 30px 0 rgba(119,135,147,.1);
            border-radius: 6px;
            } 
    </style>

</head>
<BODY>
        <center>
<div class="EmbedModel-module--embedContainer--1-R1j">

    <div>
        <form method="POST" action="" >
            <center>
            <H1> Test you text </H1> <br>
            <span>Put your text to see the sentiment analysis</span><br>
            <input type = "text" name = "sentence" style="height:200px;width:500px;font-size:14pt;"/> <br>
            <input type="hidden" name="form_type" value="classify"/>
            <input type = "submit">
            </center>
        </form>
    </div>
    <div>
        <h3>Results</h3>
        <div>
            <div>
                <span>Positive</span>
            </div>
        </div>
    </div>
</div>
</BODY>
</HTML>'''.encode())



if __name__ == '__main__':
	unittest.main()		
