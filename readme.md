This project's goal is to build an online calculator based on FLASK framework.
It can take in integers, floating values and rational numbers = p/q form.

EXECUTION:
		$ cd directory/file
		$ export FLASK_APP=main (or) $ export FLASK_APP=main.py
		$flask run 
#your server starts running on your local host on port 5000
 		$curl 'http://127.0.0.1:5000/<functionality>?A=<num1>&B=<num2>'
#functionality= add/sub/mul/div
#num1 & num2 =any int/fraction/float number

TEST:
	test.py is the test script written to validate main.py
	to run make sure you run your flask app
	$python test.py

 	or make the file executable by 
 	$ chmod u+x test.py
 	and 
 	$ ./test.py

 	we don't need to give input to test as it generates numbers randomly

 	



