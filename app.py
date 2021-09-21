from flask import Flask, render_template, request, redirect, send_file
from os import path
from werkzeug.utils import secure_filename
from moviepy.editor import VideoFileClip, AudioFileClip
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os
import imageio
from moviepy.editor import *
from pydub import silence, AudioSegment

app = Flask(__name__,template_folder='templates')

def function(file, selected_language):
    def myfunction(add):
        sound = AudioSegment.from_mp3(add)
        sound.export("Speech.wav", format="wav")

        recog1 = spr.Recognizer()
        Audio_file = path.join("Speech.wav")

        try:
            with spr.AudioFile(Audio_file) as source:
                audio = recog1.listen(source)
                MyText = recog1.recognize_google(audio)
                translator = Translator()
                translated = translator.translate(MyText, dest=selected_language)
                translated = str(translated).split(", ")
                result = translated[2]
                stopword = ['text']
                abc = str(result).split("=")
                resultword = [word for word in abc if word.lower() not in stopword]
                converted = ''.join(resultword)
            return converted
        except:
            return 0

    filename = file.filename
    video_file = path.join(filename)
    video = VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile('myfile.mp3')

    audio = AudioSegment.from_file('myfile.mp3')
    duration = audio.duration_seconds
    print(duration)

    abcd = [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300]

    a1 = abcd[0]
    b1 = abcd[1]
    if a1 <= duration and b1 <= duration:

        clip = AudioFileClip("myfile.mp3").subclip(a1, b1)
        clip.write_audiofile("audio1.mp3")
        a = myfunction('audio1.mp3')
        if a != 0:
            def speak(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good.mp3")

            speak(a)
            sound = AudioSegment.from_file("good.mp3")
        else:
            sound = AudioSegment.empty()

    else:
        sound = AudioSegment.empty()

    a2 = abcd[2]
    b2 = abcd[3]
    if b1 <= duration and a2 <= duration:
        clip1 = AudioFileClip("myfile.mp3").subclip(b1, a2)
        clip1.write_audiofile("audio11.mp3")
        a1 = myfunction('audio11.mp3')
        if a1 != 0:
            def speak(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good111.mp3")

            speak(a1)
            sound1 = AudioSegment.from_file("good111.mp3")
        else:
            sound1 = AudioSegment.empty()
    else:
        sound1 = AudioSegment.empty()

    a3 = abcd[4]
    b3 = abcd[5]
    if a2 <= duration and b2 <= duration:
        clip2 = AudioFileClip("myfile.mp3").subclip(a2, b2)
        clip2.write_audiofile("audio2.mp3")
        b = myfunction('audio2.mp3')
        if b != 0:
            def speak1(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good1.mp3")

            speak1(b)
            sound2 = AudioSegment.from_file("good1.mp3")
        else:
            sound2 = AudioSegment.empty()

    else:
        sound2 = AudioSegment.empty()

    a4 = abcd[6]
    b4 = abcd[7]
    if b2 <= duration and a3 <= duration:
        clip3 = AudioFileClip("myfile.mp3").subclip(b2, a3)
        clip3.write_audiofile("audio3.mp3")
        c = myfunction('audio3.mp3')
        if c != 0:
            def speak2(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good2.mp3")

            speak2(c)
            sound3 = AudioSegment.from_file("good2.mp3")
        else:
            sound3 = AudioSegment.empty()

    else:
        sound3 = AudioSegment.empty()

    a5 = abcd[8]
    b5 = abcd[9]
    if a3 <= duration and b3 <= duration:
        clip4 = AudioFileClip("myfile.mp3").subclip(a3, b3)
        clip4.write_audiofile("audio4.mp3")
        d = myfunction('audio4.mp3')
        if d != 0:
            def speak3(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good3.mp3")

            speak3(d)
            sound4 = AudioSegment.from_file("good3.mp3")
        else:
            sound4 = AudioSegment.empty()

    else:
        sound4 = AudioSegment.empty()

    a6 = abcd[10]
    b6 = abcd[11]
    if b3 <= duration and a4 <= duration:
        clip5 = AudioFileClip("myfile.mp3").subclip(b3, a4)
        clip5.write_audiofile("audio5.mp3")
        e = myfunction('audio5.mp3')
        if e != 0:
            def speak4(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good4.mp3")

            speak4(e)
            sound5 = AudioSegment.from_file("good4.mp3")
        else:
            sound5 = AudioSegment.empty()

    else:
        sound5 = AudioSegment.empty()

    a7 = abcd[12]
    b7 = abcd[13]
    if a4 <= duration and b4 <= duration:
        clip6 = AudioFileClip("myfile.mp3").subclip(a4, b4)
        clip6.write_audiofile("audio6.mp3")
        f = myfunction('audio6.mp3')
        if f != 0:
            def speak(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good5.mp3")

            speak(f)
            sound6 = AudioSegment.from_file("good5.mp3")
        else:
            sound6 = AudioSegment.empty()

    else:
        sound6 = AudioSegment.empty()

    a8 = abcd[14]
    b8 = abcd[15]
    if b4 <= duration and a5 <= duration:
        clip7 = AudioFileClip("myfile.mp3").subclip(b4, a5)
        clip7.write_audiofile("audio7.mp3")
        g = myfunction('audio7.mp3')
        if g != 0:
            def speak6(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good6.mp3")

            speak6(g)
            sound7 = AudioSegment.from_file("good6.mp3")
        else:
            sound7 = AudioSegment.empty()

    else:
        sound7 = AudioSegment.empty()

    a9 = abcd[16]
    b9 = abcd[17]
    if a5 <= duration and b5 <= duration:
        clip8 = AudioFileClip("myfile.mp3").subclip(a5, b5)
        clip8.write_audiofile("audio8.mp3")
        h = myfunction('audio8.mp3')
        if h != 0:
            def speak7(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good7.mp3")

            speak7(h)
            sound8 = AudioSegment.from_file("good7.mp3")
        else:
            sound8 = AudioSegment.empty()
    else:
        sound8 = AudioSegment.empty()

    a10 = abcd[18]
    b10 = abcd[19]
    if b5 <= duration and a6 <= duration:
        clip9 = AudioFileClip("myfile.mp3").subclip(b5, a6)
        clip9.write_audiofile("audio9.mp3")
        i = myfunction('audio9.mp3')
        if i != 0:
            def speak8(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good8.mp3")

            speak8(i)
            sound9 = AudioSegment.from_file("good8.mp3")
        else:
            sound9 = AudioSegment.empty()

    else:
        sound9 = AudioSegment.empty()

    a11 = abcd[20]

    if a6 <= duration and b6 <= duration:
        clip10 = AudioFileClip("myfile.mp3").subclip(a6, b6)
        clip10.write_audiofile("audio10.mp3")
        j = myfunction('audio10.mp3')
        if j != 0:
            def speak9(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good9.mp3")

            speak9(j)
            sound10 = AudioSegment.from_file("good9.mp3")
        else:
            sound10 = AudioSegment.empty()

    else:
        sound10 = AudioSegment.empty()

    if b6 <= duration and a7 <= duration:
        clip11 = AudioFileClip("myfile.mp3").subclip(b6, a7)
        clip11.write_audiofile("audio12.mp3")
        k = myfunction('audio12.mp3')
        if k != 0:
            def speak(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good10.mp3")

            speak(k)
            sound11 = AudioSegment.from_file("good10.mp3")
        else:
            sound11 = AudioSegment.empty()

    else:
        sound11 = AudioSegment.empty()

    if a7 <= duration and b7 <= duration:
        clip12 = AudioFileClip("myfile.mp3").subclip(a7, b7)
        clip12.write_audiofile("audio13.mp3")
        l = myfunction('audio13.mp3')
        if l != 0:
            def speak(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good11.mp3")

            speak(l)
            sound12 = AudioSegment.from_file("good11.mp3")
        else:
            sound12 = AudioSegment.empty()

    else:
        sound12 = AudioSegment.empty()

    if b7 <= duration and a8 <= duration:
        clip13 = AudioFileClip("myfile.mp3").subclip(b7, a8)
        clip13.write_audiofile("audio14.mp3")
        m = myfunction('audio14.mp3')
        if m != 0:
            def speak(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good12.mp3")

            speak(m)
            sound13 = AudioSegment.from_file("good12.mp3")
        else:
            sound13 = AudioSegment.empty()

    else:
        sound13 = AudioSegment.empty()

    if a8 <= duration and b8 <= duration:
        clip14 = AudioFileClip("myfile.mp3").subclip(a8, b8)
        clip14.write_audiofile("audio15.mp3")
        n = myfunction('audio15.mp3')
        if n != 0:
            def speak(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good13.mp3")

            speak(n)
            sound14 = AudioSegment.from_file("good13.mp3")
        else:
            sound14 = AudioSegment.empty()

    else:
        sound14 = AudioSegment.empty()

    if b8 <= duration and a9 <= duration:
        clip15 = AudioFileClip("myfile.mp3").subclip(b8, a9)
        clip15.write_audiofile("audio16.mp3")
        o = myfunction('audio16.mp3')
        if o != 0:
            def speak(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good14.mp3")

            speak(o)
            sound15 = AudioSegment.from_file("good14.mp3")
        else:
            sound15 = AudioSegment.empty()
    else:
        sound15 = AudioSegment.empty()

    if a9 <= duration and b9 <= duration:
        clip16 = AudioFileClip("myfile.mp3").subclip(a9, b9)
        clip16.write_audiofile("audio17.mp3")
        p = myfunction('audio17.mp3')
        if p != 0:
            def speak(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good15.mp3")

            speak(p)
            sound16 = AudioSegment.from_file("good15.mp3")
        else:
            sound16 = AudioSegment.empty()

    else:
        sound16 = AudioSegment.empty()

    if b9 <= duration and a10 <= duration:
        clip17 = AudioFileClip("myfile.mp3").subclip(b9, a10)
        clip17.write_audiofile("audio18.mp3")
        q = myfunction('audio18.mp3')
        if q != 0:
            def speak(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good16.mp3")

            speak(q)
            sound17 = AudioSegment.from_file("good16.mp3")
        else:
            sound17 = AudioSegment.empty()

    else:
        sound17 = AudioSegment.empty()

    if a10 <= duration and b10 <= duration:
        clip18 = AudioFileClip("myfile.mp3").subclip(a10, b10)
        clip18.write_audiofile("audio19.mp3")
        r = myfunction('audio19.mp3')
        if r != 0:
            def speak(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good17.mp3")

            speak(r)
            sound18 = AudioSegment.from_file("good17.mp3")
        else:
            sound18 = AudioSegment.empty()

    else:
        sound18 = AudioSegment.empty()

    if b10 <= duration and a11 <= duration:
        clip19 = AudioFileClip("myfile.mp3").subclip(b10, a11)
        clip19.write_audiofile("audio20.mp3")
        s = myfunction('audio20.mp3')
        if s != 0:
            def speak(text):
                tts = gTTS(text=text, lang='en')
                tts.save("good18.mp3")

            speak(s)
            sound19 = AudioSegment.from_file("good18.mp3")
        else:
            sound19 = AudioSegment.empty()

    else:
        sound19 = AudioSegment.empty()

    combined = sound + sound1 + sound2 + sound3 + sound4 + sound5 + sound6 + sound7 + sound8 + sound9 + sound10 + sound11 + sound12 + sound13 + sound14 + sound15 + sound16 + sound17 + sound18 + sound19
    # simple export
    file_handle = combined.export("output.mp3", format="mp3")
    global silence
    myaudio = AudioSegment.from_mp3("myfile.mp3")
    dBFS = myaudio.dBFS
    silence = silence.detect_silence(myaudio, min_silence_len=2000, silence_thresh=dBFS - 8)
    silence = [((start / 1000), (stop / 1000)) for start, stop in silence]
    audio1 = AudioSegment.from_file('output.mp3')
    duration1 = audio1.duration_seconds

    for start, stop in silence:

        if silence[0] in silence:
            a = silence[0]
            abc = a[:1]
            res = str(abc)[1:-1]
            b = ''.join(str(res).split(','))
            lst_str = b
            ab = int(float(lst_str))

            a1 = silence[0]
            abc1 = a1[1:]
            res1 = str(abc1)[1:-1]
            b1 = ''.join(str(res1).split(','))
            lst_str2 = b1
            ab2 = int(float(lst_str2))
            if ab <= duration1 and ab2 <= duration1:
                clip11 = AudioFileClip('output.mp3').subclip(0, ab)
                clip11.write_audiofile("abc.mp3")
                sound4 = AudioSegment.from_file('abc.mp3')
                n = ab2 - ab
                second_silence = AudioSegment.silent(duration=n * 1000)
                combined1 = sound4 + second_silence
                file_handle12 = combined1.export("output121.mp3", format="mp3")
                sound11 = AudioSegment.from_file("output121.mp3")
            else:
                sound11 = AudioSegment.empty()
        else:
            sound11 = AudioSegment.empty()

        if silence[1] in silence:
            a11 = silence[1]
            abc11 = a11[:1]
            res11 = str(abc11)[1:-1]
            b11 = ''.join(str(res11).split(','))
            lst_str11 = b11
            ab11 = int(float(lst_str11))

            a12 = silence[1]
            abc12 = a12[1:]
            res12 = str(abc12)[1:-1]
            b12 = ''.join(str(res12).split(','))
            lst_str22 = b12
            ab22 = int(float(lst_str22))

            a1 = silence[0]
            abc1 = a1[1:]
            res1 = str(abc1)[1:-1]
            b1 = ''.join(str(res1).split(','))
            lst_str2 = b1
            ab2 = int(float(lst_str2))

            if ab2 <= duration1 and ab11 <= duration1:
                clip12 = AudioFileClip('output.mp3').subclip(ab2, ab11)
                clip12.write_audiofile("abc1.mp3")
                sound42 = AudioSegment.from_file('abc1.mp3')
                n1 = ab22 - ab11

                second_silence2 = AudioSegment.silent(duration=n1 * 1000)
                combined12 = sound42 + second_silence2
                file_handle122 = combined12.export("output122.mp3", format="mp3")
                sound22 = AudioSegment.from_file("output122.mp3")
            else:
                sound22 = AudioSegment.empty()

        else:
            sound22 = AudioSegment.empty()

        if silence[2] in silence:
            a66 = silence[2]
            abc66 = a66[:1]
            res66 = str(abc66)[1:-1]
            b66 = ''.join(str(res66).split(','))
            lst_str66 = b66
            ab66 = int(float(lst_str66))

            a12 = silence[1]
            abc12 = a12[1:]
            res12 = str(abc12)[1:-1]
            b12 = ''.join(str(res12).split(','))
            lst_str22 = b12
            ab22 = int(float(lst_str22))


            a77 = silence[2]
            abc77 = a77[1:]
            res77 = str(abc77)[1:-1]
            b77 = ''.join(str(res77).split(','))
            lst_str77 = b77
            ab77 = int(float(lst_str77))


            if ab22 <= duration1 and ab66 <= duration1:
                clip13 = AudioFileClip('output.mp3').subclip(ab22, ab66)
                clip13.write_audiofile("abc2.mp3")
                sound66 = AudioSegment.from_file('abc2.mp3')
                n2 = ab77 - ab66
                second_silence3 = AudioSegment.silent(duration=n2 * 1000)

                combined13 = sound66 + second_silence3
                file_handle13 = combined13.export("output123.mp3", format="mp3")
                sound33 = AudioSegment.from_file("output123.mp3")
            else:
                sound33 = AudioSegment.empty()
        else:
            sound33 = AudioSegment.empty()

        if silence[3] in silence:
            a14 = silence[3]
            abc14 = a14[:1]
            res14 = str(abc14)[1:-1]
            b14 = ''.join(str(res14).split(','))
            lst_str14 = b14
            ab14 = int(float(lst_str14))

            a15 = silence[3]
            abc15 = a15[1:]
            res15 = str(abc15)[1:-1]
            b15 = ''.join(str(res15).split(','))
            lst_str25 = b15
            ab25 = int(float(lst_str25))

            a77 = silence[2]
            abc77 = a77[1:]
            res77 = str(abc77)[1:-1]
            b77 = ''.join(str(res77).split(','))
            lst_str77 = b77
            ab77 = int(float(lst_str77))

            if ab77 <= duration1 and ab14 <= duration1:
                clip14 = AudioFileClip('output.mp3').subclip(ab77, ab14)
                clip14.write_audiofile("abc3.mp3")
                sound44 = AudioSegment.from_file('abc3.mp3')
                n3 = ab25 - ab14
                second_silence4 = AudioSegment.silent(duration=n3 * 1000)
                combined14 = sound44 + second_silence4
                file_handle14 = combined14.export("output124.mp3", format="mp3")
                sound44 = AudioSegment.from_file("output124.mp3")
            else:
                sound44 = AudioSegment.empty()
        else:
            sound44 = AudioSegment.empty()

        combined16 = sound11 + sound22 + sound33 + sound44
        file_handle16 = combined16.export("output126.mp3", format="mp3")

        audio2 = AudioSegment.from_mp3('output126.mp3')
        duration2 = audio2.duration_seconds

        clip99 = VideoFileClip(video_file)

        clip99 = clip99.subclip(0, duration2)

        new_clip = clip99.set_duration(duration2)

        audioclip = AudioFileClip('output126.mp3')

        clip99 = clip99.set_audio(audioclip)

        clip99.write_videofile(video_file, fps=60)

        break

    return video_file

@app.route("/", methods=["GET","POST"])
def upload_file():

    if request.method == 'POST':
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files.get('file')
        selected_language = request.form["select-language"]
        filename = secure_filename(file.filename)
        filename = file.filename

        translation = function(file, selected_language)

        if file.filename == '':
            print('no filename')
            return redirect(request.url)
        else:
            filename = secure_filename(translation)

            return redirect('/downloadfile/' + filename)

    return render_template('index.html')

@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
    return render_template('index.html', value=filename)

@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = filename
    return send_file(file_path, as_attachment=True, attachment_filename='')

@app.route("/about", methods = ['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    return render_template('contact.html')

if __name__== "__main__":
    app.run("0.0.0.0", debug=True)