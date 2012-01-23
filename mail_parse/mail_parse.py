import email

mail = open('mail.txt','r').read()
fn = 'mail.txt'
msg = email.message_from_file(open(fn,'r'))

print msg.get_payload()
for k in msg.keys():
    print k, msg[k]

