(window.webpackJsonpfrontend=window.webpackJsonpfrontend||[]).push([[0],{153:function(e,a,t){e.exports=t(188)},159:function(e,a,t){},160:function(e,a,t){},188:function(e,a,t){"use strict";t.r(a);var n=t(0),r=t.n(n),l=t(11),o=t.n(l),c=t(250),i=t(249),u=t(14),s=(t(158),t(159),t(9)),m=t(31),d=t(50),f=(t(160),t(38)),p=t(7),E=t.n(p),g=t(228),h=t(229),b=t(230),v=t(46),y=t(222),O=t(102),w=t(21),_=t(227),k=t(104),C=t.n(k),j=r.a.createContext(),S=j.Provider,x=(j.Consumer,j),P="http://localhost:"+window.BACKEND_PORT,I=t(220),D=t(100),W=t.n(D),F=t(224),N=t(191),R=t(77),T=t(223),L=t(226),z=t(225),V=!0,A=function(){return V},q=function(e){return V=!!e},B=2e3,M=[],U=function(e){return M.push(e)},H=function(e){return M=M.filter((function(a){return a!==e}))},J=function(){return M.forEach((function(e){return e()}))},K=["Live","Step"];var G=function(){var e=r.a.useState(!1),a=Object(s.a)(e,2),t=a[0],n=a[1],l=r.a.useRef(null),o=r.a.useState(A()?0:1),c=Object(s.a)(o,2),i=c[0],u=c[1],m=function(e){l.current&&l.current.contains(e.target)||n(!1)};return r.a.createElement(r.a.Fragment,null,r.a.createElement(I.a,{variant:"contained",color:"primary",ref:l,"aria-label":"split button",style:{marginRight:15}},r.a.createElement(y.a,{onClick:function(){J()},disabled:0===i},K[i]),r.a.createElement(y.a,{color:"primary",size:"small","aria-owns":t?"menu-list-grow":void 0,"aria-haspopup":"true",onClick:function(){n((function(e){return!e}))}},r.a.createElement(W.a,null))),r.a.createElement(T.a,{open:t,anchorEl:l.current,transition:!0,disablePortal:!0},(function(e){var a=e.TransitionProps,t=e.placement;return r.a.createElement(N.a,Object.assign({},a,{style:{transformOrigin:"bottom"===t?"center top":"center bottom"}}),r.a.createElement(R.a,{id:"menu-list-grow"},r.a.createElement(F.a,{onClickAway:m},r.a.createElement(z.a,null,K.map((function(e,a){return r.a.createElement(L.a,{key:e,disabled:2===a,selected:a===i,onClick:function(e){return function(e,a){q(0===a),u(a),n(!1)}(0,a)}},e)}))))))})))},$=Object(O.a)((function(e){return{appBar:Object(f.a)({marginLeft:240},e.breakpoints.up("sm"),{width:"calc(100% - ".concat(240,"px)")}),menuButton:{marginRight:e.spacing(2)},title:{flexGrow:1},logoutButton:{float:"right"}}}));var Q=function(e){var a=e.handleMenuToggle,t=void 0===a?function(){}:a,n=$(),l=Object(w.a)(),o=Object(_.a)(l.breakpoints.up("sm")),c=r.a.useContext(x),i=r.a.useState(!1),u=Object(s.a)(i,2),f=u[0],p=u[1];return f?(E.a.post("/auth/logout",{token:c}).then((function(e){console.log(e)})).catch((function(e){console.error(e)})),localStorage.removeItem("token"),localStorage.removeItem("u_id"),r.a.createElement(d.a,{to:"/login"})):r.a.createElement(g.a,{position:"fixed",className:n.appBar},r.a.createElement(h.a,null,!o&&r.a.createElement(r.a.Fragment,null,r.a.createElement(b.a,{color:"inherit","aria-label":"open drawer",edge:"start",onClick:t,className:n.menuButton},r.a.createElement(C.a,null)),r.a.createElement(m.b,{to:"/",style:{color:"white",textDecoration:"none"}},r.a.createElement(v.a,{variant:"h5",noWrap:!0},"Slackr"))),r.a.createElement("div",{variant:"h6",className:n.title}),r.a.createElement("div",{style:{display:"flex"}},r.a.createElement(G,null),r.a.createElement(y.a,{color:"inherit",className:n.logoutButton,onClick:function(){p(!0)}},"Logout"))))},X=t(254),Y=t(256),Z=t(231);function ee(e,a){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);a&&(n=n.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),t.push.apply(t,n)}return t}function ae(e){for(var a=1;a<arguments.length;a++){var t=null!=arguments[a]?arguments[a]:{};a%2?ee(t,!0).forEach((function(a){Object(f.a)(e,a,t[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):ee(t).forEach((function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(t,a))}))}return e}var te=Object(O.a)((function(e){return{drawer:Object(f.a)({},e.breakpoints.up("sm"),{width:240,flexShrink:0}),drawerPaper:{width:240},toolbar:ae({},e.mixins.toolbar,{display:"flex",alignItems:"center",paddingLeft:e.spacing(2)})}}));var ne=function(e){var a=e.container,t=e.children,n=e.open,l=e.setOpen,o=te(),c=Object(w.a)();return r.a.createElement("nav",{className:o.drawer,"aria-label":"channels"},r.a.createElement(X.a,{smUp:!0,implementation:"css"},r.a.createElement(Y.a,{container:a,variant:"temporary",anchor:"rtl"===c.direction?"right":"left",open:n,onClose:function(){return l(!1)},classes:{paper:o.drawerPaper},ModalProps:{keepMounted:!0}},r.a.createElement("div",{className:o.toolbar}),r.a.createElement(Z.a,null),t)),r.a.createElement(X.a,{xsDown:!0,implementation:"css"},r.a.createElement(Y.a,{classes:{paper:o.drawerPaper},variant:"permanent",open:!0},r.a.createElement("div",{className:o.toolbar},r.a.createElement(m.b,{to:"/",style:{color:"black",textDecoration:"none"}},r.a.createElement(v.a,{variant:"h5",noWrap:!0},"Slackr"))),t)))},re=Object(O.a)((function(e){var a;return{body:(a={},Object(f.a)(a,e.breakpoints.up("sm"),{width:"calc(100% - ".concat(240,"px)")}),Object(f.a)(a,"padding",20),a),toolbar:e.mixins.toolbar}}));var le=function(e){var a=e.children,t=re();return r.a.createElement("div",{className:t.body},r.a.createElement("div",{className:t.toolbar}),a)};var oe=function(e){var a=e.menu,t=e.body,n=r.a.useState(!1),l=Object(s.a)(n,2),o=l[0],c=l[1];return r.a.createElement("div",{style:{display:"flex"}},r.a.createElement(Q,{handleMenuToggle:function(){c((function(e){return!e}))}}),r.a.createElement(ne,{open:o,setOpen:c},a),r.a.createElement(le,null,t))},ce=t(192),ie=t(193),ue=t(232),se=t(233),me=t(105),de=t.n(me);function fe(e){var a=localStorage.getItem("u_id");return null==a&&(a=-1),a}var pe=function(){var e=fe(r.a.useContext(x));return r.a.createElement(ce.a,null,r.a.createElement(ie.a,{button:!0,key:"profile",component:m.b,to:"/profile/".concat(e)},r.a.createElement(ue.a,null,r.a.createElement(de.a,null)),r.a.createElement(se.a,{primary:"Profile"})))},Ee=t(242),ge=t(73),he=t.n(ge),be=t(74),ve=t.n(be),ye=t(106),Oe=t(234),we=t(235),_e=t(236),ke=t(237),Ce=t(238),je=t(252),Se=t(240),xe=t(257),Pe=t(241),Ie=t(110),De=t.n(Ie),We=t(111),Fe=t.n(We),Ne=t(109),Re=t.n(Ne),Te="An error occured. Try again later",Le="Unable to retrieve channel information";var ze=function(e){Object(ye.a)({},e);var a=r.a.useState(!1),t=Object(s.a)(a,2),n=t[0],l=t[1],o=r.a.useContext(x);function c(){l(!1)}return r.a.createElement("div",null,r.a.createElement(b.a,{size:"small",onClick:function(){l(!0)}},r.a.createElement(Re.a,null)),r.a.createElement(Oe.a,{open:n,onClose:c,"aria-labelledby":"form-dialog-title"},r.a.createElement(we.a,{id:"form-dialog-title"},"Create Channel"),r.a.createElement("form",{onSubmit:function(e){e.preventDefault();var a=e.target[0].value,t=!e.target[1].checked;a&&E.a.post("/channels/create",{token:o,name:a,is_public:t}).then((function(e){console.log(e)})).catch((function(e){console.error(e),u.b.error(Te)}))}},r.a.createElement(_e.a,null,r.a.createElement(ke.a,null,"Complete the form below to create a new channel"),r.a.createElement(Ce.a,{container:!0,spacing:2,direction:"row",justify:"center",alignItems:"center"},r.a.createElement(Ce.a,{item:!0,xs:12},r.a.createElement(je.a,{autoFocus:!0,margin:"dense",id:"channel_name",label:"Channel Name",name:"channel_name",fullWidth:!0})),r.a.createElement(Ce.a,{container:!0,item:!0,justify:"center",alignItems:"center"},r.a.createElement(De.a,null),r.a.createElement(Se.a,{control:r.a.createElement(xe.a,{value:"secret",inputProps:{"aria-label":"Secret"}}),label:"Secret",labelPlacement:"top"}),r.a.createElement(Fe.a,null)))),r.a.createElement(Pe.a,null,r.a.createElement(y.a,{onClick:c,color:"primary"},"Cancel"),r.a.createElement(y.a,{onClick:c,type:"submit",color:"primary"},"Create")))))};function Ve(e,a){var t=Object(n.useRef)();Object(n.useEffect)((function(){t.current=e}),[e]),Object(n.useEffect)((function(){if(null!==a){var e=setInterval((function(){t.current()}),a);return function(){return clearInterval(e)}}}),[a])}var Ae=function(e){var a=e.channel_id,t=r.a.useState([]),n=Object(s.a)(t,2),l=n[0],o=n[1],c=r.a.useState([]),i=Object(s.a)(c,2),u=i[0],d=i[1],f=r.a.useContext(x),p=function(){var e=E.a.get("/channels/list",{params:{token:f}}),a=E.a.get("/channels/listall",{params:{token:f}});E.a.all([e,a]).then(E.a.spread((function(e,a){var t=e.data.channels;console.log(t);var n=a.data.channels.filter((function(e){return void 0===t.find((function(a){return a.channel_id===e.channel_id}))}));console.log(n),o(t),d(n)})))};return r.a.useEffect((function(){return p(),U(p),function(){return H(p)}}),[]),Ve((function(){A()&&p()}),2*B),r.a.createElement(r.a.Fragment,null,r.a.createElement(ce.a,{subheader:r.a.createElement(Ee.a,{style:{display:"flex"}},r.a.createElement("span",{style:{flex:1}},"My Channels"),r.a.createElement(ze,null))},l.map((function(e,t){var n=e.channel_id,l=e.name;return r.a.createElement(ie.a,{button:!0,key:n,component:m.b,to:"/channel/".concat(n)},r.a.createElement(ue.a,null,n==a?r.a.createElement(he.a,null):r.a.createElement(ve.a,null)),r.a.createElement(se.a,{primary:l}))}))),r.a.createElement(ce.a,{subheader:r.a.createElement(Ee.a,null,"Other Channels")},u.map((function(e,t){var n=e.channel_id,l=e.name;return r.a.createElement(ie.a,{button:!0,key:n,component:m.b,to:"/channel/".concat(n)},r.a.createElement(ue.a,null,n==a?r.a.createElement(he.a,null):r.a.createElement(ve.a,null)),r.a.createElement(se.a,{primary:l}))}))))};var qe=function(e){var a=e.channel_id;return r.a.createElement(r.a.Fragment,null,r.a.createElement(pe,null),r.a.createElement(Ae,{channel_id:a}))};var Be=function(e){return r.a.createElement(oe,{menu:r.a.createElement(qe,null),body:r.a.createElement(r.a.Fragment,null,r.a.createElement(v.a,{variant:"h4"},"WELCOME"),r.a.createElement("div",{style:{paddingTop:15}},r.a.createElement(v.a,{variant:"body1"},"This is SengChat: agile messaging for Software Engineers \u2764\ufe0f")))})},Me=t(32),Ue=t(245),He=t(247),Je=t(121),Ke=t.n(Je),Ge=t(120),$e=t.n(Ge);var Qe=function(e){var a=e.channel_id,t=(Object(Me.a)(e,["channel_id"]),r.a.useState(!1)),n=Object(s.a)(t,2),l=n[0],o=n[1],c=r.a.useContext(x);function i(){o(!1)}return r.a.createElement("div",null,r.a.createElement(y.a,{variant:"outlined",color:"primary",onClick:function(){o(!0)}},"Invite Member"),r.a.createElement(Oe.a,{open:l,onClose:i,"aria-labelledby":"form-dialog-title"},r.a.createElement(we.a,{id:"form-dialog-title"},"Invite User"),r.a.createElement("form",{onSubmit:function(e){e.preventDefault();var t=e.target[0].value;t&&E.a.post("/channel/invite",{token:c,user_id:t,channel_id:a}).then((function(e){console.log(e)})).catch((function(e){console.error(e),u.b.error(Te)}))}},r.a.createElement(_e.a,null,r.a.createElement(ke.a,null,"Enter a user id below to invite a user to this channel"),r.a.createElement(je.a,{autoFocus:!0,margin:"dense",id:"user_id",label:"User ID",name:"user_id",fullWidth:!0})),r.a.createElement(Pe.a,null,r.a.createElement(y.a,{onClick:i,color:"primary"},"Cancel"),r.a.createElement(y.a,{onClick:i,type:"submit",color:"primary"},"Invite")))))},Xe=t(112),Ye=t.n(Xe),Ze=t(75),ea=t.n(Ze),aa=t(76),ta=t(243);var na=Object(ta.a)((function(e){var a=e.message_id,t=e.is_pinned,n=void 0!==t&&t,l=e.theme,o=r.a.useState(n),c=Object(s.a)(o,2),i=c[0],u=c[1];r.a.useEffect((function(){return u(n)}),[n]);var m=r.a.useContext(x);return r.a.createElement(b.a,{onClick:function(){i?E.a.post("/message/unpin",{token:m,message_id:a}):E.a.post("/message/pin",{token:m,message_id:a})},style:{margin:1},size:"small",edge:"end","aria-label":"delete"},i?r.a.createElement(ea.a,{path:aa.a,size:"1em",color:l&&l.palette.action.active}):r.a.createElement(ea.a,{path:aa.b,size:"1em",color:l&&l.palette.action.active}))})),ra=t(244),la=t(113),oa=t.n(la),ca=t(114),ia=t.n(ca);var ua=function(e){var a=e.message_id,t=e.reacts,n=void 0===t?[]:t,l=r.a.useContext(x),o=0,c=!1,i=n.findIndex((function(e){return 1===e.react_id}));return-1!==i&&(o=n[i].u_ids.length,c=n[i].is_this_user_reacted),r.a.createElement(ra.a,{anchorOrigin:{horizontal:"right",vertical:"bottom"},badgeContent:o,color:"secondary"},r.a.createElement(b.a,{onClick:function(){return function(e){e?E.a.post("/message/unreact",{token:l,message_id:a,react_id:1}):E.a.post("/message/react",{token:l,message_id:a,react_id:1})}(c)},style:{margin:1},size:"small",edge:"end","aria-label":"delete"},c?r.a.createElement(oa.a,{fontSize:"small"}):r.a.createElement(ia.a,{fontSize:"small"})))},sa=t(115),ma=t.n(sa);var da=function(e){var a=e.message_id,t=r.a.useContext(x);return r.a.createElement(b.a,{onClick:function(){E.a.delete("/message/remove",{data:{token:t,message_id:a}})},style:{margin:1},size:"small",edge:"end","aria-label":"delete"},r.a.createElement(ma.a,{fontSize:"small"}))};var fa=function(e){var a=e.message_id,t=e.message,n=void 0===t?"":t,l=e.u_id,o=e.time_created,c=(e.is_unread,e.is_pinned),i=void 0!==c&&c,u=e.reacts,m=void 0===u?[]:u,d=r.a.useState(),f=Object(s.a)(d,2),p=f[0],g=f[1],h=r.a.useState(),b=Object(s.a)(h,2),v=b[0],y=b[1],O=r.a.useContext(x);return r.a.useEffect((function(){g(),y(),E.a.get("/user/profile",{params:{token:O,u_id:l}}).then((function(e){var a=e.data,t=(a.email,a.name_first),n=void 0===t?"":t,r=a.name_last,l=void 0===r?"":r;a.handle_str;g("".concat(n," ").concat(l)),y("".concat(n[0]).concat(l[0]))})).catch((function(e){console.error(e)}))}),[a,O,l]),r.a.createElement(ie.a,{key:a,style:{width:"100%"}},p&&v&&n&&r.a.createElement(r.a.Fragment,null,r.a.createElement(ue.a,null,r.a.createElement(Ue.a,null,v)),r.a.createElement("div",{style:{display:"flex",width:"100%",justifyContent:"space-between",alignItems:"center"}},r.a.createElement(se.a,{primary:r.a.createElement(r.a.Fragment,null,r.a.createElement("span",null,p),r.a.createElement("span",{style:{paddingLeft:10,fontSize:10}},Ye()(1e3*o))),secondary:n}),r.a.createElement("div",{style:{display:"flex",height:30,marginLeft:20}},r.a.createElement(ua,{message_id:a,reacts:m,u_id:l}),r.a.createElement(na,{message_id:a,is_pinned:i}),r.a.createElement(da,{message_id:a})))))},pa=t(246),Ea=t(119),ga=t.n(Ea),ha=t(118),ba=t.n(ha),va=t(195),ya=t(251);var Oa=function(e){var a=e.open,t=e.handleClose,n=e.onTimerChange,l=(Object(Me.a)(e,["open","handleClose","onTimerChange"]),r.a.useState(new Date)),o=Object(s.a)(l,2),c=o[0],i=o[1];return r.a.createElement("div",null,r.a.createElement(Oe.a,{open:a,onClose:t,"aria-labelledby":"form-dialog-title"},r.a.createElement(we.a,{id:"form-dialog-title"},"Send later"),r.a.createElement("form",{onSubmit:function(e){e.preventDefault(),n(c)}},r.a.createElement(_e.a,null,r.a.createElement(ya.a,{margin:"normal",id:"time-picker",label:"Time picker",value:c,onChange:function(e){return i(e.toDate())},KeyboardButtonProps:{"aria-label":"change time"}}),r.a.createElement(ke.a,null,"Enter a time to send")),r.a.createElement(Pe.a,null,r.a.createElement(y.a,{onClick:t,color:"primary"},"Cancel"),r.a.createElement(y.a,{onClick:t,type:"submit",color:"primary"},"Set Time")))))},wa=Object(va.a)((function(e){return{flex:{display:"flex",flexDirection:"row",alignItems:"center"},input:{margin:e.spacing(1),marginRight:0},button:{margin:e.spacing(1),marginLeft:0,alignSelf:"stretch"},rightIcon:{marginLeft:e.spacing(1)}}})),_a=-1;var ka=function(e){var a=e.channel_id,t=void 0===a?"":a,n=wa(),l=r.a.useState(""),o=Object(s.a)(l,2),c=o[0],i=o[1],m=r.a.useState(_a),d=Object(s.a)(m,2),f=d[0],p=d[1],g=r.a.useState(!1),h=Object(s.a)(g,2),v=h[0],O=h[1],w=r.a.useContext(x),_=f!==_a,k=function(){var e=c.trim();e&&(i(""),_?(E.a.post("/message/sendlater",{token:w,channel_id:t,message:e,time_sent:f.toISOString()}).then((function(e){var a=e.data;console.log(a)})).catch((function(e){console.error(e),u.b.error(Te)})),p(_a)):("/standup"==e&&alert("Hello. This feature isn't finished yet. We won't be expecting you to demonstrate this on the frontend in iteration 2"),E.a.post("/message/send",{token:w,channel_id:t,message:e}).then((function(e){var a=e.data;console.log(a)})).catch((function(e){console.error(e),u.b.error(Te)}))))};return r.a.createElement(r.a.Fragment,null,r.a.createElement("div",{className:n.flex},r.a.createElement(je.a,{className:n.input,label:"Send a message \ud83d\udcac",multiline:!0,placeholder:"...",fullWidth:!0,margin:"normal",variant:"filled",onKeyDown:function(e){"Enter"!==e.key||e.getModifierState("Shift")||(e.preventDefault(),k())},value:c,onChange:function(e){return i(e.target.value)},InputProps:{endAdornment:r.a.createElement(pa.a,{position:"end"},r.a.createElement(b.a,{"aria-label":"toggle visibility",onClick:function(){return _?p(-1):O(!0)}},r.a.createElement(ba.a,{color:_?"secondary":void 0})))}}),r.a.createElement(y.a,{className:n.button,variant:"contained",color:"primary",onClick:k},"Send",r.a.createElement(ga.a,{className:n.rightIcon}))),r.a.createElement(Oa,{open:v,handleClose:function(){return O(!1)},onTimerChange:p}))};var Ca=function(e){var a=e.channel_id,t=void 0===a?"":a,n=r.a.useState([]),l=Object(s.a)(n,2),o=l[0],c=l[1],i=r.a.useState(0),m=Object(s.a)(i,2),d=m[0],f=m[1],p=r.a.useContext(x),g=function(){return E.a.get("/channel/messages",{params:{token:p,channel_id:t,start:d}}).then((function(e){var a=e.data,t=a.messages,n=(a.start,a.end);f(n),c(t)})).catch((function(e){console.error(e),u.b.error(Le)}))};return r.a.useEffect((function(){return g(),U(g),function(){return H(g)}}),[t]),Ve((function(){A()&&g()}),B),r.a.createElement(r.a.Fragment,null,r.a.createElement(ce.a,{subheader:r.a.createElement(Ee.a,null,"Messages"),style:{width:"100%"}},o.slice().reverse().map((function(e){return r.a.createElement(fa,e)}))),r.a.createElement(ka,{channel_id:t}))};var ja=function(e){var a=e.channel_id,t=(Object(Me.a)(e,["channel_id"]),r.a.useState("")),n=Object(s.a)(t,2),l=n[0],o=n[1],c=r.a.useState([]),i=Object(s.a)(c,2),m=i[0],d=i[1],f=r.a.useState([]),p=Object(s.a)(f,2),g=p[0],h=p[1],O=r.a.useContext(x),w=fe();function _(e,a){E.a.get("/channel/details",{params:{token:a,channel_id:e}}).then((function(e){var a=e.data;console.log(a);var t=a.name,n=a.owner_members,r=a.all_members;d(r),h(n),o(t)})).catch((function(e){console.error(e),u.b.error(Le)}))}function k(e,a){return void 0!==e.find((function(e){return e.u_id===a}))}r.a.useEffect((function(){_(a,O)}),[a,O]);var C=k(g,w);return r.a.createElement(r.a.Fragment,null,r.a.createElement(v.a,{variant:"h4"},l.toUpperCase()),r.a.createElement(ce.a,{subheader:r.a.createElement(Ee.a,null,"Members")},m.map((function(e){var t=e.u_id,n=e.name_first,l=e.name_last;return r.a.createElement(ie.a,{key:t},r.a.createElement(ue.a,null,r.a.createElement(Ue.a,null,n[0],l[0])),r.a.createElement(se.a,{primary:r.a.createElement(r.a.Fragment,null,r.a.createElement(Ce.a,{container:!0,alignItems:"center",spacing:1},r.a.createElement(Ce.a,{item:!0},r.a.createElement(He.a,{href:"/profile/".concat(t)},"".concat(n," ").concat(l)),"".concat(k(g,t)?" \u2b50":" ")),C&&r.a.createElement(Ce.a,{item:!0},k(g,t)?r.a.createElement(b.a,{size:"small",onClick:function(){return function(e){E.a.post("/channel/removeowner",{token:O,channel_id:a,u_id:e}).then((function(){_(a,O)})).catch((function(e){console.error(e),u.b.error(Te)}))}(t)}},r.a.createElement($e.a,null)):r.a.createElement(b.a,{size:"small",onClick:function(){return function(e){E.a.post("/channel/addowner",{token:O,channel_id:a,u_id:e}).then((function(){_(a,O)})).catch((function(e){console.error(e),u.b.error(Te)}))}(t)}},r.a.createElement(Ke.a,null)))))}))})),r.a.createElement(ie.a,{key:"invite_member"},function(e){return console.log(e),void 0!==e.find((function(e){return e.u_id===w}))}(m)?r.a.createElement(Ce.a,{container:!0,spacing:1},r.a.createElement(Ce.a,{item:!0},r.a.createElement(Qe,{channel_id:a})),r.a.createElement(Ce.a,{item:!0},r.a.createElement(y.a,{variant:"outlined",onClick:function(){return function(e,a){E.a.post("/channel/leave",{token:a,channel_id:e}).then((function(){_(e,a)})).catch((function(e){console.error(e),u.b.error(Te)}))}(a,O)}},"Leave Channel"))):r.a.createElement(y.a,{variant:"outlined",color:"primary",onClick:function(){return function(e,a){E.a.post("/channel/join",{token:a,channel_id:e}).then((function(){_(e,a)})).catch((function(e){console.error(e),u.b.error(Te)}))}(a,O)}},"Join Channel"))),r.a.createElement(Ca,{channel_id:a}))};var Sa=function(e){var a=e.match.params.channel_id;return r.a.createElement(oe,{menu:r.a.createElement(qe,{channel_id:a}),body:r.a.createElement(ja,{channel_id:a})})},xa=t(248),Pa=t(253),Ia=t(122),Da=t.n(Ia),Wa=Object(O.a)((function(e){return{"@global":{body:{backgroundColor:e.palette.primary.light}},card:{backgroundColor:e.palette.background.paper,marginTop:e.spacing(8),padding:e.spacing(8),display:"flex",flexDirection:"column",alignItems:"center",borderRadius:e.shape.borderRadius}}}));var Fa=function(e){var a=e.setAuth,t=Object(Me.a)(e,["setAuth"]),n=Wa();return r.a.createElement(xa.a,{component:"main",maxWidth:"sm"},r.a.createElement(Pa.a,{boxShadow:3,className:n.card},r.a.createElement(Ue.a,null,r.a.createElement(Da.a,null)),r.a.createElement(v.a,{component:"h1",variant:"h5"},"Login"),r.a.createElement("form",{noValidate:!0,onSubmit:function(e){e.preventDefault();var n=e.target[0].value,r=e.target[2].value;n&&r&&E.a.post("/auth/login",{email:n,password:r}).then((function(e){console.log(e);var n=e.data;a(n.token,n.u_id),t.history.push("/")})).catch((function(e){console.error(e),u.b.error(Te)}))}},r.a.createElement(je.a,{variant:"outlined",margin:"normal",required:!0,fullWidth:!0,id:"email",label:"Email",name:"email",type:"text",autoFocus:!0}),r.a.createElement(je.a,{variant:"outlined",margin:"normal",required:!0,fullWidth:!0,name:"password",label:"Password",type:"password",id:"password",autoComplete:"current-password"}),r.a.createElement(y.a,{type:"submit",fullWidth:!0,variant:"contained",color:"primary"},"Sign In"),r.a.createElement(Ce.a,{container:!0,direction:"column",alignItems:"center"},r.a.createElement(Ce.a,{item:!0},r.a.createElement("br",null),r.a.createElement(He.a,{href:"/register",variant:"body1"},"Don't have an account? Register")),r.a.createElement(Ce.a,{item:!0},r.a.createElement("br",null),r.a.createElement(He.a,{href:"/forgot_password",variant:"body1"},"Forgot password?"))))))},Na=t(55),Ra=t.n(Na);function Ta(e,a){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);a&&(n=n.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),t.push.apply(t,n)}return t}function La(e){for(var a=1;a<arguments.length;a++){var t=null!=arguments[a]?arguments[a]:{};a%2?Ta(t,!0).forEach((function(a){Object(f.a)(e,a,t[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):Ta(t).forEach((function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(t,a))}))}return e}var za=Object(O.a)((function(e){return{"@global":{body:{backgroundColor:e.palette.primary.light}},card:{backgroundColor:e.palette.background.paper,marginTop:e.spacing(8),padding:e.spacing(8),display:"flex",flexDirection:"column",alignItems:"center",borderRadius:e.shape.borderRadius}}}));var Va=function(e){var a=e.setAuth,t=Object(Me.a)(e,["setAuth"]),n=r.a.useState({name_first:"",name_last:"",email:"",password:""}),l=Object(s.a)(n,2),o=l[0],c=l[1],i=function(e){return function(a){c(La({},o,Object(f.a)({},e,a.target.value)))}},m=za();return r.a.createElement(xa.a,{component:"main",maxWidth:"sm"},r.a.createElement(Pa.a,{boxShadow:3,className:m.card},r.a.createElement(Ue.a,null,r.a.createElement(Ra.a,{color:"secondary"})),r.a.createElement(v.a,{component:"h1",variant:"h5"},"Register"),r.a.createElement("form",{noValidate:!0,onSubmit:function(e){e.preventDefault(),o.email&&o.password&&E.a.post("/auth/register",La({},o)).then((function(e){console.log(e);var n=e.data;a(n.token,n.u_id),t.history.push("/")})).catch((function(e){console.error(e),u.b.error(Te)}))}},r.a.createElement(je.a,{variant:"outlined",margin:"normal",required:!0,fullWidth:!0,id:"name_first",label:"First name",name:"name_first",type:"text",autoFocus:!0,value:o.name_first,onChange:i("name_first")}),r.a.createElement(je.a,{variant:"outlined",margin:"normal",required:!0,fullWidth:!0,id:"name_last",label:"Last name",name:"name_last",type:"text",value:o.name_last,onChange:i("name_last")}),r.a.createElement(je.a,{variant:"outlined",margin:"normal",required:!0,fullWidth:!0,id:"email",label:"Email",name:"email",type:"email",value:o.email,onChange:i("email")}),r.a.createElement(je.a,{variant:"outlined",margin:"normal",required:!0,fullWidth:!0,name:"password",label:"Password",type:"password",id:"password",autoComplete:"current-password",value:o.password,onChange:i("password")}),r.a.createElement(y.a,{type:"submit",fullWidth:!0,variant:"contained",color:"primary"},"Sign Up"),r.a.createElement(Ce.a,{container:!0},r.a.createElement(Ce.a,{item:!0},r.a.createElement("br",null),r.a.createElement(He.a,{href:"/login",variant:"body1"},"Already have an account? Login"))))))},Aa=Object(O.a)((function(e){return{"@global":{body:{backgroundColor:e.palette.primary.light}},card:{backgroundColor:e.palette.background.paper,marginTop:e.spacing(8),padding:e.spacing(8),display:"flex",flexDirection:"column",alignItems:"center",borderRadius:e.shape.borderRadius}}}));var qa=function(e){var a=Aa();return r.a.createElement(xa.a,{component:"main",maxWidth:"sm"},r.a.createElement(Pa.a,{boxShadow:3,className:a.card},r.a.createElement(Ue.a,null,r.a.createElement(Ra.a,{color:"secondary"})),r.a.createElement(v.a,{component:"h1",variant:"h5"},"Forgot Password"),r.a.createElement("form",{noValidate:!0,onSubmit:function(a){a.preventDefault();var t=a.target[0].value;t&&E.a.post("/auth/passwordreset/request",{email:t}).then((function(a){console.log(a),e.history.push("/reset_password")})).catch((function(e){console.error(e),u.b.error(Te)}))}},r.a.createElement(je.a,{variant:"outlined",margin:"normal",required:!0,fullWidth:!0,id:"email",label:"Email",name:"email",type:"email",autoFocus:!0}),r.a.createElement(y.a,{type:"submit",fullWidth:!0,variant:"contained",color:"primary"},"Send Recovery Email"),r.a.createElement(Ce.a,{container:!0},r.a.createElement(Ce.a,{item:!0},r.a.createElement("br",null),r.a.createElement(He.a,{href:"/login",variant:"body1"},"Remember your password? Login"))))))},Ba=Object(O.a)((function(e){return{"@global":{body:{backgroundColor:e.palette.primary.light}},card:{backgroundColor:e.palette.background.paper,marginTop:e.spacing(8),padding:e.spacing(8),display:"flex",flexDirection:"column",alignItems:"center",borderRadius:e.shape.borderRadius}}}));var Ma=function(e){var a=Ba();return r.a.createElement(xa.a,{component:"main",maxWidth:"sm"},r.a.createElement(Pa.a,{boxShadow:3,className:a.card},r.a.createElement(Ue.a,null,r.a.createElement(Ra.a,{color:"secondary"})),r.a.createElement(v.a,{component:"h1",variant:"h5"},"Reset Password"),r.a.createElement("form",{noValidate:!0,onSubmit:function(a){a.preventDefault();var t=a.target[0].value,n=a.target[2].value;t&&n&&E.a.post("/auth/passwordreset/reset",{reset_code:t,new_password:n}).then((function(a){console.log(a),e.history.push("/login")})).catch((function(e){console.error(e),u.b.error(Te)}))}},r.a.createElement(je.a,{variant:"outlined",margin:"normal",required:!0,fullWidth:!0,id:"reset_code",label:"Reset code",name:"reset_code",type:"text",autoFocus:!0}),r.a.createElement(je.a,{variant:"outlined",margin:"normal",required:!0,fullWidth:!0,id:"new_password",label:"New Password",name:"new_password",type:"password"}),r.a.createElement(y.a,{type:"submit",fullWidth:!0,variant:"contained",color:"primary"},"Change Password"),r.a.createElement(Ce.a,{container:!0},r.a.createElement(Ce.a,{item:!0},r.a.createElement("br",null),r.a.createElement(He.a,{href:"/login",variant:"body1"},"Remember your password? Login"))))))},Ua=t(130),Ha=t(125),Ja=t.n(Ha),Ka=t(124),Ga=t.n(Ka),$a=t(123),Qa=t.n($a);var Xa=function(e){var a=e.editable,t=e.master,n=e.masterValue,l=e.slaves,o=e.slaveValues,c=e.onSave,i=(Object(Me.a)(e,["editable","master","masterValue","slaves","slaveValues","onSave"]),r.a.useState(!1)),u=Object(s.a)(i,2),m=u[0],d=u[1],f=r.a.useState(),p=Object(s.a)(f,2),E=p[0],g=p[1],h=r.a.useState(n),b=Object(s.a)(h,2),v=b[0],y=b[1],O=r.a.useState([]),w=Object(s.a)(O,2),_=w[0],k=w[1],C=r.a.useState(o),j=Object(s.a)(C,2),S=j[0],x=j[1];function P(){g(v),k(S),d(!m)}return r.a.useEffect((function(){y(n),x(o)}),[n,o]),r.a.createElement(Ce.a,{container:!0,spacing:1,alignItems:"flex-end"},l&&l.map((function(e,a){return r.a.createElement(Ce.a,{item:!0,key:a},e({value:S[a]||"",InputProps:{readOnly:!m},onChange:function(e){return function(e,a){var t=S.map((function(t,n){return n===a?e.target.value:t}));x(t)}(e,a)}}))})),r.a.createElement(Ce.a,{item:!0},t({value:v||"",InputProps:{readOnly:!m},onChange:function(e){y(e.target.value)}})),a&&r.a.createElement(Ce.a,{item:!0},a?m?r.a.createElement(r.a.Fragment,null,r.a.createElement(Qa.a,{style:{cursor:"pointer"},onClick:function(){v&&(c&&(S?c.apply(void 0,[v].concat(Object(Ua.a)(S))):c(v)),P())}}),r.a.createElement(Ga.a,{style:{cursor:"pointer"},onClick:function(){y(E),x(_),P()}})):r.a.createElement(Ja.a,{style:{cursor:"pointer"},onClick:P}):null))};var Ya=function(e){var a=e.profile,t=r.a.useState({}),n=Object(s.a)(t,2),l=n[0],o=n[1],c=r.a.useContext(x),i=fe();r.a.useEffect((function(){E.a.get("/user/profile",{params:{token:c,u_id:i}}).then((function(e){var a=e.data;console.log(a),o(a)})).catch((function(e){console.error(e)}))}),[a,c]);var u=i.toString()===a;return r.a.createElement(r.a.Fragment,null,r.a.createElement(v.a,{variant:"h4"},"Profile"),r.a.createElement(ce.a,{subheader:r.a.createElement(Ee.a,null,"Profile Details")},r.a.createElement(ie.a,{key:"name"},r.a.createElement(Xa,{editable:u,masterValue:l.name_last,slaveValues:[l.name_first],master:function(e){return r.a.createElement(je.a,Object.assign({label:"Last Name"},e))},slaves:[function(e){return r.a.createElement(je.a,Object.assign({label:"First Name"},e))}],onSave:function(e,a){E.a.put("/user/profile/setname",{token:c,name_first:a,name_last:e}).then((function(){console.log("all good")})).catch((function(e){console.error(e)}))}})),r.a.createElement(ie.a,{key:"email"},r.a.createElement(Xa,{editable:u,masterValue:l.email,master:function(e){return r.a.createElement(je.a,Object.assign({label:"Email"},e))},onSave:function(e){E.a.put("/user/profile/setemail",{token:c,email:e}).then((function(){console.log("all good")})).catch((function(e){console.error(e)}))}})),r.a.createElement(ie.a,{key:"handle"},r.a.createElement(Xa,{editable:u,masterValue:l.handle_str,master:function(e){return r.a.createElement(je.a,Object.assign({label:"Handle"},e))},onSave:function(e){E.a.put("/user/profile/sethandle",{token:c,handle_str:e}).then((function(){console.log("all good")})).catch((function(e){console.error(e)}))}}))))};var Za=function(e){var a=e.match.params.profile;return r.a.createElement(oe,{menu:r.a.createElement(qe,null),body:r.a.createElement(Ya,{profile:a})})};var et=function(e){var a=r.a.useContext(x);return console.log(a),a?r.a.createElement(d.b,e):r.a.createElement(d.a,{to:"/login"})},at=t(126),tt=t.n(at);E.a.defaults.baseURL=P,E.a.defaults.headers.put["Content-Type"]="application/x-www-form-urlencoded",E.a.defaults.headers.post["Content-Type"]="application/x-www-form-urlencoded",E.a.defaults.headers.delete["Content-Type"]="application/x-www-form-urlencoded",E.a.interceptors.request.use((function(e){return"put"!==e.method&&"post"!==e.method&&"delete"!==e.method||(e.data=tt.a.stringify(e.data)),e}));var nt=function(){var e=r.a.useState(localStorage.getItem("token")),a=Object(s.a)(e,2),t=a[0],n=a[1];function l(e,a){localStorage.setItem("token",e),localStorage.setItem("u_id",a),n(e)}return r.a.createElement(S,{value:t},r.a.createElement(m.a,null,r.a.createElement(d.d,null,r.a.createElement(d.b,{exact:!0,path:"/login",render:function(e){return r.a.createElement(Fa,Object.assign({},e,{setAuth:l}))}}),r.a.createElement(d.b,{exact:!0,path:"/register",render:function(e){return r.a.createElement(Va,Object.assign({},e,{setAuth:l}))}}),r.a.createElement(d.b,{exact:!0,path:"/forgot_password",component:qa}),r.a.createElement(d.b,{exact:!0,path:"/reset_password",component:Ma}),r.a.createElement(et,{exact:!0,path:"/",component:Be}),r.a.createElement(et,{path:"/profile/:profile",component:Za}),r.a.createElement(et,{path:"/channel/:channel_id",component:Sa}))))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));var rt=t(67),lt=t(129),ot=Object(lt.a)({palette:{primary:{main:"#556cd6"},secondary:{main:"#19857b"},error:{main:rt.a.A400},background:{default:"#fff"}}}),ct=t(22),it=t(127);o.a.render(r.a.createElement(i.a,{theme:ot},r.a.createElement(ct.a,{utils:it.a},r.a.createElement(c.a,null),r.a.createElement(nt,null),r.a.createElement(u.a,{position:"top-center",autoClose:5e3,hideProgressBar:!1,newestOnTop:!0,closeOnClick:!0,rtl:!1,pauseOnVisibilityChange:!0,draggable:!0,pauseOnHover:!0}))),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))}},[[153,1,2]]]);
//# sourceMappingURL=main.021d5312.chunk.js.map