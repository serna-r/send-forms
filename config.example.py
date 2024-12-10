class user_config:
    USER = "something@gmail.com"
    PASSWORD = "Password"
    
class emails_config:
    RECIPIENTS_FILENAME = "emails.xlsx"

    class english:
        SUBJECT = "Test"
        LINKS = ['1', '2', '3']
        BODY = """Dear $name
        Test message
        $link"""
    
    class spanish:
        SUBJECT = "Prueba"
        LINKS = ['4', '5', '6']
        BODY = """Estimado $nombre
        Mensaje de prueba
        $link"""