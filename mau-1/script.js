(function(){
var $=function(s){return document.querySelector(s)},$$=function(s){return[].slice.call(document.querySelectorAll(s))};
var mb=$('#mb'),nav=$('#nav'),veil=$('#veil');
function toggle(o){nav.classList.toggle('open',o);veil.classList.toggle('on',o);mb.classList.toggle('open',o);mb.setAttribute('aria-expanded',o);mb.setAttribute('aria-label',o?'Đóng menu':'Mở menu')}
mb.addEventListener('click',function(){toggle(!nav.classList.contains('open'))});
veil.addEventListener('click',function(){toggle(false)});
nav.addEventListener('click',function(e){if(e.target.closest('a'))toggle(false)});
document.addEventListener('keydown',function(e){if(e.key==='Escape')toggle(false)});
// Ngôi sao khi click
document.addEventListener('click',function(ev){
 for(var i=0;i<5;i++){var s=document.createElement('span');s.className='star';s.textContent='★';
  s.style.left=ev.clientX+'px';s.style.top=ev.clientY+'px';
  s.style.setProperty('--dx',(Math.random()*80-40)+'px');s.style.setProperty('--dy',(Math.random()*80-50)+'px');
  s.style.fontSize=(10+Math.random()*12)+'px';document.body.appendChild(s);setTimeout(function(x){x.remove()},850,s)}});
// Đồng hồ chạy thật
function rot(id,a){$(id).setAttribute('transform','rotate('+a+' 100 100)')}
(function t(){var d=new Date(),s=d.getSeconds()+d.getMilliseconds()/1000,m=d.getMinutes()+s/60,h=d.getHours()%12+m/60;rot('#hh',h*30);rot('#mh',m*6);rot('#sh',s*6);requestAnimationFrame(t)})();
// Hiện dần khi cuộn
var io=new IntersectionObserver(function(l){l.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{threshold:.12});
$$('.reveal').forEach(function(el){io.observe(el)});
// Đánh dấu mục đang đọc trong menu
var links={};$$('#nav a').forEach(function(a){links[a.getAttribute('href').slice(1)]=a});
var spy=new IntersectionObserver(function(l){l.forEach(function(x){if(x.isIntersecting){$$('#nav a.on').forEach(function(a){a.classList.remove('on')});var a=links[x.target.id];a&&a.classList.add('on')}})},{rootMargin:'-40% 0px -55% 0px'});
$$('section[id],article[id]').forEach(function(el){spy.observe(el)});
// Thanh tiến trình + nút lên đầu
var pg=$('#pg'),tb=$('#topb');tb.addEventListener('click',function(){scrollTo({top:0,behavior:'smooth'})});
addEventListener('scroll',function(){pg.style.width=100*scrollY/Math.max(1,document.body.scrollHeight-innerHeight)+'%';tb.hidden=scrollY<600},{passive:true});
})();
