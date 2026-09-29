from flask import Flask, request, jsonify, render_template_string
import kkk

app = Flask(__name__, static_folder='public', static_url_path='')
PAGE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>锟斤拷</title>
<style>
    body { font-family: system-ui, "Microsoft YaHei", sans-serif;
            max-width: 760px; margin: 40px auto; padding: 0 16px; color: #222; }
    h1 { font-size: 22px; }
    label { display: block; margin: 16px 0 6px; font-weight: 600; font-size: 14px; }
    textarea { width: 100%; height: 140px; padding: 10px; font-size: 14px;
                font-family: Consolas, ui-monospace, monospace;
                border: 1px solid #ccc; border-radius: 6px;
                resize: vertical; box-sizing: border-box; }
    button { margin: 12px 8px 12px 0; padding: 9px 22px; font-size: 15px;
            background: #2563eb; color: #fff; border: 0;
            border-radius: 6px; cursor: pointer; }
    button:hover { background: #1d4ed8; }
    #output { background: #f6f7f9; }
</style>
</head>
<body>
    <h1>文字转编码?</h1>

    <label for="input">输入</label>
    <textarea id="input" placeholder="在这里输入要转换的文字…"></textarea>

    <button id="convert">转换</button>
    <button id="clear">清空</button>
    <button id="copy" onclick="navigator.clipboard.writeText($out.value)">复制</button>

    <label for="output">输出</label>
    <textarea id="output" readonly placeholder="结果"></textarea>

    <div id="status"></div>

<script>
    const $in     = document.getElementById('input');
    const $out    = document.getElementById('output');

    async function run() {
    if (!$in.value) { $out.value = ''; return; }
    try {
        const r = await fetch('/api/convert', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: $in.value })
        });
        const d = await r.json();
        if (!r.ok) throw new Error(d.error || r.statusText);
        $out.value = d.result;
    } catch (e) {
        $out.value = '';
        alert('error: ' + e.message);
    }
    }

    document.getElementById('convert').onclick = run;
    document.getElementById('clear').onclick = () => {
    $in.value = $out.value = '';
    $in.focus();
    };
    $in.addEventListener('keydown', e => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') run();
    });
</script>
</body>
</html>"""
@app.get('/')
def index():
    return render_template_string(PAGE)
@app.post('/api/convert')
def convert():
    text = (request.get_json(silent=True) or {}).get('text', '')
    return jsonify(result=kkk.to_kkk(text))

if __name__ == '__main__':
    app.run(port=3000, debug=True, use_reloader=False)
