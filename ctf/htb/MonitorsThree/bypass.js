const CryptoJS = require('crypto-js');
var noncepwd = CryptoJS.SHA256(CryptoJS.enc.Hex.parse(CryptoJS.enc.Base64.parse('go24rf3kpkwB+MemZPNrloBk4veQRQmlceOs29ZKMEc=') + '59be9ef39e4bdec37d2d3682bb03d7b9abadb304c841b7a498c02bec1acad87a')).toString(CryptoJS.enc.Base64);
console.log(noncepwd)