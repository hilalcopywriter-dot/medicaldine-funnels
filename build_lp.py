# -*- coding: utf-8 -*-
# Générateur des 4 landing pages Medicaldine (parcours personnalisé)
import os, hashlib
OUT = os.path.dirname(os.path.abspath(__file__))

def _ver(fname):
    """Empreinte courte du fichier pour casser le cache navigateur (anti-cache)."""
    try:
        return hashlib.md5(open(os.path.join(OUT, fname), 'rb').read()).hexdigest()[:8]
    except OSError:
        return '1'

SHAR='https://medicaldine.ma/wp-content/uploads/2026/05/medicaldine6-1.png'
CREAM='https://medicaldine.ma/wp-content/uploads/2026/05/Untitled-3-e1777773509158.webp'
DRINK='https://medicaldine.ma/wp-content/uploads/2026/05/hh-1.png'
PACK='https://medicaldine.ma/wp-content/uploads/2025/04/medicaldine-pack2.jpg'
L7='https://medicaldine.ma/wp-content/uploads/2025/05/medicaldine8-7.jpg'
L11='https://medicaldine.ma/wp-content/uploads/2025/05/medicaldine8-11.jpg'
L15='https://medicaldine.ma/wp-content/uploads/2025/05/medicaldine8-15.jpg'
# Photos produit locales (dossier img/)
P_BLANC='img/femme-blanc.jpg'        # femme robe blanche + Shar Slim (hero élégant)
P_SOLEIL='img/femme-soleil.jpg'      # jeune femme coucher de soleil + Shar Slim (hero)
P_RIAD='img/femme-riad.jpg'          # femme au riad + Shar Slim (paysage, média)
P_SPORT='img/sport-selfie.jpg'       # selfie salle de sport (résultats / vie)
P_PACK='img/pack-nature.jpg'         # femme + les 3 produits dans l'herbe (hero pack complet)
P_SHARCREAM='img/shar-cream.jpg'     # Shar Slim + Belly Cream (nature)
P_CREAMDRINK='img/cream-drink.jpg'   # Belly Cream + Fat Burn Drink (nature)
P_CREAMING='img/cream-ingredients.jpg' # Belly Cream + ingrédients naturels
P_DRINK='img/fat-burn-drink.jpg'     # Burn Fat Drink en main

# Mécanisme réel de chaque produit (doc OTO)
ROLE={SHAR:'كيرفع معدّل الأيض ويخلي الجسم يحرق الدهون أسرع',
      DRINK:'فيه حمض HCA — كيستهدف دهون البطن العميقة ويقلّل الجوع',
      CREAM:'كيشتغل من برّا — كيمنع ترهّل الجلد وعلامات التمدد ويشدّ البشرة'}
PNAME={SHAR:'Shar Slim',CREAM:'Belly Cream',DRINK:'Fat Burn Drink'}
NAME2CONST={v:k for k,v in PNAME.items()}
# nom produit -> image (vignettes dans les cartes d'offre) — versions contrastées (fond coloré) pour rester visibles en petit
SHAR_THUMB='https://medicaldine.ma/wp-content/uploads/2025/04/Shar-Slim.jpg'
IMGOF={'Shar Slim':SHAR,'Belly Cream':CREAM,'Fat Burn Drink':DRINK}

# Fiche produit : image, fondants (fوائد) et مكوّنات — d'après le doc OTO + pages produits
PRODUCT_INFO={
 SHAR: dict(name='Shar Slim', img=SHAR,
   ben=['كيرفع معدّل الأيض ويسرّع الحرق','كيخلي الجسم يحرق الدهون أسرع','كيقلّل الشهية والجوع'],
   ing=['Guggul','Triphala','Garcinia','Ashwagandha']),
 DRINK: dict(name='Fat Burn Drink', img=DRINK,
   ben=['فيه حمض HCA','كيستهدف دهون البطن العميقة','كيقلّل الرغبة فالأكل والحلو'],
   ing=['الشاي الأخضر','Garcinia','حمض HCA']),
 CREAM: dict(name='Belly Cream', img=CREAM,
   ben=['كيشتغل من برّا على البطن والأرداف','كيمنع الترهّل وعلامات التمدد','كيشدّ البشرة'],
   ing=['الزنجبيل','الفلفل الأسود']),
}

