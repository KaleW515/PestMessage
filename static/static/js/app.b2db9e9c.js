(function(e){function n(n){for(var a,r,c=n[0],i=n[1],l=n[2],f=0,s=[];f<c.length;f++)r=c[f],Object.prototype.hasOwnProperty.call(u,r)&&u[r]&&s.push(u[r][0]),u[r]=0;for(a in i)Object.prototype.hasOwnProperty.call(i,a)&&(e[a]=i[a]);h&&h(n);while(s.length)s.shift()();return o.push.apply(o,l||[]),t()}function t(){for(var e,n=0;n<o.length;n++){for(var t=o[n],a=!0,r=1;r<t.length;r++){var c=t[r];0!==u[c]&&(a=!1)}a&&(o.splice(n--,1),e=i(i.s=t[0]))}return e}var a={},r={app:0},u={app:0},o=[];function c(e){return i.p+"static/js/"+({}[e]||e)+"."+{"chunk-00188d6a":"64815090","chunk-0e490c7a":"33149d1f","chunk-1027850a":"804404f9","chunk-1b85e661":"7d0dede2","chunk-3a1a25d8":"6bde71e7","chunk-502bf7a9":"8d6210f1","chunk-27e9aa7a":"d3819922","chunk-60b76a16":"c7bd1ad3","chunk-67b409f0":"ca049ef6","chunk-57a62ed8":"5e9e7da3","chunk-6568a628":"3efe84c0","chunk-983257a2":"e5cd84a1"}[e]+".js"}function i(n){if(a[n])return a[n].exports;var t=a[n]={i:n,l:!1,exports:{}};return e[n].call(t.exports,t,t.exports,i),t.l=!0,t.exports}i.e=function(e){var n=[],t={"chunk-00188d6a":1,"chunk-0e490c7a":1,"chunk-1027850a":1,"chunk-1b85e661":1,"chunk-3a1a25d8":1,"chunk-27e9aa7a":1,"chunk-60b76a16":1,"chunk-67b409f0":1,"chunk-57a62ed8":1,"chunk-6568a628":1,"chunk-983257a2":1};r[e]?n.push(r[e]):0!==r[e]&&t[e]&&n.push(r[e]=new Promise((function(n,t){for(var a="static/css/"+({}[e]||e)+"."+{"chunk-00188d6a":"c64d0b24","chunk-0e490c7a":"7a6b8d66","chunk-1027850a":"ab2d9aa9","chunk-1b85e661":"961c7256","chunk-3a1a25d8":"ebac6787","chunk-502bf7a9":"31d6cfe0","chunk-27e9aa7a":"8568a11d","chunk-60b76a16":"c440e3f4","chunk-67b409f0":"482e5e7b","chunk-57a62ed8":"226fd0dd","chunk-6568a628":"e6d369c1","chunk-983257a2":"e41db866"}[e]+".css",u=i.p+a,o=document.getElementsByTagName("link"),c=0;c<o.length;c++){var l=o[c],f=l.getAttribute("data-href")||l.getAttribute("href");if("stylesheet"===l.rel&&(f===a||f===u))return n()}var s=document.getElementsByTagName("style");for(c=0;c<s.length;c++){l=s[c],f=l.getAttribute("data-href");if(f===a||f===u)return n()}var h=document.createElement("link");h.rel="stylesheet",h.type="text/css",h.onload=n,h.onerror=function(n){var a=n&&n.target&&n.target.src||u,o=new Error("Loading CSS chunk "+e+" failed.\n("+a+")");o.code="CSS_CHUNK_LOAD_FAILED",o.request=a,delete r[e],h.parentNode.removeChild(h),t(o)},h.href=u;var d=document.getElementsByTagName("head")[0];d.appendChild(h)})).then((function(){r[e]=0})));var a=u[e];if(0!==a)if(a)n.push(a[2]);else{var o=new Promise((function(n,t){a=u[e]=[n,t]}));n.push(a[2]=o);var l,f=document.createElement("script");f.charset="utf-8",f.timeout=120,i.nc&&f.setAttribute("nonce",i.nc),f.src=c(e);var s=new Error;l=function(n){f.onerror=f.onload=null,clearTimeout(h);var t=u[e];if(0!==t){if(t){var a=n&&("load"===n.type?"missing":n.type),r=n&&n.target&&n.target.src;s.message="Loading chunk "+e+" failed.\n("+a+": "+r+")",s.name="ChunkLoadError",s.type=a,s.request=r,t[1](s)}u[e]=void 0}};var h=setTimeout((function(){l({type:"timeout",target:f})}),12e4);f.onerror=f.onload=l,document.head.appendChild(f)}return Promise.all(n)},i.m=e,i.c=a,i.d=function(e,n,t){i.o(e,n)||Object.defineProperty(e,n,{enumerable:!0,get:t})},i.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(e,n){if(1&n&&(e=i(e)),8&n)return e;if(4&n&&"object"===typeof e&&e&&e.__esModule)return e;var t=Object.create(null);if(i.r(t),Object.defineProperty(t,"default",{enumerable:!0,value:e}),2&n&&"string"!=typeof e)for(var a in e)i.d(t,a,function(n){return e[n]}.bind(null,a));return t},i.n=function(e){var n=e&&e.__esModule?function(){return e["default"]}:function(){return e};return i.d(n,"a",n),n},i.o=function(e,n){return Object.prototype.hasOwnProperty.call(e,n)},i.p="/",i.oe=function(e){throw console.error(e),e};var l=window["webpackJsonp"]=window["webpackJsonp"]||[],f=l.push.bind(l);l.push=n,l=l.slice();for(var s=0;s<l.length;s++)n(l[s]);var h=f;o.push([0,"chunk-vendors"]),t()})({0:function(e,n,t){e.exports=t("56d7")},"199c":function(e,n){},"23be":function(e,n,t){"use strict";var a=t("199c"),r=t.n(a);n["default"]=r.a},"3dfd":function(e,n,t){"use strict";var a=t("faa3"),r=t("23be"),u=t("2877"),o=Object(u["a"])(r["default"],a["a"],a["b"],!1,null,null,null);n["default"]=o.exports},"56d7":function(e,n,t){"use strict";t.r(n);t("d3b7"),t("e260"),t("e6cf"),t("cca6"),t("a79d");var a=t("2b0e"),r=t("bc3a"),u=t.n(r),o={},c=u.a.create(o);c.interceptors.request.use((function(e){return e}),(function(e){return Promise.reject(e)})),c.interceptors.response.use((function(e){return e}),(function(e){return Promise.reject(e)})),Plugin.install=function(e,n){e.axios=c,window.axios=c,Object.defineProperties(e.prototype,{axios:{get:function(){return c}},$axios:{get:function(){return c}}})},a["default"].use(Plugin);Plugin;var i=t("3dfd"),l=t("8c4f"),f=t("5c96"),s=t.n(f);a["default"].use(l["a"]);var h=function(){return Promise.all([t.e("chunk-502bf7a9"),t.e("chunk-27e9aa7a")]).then(t.bind(null,"578a"))},d=function(){return Promise.all([t.e("chunk-502bf7a9"),t.e("chunk-67b409f0")]).then(t.bind(null,"1feb"))},p=function(){return t.e("chunk-1027850a").then(t.bind(null,"67f4"))},b=function(){return t.e("chunk-3a1a25d8").then(t.bind(null,"4423"))},m=function(){return t.e("chunk-57a62ed8").then(t.bind(null,"70cb"))},g=function(){return t.e("chunk-00188d6a").then(t.bind(null,"f45b"))},k=function(){return t.e("chunk-983257a2").then(t.bind(null,"ead1"))},v=function(){return t.e("chunk-1b85e661").then(t.bind(null,"3df1"))},y=function(){return Promise.all([t.e("chunk-502bf7a9"),t.e("chunk-60b76a16")]).then(t.bind(null,"571f"))},P=function(){return t.e("chunk-0e490c7a").then(t.bind(null,"990d"))},w=[{path:"/",name:"Home",redirect:"/Login"},{path:"/Login",name:"Login",component:h},{path:"/Register",name:"Register",component:d},{path:"/MainPage",name:"MainPage",component:p,children:[{path:"/AboutVirus",name:"AboutVirus",component:b},{path:"/Volunteer",name:"Volunteer",component:m},{path:"/Donate",name:"Donate",component:g},{path:"/MessageBoard",name:"MessageBoard",component:k},{path:"/MyPage",name:"MyPage",component:v},{path:"/RevisePwd",name:"RevisePwd",component:y},{path:"/PutMessage",name:"putMessage",component:P}]},{path:"/OtherPeople",name:"OtherPeople",component:function(){return t.e("chunk-6568a628").then(t.bind(null,"7852"))}}],A=new l["a"]({routes:w});A.beforeEach((function(e,n,t){if("/Login"===e.path)t();else if("/Register"===e.path)t();else{var a=localStorage.getItem("Authorization");null===a||""===a?t("/Login"):t()}}));var S=A,j=t("2f62");a["default"].use(j["a"]);var O=new j["a"].Store({state:{Authorization:localStorage.getItem("Authorization")?localStorage.getItem("Authorization"):""},mutations:{changeLogin:function(e,n){e.Authorization=n.Authorization,localStorage.setItem("Authorization",n.Authorization)}}}),x=O;t("0fae");a["default"].use(s.a),a["default"].config.productionTip=!1,axios.defaults.baseURL="http://192.168.0.104/message/api/",axios.defaults.withCredentials=!0,new a["default"]({router:S,store:x,render:function(e){return e(i["default"])}}).$mount("#app"),axios.interceptors.request.use((function(e){return localStorage.getItem("Authorization")&&(e.headers.Authorization=localStorage.getItem("Authorization")),e}),(function(e){return Promise.reject(e)}))},faa3:function(e,n,t){"use strict";var a=function(){var e=this,n=e.$createElement,t=e._self._c||n;return t("div",{staticClass:"app",staticStyle:{overflow:"hidden"}},[t("router-view")],1)},r=[];t.d(n,"a",(function(){return a})),t.d(n,"b",(function(){return r}))}});