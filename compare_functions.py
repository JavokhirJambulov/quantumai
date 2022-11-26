import face_recognition

#strong cutoff = 0.5, normal cutoff = 0.6
cutoff = 0.5

# Load some images to compare against
alexis_image = face_recognition.load_image_file("images/alexis.jpeg")
javo_image = face_recognition.load_image_file("images/javo.jpeg")
abror_image = face_recognition.load_image_file("images/abror.jpeg")
elyor_image = face_recognition.load_image_file("images/elyor.jpeg")
ogabek_image = face_recognition.load_image_file("images/ogabek.jpeg")

# Get the face encodings for the known images
alexis_encoding = face_recognition.face_encodings(alexis_image)[0]
javo_encoding = face_recognition.face_encodings(javo_image)[0]
abror_encoding = face_recognition.face_encodings(abror_image)[0]
elyor_encoding = face_recognition.face_encodings(elyor_image)[0]
ogabek_encoding = face_recognition.face_encodings(ogabek_image)[0]

known_encodings = [
    (alexis_encoding, "Alexis"),
    (javo_encoding, "Javokhir delivery guy"),
    (abror_encoding, "Abror"),
    (elyor_encoding, "Elyor neighbour"),
    (ogabek_encoding, "Ogabek")
]


def compare_images(img_src):
    img1 = face_recognition.load_image_file(img_src)
    if len(face_recognition.face_encodings(img1)) == 0:
        return 'Unknown'
    img1_face_encoding = face_recognition.face_encodings(img1)[0]
    face_distances = face_recognition.face_distance(list(map(lambda n: n[0], known_encodings)), img1_face_encoding)
    return get_face_name(face_distances)

def get_face_name(face_distances):
    index_min = min(range(len(face_distances)), key=face_distances.__getitem__)
    min_dist = min(face_distances)
    #print('minimal distance: ' + str(min_dist))
    #print('to: ' + known_encodings[index_min][1])
    if min_dist > cutoff:
        return 'Unknown'
    else:
        return known_encodings[index_min][1]