V=['https://hercules-cdn.com/file_6XPSLk4vPr1f1O9xgx2mrC9W','https://hercules-cdn.com/file_IkcJ6rBUwxbB2LXZXwp2eBKx',
   'https://hercules-cdn.com/file_jP07vw7gUMTux3nOgnB066HA','https://hercules-cdn.com/file_1Klh8MbspVSRrg1yC8MV3YmT',
   'https://hercules-cdn.com/file_FASAhalsgPLLg1ElwjhV9zJK','https://hercules-cdn.com/file_1VFLouS1vL1zg4wNRny8quR6',
   'https://hercules-cdn.com/file_qrR12d9LzjSlIjiSPc93suGt','https://hercules-cdn.com/file_wztPMmOhoNeUh25DnfRaJ5sR',
   'https://hercules-cdn.com/file_Wed1TKl1HzpdDYy9LZUGYFNX','https://hercules-cdn.com/file_InvNrKy7YloPru2eCg4Fkkj1']

CHK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M20 6 9 17l-5-5"/></svg>'
BOX='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 8l9-5 9 5v8l-9 5-9-5z"/><path d="M3 8l9 5 9-5M12 13v8"/></svg>'
LOGO='<svg viewBox="0 0 44 42" fill="none"><circle cx="12" cy="7" r="6" fill="currentColor"/><path d="M4 40c0-9 2-16 7-19-3-1-6 0-8 3M20 40c0-9-2-16-7-19 3-1 6 0 8 3" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/><rect x="22" y="12" width="4" height="28" rx="2" fill="currentColor"/></svg>'

# Programmes OTO (doc) : nom, composition, valeur (السعر الأصلي), prix OTO, durée, phrase courte
PROG={
 'trio':      dict(name='Trio',         comp=['1 × Shar Slim','1 × Fat Burn Drink','1 × Belly Cream'], val=845, price=570, dur='شهر ونصف', one='حل شامل لكل الجسم'),
 'ventre':    dict(name='البطن المنحوت', comp=['2 × Shar Slim','1 × Belly Cream'],                     val=995, price=590, dur='3 أشهر', one='مخصّص للبطن والجزء العلوي'),
 'stop':      dict(name='وقف القرم',     comp=['2 × Shar Slim','1 × Fat Burn Drink'],                  val=1050,price=600, dur='3 أشهر', one='كيكبح الشهية والرغبة فالسكر'),
 'reset':     dict(name='ضبط الأيض',     comp=['3 × Shar Slim'],                                       val=1200,price=620, dur='3 أشهر', one='3 مراحل: ديتوكس · تنشيط · تثبيت'),
 'intensive': dict(name='المكثّف',       comp=['2 × Shar Slim','1 × Fat Burn Drink','1 × Belly Cream'],val=1245,price=650, dur='3 أشهر', one='أقوى وأسرع نتيجة · 4 منتجات'),
}
TIER={
 'good': dict(label='البديل الأوفر', badge='', reco=False, ben=['كوتش + تطبيق هاتفي','توصيل مجاني · حتا يوصلك عاد خلصي']),
 'better':dict(label='موصى بها ليكِ', badge='الأكثر ملاءمة', reco=True, ben=['مصمّمة لحالتكِ بالضبط','كوتش خاصة + تطبيق هاتفي','توصيل مجاني · حتا يوصلك عاد خلصي']),
 'best': dict(label='بريميوم', badge='', reco=False, ben=['أقصى وأسرع نتيجة','كوتش مكثّف + أولوية','توصيل مجاني · حتا يوصلك عاد خلصي']),
}
def offer(plabel, tk, pk):
    p=PROG[pk]; t=TIER[tk]
    promo=round((1-p['price']/p['val'])*100)
    return dict(reco=t['reco'], tlabel=t['label'], badge=t['badge'], pname=p['name'], comp=p['comp'],
                old=p['val'], now=p['price'], promo=promo, ben=t['ben'], dur=p['dur'], one=p['one'],
                pack=f"{plabel} — {p['name']} — {p['price']} درهم")

