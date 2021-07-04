
GOOGLE_APPLICATION_CREDENTIAL = r"E:\Projects\Image Detection\tactical-hydra-317914-2ab148e32474.json"
def detect_text (path):
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path,'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content = content)

    response = client.text_detection(image = image)
    texts = response.text_annotations
    print("Texts:")

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['{},{}'.format(vertex.x,vertex.y)
                    for vertex in text.bounding_ploy.vertices])
        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            print("some error")
        
        )
            


detect_text(r"E:\Projects\Image Detection\processed.png")