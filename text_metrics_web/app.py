import matplotlib

matplotlib.use("Agg")
"""
Text Metrics Calculator Web Application (Flask)

This web app provides all features of the original GUI:
- Manual text input and file upload
- Text metrics calculation
- Language detection
- Report saving
- Professional, modern UI
"""

import os
import re
import io
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_file,
    flash,
    Response,
)
from werkzeug.utils import secure_filename
from langdetect import detect, LangDetectException

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a secure key in production
UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)


# --- Utility Functions ---
def calculate_text_metrics(text):
    sentences = len(re.findall(r"[.!?]+", text))
    words = len(re.findall(r"\b\w+\b", text))
    characters = len(re.findall(r"\S", text))
    whitespace = len(re.findall(r"\s", text))
    special_characters = len(re.findall(r"[^\w\s]", text))
    return {
        "sentences": sentences,
        "words": words,
        "characters": characters,
        "whitespace": whitespace,
        "special_characters": special_characters,
    }


def generate_metrics_chart(metrics):
    # Only plot if metrics is not None
    if not metrics:
        return None
    metric_names = [
        k.replace("_", " ").capitalize() for k in metrics.keys() if k != "language"
    ]
    metric_values = [v for k, v in metrics.items() if k != "language"]
    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(metric_names, metric_values, color="#4a90e2")
    ax.set_ylabel("Value")
    ax.set_title("Text Metrics Visualization")
    ax.set_xticks(range(len(metric_names)))
    ax.set_xticklabels(metric_names, rotation=15, ha="right", fontsize=11)
    plt.subplots_adjust(bottom=0.22)
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return buf


def detect_language(text):
    try:
        language_code = detect(text)
        language_map = {
            "en": "English",
            "fr": "French",
            "de": "German",
            "es": "Spanish",
            "it": "Italian",
            "pt": "Portuguese",
            "ru": "Russian",
            "zh-cn": "Chinese (Simplified)",
            "zh-tw": "Chinese (Traditional)",
            "ja": "Japanese",
            "ko": "Korean",
            "ar": "Arabic",
            "hi": "Hindi",
            "bn": "Bengali",
            "tr": "Turkish",
            "vi": "Vietnamese",
            "id": "Indonesian",
            "fa": "Persian",
            "pl": "Polish",
            "uk": "Ukrainian",
            "ro": "Romanian",
            "nl": "Dutch",
            "el": "Greek",
            "sv": "Swedish",
            "no": "Norwegian",
            "fi": "Finnish",
            "da": "Danish",
            "hu": "Hungarian",
            "cs": "Czech",
            "sk": "Slovak",
            "he": "Hebrew",
            "th": "Thai",
            "ms": "Malay",
            "ta": "Tamil",
            "te": "Telugu",
            "mr": "Marathi",
            "ur": "Urdu",
            "sw": "Swahili",
            "af": "Afrikaans",
            "sl": "Slovenian",
            "hr": "Croatian",
            "sr": "Serbian",
            "lt": "Lithuanian",
            "lv": "Latvian",
            "et": "Estonian",
            "fil": "Filipino",
            "bg": "Bulgarian",
            "ca": "Catalan",
            "eu": "Basque",
            "gl": "Galician",
            "is": "Icelandic",
            "mk": "Macedonian",
            "sq": "Albanian",
            "az": "Azerbaijani",
            "hy": "Armenian",
            "ka": "Georgian",
            "uz": "Uzbek",
            "kk": "Kazakh",
            "mn": "Mongolian",
            "my": "Burmese",
            "km": "Khmer",
            "lo": "Lao",
            "si": "Sinhala",
            "pa": "Punjabi",
            "gu": "Gujarati",
            "kn": "Kannada",
            "ml": "Malayalam",
            "or": "Odia",
            "ne": "Nepali",
            "ps": "Pashto",
            "sd": "Sindhi",
            "tk": "Turkmen",
            "ky": "Kyrgyz",
            "tg": "Tajik",
            "tt": "Tatar",
            "ba": "Bashkir",
            "be": "Belarusian",
            "mo": "Moldavian",
            "bs": "Bosnian",
            "ceb": "Cebuano",
            "jv": "Javanese",
            "su": "Sundanese",
            "yo": "Yoruba",
            "ig": "Igbo",
            "ha": "Hausa",
            "zu": "Zulu",
            "xh": "Xhosa",
            "st": "Southern Sotho",
            "tn": "Tswana",
            "ts": "Tsonga",
            "ss": "Swati",
            "ve": "Venda",
            "nr": "South Ndebele",
            "rw": "Kinyarwanda",
            "ln": "Lingala",
            "kg": "Kongo",
            "lu": "Luba-Katanga",
            "wa": "Walloon",
            "fo": "Faroese",
            "gd": "Scottish Gaelic",
            "cy": "Welsh",
            "br": "Breton",
            "co": "Corsican",
            "lb": "Luxembourgish",
            "mt": "Maltese",
            "rm": "Romansh",
            "sco": "Scots",
            "ga": "Irish",
            "yi": "Yiddish",
            "io": "Ido",
            "eo": "Esperanto",
            "la": "Latin",
            "sa": "Sanskrit",
            "tl": "Tagalog",
            "mi": "Maori",
            "qu": "Quechua",
            "ay": "Aymara",
            "gn": "Guarani",
            "ug": "Uyghur",
        }
        return language_map.get(language_code, language_code)
    except LangDetectException:
        return "Unknown"


