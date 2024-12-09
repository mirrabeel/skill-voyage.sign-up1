from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from twilio.rest import Client

app =  Flask(__name__)  # name-ში დავწერთ ფლასკის სერვერის სახელს

# flask_mail კონფიგურაცია
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587       # ეს არის უნიკალური პორტის ნომერი, რომელიც გამოიყენება ელ-ფოსტის გაგზავნისთვის.                 
app.config['MAIL_USE_TLS'] = True   # ამით მონაცემები იქცევა დაშიფრულად ანუ მეილის გაგზავნის პროცესში ვერავინ შეძლებს მეილის მოპარვას.
app.config['MAIL_USERNAME'] = 'your-email@gmail.com' # აქ იგულისხმება ჩვენი საიტის სერვერის ელ-ფოსტა.
app.config['MAIL_PASSWORD'] = 'your-email-password'  # აქაც საიტის სერვერის ელექტრონული ფოსტის მისამართი უნდა ჩავწეროთ.

mail = Mail(app)


# twilio კონფიგურაცია
account_sid = 'your_twilio_account_sid'
auth_token = 'your_twilio_auth_token'
client = Client(account_sid, auth_token) # twilio API კლასი

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    phone = request.form['phone']
    deadline = request.form['deadline']

 # იმეილზე შეტყობინების გაგზავნა
    msg = Message('პროექტის დედლაინი', sender='your-email@gmail.com', recipients=[email])  #sender='your-email@gmail.com'-ში ასევე ვწერთ საიტის სერვერის ელექტრონულ მისამართს. მოგვიწევს შევქმნათ სპეციალური მეილის ანგარიში.
    msg.body = f'თქვენ მიერ შერჩეული პროექტის დედლაინი მოახლოვდა. გთხოვთ, გაითვალისწინოთ, რომ პროექტზე რეგისტრაცია სრულდება : {deadline}.' # აქ ჩავწერთ დედლაინის თარიღს, იმის მიხედვით თუ რომელი პროექტი აირჩია მომხმარებელმა.
    mail.send(msg)

 # SMS გაგზავნა
    message = client.messages.create(
        body=f"თქვენ მიერ შერჩეული პროექტის დედლაინი მოახლოვდა. გთხოვთ, გაითვალისწინოთ, რომ პროექტზე რეგისტრაცია სრულდება : {deadline}.", # ანალოგიურად. დედლაინში ვწერთ მომხმარებლის მიერ არჩეული პროექტის რეგისტრაციის დასრულების თარიღს.
        from_='+1234567890',  # Twilio-ს ტელეფონის ნომერი
        to=phone
    )

    return redirect(url_for('success'))

@app.route('/success')
def success():
    return "შეტყობინება წარმატებით გაიგზავნა!"

if __name__ == '__main__':
    app.run(debug=True)   