# Choix 1 : le produit seul (Shar Slim), le moins cher, sans programme — ancre de valeur
def product_only(plabel):
    return dict(reco=False, tlabel='المنتج بوحدو', badge='', pname='Shar Slim', comp=['1 × Shar Slim'],
                old=600, now=400, promo=33, ben=['توصيل مجاني','حتا يوصلك عاد خلصي'],
                dur='شهر واحد', one='المنتج فقط · بلا كوتش ولا متابعة',
                pack=f"{plabel} — المنتج بوحدو (Shar Slim) — 400 درهم")

DATA={
'ventre':{'title':'پاك البطن والأرداف — Medicaldine','kicker':'البطن والأرداف · 3 أشهر','plabel':'البطن',
  'h1':'الكرش مابغاتش تنقص <span>وخا عييتي ما درتي ليها؟</span>','sub':'برنامج كامل لمدة 3 أشهر باش تنقصي دهون الكرش والأرداف، مع كوتش خاصة وتطبيق هاتفي كيتبع معاك خطوة بخطوة.',
  'hero':P_BLANC,'agit_img':P_SPORT,'life':P_SHARCREAM,'agit_h':'واش هادشي لي واقع ليك دبا؟',
  'pains':['الكرش مبغاتش تنقص','كتنقصي من جسمك كامل… غير الكرش باقي كيف ما هو','الكرش مرخوفة ومنفوخة','من بعد الولادة… الكرش ما رجعاتش كيف كانت','الدهون متجمعين فالبطن والأرداف وما كيمشيوش','جربتي ريجيمات ومنتجات كثيرة بلا نتيجة'],
  'products':[SHAR,CREAM],
  'offers':[offer('البطن','good','trio'),offer('البطن','better','ventre'),offer('البطن','best','intensive')],
  'faq':[('الكريم وحدو كافي؟','لا. الكريم كيشدّ من فوق والدوا كيذوّب من داخل. بجوج مزيان.'),
         ('آمن من بعد الولادة والرضاعة؟','[ خاصو تصديق طبي قبل النشر. ]')],
  'vids':V[0:6]},
'fringales':{'title':'پاك وقف القرم — Medicaldine','kicker':'الشهوة والحلويات · 3 أشهر','plabel':'القرم',
  'h1':'الشهوة للأكل <span>مكتخليكش تزيدي فالوزن؟</span>','sub':'برنامج لمدة 3 أشهر باش تسيطري على الشهوة للأكل، خصوصاً الحلويات، وترجعي تتحكمي فالشهية ديالك، مع كوتش خاصة وتطبيق هاتفي كيتابع معاك خطوة بخطوة.',
  'hero':P_SOLEIL,'agit_img':P_RIAD,'life':P_CREAMDRINK,'agit_h':'واش هادشي لي كيوقع ليك؟',
  'pains':['كتقاومي طول النهار… وبالليل كتبدا الشهوة فالحلويات','ماشي جوع… غير كتحسي برغبة قوية تاكلي، خصوصاً الحلو','كل مرة كتقولي «غادي نبدأ من جديد»… ولكن نفس الشي كيتعاود','كتحسي أنك فاقدة السيطرة على الشهية ديالك'],
  'products':[SHAR,DRINK],
  'offers':[offer('القرم','good','trio'),offer('القرم','better','stop'),offer('القرم','best','intensive')],
  'faq':[('غادي نبقى جيعانة؟','لا، بالعكس. الهدف هو تحبسي القرم بلا حرمان.'),
         ('وإلا قرمت؟','الكوتش كتعاونكِ فهاد اللحظات، والتطبيق الهاتفي فيه مهام ضد القرم.')],
  'vids':V[2:8]},
'metabolisme':{'title':'پاك إعادة ضبط الأيض — Medicaldine','kicker':'الحرق البطيء · 3 أشهر','plabel':'الأيض',
  'h1':'كتاكلي غير شوية… <span>ولكن مكتنقصيش؟</span>','sub':'برنامج لمدة 3 أشهر كيساعد ينشط الحرق ويعاون الجسم يبدا يحرق الدهون بشكل أفضل، مع كوتش خاصة وتطبيق هاتفي كيتابع معاك يومياً.',
  'hero':P_PACK,'agit_img':P_SPORT,'life':P_CREAMING,'agit_h':'كتديري كلشي مزيان… والميزان ما كيتحرّك.',
  'pains':['كتاكلي شوية وكتحركي وما كتنقصيش','كتحسي بالنفخة واحتباس الماء','بحال جسمكِ كيخزّن كلشي'],
  'products':[SHAR],
  'offers':[offer('الأيض','good','trio'),offer('الأيض','better','reset'),offer('الأيض','best','intensive')],
  'faq':[('علاش 3 ديال Shar Slim؟','ماشي تكرار: بروتوكول 3 مراحل — ديتوكس، تنشيط، تثبيت.'),
         ('إمتى غادي يتحرّك الميزان؟','[ مدة واقعية — بلا وعد مضمون. ]')],
  'vids':V[4:10]},
'transformation':{'title':'برنامج التحول الكامل — Medicaldine','kicker':'التحول الكامل','plabel':'التحول',
  'h1':'بغيتي تنقصي <span>من كل جهة؟</span>','sub':'برنامج كامل كيهاجم من 3 جهات، مع كوتش وتطبيق هاتفي.',
  'hero':P_PACK,'agit_img':P_RIAD,'life':P_CREAMDRINK,'agit_h':'جرّبتي بزّاف… وما داز والو.',
  'pains':['جرّبتي رجيمات بزّاف وحتى وحدة ما دامت','ما عارفاش منين تبدّي: الماكلة؟ الرياضة؟ المكمّلات؟','بغيتي نتيجة، وخصوصاً شي حد يوجّهكِ'],
  'products':[SHAR,DRINK,CREAM],
  'offers':[offer('التحول','better','trio'),offer('التحول','best','intensive')],
  'faq':[('علاش 3 منتجات ماشي وحدة؟','حيت جهة وحدة ما كتكفيش. كنهاجمو كلشي فنفس الوقت.'),
         ('أنا مبتدئة، هادشي ليا؟','أيّه، مصمّم ليكِ. الكوتش كتبدا من مستواكِ.')],
  'vids':V[0:3]+V[6:9]},
}
FAQ_COMMON=[('كيفاش المتابعة مع الكوتش؟','من بعد الطلب، الكوتش كتعيّط لكِ وكتثبّتكِ فالتطبيق الهاتفي.'),
            ('أول مرة نجرّب پاك؟','الكوتش كتبدا معكِ من الصفر وتوجّهكِ خطوة بخطوة.')]

