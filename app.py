from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def purchase():
    if request.method == 'POST':
        name = request.form.get('name')
        car_model = request.form.get('car_model')
        price = request.form.get('price')

        # Memastikan semua data diisi
        if not name or not car_model or not price:
            return render_template('index.html', message="Semua data harus diisi.")

        # Mengirim pesan konfirmasi
        message = f"Terima kasih {name}, telah membeli {car_model} seharga {price}. " \
                  f"Terima kasih telah berbelanja di showroom kami!"
        return render_template('index.html', message=message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)