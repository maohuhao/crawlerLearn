let JSEncrypt = require('node-encrypt-js')

let encrypt = new JSEncrypt();

function getRsa(public_key, data){
    encrypt.setPublicKey(public_key);
    return encrypt.encryptLong(data);
}


  public_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCs4oTSnuLDyCLz5rfvrPYqPh5vxyXoWqU1LEse1AdWhW/bjpfJJ/a/GpsvHY+/+wi8U8gara1tNLTOpoEV+jUTmiYZ4korOXLvQOoElv6UbscGQypZV3RWgJTTSqMcdIbrRBbrj3Q9PFRfPQHEH2kYwkwc2rvABuWrk7aRSkv3mQIDAQAB"

    data = {
    "inviteMethod": "",
    "businessClassfication": "",
    "mc": "",
    "lx": "ZBGG",
    "dwmc": "",
    "pageIndex": 1,
    "sign": "c9931b3d8f222bbcebfacde8fdd0fa60",
    "timeStamp": 1680860135511
}

getRsa(public_key, data)