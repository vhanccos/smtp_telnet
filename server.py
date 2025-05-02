import asyncio
from email import message_from_bytes
from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Message
from email.policy import default as default_policy


class CustomHandler:
    async def handle_DATA(self, server, session, envelope):
        print("Nuevo correo recibido")
        print(f"De: {envelope.mail_from}")
        print(f"A: {envelope.rcpt_tos}")
        print("Contenido:")

        msg = message_from_bytes(envelope.content, policy=default_policy)
        print("Asunto:", msg["Subject"])
        print("Texto:")

        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    print(part.get_content())
                elif part.get_filename():
                    filename = part.get_filename()
                    payload = part.get_payload(decode=True)
                    with open(f"adjunto_{filename}", "wb") as f:
                        f.write(payload)
                    print(f"Adjunto guardado: adjunto_{filename}")
        else:
            print(msg.get_content())

        return "250 OK"


if __name__ == "__main__":
    print("Servidor SMTP ejecutándose en localhost:1025 (Ctrl+C para salir)")
    controller = Controller(CustomHandler(), hostname="localhost", port=1025)
    controller.start()

    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_forever()
    except KeyboardInterrupt:
        print("Servidor detenido.")
        controller.stop()