UNIT={SHAR:450,DRINK:350,CREAM:350}
ARR='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M14 6l-6 6 6 6"/></svg>'
def r10(x): return int(round(x/10.0))*10
def chip(t): return f'<span class="chip">{CHK} {t}</span>'
def li_check(t): return f'<li>{CHK} {t}</li>'

def packs_html(prod):
    u=UNIT[prod]; name=PNAME[prod]
    rows=[('شهر',1,'',1.00),('شهرين',2,'الأكثر طلباً',0.90),('3 أشهر',3,'أحسن قيمة',0.80)]
    out=''
    for label,qty,tag,d in rows:
        now=r10(u*qty*d); old=u*qty; pop=' pop' if qty==3 else ''
        tag_html=f'<span class="pk-tag">{tag}</span>' if tag else ''
        old_html=f'<span class="pk-old">{old} درهم</span>' if old>now else ''
        pack=f'{name} — {label} ({qty} وحدة) — {now} درهم'
        out+=f'''<button class="pack{pop} js-open" data-pack="{pack}">
          <span class="pk-l"><span class="pk-name">{label} · {qty} وحدة</span>{tag_html}</span>
          <span class="pk-r">{old_html}<span class="pk-now">{now} درهم</span></span>{ARR}</button>'''
    return f'<div class="packs">{out}</div>'

def products_html(prods):
    cards=''
    for p in prods:
        cards+=f'''<div class="prod-card"><div class="pimg"><img src="{p}" alt="{PNAME[p]}" loading="lazy"></div>
        <div class="pbody"><h3>{PNAME[p]}</h3><p>{ROLE[p]}</p>{packs_html(p)}</div></div>'''
    return f'<div class="prod-grid">{cards}</div>'

