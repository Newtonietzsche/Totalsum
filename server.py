from flask import Flask, request, jsonify, send_file , send_from_directory, render_template
from flask_cors import CORS
from py.summaryCreator import *
import random
import os

app = Flask(__name__)
CORS(app)  


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/')
def index():
    return render_template('index.html')
@app.route('/interface')
def interface():
    return render_template('interface.html')

@app.route('/help')
def page1():
    return render_template('help.html')

@app.route('/about_us')
def page2():
    return render_template('about_us.html')
@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('js', filename)
@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('css', filename)

# Route pour servir les fichiers inclus
@app.route('/includes/<path:filename>')
def serve_includes(filename):
    return send_from_directory('includes', filename)

@app.route('/assets/<path:filename>')
def serve_image(filename):
    return send_from_directory('assets', filename)


@app.route('/registerPDF', methods=['POST'])
def savefile():
    print("register called")
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename="PdfToSummerize.pdf"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'File successfully uploaded'}), 200
    else:
        return jsonify({'error': 'Invalid file type'}), 400

@app.route('/download_mp3')
def download_mp3():
   
    mp3_path = './toDownload/summary.mp3'
    return send_file(mp3_path, as_attachment=True, download_name='summary.mp3', mimetype='audio/mpeg')


@app.route('/download_pdf')
def download_pdf():
    
    pdf_path = './toDownload/summary.pdf'
    return send_file(pdf_path, as_attachment=True, download_name='summary.pdf', mimetype='application/pdf')

@app.route('/createPDF')
def create_pdf():
    pdfFilePath="./uploads/PdfToSummerize.pdf"
    typeSum = request.args.get('sumType')
    language = request.args.get('language')
    key = request.args.get('key')  
    output=generate_files(pdfFilePath,typeSum,language,key)
    return(jsonify(output))
# generate_files('/content/Lettre de Motivation Fintech.pdf', "Can you summarize this text", 'fr', 'you openAI key' )



if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True,port=5001)