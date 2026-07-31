import json, os

BASE = "https://cqyqds.cn"
with open("works_data.json", encoding="utf-8") as f:
    works = json.load(f)

TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Yanqing Sculpture — {category}</title>
    <meta name="description" content="{title} — {category}。{material}。Zhao Yanqing。{year}。">
    <meta property="og:title" content="{title} | Yanqing Sculpture">
    <meta property="og:description" content="{og_desc}">
    <meta property="og:image" content="https://cqyqds.cn/{og_img}">
    <link rel="canonical" href="https://cqyqds.cn/works/{slug}.html">
    <link rel="icon" type="image/png" href="../logo.png">
    <meta name="theme-color" content="#0a0a0a">
    <meta name="robots" content="index, follow">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "VisualArtwork",
        "name": "{title}",
        "creator": {{"@type": "Person", "name": "Zhao Yanqing"}},
        "artMedium": "{material}",
        "dateCreated": "{year}"{loc_json}
    }}
    </script>
    <link rel="stylesheet" href="works.css">
</head>
<body>
<nav>
    <div class="nav-inner">
        <a href="../index.html" class="nav-brand-wrap">
            <img src="../logo.png" alt="Yanqing Sculpture" class="nav-logo">
            <span class="nav-brand">MAISON <span>&middot;</span> YANQING</span>
        </a>
        <ul class="nav-links">
            <li><a href="../index.html#about">About</a></li>
            <li><a href="../index.html#portfolio">Works</a></li>
            <li><a href="../index.html#projects">Projects</a></li>
            <li><a href="../index.html#honors">Honors</a></li>
            <li><a href="../index.html#contact">Contact</a></li>
        </ul>
        <div class="breadcrumb">
            <a href="../index.html">Home</a> / <a href="index.html">Works</a> / <span>{category}</span>
        </div>
    </div>
</nav>

<div class="work-container">
    <div class="work-header">
        {overhead}
        <h1 class="work-title">{title}</h1>
        <p class="work-subtitle">{title_en}</p>
        <div class="work-line"></div>
    </div>

    <img src="{hero_img}" alt="{title}" class="work-hero" loading="lazy">

    <div class="work-grid">
        <div class="work-col">
            <div class="work-col-label">Details</div>
            <h2>About This Work</h2>
            <div class="work-specs">
                <div class="work-spec-item">
                    <div class="work-spec-label">Category</div>
                    <div class="work-spec-value">{category}</div>
                    <div class="work-spec-value en">{category_en}</div>
                </div>
                <div class="work-spec-item">
                    <div class="work-spec-label">Year</div>
                    <div class="work-spec-value">{year}</div>
                </div>
                <div class="work-spec-item">
                    <div class="work-spec-label">Material</div>
                    <div class="work-spec-value">{material}</div>
                    <div class="work-spec-value en">{material_en}</div>
                </div>
                {dims_html}
                {award_html}
            </div>
            {intro_html}
        </div>
        <div class="work-col">
            <div class="work-col-label">Atelier Notes</div>
            <h2>Certificate</h2>
            <div class="work-cert">
                <div class="work-cert-title">Certificate of Authenticity</div>
                <h3>{num}</h3>
                <p>{title}<br>Zhao Yanqing &middot; Handcrafted Unique Piece</p>
                <p class="en">{title_en}<br>Handcrafted by Zhao Yanqing &middot; Unique Piece</p>
                <p class="en" style="margin-top:1rem;">Materials: {material_en}<br>Year: {year}{cert_loc}</p>
                <div class="atelier">MAISON <span>&middot;</span> YANQING <span>&middot;</span> ATELIER <span>&middot;</span> Est. MMXVI</div>
            </div>
        </div>
    </div>

    {gallery_html}
    {story_html}

    <div class="work-back">
        <a href="index.html">Back to Works</a>
    </div>
</div>

<footer>
    <div class="footer-brand">MAISON <span>&middot;</span> YANQING <span>&middot;</span> ATELIER</div>
    <div class="footer-tagline">Est. MMXVI &middot; Chongqing &amp; Baoxing</div>
    <div class="footer-copy">&copy; 2016&ndash;2026 Yanqing Sculpture Art Co., Ltd. &middot; Baoxing Yanqing Sculpture Art Co., Ltd.</div>
</footer>
</body>
</html>"""

def build(work):
    loc = work.get("location", "")
    overhead = f'<div class="work-overline">{work["num"]} &middot; {work["year"]}'
    if loc:
        overhead += f' &middot; {loc}'
    overhead += "</div>"

    dims = ""
    if work.get("dimensions"):
        dims = f'<div class="work-spec-item"><div class="work-spec-label">Dimensions</div><div class="work-spec-value">{work["dimensions"]}</div><div class="work-spec-value en">{work["dimensions_en"]}</div></div>'

    award = ""
    if work.get("award"):
        award = f'<div class="work-spec-item"><div class="work-spec-label">Award</div><div class="work-spec-value">{work["award"]}</div><div class="work-spec-value en">{work["award_en"]}</div></div>'

    intro_html = ""
    if work.get("intro"):
        intro_html = f'<p>{work["intro"]}</p>\n            <p class="en">{work["intro_en"]}</p>'

    gallery = ""
    if work.get("gallery"):
        gallery = '<div class="work-gallery">\n'
        for img in work["gallery"]:
            gallery += f'            <img src="{img}" loading="lazy" alt="{work["title"]}">\n'
        gallery += '        </div>'

    story = ""
    if work.get("story"):
        story = f'''    <div class="work-story">
        <div class="work-story-inner">
            <div class="tag">The Story</div>
            <h2>Creative Story</h2>
            <blockquote>{work["story"]}</blockquote>
            <blockquote class="en">{work["story_en"]}</blockquote>
        </div>
    </div>'''

    loc_json = ""
    if loc:
        loc_json = f',"locationCreated": "{loc}"'

    cert_loc = ""
    if loc:
        cert_loc = f' &middot; Location: {loc}'

    og_desc = (work.get("intro") or work.get("title", ""))[:150]
    og_img = work["hero_img"].replace("../", "")

    return TEMPLATE.format(
        slug=work["slug"], title=work["title"], title_en=work["title_en"],
        category=work["category"], category_en=work["category_en"],
        num=work["num"], year=work["year"],
        material=work["material"], material_en=work["material_en"],
        hero_img=work["hero_img"], overhead=overhead,
        dims_html=dims, award_html=award, intro_html=intro_html,
        gallery_html=gallery, story_html=story,
        loc_json=loc_json, cert_loc=cert_loc,
        og_desc=og_desc, og_img=og_img,
    )

os.makedirs("works", exist_ok=True)
for w in works:
    path = os.path.join("works", f'{w["slug"]}.html')
    with open(path, "w", encoding="utf-8") as f:
        f.write(build(w))
    print(f"  OK: {path}")
print(f"\nDone: {len(works)} pages.")