def pinfo_section(products):
    cards=''
    for p in products:
        info=PRODUCT_INFO[p]
        ben=''.join(f'<li>{CHK} {b}</li>' for b in info['ben'])
        ing=''.join(f'<span class="ing">{i}</span>' for i in info['ing'])
        cards+=f'''<div class="pinfo">
      <div class="pinfo-media"><img src="{info['img']}" alt="{info['name']}" loading="lazy"></div>
      <div class="pinfo-content">
        <h3>{info['name']}</h3>
        <div class="pinfo-label">الفوائد</div>
        <ul class="check-list">{ben}</ul>
        <div class="pinfo-label">المكوّنات</div>
        <div class="ingredients">{ing}</div>
      </div>
    </div>'''
    return f'<div class="pinfo-grid n{len(products)}">{cards}</div>'

def tier_html(o):
    cls=' reco sel' if o['reco'] else ''
    pressed='true' if o['reco'] else 'false'
    hot=f'<span class="tier-hot">{o["badge"]}</span>' if o['badge'] else ''
    def prod_li(x):
        name=x.split(' × ')[-1].strip()
        img=IMGOF.get(name)
        thumb=f'<img class="pthumb" src="{img}" alt="{name}" loading="lazy">' if img else BOX
        return f'<li class="prod">{thumb} <span>{x}</span></li>'
    prod=''.join(prod_li(x) for x in o['comp'])
    ben=''.join(f'<li>{CHK} {x}</li>' for x in o['ben'])
    prods_data='~~'.join(f"{IMGOF.get(x.split(' × ')[-1].strip(),'')}::{x}" for x in o['comp'])
    # Vignette du pack : une image par produit du pack (grille compacte)
    pack_names=[x.split(' × ')[-1].strip() for x in o['comp']]
    pack_imgs=[IMGOF[nm] for nm in pack_names if IMGOF.get(nm)]
    n_imgs=len(pack_imgs) or 1
    imgs_html=''.join(f'<img src="{u}" alt="" loading="lazy">' for u in pack_imgs) or BOX
    thumb_main=f'<div class="tier-imgs" data-count="{n_imgs}">{imgs_html}</div>'
    return f'''<div class="tier{cls}" role="button" tabindex="0" aria-pressed="{pressed}" data-pack="{o['pack']}" data-products="{prods_data}">
      <div class="tier-head">
        {thumb_main}
        <div class="tier-info">
          <span class="tier-tag"><i class="tdot"></i>{o['tlabel']}{hot}</span>
          <h3>{o['pname']}</h3>
          <div class="tprice"><span class="told">{o['old']} درهم</span><span class="tnow">{o['now']} <small>درهم</small></span></div>
          <button class="tier-toggle" type="button"><span class="tt-label">اقرأ المزيد</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg></button>
        </div>
        <span class="tier-radio" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></span>
      </div>
      <div class="tier-more">
        <div class="tlabel">المنتجات</div>
        <ul class="tlist">{prod}</ul>
        <div class="tlabel">المزايا</div>
        <ul class="tlist">{ben}</ul>
      </div>
    </div>'''

def videos_html(vids):
    return ''.join(f'<div class="vcard"><video src="{u}" controls preload="metadata" playsinline></video></div>' for u in vids)
def faq_html(specific):
    items=specific+FAQ_COMMON; out=''
    for i,(q,a) in enumerate(items):
        op=' open' if i==0 else ''
        out+=f'<details{op}><summary>{q}</summary><div class="a">{a}</div></details>'
    return out

