from flask import Flask, redirect, url_for, request
import openai
app = Flask(__name__)

openai.api_key = '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'
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]

@app.route('/results/<name>')
def success(name):
   return name

@app.route('/home',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      messages.append(
            {"role": "user", "content": user})
      chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
      )
      reply = chat.choices[0].message.content
      messages.append({"role": "assistant", "content": reply})
      return redirect(url_for('success',name=reply))

if __name__ == '__main__':
   app.run(debug = True)
