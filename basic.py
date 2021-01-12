from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def swiper():
    return render_template('swiper.html')


if __name__=='__main__':
    app.run(debug=True)