PAGE='''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="theme-color" content="#1f8f4e">
<link rel="preconnect" href="https://medicaldine.ma"><link rel="preconnect" href="https://hercules-cdn.com">
<link rel="stylesheet" href="styles.css?v={cssver}">
</head>
<body class="has-mcta">

<header><div class="wrap nav" style="justify-content:center">
  <a href="index.html" class="logo">{logo}Medicaldine</a>
</div></header>

<section class="hero"><div class="wrap"><div class="hero-grid">
  <div class="hero-photo"><img src="{hero}" alt="" width="700" height="700" fetchpriority="high"></div>
  <div class="hero-txt">
    <span class="eyebrow">{kicker}</span>
    <h1>{h1}</h1>
    <p class="sub">{sub}</p>
    <div class="trust-row">{chips}</div>
    <div class="rating"><span class="stars">★★★★★</span> 4,8/5 · أكثر من 2300 مرا</div>
  </div>
</div></div></section>

<section class="bg-white"><div class="wrap media">
  <div class="m-img"><img src="{agit_img}" alt="" loading="lazy"></div>
  <div>
    <h2>{agit_h}</h2>
    <ul class="check-list">{pains}</ul>
  </div>
</div></section>

<section class="bg-paper" id="temoignages"><div class="wrap">
  <div class="section-head center"><span class="eyebrow">دارتها قبلكِ</span><h2>شوفي بعينيك — نتائج حقيقية</h2></div>
  <div class="video-grid">{videos}</div>
  <div class="testi-row">
    <div class="testi"><div class="stars">★★★★★</div><p>«ف3 أشهر تبدّل كلشي. الكوتش ما خلّاتنيش نحبس.»</p><div class="who"><span class="av">س</span><div><b>سناء</b><span>الدار البيضاء</span></div></div></div>
    <div class="testi"><div class="stars">★★★★★</div><p>«أول مرة نلقى نتيجة كتبقى. التطبيق الهاتفي عاوني بزّاف.»</p><div class="who"><span class="av">ح</span><div><b>حنان</b><span>الرباط</span></div></div></div>
    <div class="testi"><div class="stars">★★★★★</div><p>«حسّيت بواحد اللي كيتبعني بصح. ماشي غير منتج.»</p><div class="who"><span class="av">ف</span><div><b>فاطمة</b><span>مراكش</span></div></div></div>
  </div>
  <div class="cta"><a href="#offres" class="btn">بغيت نفس النتيجة ←</a>
    <div class="ctv">{chk} حتا يوصلك عاد خلصي · التوصيل مجاني</div></div>
</div></section>

<section class="bg-mint" id="offres"><div class="wrap">
  <div class="section-head center maxw">
    <span class="oto-pill">⏳ عرض محدود — سعر خاص</span>
    <h2 style="margin-top:12px">اختاري العرض ديالكِ</h2>
    <p class="lead" style="margin-top:8px">نفس المرافقة فكل العروض (كوتش + تطبيق هاتفي + توصيل مجاني + حتا يوصلك عاد خلصي).</p></div>
  <div class="tiers{tiers_mod}">{tiers}</div>
  <div class="tiers-cta">
    <button class="btn js-order-selected" type="button">أطلبي دابا ←</button>
    <div class="tctv">{chk} حتا يوصلك عاد خلصي</div>
  </div>
  <div class="not-sure">
    <button class="js-open" data-pack="غير متأكدة — {plabel} — الكوتش توجّهني" data-desc="{desc}">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.7.3-1 .8-1 1.7"/><path d="M12 17h.01"/></svg>
      إلا معرفتيش الپاك لي مناسبك ماعليك غير تكليكي هنا
    </button>
  </div>
  <div class="guarantee"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 6v6c0 5 3.5 8 8 10 4.5-2 8-5 8-10V6z"/><path d="M9 12l2 2 4-4"/></svg><span>إلا مبانتش ليك النتيجة، فلوسك كاملين يرجعو ليك</span></div>
</div></section>

<section class="bg-white" id="produits"><div class="wrap">
  <div class="section-head center"><span class="eyebrow">المنتجات</span><h2>شنو كاين فالباقة — الفوائد والمكوّنات</h2></div>
  {pinfo}
</div></section>

<section class="bg-paper"><div class="wrap media">
  <div class="m-img"><img src="{life11}" alt="" loading="lazy"></div>
  <div>
    <span class="eyebrow">الفرق الحقيقي</span>
    <h2>النتيجة كتجي من المتابعة.</h2>
    <p class="lead" style="margin-top:10px">ماشي المنتج بوحدو. معكِ كوتش وتطبيق هاتفي كل نهار حتى للآخر.</p>
    <div class="value-cols">
      <div class="vbox"><div class="vh"><span class="vi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/></svg></span><h4>التطبيق الهاتفي</h4></div>
        <ul><li>{chk} ماكلة على قياسكِ</li><li>{chk} مهام كل نهار</li><li>{chk} نقط ومكافآت</li></ul></div>
      <div class="vbox"><div class="vh"><span class="vi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5S15 16.7 15 20"/><path d="M16 11l2 2 3-3"/></svg></span><h4>الكوتش</h4></div>
        <ul><li>{chk} معكِ من اليوم 1 حتى 90</li><li>{chk} كتبدّل البرنامج معكِ</li><li>{chk} كتجاوب أسئلتكِ</li></ul></div>
    </div>
  </div>
</div></section>

<section class="bg-mint"><div class="wrap">
  <div class="reassure">
    <div class="r"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2 4 6v6c0 5 3.5 8 8 10 4.5-2 8-5 8-10V6z"/><path d="M9 12l2 2 4-4"/></svg><div><b>خلّصي عند الاستلام</b><span>بلا خلاص أونلاين.</span></div></div>
    <div class="r"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5S15 16.7 15 20"/><path d="M16 11l2 2 3-3"/></svg><div><b>كوتش بنيّة</b><span>من اليوم 1 حتى 90.</span></div></div>
    <div class="r"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="6" y="3" width="12" height="18" rx="2.5"/><path d="M11 18h2"/></svg><div><b>التطبيق الهاتفي داخل</b><span>طول الپاك.</span></div></div>
  </div>
</div></section>

<section class="bg-white" id="faq"><div class="wrap">
  <div class="section-head center"><span class="eyebrow">الأسئلة</span><h2>اللي بغيتي تعرفي</h2></div>
  <div class="faq">{faq}</div>
</div></section>

<section class="bg-dark" id="reserver"><div class="wrap media">
  <div class="m-img"><img src="{hero}" alt="" loading="lazy"></div>
  <div>
    <div class="urgency"><span class="pulse"></span> عرض محدود · الأماكن قليلة هاد السيمانة</div>
    <h2>سعر العرض الخاص ما غاديش يدوم.</h2>
    <p class="lead" style="margin-top:10px">خلّي سميتكِ ورقمكِ، الكوتش كتعيّط لكِ باش تبداي بالسعر الخاص.</p>
    <div class="cta" style="text-align:right"><a href="#offres" class="btn white">خودي القرار دبا وبدلي حياتك ←</a>
      <div class="ctv" style="justify-content:flex-start">{chk} حتا يوصلك عاد خلصي · بلا تسبيق</div></div>
  </div>
</div></section>

<footer><div class="wrap">
  <a href="index.html" class="logo on-dark">{logo}Medicaldine</a>
  <p>التنحيف · كوتش + تطبيق هاتفي · حتا يوصلك عاد خلصي فكل المغرب</p>
  <p style="margin-top:6px;opacity:.7"><a href="index.html">↺ بدّلي المشكل ديالكِ</a> · النتائج كتبدّل من مرا لأخرى.</p>
</div></footer>

<div class="mobile-cta">
  <a href="#offres" class="btn">خودي القرار دبا وبدلي حياتك ←</a>
  <div class="ctv">{chk} حتا يوصلك عاد خلصي · التوصيل مجاني</div>
</div>

<div class="modal" id="modal" role="dialog" aria-modal="true">
  <div class="modal-ov js-close"></div>
  <div class="modal-card" id="modal-card">
    <button class="modal-close js-close" aria-label="إغلاق">✕</button>
    <div class="modal-head">
      <div class="k">حجزي الپاك ديالكِ</div>
      <p>خلّي معلوماتكِ، الكوتش كتعيّط لكِ. بلا خلاص أونلاين.</p>
      <div class="chosen">{box}<span>الباقة: <span id="chosen-pack">—</span></span></div>
      <div class="chosen-imgs" id="chosen-imgs"></div>
      <div class="chosen-desc" id="chosen-desc"></div>
    </div>
    <form id="lead-form" novalidate>
      <input type="hidden" id="pack-field" name="pack">
      <div class="field" id="field-probleme" style="display:none"><label for="f-probleme">شرحي لينا المشكل ديالك</label><textarea id="f-probleme" name="probleme" rows="3" placeholder="اكتبي شنو حاسة بيه ولا شنو المشكل ديالك…"></textarea></div>
      <div class="field"><label for="f-nom">السمية الكاملة</label><input id="f-nom" name="nom" type="text" autocomplete="name" placeholder="السمية ديالكِ" required><div class="err-msg">دخّلي السمية.</div></div>
      <div class="field"><label for="f-tel">الهاتف</label><input id="f-tel" name="tel" type="tel" inputmode="numeric" autocomplete="tel" placeholder="06 12 34 56 78" required style="direction:ltr;text-align:right"><div class="err-msg">رقم غير صحيح (06 / 07).</div></div>
      <div class="field"><label for="f-ville">المدينة</label><input id="f-ville" name="ville" type="text" autocomplete="address-level2" placeholder="المدينة ديالكِ" required><div class="err-msg">دخّلي المدينة.</div></div>
      <button type="submit" class="btn" style="width:100%;margin-top:18px">حجزي المكان ديالكِ ←</button>
      <div class="form-note"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg> معلوماتكِ تبقى سرية.</div>
    </form>
    <div class="modal-success">
      <div class="ok"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6 9 17l-5-5"/></svg></div>
      <h3>تسجّل الطلب، <span class="uname">عزيزتي</span>!</h3>
      <p style="color:var(--muted);margin-top:6px">الكوتش كتعيّط لكِ قريب. وجّدي أسئلتكِ 😊</p>
      <button class="btn white js-close" style="margin-top:16px">إغلاق</button>
    </div>
  </div>
</div>

<script src="app.js?v={jsver}"></script>
</body>
</html>
'''

