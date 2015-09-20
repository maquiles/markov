import imaplib
import email
import datetime
import os
import getpass

emailaddress = 'mattaquiles@gmail.com'
print "Attempting Login..."
mail = imaplib.IMAP4_SSL('imap.gmail.com')

try:
	mail.login(emailaddress, getpass.getpass())
	print "Login Successful"
	mail.select('INBOX')
	typ, data = mail.uid('search', None, '(HEADER Subject "GDSN:")')
	id_list = data[0].split() 
	latest_email_id = int(id_list[-1])

	for i in id_list:
		typ, data = mail.uid('fetch', i, '(BODY.PEEK[])')
		raw_mail = data[0][1].decode('utf-8')
		mail_message = email.message_from_string(raw_mail)
		for part in mail_message.walk():

			if part.get_content_type() == "text/plain":
				body = part.get_payload(decode=True)
				save_string = str("email_body.txt")
				myfile = open(save_string, 'a')
				myfile.write(body)
				myfile.write('\n')
				myfile.close()

			else:
				continue
	
	sourcefile = "email_body.txt"
	newfile = "less_rubbish.txt"
	rubbish = ['>', '--', 'You received this message', 'To unsubscribe from this', 'For more options', 'wrote:']

	fin = open(sourcefile)
	fout = open(newfile, "w")
	for line in fin:
		if not True in [item in line for item in rubbish]:
			fout.write(line)
	fin.close()
	fout.close()

	os.remove("email_body.txt")

except imaplib.IMAP4.error:
	print 'Failed'