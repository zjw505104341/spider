

function m(t) {
    CryptoJS = require('crypto-js')
    var p = CryptoJS.enc.Utf8.parse("jo8j9wGw%6HbxfFn")
    var f = CryptoJS.enc.Utf8.parse("0123456789ABCDEF");
    var e = CryptoJS.enc.Hex.parse(t)
        , n = CryptoJS.enc.Base64.stringify(e)
        , a = CryptoJS.AES.decrypt(n, p, {
        iv: f,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    }), i = a.toString(CryptoJS.enc.Utf8);
    return i.toString()
}

var t = "9ca17ae2e6fecda16ae2e6eeb5cb528ab69db8ea65bcaeaf9ad05b9c94a3a3c434898987d2b25ef4b2a983bb2af0feacc3b92ae2f4ee95a132e29aa3b1cd72abae8cd1d44eb0b7bb82f55bb08fa3afd437fffeb3"
console.log(m(t))