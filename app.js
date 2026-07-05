/* ===== Medicaldine — shared JS ===== */
(function(){

  /* ---------- GATEWAY : sélection + redirection ---------- */
  var gate = document.getElementById('gate');
  if(gate){
    var cards = gate.querySelectorAll('.prob-card');
    var goBtn = document.getElementById('gate-go');
    var chosen = null;
    cards.forEach(function(c){
      c.addEventListener('click', function(){
        cards.forEach(function(x){ x.classList.remove('sel'); x.setAttribute('aria-checked','false'); });
        c.classList.add('sel'); c.setAttribute('aria-checked','true');
        chosen = c.getAttribute('data-target');
        goBtn.removeAttribute('disabled');
      });
    });
    goBtn.addEventListener('click', function(){
      if(!chosen) return;
      if(chosen === '__consult__'){
        if(typeof openModal === 'function'){
          openModal('استشارة مع الخبير — ما عارفة المشكل', null,
            'ما عارفة المشكل ديالك؟ ماشي مشكل — عمّري المعلومات ديالك والخبير ديالنا غادي يتواصل معاك، يفهم حالتك ويوجّهك للحل المناسب.',
            'استشارة مجانية مع الخبير');
        }
        return;
      }
      try{ localStorage.setItem('md_problem', chosen); }catch(e){}
      window.location.href = chosen;
    });
  }

  /* ---------- MODAL FORM (landing pages) ---------- */
  var modal = document.getElementById('modal');
  if(!modal) return;
  var card = document.getElementById('modal-card');
  var form = document.getElementById('lead-form');
  var chosenEl = document.getElementById('chosen-pack');
  var packField = document.getElementById('pack-field');
  var lastFocus = null;

  var imgsWrap = document.getElementById('chosen-imgs');
  var descEl = document.getElementById('chosen-desc');
  function openModal(pack, products, desc, title){
    lastFocus = document.activeElement;
    pack = pack || 'الباقة الموصى بها';
    if(chosenEl) chosenEl.textContent = title || (desc ? 'الكوتش غادي تختار ليك الپاك المناسب' : pack);
    if(packField) packField.value = pack;
    if(descEl){
      if(desc){ descEl.textContent = desc; descEl.style.display = 'block'; }
      else { descEl.textContent = ''; descEl.style.display = 'none'; }
    }
    var probField = document.getElementById('field-probleme');
    if(probField) probField.style.display = desc ? 'block' : 'none';
    if(imgsWrap){
      imgsWrap.innerHTML = '';
      if(products){
        products.split('~~').forEach(function(it){
          var p = it.split('::'), url = p[0], label = p[1] || '';
          if(!url) return;
          var d = document.createElement('div'); d.className = 'ci';
          var im = document.createElement('img'); im.src = url; im.alt = label; im.loading = 'lazy';
          var sp = document.createElement('span'); sp.textContent = label;
          d.appendChild(im); d.appendChild(sp); imgsWrap.appendChild(d);
        });
      }
    }
    card.classList.remove('done');
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
    setTimeout(function(){ var f=document.getElementById('f-nom'); if(f) f.focus(); }, 60);
    if(window.fbq) try{ fbq('track','InitiateCheckout',{content_name:pack}); }catch(e){}
  }
  function closeModal(){
    modal.classList.remove('open');
    document.body.style.overflow = '';
    if(lastFocus) try{ lastFocus.focus(); }catch(e){}
  }
  document.querySelectorAll('.js-open').forEach(function(b){
    b.addEventListener('click', function(){ openModal(b.getAttribute('data-pack'), b.getAttribute('data-products'), b.getAttribute('data-desc')); });
  });
  document.querySelectorAll('.js-close').forEach(function(b){ b.addEventListener('click', closeModal); });
  document.addEventListener('keydown', function(e){ if(e.key==='Escape' && modal.classList.contains('open')) closeModal(); });

  /* Toggle "اقرأ المزيد" sur mobile (déplie la carte d'offre) */
  document.querySelectorAll('.tier-toggle').forEach(function(b){
    b.addEventListener('click', function(){
      var t = b.closest('.tier');
      var open = t.classList.toggle('open');
      var lab = b.querySelector('.tt-label');
      if(lab) lab.textContent = open ? 'قلّل' : 'اقرأ المزيد';
    });
  });

  function normTel(v){ return v.replace(/[\s().-]/g,''); }
  function validTel(v){ v=normTel(v); return /^0[67]\d{8}$/.test(v) || /^(\+?212)[67]\d{8}$/.test(v); }

  if(form){
    form.querySelectorAll('input,select').forEach(function(el){
      el.addEventListener('input', function(){ el.classList.remove('err'); });
      el.addEventListener('change', function(){ el.classList.remove('err'); });
    });
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var nom=form.nom, tel=form.tel, ville=form.ville, ok=true, firstErr=null;
      function fail(el){ el.classList.add('err'); if(!firstErr) firstErr=el; ok=false; }
      if(nom.value.trim().length<3) fail(nom);
      if(!validTel(tel.value)) fail(tel);
      if(ville.value.trim().length<2) fail(ville);
      if(!ok){ firstErr.focus(); return; }
      var probEl = form.probleme, prob = (probEl && probEl.value.trim()) || '';
      var data = {
        nom:nom.value.trim(), tel:normTel(tel.value), ville:ville.value.trim(),
        pack:(packField?packField.value:''), probleme:prob, source:document.title, ts:new Date().toISOString()
      };
      /* ---- Envoi du lead vers le CRM (API d'ingestion) ---- */
      var CRM_URL   = 'https://crmsalescopy-production.up.railway.app/api/leads/ingest';
      var CRM_TOKEN = 'lead_79b33cd21a4743b4a558662fd8f0f4d1';
      try{
        fetch(CRM_URL, {
          method: 'POST',
          headers: { 'Authorization': 'Bearer ' + CRM_TOKEN, 'Content-Type': 'application/json' },
          body: JSON.stringify({
            nom: data.nom,
            telephone: data.tel,
            email: '',
            message: 'الباقة: ' + data.pack + (data.probleme ? ' · المشكل: ' + data.probleme : ''),
            ville: data.ville,
            pack: data.pack,
            probleme: data.probleme,
            source: data.source
          })
        }).then(function(r){ if(!r.ok) console.warn('CRM ingest HTTP', r.status); })
          .catch(function(err){ console.warn('CRM ingest failed', err); });
      }catch(e){ console.warn('CRM ingest error', e); }
      console.log('LEAD', data);
      if(window.fbq) try{ fbq('track','Lead',{content_name:data.pack}); }catch(e){}
      var uname = data.nom.split(' ')[0] || data.nom;
      card.querySelectorAll('.uname').forEach(function(el){ el.textContent = uname; });
      card.classList.add('done'); card.scrollTop = 0;
    });
  }

  /* ---------- Barre CTA fixe : n'apparaît qu'au milieu de la section 3 (vidéos) ---------- */
  var mcta = document.querySelector('.mobile-cta');
  var sec3 = document.getElementById('temoignages');
  if(mcta && sec3){
    function updateBar(){
      var r = sec3.getBoundingClientRect();
      // Apparaît quand la section vidéos (3) occupe le haut de l'écran, puis reste visible ensuite
      mcta.classList.toggle('show', r.top <= (window.innerHeight * 0.35));
    }
    window.addEventListener('scroll', updateBar, {passive:true});
    window.addEventListener('resize', updateBar);
    document.addEventListener('DOMContentLoaded', updateBar);
    window.addEventListener('load', updateBar);
    updateBar();
  }
})();