def save_report(metrics, content, filename):
    report_path = os.path.join(REPORT_FOLDER, filename)
    language = metrics.get("language", None)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("CONTENT:\n" + str(content) + "\n\n")
        f.write("Text Metrics Summary Report\n")
        f.write("---------------------------\n")
        # Table rows (no vertical bars, left-aligned metric, right-aligned value)
        for key, value in metrics.items():
            if key == "language":
                continue
            metric_name = key.replace("_", " ").capitalize()
            f.write(f"{metric_name:<32}{str(value):>10}\n")
        if language:
            f.write(f"{'Language detected':<32}{language:>10}\n")
        f.write("\n")
    return report_path


# --- Routes ---
@app.route("/", methods=["GET", "POST"])
def index():
    metrics = None
    language = None
    content = ""
    chart_available = False
    if request.method == "POST":
        file = request.files.get("file")
        content = request.form.get("text", "")
        if file and file.filename:
            try:
                file.seek(0)
                content = file.read().decode("utf-8")
            except Exception:
                filename = secure_filename(file.filename)
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                file.save(filepath)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
        if content.strip():
            metrics = calculate_text_metrics(content)
            language = detect_language(content)
            chart_available = True
        else:
            flash("Please enter text or upload a file.", "warning")
    return render_template(
        "index.html",
        metrics=metrics,
        language=language,
        content=content,
        chart_available=chart_available,
    )


@app.route("/metrics_chart.png")
def metrics_chart():
    # Get metrics from query string (for demo, use session or pass via POST for production)
    # Here, we use last POSTed metrics (not persistent, for demo only)
    content = request.args.get("content", "")
    if not content.strip():
        return Response(status=404)
    metrics = calculate_text_metrics(content)
    buf = generate_metrics_chart(metrics)
    if buf:
        return Response(buf.getvalue(), mimetype="image/png")
    return Response(status=404)


@app.route("/calculate", methods=["POST"])
def calculate():
    content = request.form.get("text", "")
    if not content.strip():
        flash("No content provided for analysis.", "warning")
        return redirect(url_for("index"))

    metrics = calculate_text_metrics(content)
    language = detect_language(content)
    filename = secure_filename(request.form.get("filename", "report.txt"))
    report_path = save_report(metrics, content, filename)
    return send_file(report_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
