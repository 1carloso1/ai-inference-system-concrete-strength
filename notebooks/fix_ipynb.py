import json, sys, pathlib, traceback

def die(msg, code=1):
    print(f"[ERROR] {msg}")
    sys.exit(code)

try:
    if len(sys.argv) < 2:
        die("Uso: python fix_ipynb.py RUTA_AL_NOTEBOOK.ipynb")

    p = pathlib.Path(sys.argv[1])
    if not p.exists():
        die(f"No existe el archivo: {p}")

    print(f"[INFO] Leyendo: {p}")
    raw = p.read_text(encoding="utf-8")
    nb = json.loads(raw)
    print("[INFO] JSON cargado OK")

    md = nb.get("metadata", {})
    had_widgets_meta = "widgets" in md
    if had_widgets_meta:
        print("[INFO] metadata.widgets presente -> será eliminado")
        md.pop("widgets", None)
    else:
        print("[INFO] NO había metadata.widgets en el nivel raíz")

    nb["metadata"] = md

    removed_cell_keys = 0
    for cell in nb.get("cells", []):
        cm = cell.get("metadata", {})
        for k in ["widgets", "widget_view", "init_cell", "execution"]:
            if k in cm:
                cm.pop(k, None)
                removed_cell_keys += 1
        cell["metadata"] = cm

    p.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")

    print("[OK] Notebook limpiado y guardado")
    print(f"      - widgets en raíz eliminado: {had_widgets_meta}")
    print(f"      - claves removidas en celdas: {removed_cell_keys}")
    print(f"Archivo: {p.name}")
except Exception as e:
    print("[ERROR] Excepción durante la limpieza:")
    traceback.print_exc()
    sys.exit(2)
