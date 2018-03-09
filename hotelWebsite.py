from flask import Flask, render_template
from flask import request
import csv
from datetime import datetime
app = Flask(__name__)



	
@app.route('/')
def home(): 
    return render_template('home.html')


@app.route('/gallery')
def gallery():
	return render_template('gallery.html')
	
	
@app.route('/rooms')
def rooms():
	return render_template('rooms.html')
	
@app.route('/location')
def location():
	return render_template('location.html')

	
@app.route('/booking')
def booking():
	with open('static\\booking.csv','r') as inFile:
		reader = csv.reader(inFile)
		aFile = [row for row in reader]
	return render_template('booking.html', aFile = aFile)

@app.route('/reviews')
def reviews():
	with open('static\\reviews.csv','r') as inFile:
		reader = csv.reader(inFile)
		aList = [row for row in reader]
	
	
	return render_template('reviews.html', aList = aList)

	
@app.route('/addReview', methods = ['POST']) 
def addReview(): 
# add an entry to the Review list
	#read the reviews from file 
	reviewFile = 'static\\reviews.csv' 
	review = readFile(reviewFile)
	
	
	
	#add the new entry    
	newReview = request.form[('Review')] 
	name = request.form[('Name')]
	choice = request.form['choice']
	if choice == '1':
		response = '1 Star'
	elif choice == '2':
		response = '2 Star'
	elif choice == '3':
		response = '3 Star'
	elif choice == '4':
		response = '4 Star'
	elif choice == '5':
		response = '5 Star'
	
	date = datetime.now()
	
	format = "%d-%m-%y"
	date = date.strftime(format)
	#Validation checker
	if newReview == "":
		return render_template('reviews.html', aList=review)	
	else:
		newEntry = [name, newReview, response, date]    
		review.append(newEntry)
	
		#save the review to the file 
		writeFile(review, reviewFile) 
		return render_template('reviews.html', aList=review)

	
def writeFile(aList, aFile): 
#write 'aList' to 'aFile'
	with open(aFile, 'w', newline='') as outFile:
		writer = csv.writer(outFile) 
		writer.writerows(aList)      
	return

def readFile(aFile): 
#read in 'aFile' 
	with open(aFile, 'r') as inFile: 
		reader = csv.reader(inFile) 
		reviewFile = [row for row in reader] 
	return reviewFile
	
@app.route('/addBooking', methods = ['POST']) 
def addBooking(): 
 #add an entry to the booking list
	#read the bookings from file 
	bookingFile = 'static\\booking.csv' 
	booking = readFile(bookingFile)
	
	#add the new entry    
	indate = request.form[('indate')] 
	outdate = request.form[('outdate')] 
	room = request.form[('room')]
	adults = request.form[('adults')] 
	children = request.form[('children')] 
	name = request.form[('Name')] 
	email = request.form[('Email')] 
	

	indate_dt = datetime.strptime(indate,'%Y-%m-%d')
	format = "%d-%m-%y"
	indate = indate_dt.strftime(format)
	outdate_dt = datetime.strptime(outdate,'%Y-%m-%d')
	outdate = outdate_dt.strftime(format)
	#Error condition for empty fields
	if name == "":
		return render_template('booking.html', aFile=booking)		
	elif email == "":
		return render_template('booking.html', aFile=booking)
	else:
		newEntry = [indate, outdate, room, adults, children, name, email]    
		booking.append(newEntry)
		
		#save the skills to the file 
		writeFile(booking, bookingFile) 
		return render_template('booking.html', aFile=booking)

def writeFile(aFile, aBookingFile): 
#write 'aBookingFile' to 'aFile'
	with open(aBookingFile, 'w', newline='') as outFile:
		writer = csv.writer(outFile) 
		writer.writerows(aFile)      
	return

def readFile(aFile): 
#read in 'aFile' 
	with open(aFile, 'r') as inFile: 
		reader = csv.reader(inFile) 
		bookingFile = [row for row in reader] 
	return bookingFile
	


if __name__ == '__main__':
	app.run(debug = True)


