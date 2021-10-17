#!/usr/bin/env python
from flask import Flask, request, send_file
from werkzeug.exceptions import BadRequest, Forbidden

from gtts import gTTS

import io


app = Flask(__name__)
with open("/run/secrets/token") as fp:
    configured_token = fp.read().strip()

@app.route("/talk")
def talk():
    text = request.args.get("text")
    token = request.args.get("token")
    if not text:
        raise BadRequest

    if token != configured_token:
        raise Forbidden

    tts = gTTS(text=text, lang="cs", slow=False)
    output_buffer = io.BytesIO()
    tts.write_to_fp(output_buffer)
    output_buffer.seek(0)

    return send_file(
        output_buffer,
        mimetype='audio/mpeg'
    )
