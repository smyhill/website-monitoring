import smtplib

# choose your carrier when you call the function below
carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

email = 'youremail@gmail.com'
password = 'yourgmailpassword'

def send(message, phone_number, carrier):
    	# replace the carrier with your own from the options above
	to_number = phone_number + '{}'.format(carrier)
	auth = (email, password)

	# Establish session with SMTP server using gmail account
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	server.login(auth[0], auth[1])

	# Send text message through SMS gateway of destination number
	server.sendmail( auth[0], to_number, message)
