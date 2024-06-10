import smtplib
import email.message

def enviar_email(precoTotalPrint, pagouNo, desconto, acrescimo, valorPagamento):
    corpo_email = f"""
    <p>#############################################</p>
    <p>--------------- NOTA FISCAL ---------------</p>
    <p>Valor Total: R$ {precoTotalPrint:.2f}</p>
    <p>Forma de pagamento: {pagouNo}</p>
    <p>Desconto: {desconto}</p>
    <p>Acréscmo: {acrescimo}</p>
    <p>Valor a ser pago: R$ {valorPagamento:.2f}</p>
    <p>OBRIGADO PELA COMPRA, E TENHA UM BOM FILME!</p>
    <p>#############################################</p>"""

    msg = email.message.Message()
    msg['Subject'] = "CINE SERTÃO - NOTA FISCAL"
    msg['From'] = 'wesley.fernandes@estudante.ufcg.edu.br'
    msg['To'] = 'wesley.fernandes@estudante.ufcg.edu.br'
    password = 'mdxbgewtptshzvje'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))