DESC={
 'ventre':'المشكل ديالك: الكرش والدهون فالبطن والأرداف، السيلوليت، والجلد المترهّل — خصوصاً من بعد الولادة. عمّري المعلومات ديالك وكوتشك غادي تختار ليك الپاك المناسب لحالتك.',
 'fringales':'المشكل ديالك: الرغبة فالحلويات والتسنيك بين الوجبات وصعوبة التحكّم فالأكل. عمّري المعلومات ديالك وكوتشك غادي توجّهك للپاك المناسب.',
 'metabolisme':'المشكل ديالك: أيض بطيء وحرق ضعيف — كتاكلي شوية وما كتنقصيش. عمّري المعلومات ديالك وكوتشك غادي تختار ليك البروتوكول المناسب.',
 'transformation':'المشكل ديالك: وزن زائد شامل وبغيتي تعالجي كلشي. عمّري المعلومات ديالك وكوتشك غادي توجّهك للپاك المناسب لحالتك.',
}

CSSVER=_ver('styles.css'); JSVER=_ver('app.js')
for slug,d in DATA.items():
    offers=[product_only(d['plabel'])] + d['offers']   # choix 1 = produit seul + le reste
    reco=[o for o in offers if o['reco']][0]
    tiers_mod=' n'+str(len(offers))
    # Section produits = TOUS les produits présents dans les offres (union), ordre fixe
    used=set()
    for o in offers:
        for x in o['comp']:
            c=NAME2CONST.get(x.split(' × ')[-1].strip())
            if c: used.add(c)
    pinfo_products=[p for p in (SHAR,DRINK,CREAM) if p in used]
    html=PAGE.format(
        title=d['title'],logo=LOGO,kicker=d['kicker'],h1=d['h1'],sub=d['sub'],
        hero=d['hero'],agit_img=d['agit_img'],agit_h=d['agit_h'],
        chips=chip('حتا يوصلك عاد خلصي')+chip('التوصيل مجاني')+chip('كوتش + تطبيق هاتفي'),
        chk=CHK,box=BOX,pains=''.join(li_check(p) for p in d['pains']),
        plabel=d['plabel'],desc=DESC[slug],
        products=products_html(d['products']),pinfo=pinfo_section(pinfo_products),
        tiers=''.join(tier_html(o) for o in offers),tiers_mod=tiers_mod,
        life11=d['life'],videos=videos_html(d['vids']),faq=faq_html(d['faq']),
        reco_now=reco['now'],cssver=CSSVER,jsver=JSVER)
    open(os.path.join(OUT,f'p-{slug}.html'),'w',encoding='utf-8').write(html)
    print('wrote p-%s.html (%d offres, reco=%s)'%(slug,len(offers),reco['pname']))
print('done')
