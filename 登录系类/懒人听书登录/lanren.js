
CryptoJS = require('crypto-js')
function cryptoLogin (password,token){
    var key = CryptoJS.enc.Utf8.parse(token);
    var iv = CryptoJS.enc.Utf8.parse("lrts8621");
    var encryptedPassword = CryptoJS.DES.encrypt(CryptoJS.MD5(password).toString(), key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    encryptedPassword = encryptedPassword.toString();
    return encryptedPassword
};


var password = '123456'
var token = '31dfe6d5974c4015'

console.log(cryptoLogin(password,token))

