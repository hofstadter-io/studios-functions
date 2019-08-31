import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent, SendGridException


def readEmail(which_email):
    subject = ""
    text = ""
    html = ""

    with open(which_email + "/subject.txt") as f:
        subject = f.read()

    with open(which_email + "/content.txt") as f:
        text = f.read()

    with open(which_email + "/content.html") as f:
        html = f.read()

    return subject, text, html


def sendEmail(config, data):

    subject, text, html = readEmail(config['which_email'])

    print(subject)
    print(text)
    print(html)
    print(os.environ.get('SENDGRID_API_KEY'))

    ts = []
    for t in config['to_emails']:
        ts.append(To(t['email'], t['name']))

    message = Mail(
        from_email=From(config['from_email'], config['from_name']),
        to_emails=ts,
        subject=Subject(subject),
        plain_text_content=PlainTextContent(text),
        html_content=HtmlContent(html)
    )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except SendGridException as e:
        print(e.message)

    except Exception as e:
        print(str(e))


def run(event, context):
    print(event)

    config = {
        "to_emails": [
            {
                "name": "verdverm",
                "email": "verdverm@gmail.com"
            }
        ],
        "from_name": "Hofstadter Studios",
        "from_email": "no-reply@hofstadter.io",
        "which_email": "emails/welcome"
    }

    data = {
        "name": "verdverm"
    }

    sendEmail(config, data)
    return 'message sent'


run("blah", "blah")
