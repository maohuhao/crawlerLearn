const crypto = require('crypto');

// sign 加密
function getSign() {
    let timestamp = (new Date).getTime();
    let l = 'fanyideskweb';
    let d = 'webfanyi';
    let e = 'fsdsogkndfokasodnaso';

    let g = `client=${l}&mysticTime=${timestamp}&product=${d}&key=${e}`;
    let sign = crypto.createHash("md5").update(g.toString()).digest("hex");
    console.log(sign);
    return sign;
}
function getText(text) {
    oldKey = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl';
    oldIv = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4';

    key = Buffer.alloc(16, crypto.createHash("md5").update(oldKey).digest());
    iv = Buffer.alloc(16, crypto.createHash("md5").update(oldIv).digest());

    let decipheriv = crypto.createDecipheriv('aes-128-cbc', key, iv);

    let plaintext = decipheriv.update(text, 'base64', 'utf-8');
    plaintext += decipheriv.final('utf-8');
    return plaintext;
}