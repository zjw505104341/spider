function A_1(t) {
    for (var e = [], n = 0; n < t.length; n++)
        e.push(255 & t.charCodeAt(n));
    return e
}

function A_2(t) {
    for (var e = [], n = 0, r = 0; n < t.length; n++,
        r += 8)
        e[r >>> 5] |= t[n] << 24 - r % 32;
    return e
}

(function(t, e, n) {
    var n = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    var r = {
        rotl: function(t, e) {
            return t << e | t >>> 32 - e
        },
        rotr: function(t, e) {
            return t << 32 - e | t >>> e
        },
        endian: function(t) {
            if (t.constructor == Number)
                return 16711935 & r.rotl(t, 8) | 4278255360 & r.rotl(t, 24);
            for (var e = 0; e < t.length; e++)
                t[e] = r.endian(t[e]);
            return t
        },
        randomBytes: function(t) {
            for (var e = []; t > 0; t--)
                e.push(Math.floor(256 * Math.random()));
            return e
        },
        bytesToWords: function(t) {
            for (var e = [], n = 0, r = 0; n < t.length; n++,
                r += 8)
                e[r >>> 5] |= t[n] << 24 - r % 32;
            return e
        },
        wordsToBytes: function(t) {
            for (var e = [], n = 0; n < 32 * t.length; n += 8)
                e.push(t[n >>> 5] >>> 24 - n % 32 & 255);
            return e
        },
        bytesToHex: function(t) {
            for (var e = [], n = 0; n < t.length; n++)
                e.push((t[n] >>> 4).toString(16)),
                    e.push((15 & t[n]).toString(16));
            return e.join("")
        },
        hexToBytes: function(t) {
            for (var e = [], n = 0; n < t.length; n += 2)
                e.push(parseInt(t.substr(n, 2), 16));
            return e
        },
        bytesToBase64: function(t) {
            for (var e = [], r = 0; r < t.length; r += 3)
                for (var o = t[r] << 16 | t[r + 1] << 8 | t[r + 2], i = 0; i < 4; i++)
                    8 * r + 6 * i <= 8 * t.length ? e.push(n.charAt(o >>> 6 * (3 - i) & 63)) : e.push("=");
            return e.join("")
        },
        base64ToBytes: function(t) {
            t = t.replace(/[^A-Z0-9+\/]/gi, "");
            for (var e = [], r = 0, o = 0; r < t.length; o = ++r % 4)
                0 != o && e.push((n.indexOf(t.charAt(r - 1)) & Math.pow(2, -2 * o + 8) - 1) << 2 * o | n.indexOf(t.charAt(r)) >>> 6 - 2 * o);
            return e
        }
    };

    (s = function(t, e) {
            // t.constructor == String ? t = e && "binary" === e.encoding ? a.stringToBytes(t) : o.stringToBytes(t) : i(t) ? t = Array.prototype.slice.call(t, 0) : Array.isArray(t) || (t = t.toString());
            for (var n = A_2(A_1(t)), u = 8 * t.length, c = 1732584193, f = -271733879, l = -1732584194, p = 271733878, d = 0; d < n.length; d++)
                n[d] = 16711935 & (n[d] << 8 | n[d] >>> 24) | 4278255360 & (n[d] << 24 | n[d] >>> 8);
            n[u >>> 5] |= 128 << u % 32,
                n[14 + (u + 64 >>> 9 << 4)] = u;
            var h = s._ff
                , v = s._gg
                , m = s._hh
                , y = s._ii;
            for (d = 0; d < n.length; d += 16) {
                var g = c
                    , w = f
                    , b = l
                    , x = p;
                f = y(f = y(f = y(f = y(f = m(f = m(f = m(f = m(f = v(f = v(f = v(f = v(f = h(f = h(f = h(f = h(f, l = h(l, p = h(p, c = h(c, f, l, p, n[d + 0], 7, -680876936), f, l, n[d + 1], 12, -389564586), c, f, n[d + 2], 17, 606105819), p, c, n[d + 3], 22, -1044525330), l = h(l, p = h(p, c = h(c, f, l, p, n[d + 4], 7, -176418897), f, l, n[d + 5], 12, 1200080426), c, f, n[d + 6], 17, -1473231341), p, c, n[d + 7], 22, -45705983), l = h(l, p = h(p, c = h(c, f, l, p, n[d + 8], 7, 1770035416), f, l, n[d + 9], 12, -1958414417), c, f, n[d + 10], 17, -42063), p, c, n[d + 11], 22, -1990404162), l = h(l, p = h(p, c = h(c, f, l, p, n[d + 12], 7, 1804603682), f, l, n[d + 13], 12, -40341101), c, f, n[d + 14], 17, -1502002290), p, c, n[d + 15], 22, 1236535329), l = v(l, p = v(p, c = v(c, f, l, p, n[d + 1], 5, -165796510), f, l, n[d + 6], 9, -1069501632), c, f, n[d + 11], 14, 643717713), p, c, n[d + 0], 20, -373897302), l = v(l, p = v(p, c = v(c, f, l, p, n[d + 5], 5, -701558691), f, l, n[d + 10], 9, 38016083), c, f, n[d + 15], 14, -660478335), p, c, n[d + 4], 20, -405537848), l = v(l, p = v(p, c = v(c, f, l, p, n[d + 9], 5, 568446438), f, l, n[d + 14], 9, -1019803690), c, f, n[d + 3], 14, -187363961), p, c, n[d + 8], 20, 1163531501), l = v(l, p = v(p, c = v(c, f, l, p, n[d + 13], 5, -1444681467), f, l, n[d + 2], 9, -51403784), c, f, n[d + 7], 14, 1735328473), p, c, n[d + 12], 20, -1926607734), l = m(l, p = m(p, c = m(c, f, l, p, n[d + 5], 4, -378558), f, l, n[d + 8], 11, -2022574463), c, f, n[d + 11], 16, 1839030562), p, c, n[d + 14], 23, -35309556), l = m(l, p = m(p, c = m(c, f, l, p, n[d + 1], 4, -1530992060), f, l, n[d + 4], 11, 1272893353), c, f, n[d + 7], 16, -155497632), p, c, n[d + 10], 23, -1094730640), l = m(l, p = m(p, c = m(c, f, l, p, n[d + 13], 4, 681279174), f, l, n[d + 0], 11, -358537222), c, f, n[d + 3], 16, -722521979), p, c, n[d + 6], 23, 76029189), l = m(l, p = m(p, c = m(c, f, l, p, n[d + 9], 4, -640364487), f, l, n[d + 12], 11, -421815835), c, f, n[d + 15], 16, 530742520), p, c, n[d + 2], 23, -995338651), l = y(l, p = y(p, c = y(c, f, l, p, n[d + 0], 6, -198630844), f, l, n[d + 7], 10, 1126891415), c, f, n[d + 14], 15, -1416354905), p, c, n[d + 5], 21, -57434055), l = y(l, p = y(p, c = y(c, f, l, p, n[d + 12], 6, 1700485571), f, l, n[d + 3], 10, -1894986606), c, f, n[d + 10], 15, -1051523), p, c, n[d + 1], 21, -2054922799), l = y(l, p = y(p, c = y(c, f, l, p, n[d + 8], 6, 1873313359), f, l, n[d + 15], 10, -30611744), c, f, n[d + 6], 15, -1560198380), p, c, n[d + 13], 21, 1309151649), l = y(l, p = y(p, c = y(c, f, l, p, n[d + 4], 6, -145523070), f, l, n[d + 11], 10, -1120210379), c, f, n[d + 2], 15, 718787259), p, c, n[d + 9], 21, -343485551),
                    c = c + g >>> 0,
                    f = f + w >>> 0,
                    l = l + b >>> 0,
                    p = p + x >>> 0
            }
            return r.endian([c, f, l, p])
        }
    )._ff = function(t, e, n, r, o, i, a) {
        var s = t + (e & n | ~e & r) + (o >>> 0) + a;
        return (s << i | s >>> 32 - i) + e
    }
    ,
    s._gg = function(t, e, n, r, o, i, a) {
        var s = t + (e & r | n & ~r) + (o >>> 0) + a;
        return (s << i | s >>> 32 - i) + e
    }
    ,
    s._hh = function(t, e, n, r, o, i, a) {
        var s = t + (e ^ n ^ r) + (o >>> 0) + a;
        return (s << i | s >>> 32 - i) + e
    }
    ,
    s._ii = function(t, e, n, r, o, i, a) {
        var s = t + (n ^ (e | ~r)) + (o >>> 0) + a;
        return (s << i | s >>> 32 - i) + e
    }
})(t=undefined, e=undefined, n=undefined);

function js_2(t) {
    for (var e = [], n = 0; n < 32 * t.length; n += 8)
        e.push(t[n >>> 5] >>> 24 - n % 32 & 255);
    return e
}

function js_3(t) {
    for (var e = [], n = 0; n < t.length; n++)
        e.push((t[n] >>> 4).toString(16)),
            e.push((15 & t[n]).toString(16));
    return e.join("")
}

function decodes(code) {
    t = code + 'WSUDD';
    x = "X"
    encode_str = js_3(js_2(s(t=t, e=undefined)));
    return x + encode_str
}


// var t = "/fe_api/burdock/v2/homefeed/notes?pageSize=20&oid=recommend&page=1WSUDD";
// var tt = "/fe_api/burdock/v1/page/5a4384858000862471d144cd/goods?page=2pageSize&=10";
// console.log(decodes(tt));

