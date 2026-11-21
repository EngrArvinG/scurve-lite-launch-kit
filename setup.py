#!/usr/bin/env python3
"""Fill in the placeholders of the landing page and the Lite workbook.

Run from the kit folder:   python3 setup.py
Optional (no questions):   python3 setup.py --user NAME --repo REPO --form FORM_URL \
                                              [--store STORE_URL] [--email EMAIL]
Safe to run again: it always starts from the placeholder copies in ./site-template/
(created on the first run) and writes the finished files to ./site/.
"""
import argparse, os, re, shutil, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, "site")
TEMPLATE = os.path.join(HERE, "site-template")
XLSX = os.path.join("downloads", "S-Curve_Gantt_Planner_Vol2_FREE_LITE.xlsx")
XLSX_PLACEHOLDER = "[ADD YOUR STORE LINK HERE]"
DEFAULT_EMAIL = "engrkit.support@gmail.com"


def ask(label, default=None, required=True):
    while True:
        hint = f" [{default}]" if default else ""
        v = input(f"{label}{hint}: ").strip() or (default or "")
        if v or not required:
            return v
        print("  This one is required.")


def embed_url(form_url):
    if "embedded=true" in form_url:
        return form_url
    return form_url + ("&" if "?" in form_url else "?") + "embedded=true"


def xml_escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def patch_xlsx(path, new_text):
    """Replace the placeholder text inside the workbook without touching anything else."""
    tmp = path + ".tmp"
    found = False
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename.startswith("xl/") and item.filename.endswith(".xml"):
                txt = data.decode("utf-8")
                if XLSX_PLACEHOLDER in txt:
                    txt = txt.replace(XLSX_PLACEHOLDER, xml_escape(new_text))
                    data = txt.encode("utf-8")
                    found = True
            zout.writestr(item, data)
    os.replace(tmp, path)
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--user"); ap.add_argument("--repo"); ap.add_argument("--form")
    ap.add_argument("--store", default=None); ap.add_argument("--email")
    a = ap.parse_args()

    # keep an untouched copy so the script can be re-run
    if not os.path.isdir(TEMPLATE):
        shutil.copytree(SITE, TEMPLATE)
    if os.path.isdir(SITE):
        shutil.rmtree(SITE)
    shutil.copytree(TEMPLATE, SITE)

    print("\nS-Curve Lite landing page setup\n")
    user = a.user or ask("Your GitHub username")
    repo = a.repo or ask("Name of the GitHub repository you will create", "scurve-lite")
    form = a.form or ask("Your Google Form link (the one that starts with https://docs.google.com/forms/)")
    store = a.store if a.store is not None else ask("Link to your store page for the full pack (press Enter to skip)", required=False)
    email = a.email or ask("Contact email shown on the page", DEFAULT_EMAIL)

    site_url = f"https://{user.lower()}.github.io/{repo}/"
    download_url = site_url + XLSX.replace(os.sep, "/")

    # ---- landing page
    index = os.path.join(SITE, "index.html")
    html = open(index, encoding="utf-8").read()
    if store:
        html = html.replace("<!--STORE-->", "").replace("<!--/STORE-->", "")
    else:  # no store link yet: remove the "Need more room?" block
        html = re.sub(r"<!--STORE-->.*?<!--/STORE-->", "", html, flags=re.S)
    for k, v in {"{{SITE_URL}}": site_url, "{{FORM_URL}}": form, "{{FORM_EMBED_URL}}": embed_url(form),
                 "{{STORE_URL}}": store, "{{EMAIL}}": email}.items():
        html = html.replace(k, v)
    open(index, "w", encoding="utf-8").write(html)

    # ---- workbook (store link or the page link goes into START HERE!C4)
    ok = patch_xlsx(os.path.join(SITE, XLSX), store or site_url)

    print("\nDone. Files are in the 'site' folder.\n")
    print("  Landing page will be at :", site_url)
    print("  Lite file download link  :", download_url)
    print("  Workbook link patched    :", "yes" if ok else "NO - placeholder not found, edit START HERE!C4 by hand")
    print("\nNext: upload the CONTENTS of the 'site' folder to your GitHub repository (see SETUP_GUIDE.md, Step 4).")
    left = re.findall(r"\{\{[A-Z_]+\}\}", html)
    if left:
        print("WARNING: unfilled placeholders:", sorted(set(left)))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
