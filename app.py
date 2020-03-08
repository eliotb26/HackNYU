from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") # this should be the name of your html file
                                        #want this to return the updated website 


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")
    
@app.route('/receiver', methods=['POST'])
def receiver():
    if request.method == "POST":
        data = request.get_data()
        decode_base64(data)
        return render_template("index.html")


@app.route('/new', methods=['GET'])
def new():
    ans = detect_document_with_newLine()
    temp = display(ans)
    print(ans)
    export(ans)
    return temp

def export(ans):
    f = open("output.cpp", "w")
    f.write(ans)
    f.close()

def display(ans):
    return '<h1>Testing</h1><div class = "target"><p>%s</p></div>'%(ans)

def decode_base64(dataURL):
    import base64
    dataURL = str(dataURL).split(",")
    dataURL = dataURL[1]
    dataURL = b"%r"%{dataURL}

    with open("imageToSave.png", "wb") as fh:
        fh.write(base64.decodebytes(dataURL))
    return fh


def detect_document_with_newLine():
    import os,io
    from google.cloud import vision
    from google.cloud.vision import types
    import pandas as pd

    os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'Hand write code-1f0460a79a72.json'
    client = vision.ImageAnnotatorClient()

    file_name = 'imageToSave.png'
    #file_name = 'sign.png'
    image_path = file_name

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    # construct an image instance
    image = vision.types.Image(content=content)

    """
    # or we can pass the image url
    image = vision.types.Image()
    image.source.image_uri = 'https://edu.pngfacts.com/uploads/1/1/3/2/11320972/grade-10-english_orig.png'
    """
    # annotate Image Response
    response = client.document_text_detection(image=image)  # returns TextAnnotation
    df = pd.DataFrame(columns=['locale', 'description'])

    texts = response.text_annotations
    for text in texts:
        df = df.append(
            dict(
                locale=text.locale,
                description=text.description
            ),
            ignore_index=True
        )

    return df['description'][0]

if __name__ == '__main__':
    app.debug = True
    app.run()

