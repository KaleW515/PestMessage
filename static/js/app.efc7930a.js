(function(e){function n(n){for(var r,a,c=n[0],i=n[1],f=n[2],l=0,h=[];l<c.length;l++)a=c[l],Object.prototype.hasOwnProperty.call(u,a)&&u[a]&&h.push(u[a][0]),u[a]=0;for(r in i)Object.prototype.hasOwnProperty.call(i,r)&&(e[r]=i[r]);s&&s(n);while(h.length)h.shift()();return o.push.apply(o,f||[]),t()}function t(){for(var e,n=0;n<o.length;n++){for(var t=o[n],r=!0,a=1;a<t.length;a++){var c=t[a];0!==u[c]&&(r=!1)}r&&(o.splice(n--,1),e=i(i.s=t[0]))}return e}var r={},a={app:0},u={app:0},o=[];function c(e){return i.p+"static/js/"+({}[e]||e)+"."+{"chunk-00188d6a":"bfa4e20a","chunk-089942a4":"3b23d1b3","chunk-0c0353a7":"651ef9f5","chunk-0e490c7a":"71876eaf","chunk-502bf7a9":"26b24250","chunk-60b76a16":"b0737e53","chunk-67b409f0":"9996dd78","chunk-c4ceeb9c":"95d30d27","chunk-541fe021":"1baeaf4a","chunk-57a62ed8":"39a07d1b","chunk-62ad6226":"4e956b80","chunk-af2813fa":"6fd218d7"}[e]+".js"}function i(n){if(r[n])return r[n].exports;var t=r[n]={i:n,l:!1,exports:{}};return e[n].call(t.exports,t,t.exports,i),t.l=!0,t.exports}i.e=function(e){var n=[],t={"chunk-00188d6a":1,"chunk-089942a4":1,"chunk-0c0353a7":1,"chunk-0e490c7a":1,"chunk-60b76a16":1,"chunk-67b409f0":1,"chunk-c4ceeb9c":1,"chunk-541fe021":1,"chunk-57a62ed8":1,"chunk-62ad6226":1,"chunk-af2813fa":1};a[e]?n.push(a[e]):0!==a[e]&&t[e]&&n.push(a[e]=new Promise((function(n,t){for(var r="static/css/"+({}[e]||e)+"."+{"chunk-00188d6a":"c64d0b24","chunk-089942a4":"0666a3bd","chunk-0c0353a7":"b46e7bdb","chunk-0e490c7a":"7a6b8d66","chunk-502bf7a9":"31d6cfe0","chunk-60b76a16":"c440e3f4","chunk-67b409f0":"482e5e7b","chunk-c4ceeb9c":"117322f9","chunk-541fe021":"79be768e","chunk-57a62ed8":"226fd0dd","chunk-62ad6226":"df584c71","chunk-af2813fa":"56f1c392"}[e]+".css",u=i.p+r,o=document.getElementsByTagName("link"),c=0;c<o.length;c++){var f=o[c],l=f.getAttribute("data-href")||f.getAttribute("href");if("stylesheet"===f.rel&&(l===r||l===u))return n()}var h=document.getElementsByTagName("style");for(c=0;c<h.length;c++){f=h[c],l=f.getAttribute("data-href");if(l===r||l===u)return n()}var s=document.createElement("link");s.rel="stylesheet",s.type="text/css",s.onload=n,s.onerror=function(n){var r=n&&n.target&&n.target.src||u,o=new Error("Loading CSS chunk "+e+" failed.\n("+r+")");o.code="CSS_CHUNK_LOAD_FAILED",o.request=r,delete a[e],s.parentNode.removeChild(s),t(o)},s.href=u;var d=document.getElementsByTagName("head")[0];d.appendChild(s)})).then((function(){a[e]=0})));var r=u[e];if(0!==r)if(r)n.push(r[2]);else{var o=new Promise((function(n,t){r=u[e]=[n,t]}));n.push(r[2]=o);var f,l=document.createElement("script");l.charset="utf-8",l.timeout=120,i.nc&&l.setAttribute("nonce",i.nc),l.src=c(e);var h=new Error;f=function(n){l.onerror=l.onload=null,clearTimeout(s);var t=u[e];if(0!==t){if(t){var r=n&&("load"===n.type?"missing":n.type),a=n&&n.target&&n.target.src;h.message="Loading chunk "+e+" failed.\n("+r+": "+a+")",h.name="ChunkLoadError",h.type=r,h.request=a,t[1](h)}u[e]=void 0}};var s=setTimeout((function(){f({type:"timeout",target:l})}),12e4);l.onerror=l.onload=f,document.head.appendChild(l)}return Promise.all(n)},i.m=e,i.c=r,i.d=function(e,n,t){i.o(e,n)||Object.defineProperty(e,n,{enumerable:!0,get:t})},i.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(e,n){if(1&n&&(e=i(e)),8&n)return e;if(4&n&&"object"===typeof e&&e&&e.__esModule)return e;var t=Object.create(null);if(i.r(t),Object.defineProperty(t,"default",{enumerable:!0,value:e}),2&n&&"string"!=typeof e)for(var r in e)i.d(t,r,function(n){return e[n]}.bind(null,r));return t},i.n=function(e){var n=e&&e.__esModule?function(){return e["default"]}:function(){return e};return i.d(n,"a",n),n},i.o=function(e,n){return Object.prototype.hasOwnProperty.call(e,n)},i.p="/",i.oe=function(e){throw console.error(e),e};var f=window["webpackJsonp"]=window["webpackJsonp"]||[],l=f.push.bind(f);f.push=n,f=f.slice();for(var h=0;h<f.length;h++)n(f[h]);var s=l;o.push([0,"chunk-vendors"]),t()})({0:function(e,n,t){e.exports=t("56d7")},"199c":function(e,n){},"23be":function(e,n,t){"use strict";var r=t("199c"),a=t.n(r);n["default"]=a.a},"3dfd":function(e,n,t){"use strict";var r=t("faa3"),a=t("23be"),u=t("2877"),o=Object(u["a"])(a["default"],r["a"],r["b"],!1,null,null,null);n["default"]=o.exports},"56d7":function(e,n,t){"use strict";t.r(n);t("d3b7"),t("e260"),t("e6cf"),t("cca6"),t("a79d");var r=t("2b0e"),a=t("bc3a"),u=t.n(a),o={},c=u.a.create(o);c.interceptors.request.use((function(e){return e}),(function(e){return Promise.reject(e)})),c.interceptors.response.use((function(e){return e}),(function(e){return Promise.reject(e)})),Plugin.install=function(e,n){e.axios=c,window.axios=c,Object.defineProperties(e.prototype,{axios:{get:function(){return c}},$axios:{get:function(){return c}}})},r["default"].use(Plugin);Plugin;var i=t("3dfd"),f=t("8c4f"),l=t("5c96"),h=t.n(l);r["default"].use(f["a"]);var s=function(){return Promise.all([t.e("chunk-502bf7a9"),t.e("chunk-c4ceeb9c")]).then(t.bind(null,"578a"))},d=function(){return Promise.all([t.e("chunk-502bf7a9"),t.e("chunk-67b409f0")]).then(t.bind(null,"1feb"))},p=function(){return t.e("chunk-af2813fa").then(t.bind(null,"67f4"))},b=function(){return t.e("chunk-0c0353a7").then(t.bind(null,"4423"))},m=function(){return t.e("chunk-57a62ed8").then(t.bind(null,"70cb"))},g=function(){return t.e("chunk-00188d6a").then(t.bind(null,"f45b"))},k=function(){return t.e("chunk-541fe021").then(t.bind(null,"ead1"))},v=function(){return t.e("chunk-089942a4").then(t.bind(null,"3df1"))},y=function(){return Promise.all([t.e("chunk-502bf7a9"),t.e("chunk-60b76a16")]).then(t.bind(null,"571f"))},P=function(){return t.e("chunk-0e490c7a").then(t.bind(null,"990d"))},w=[{path:"/",name:"Home",redirect:"/Login"},{path:"/Login",name:"Login",component:s},{path:"/Register",name:"Register",component:d},{path:"/MainPage",name:"MainPage",component:p,children:[{path:"/AboutVirus",name:"AboutVirus",component:b},{path:"/Volunteer",name:"Volunteer",component:m},{path:"/Donate",name:"Donate",component:g},{path:"/MessageBoard",name:"MessageBoard",component:k},{path:"/MyPage",name:"MyPage",component:v},{path:"/RevisePwd",name:"RevisePwd",component:y},{path:"/PutMessage",name:"putMessage",component:P}]},{path:"/OtherPeople",name:"OtherPeople",component:function(){return t.e("chunk-62ad6226").then(t.bind(null,"7852"))}}],A=new f["a"]({routes:w});A.beforeEach((function(e,n,t){if("/Login"===e.path)t();else if("/Register"===e.path)t();else{var r=localStorage.getItem("Authorization");null===r||""===r?t("/Login"):t()}}));var S=A,j=t("2f62");r["default"].use(j["a"]);var O=new j["a"].Store({state:{Authorization:localStorage.getItem("Authorization")?localStorage.getItem("Authorization"):""},mutations:{changeLogin:function(e,n){e.Authorization=n.Authorization,localStorage.setItem("Authorization",n.Authorization)}}}),x=O;t("0fae");r["default"].use(h.a),r["default"].config.productionTip=!1,axios.defaults.baseURL="http://127.0.0.1:8000",new r["default"]({router:S,store:x,render:function(e){return e(i["default"])}}).$mount("#app"),axios.interceptors.request.use((function(e){return localStorage.getItem("Authorization")&&(e.headers.Authorization=localStorage.getItem("Authorization")),e}),(function(e){return Promise.reject(e)}))},faa3:function(e,n,t){"use strict";var r=function(){var e=this,n=e.$createElement,t=e._self._c||n;return t("div",{staticClass:"app",staticStyle:{overflow:"hidden"}},[t("router-view")],1)},a=[];t.d(n,"a",(function(){return r})),t.d(n,"b",(function(){return a}))}});