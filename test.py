from SimpleTelnetMail import TelnetMail

client = TelnetMail(
    host="localhost",
    port=1025,
    from_="vhanccos@unsa.edu.com",
    to=["vhanccos@unsa.edu.com"],
    message="Test SimpleTelnetMail",
    # username="my.address@domain.com",
    # password="password",
    # ssl=True,
    Subject="Correo con adjunto",
    attachments=["test.txt"],
)

client.send_mail()
print(client.responses.decode())
