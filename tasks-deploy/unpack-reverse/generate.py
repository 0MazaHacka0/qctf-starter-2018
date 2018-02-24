#!/usr/bin/env python3

TITLE = "Новая технология защиты ПО уже доступна для тестирования"

STATEMENT = '''
Активное обсуждение системы началось на хакерских форумах несколько дней назад.
Как утверждает компания-разработчик, в их решении применяется несколько уровней безопасности, благодаря которым секретная информация изолируется от пользователя.
Любой желающий может удостовериться в надёжности системы: авторы выложили на своём сайте [пример защищённой программы](/static/files/wwsetvnmzgylrqo/%s/protected.exe).
За нахождение путей обхода защиты обещано серьёзное вознаграждение, однако разработчики уверены, что способов взлома не существует.
'''

task_ids = ['fd16ead51a955c5e4647a37b84d238e5', 'b0f7c2984bf8d5f7e23e1bab9b7d2072', '3f5b4631681a80ffc235c003f51d2188', '9a501c5bdf2bcb6dcdc23d9c2fd92c7b', 'fd8b4ff6c87fa2b3d526c7fb9bc5496a', 'a3682e9d00d193f26662087afaa489d6', '8fe6b3617a974eda03cab943c2884083', '58526d06208c49536551c58f5b72ce79', 'ffb23f52bffe80362dfd6bfa2f574fef', 'a1ed3eadd7b4b2ef1a3d8e3cdaf78b1d', '3b067402964fa998dfd05c6a407244f1', 'aa41258e8bc6802f06bbef4ead59b78d', 'f0f83182269ffb1ab905929c43ec2b6f', '65f02c440abc38af09ec93fa1f78a07f', '026aa1fca0bb13ec567935f4deac0c40', '10c1dbedbf9d569c0fc227e084197219', 'bdd31b387c3b0b699784c6c86c1da658', '6eca4c7dc3f0ce149d0bca4e92d3f4a6', 'fcf3f601f78ab02001c39d4b5996b74e', '56e7f01749580b6c3ddf4cd3cff31126', '6d12bda06da21d941dbaefdc2930c9ee', '823c87f0add06e70872cdfbb5ec1b8a2', '48f120db8c6e874846e57b4577e75505', 'a2a1de6579b7ab8276348b93a649a201', '074f0bba5efaa8d55a68176c8f43741d', '98c2aa83e10d82dcd99af0ea5d012b0a', 'f7e57ecf33436058c6563ea7918257f4', '0ab3af16bd64716665d8278587ac4089', '8dc30b7c53c5a6b759903d8992f86d89', '819e2d23730741fc7cfb8051597f21ba', '54f29ceaed2e48a3c1d2bb86aa5aac9b', '2b593f7ee4daadb72453c88340a1872f', 'ea23ff8abc4f1890fc229534642ce18d', '20b09fab44c1a9ec1f6b0f0ecdda6c40', 'bf6582fd6287b61e736c105a2073e74e', 'f2fda8c609f3318af1df310e0bbd082d', '99e74acac5ef98622d5c6cc4d627cac2', 'e5a7bf2d1088b98921ba09ed7043a7d4', '86a35dd49254a194b7d2ec11bd2b1c3f', '7324c01702e665555305b65dc957e6ed', 'c297133425fc8065911027c71d3e0762', 'ebeee3ea6d558cc611a4f9a4f1e9bbfb', 'd9f43cf8dc6ecb7df4c55a6e30d1309b', '68ebf5393cef768769b61c512595bd9f', 'd7744228dca1fb90706e6b2ea81a03b0', '21c5eb0b8620fe99f65fe2015348016d', 'a48ed32385a386345d330d84381c2ed5', '37a0979b6604e53622ee0207a0810197', '6de0189533920d8524eb56edc3929789', '4550cab0f5d47e90fb9389f1079c6dd8', '943c464c1764047ca55347e4d3c2fdc5', '1d56f7f7b038148e4dc7d4ff73e5481f', 'a2e2befd32d74bd49821bc6adb0c0711', '7ece819edcfd99b3d9c46ccc86ac8005', '842ce4a153305d3661ec1a93c29edf93', '730d4e94fc95b2aa3271e2e9a64a9910', 'c9e890a3933bc121e9fb4f85cb59484d', '1fe8f4200858782d1fbfaf9b9c736b04', '3792f61c7fc52064208e1601cc4d31e9', 'e3921306399877ed1bcdbb9ed7a122bd', '0805968902b5c2ff6a934a342138c8a9', 'baed3a055f61b9a58f005c447f5b745c', 'dab9e5d26180582b6b8f854ef0272591', '494d19d9e6212631f8a4d7bbad12292c', 'f7bbc99a3930f824fd393a9c3b94f5d9', '43ffa8143a9429124ba76ed8534ef1bc', '942bcb1522f7b710fd7b59b48eb69b4b', '2ae5186c93c8621f6dcabbd672e64b36', '69a14bced8867d94a2e49f67f8f88fc4', '4ecbb87aaadc2a05e6d05cecc2a2468e', '2974e00fc4f0b6e0d6fce735bab7adf1', '041392ed2600093cca9d40866aae6d86', '473acf926a305d6fc7360c3d6b76e26e', 'd6395c164529da65fe96661481a6be04', '8d7dbd9806956020ae7da383acd89806', 'a7e88e1f8a25981af31de3921bfa4c91', '6e29d1c5e8d615a9d63553e08a6dee6f', 'd9666b9f3230da59c3e97fd837c6586f', 'b644617a6d811e5eb27a2ded23bd973f', 'd7b0dc171c689bcf33c95949a6d36ef6', 'aeea710ef5d33802e2a664636eab6c11', '05d006c5c8d40163797afb4c6706306e', 'bc1bd02d020b7b0d59c78b4b40db8707', '9278dd7f53c376260f8f689a68e88922', '3ea0f90dd619518bb6f9bb0d392feaf6', '88553bf6f29614f59b32e93c9323a3c3', '8ec531eccabad51fe55bafcc656c1988', '31d1df86f5616a036bbf0662b5fd9ca9', 'a14fd87220c8120d543ce2904a7ef3fc', 'ce44789e8e878e5f03c71ab4ad6c76af', '42d0e4c1fb7fbff4bdd10a4dad5b98d1', '0043899111936b87f5a2836e44804c59', '93def4f911cacfaacc66dc87e11c5384', '49b7faa73525b61a9111199fcf663311', 'ae43943f1d6ee51678fa43983ab19e77', '5060c85a256e3eb4b0c36d90c20c05a0', 'dde16bbd6175484b584caa3969bcdf4c', '39aa44965a7b8852cf39981d01689744', 'c39e995f5bd82129552544a48ca833c1', '2b93d526bec18edaff28e632d339a1b9', 'da02ac14b7c5b852a49db96d5fbd7d1a', 'a25fa7697d92f2072a0c71cc5ad2ed4b', '5d16b02a72105d13db5eb65e80c58e0a', '399a98774ced52ad4620b63ca8430be4', 'c8c1b97d67cdc316df6c079e9e53392f', '74355ddd56b382f45e0c40b3c8ec902f', 'f6ac7411fdddf12b5376d003cb219d35', '856fc5a24db08035e1a2bf795aaa2bb5', '348458d892def25aa0936a4417e55353', '121d1946eb6356e0f2d7894f0d7a7e75', 'd7b8b4a7f723eaf9f8ca8c711fdb9867', 'e74e4fc05100501e84fd6040de4f484c', '70d1bb8861195d81dcfb84125df23b8d', 'd3963b0c4540be0842b1fa2771b47f70', '1d40df06159e86e652d093cb53c2ea25', 'e4f41626ae5c8b37cd5706ddfae2cb58', '5af16db6b1703506ab3c970b6327c1d1', '73b036548282bd650518f29db7563494', '038655d2415f4883b81b473505b6dbb6', '7ab20884699efa4ebde08dd947c1ece1', 'ac840c6cd4519ae79c2d79067dba7791', 'a8ff24340c25223b93a346840b278601', 'b23bab25f5714a44fecfaaa0c815a0c1', '4b333ebb80418ba299042eefe18d91e0', 'd3b1fdcc7de7b532dc99f6ff49ead83a', 'feca34f155debce8b4fde0d55957ad54', 'e38bd630bb786059dbfda6ad339b2020', 'c995337ff23431ee85c60de5b204f828', 'ec0c843bb67b21450c1713341bccd36a', 'c432ae659e889e0d40ebfd94689ce5e1', '5ba0a9c677883231a30840adb1d3c4ed', '507cae1a1174a06c048502909ff7de22', '73936ae5c02d549e84d51c080829f930', 'cdc8a838c62b53e0fcefa6ae95cf11db', 'ffc5a29c5035ab7a2360fa51e864c266', '838eaf0203332120b10e1166e7030015', 'e46089ad271e466adf8f2fc2ae1fc3f0', 'd76507b400902920c5264a378bd358d4', '8a72a76db511dbb6df990b2ff0c72b28', '668e02a70f17e730b32dea316538b803', '9bb615990d7a138948abb8dd138fea33', '576e356fa2c33d60aef7a3a19e8f386c', '0fdf45b73fe5b94cda8dd51f0d5626d1', '843de736fc2e4c41d25921a2630ba895', 'f4f5f217a7d05a75e4c63c23de55461e', 'd85e2e3dc538c66ebc4e8f887070bf14', 'a5282a485f225df03e1af515966c2e2b', 'db61baf8cce78430153ff618bacf24c3', '2c43554aa65dfdbcb9a708e030c8eac0', '5a103f802b75c6d474e60c3172821957', 'b34c7f98ec06d266a0785975f0187039', 'dc28f287b953104b314a7e5acc42c288', '3bf17daa56c8d32dfb2d03a8fe8e15fe', 'e0a838163a4c68b502f41083cb0a1983', '5c10f6ade073f490fdf8bc71b189011a', '0b63c6c7046cd9eca873fc8fc8cfa5e9', 'de03a799d2b4edc37cf4a30e5c1dcf06', '0d2c691d3647ed07eb7da26f2c7195f8', '885988284c5bcf348c2a267da69a5eee', 'e9231594117e7f80a0eca9f086cd995f', '91918f04c0e5b341f86114889cc997af', 'd9f0a98757d5352e04057c53ed3d6b0a', '5aafdd615fd062cda3a722ff0e364cc3', 'd791ee045df5e73c194562bff9cefec0', '0f0ad130b33f3a0915c5b9f756385001', 'c6c5ad6b32cbefd1ecfbdf00e908e07c', '96535c5e279d0882f7efffcb193314a5', '01dc02052610888c328fa5970828eeb7', 'b0825fda55aa0cfa69356cfc086755da', '472aad770334341f6c6e7949ae7455f4', '2bf7039d8e8af1af9f60740ed1acd86f', '1ca73a6c5d195ab5b50a34b344b26188', '577cee897263173e9c0cfd3ab0b26fc4', 'e14c4d521a1c99fd69c7504e62bc6550', 'e921c33d374b9b6834edecd0d5ef1f29', 'cc966b8ac8b757e99d91bcc6186f8652', 'c96fdac63c8258d66b3286ec5f915d56', '04f844455c225b3282048e280639aa6c', 'bf578fde79f75693075fdda6ac323b47', 'e2e886437a0a09059f67214cd6d1d7ea', '1852f9540174774e0b375ad1199f8c33', 'c926d7017425f54a5f27f4920ac1e021', 'c53d27be9da4f2c8c39b38a80e93494d', '717ac7e996674c9530bf12e3db246e58', 'c0a9bc61ab611897988983748e50f3e5', '31ab4811ebaddc70eb6d0c7f7568ba89', '734561f6627fd6a4a353095c92ba2f25', 'dcc6e68f6a4f646e10fc9a6d927a80ef', '293d321ef9a5afdbc811a56e49bdc7ef', '81704876a415b87712aae8b51515ed8b', 'e6b73e2f36136bdc1100d0e8b99bfde5', 'ba603cbe0a41845adc7406251b9f40b2', 'd964d21ca3018f2ddd87d12c97cde722', 'a369b0e2b6d7c7ce05c2788170fbb253', 'cd4d769f982e636ddea762162252fbe2', '3120a4708613eae53d6ea84ae769e2af', '589331d85cc6095da96ab6c48b009f0e', '9fcff2c3691052d65a366490e1b11b9f', '77d7f69bce753062987d5d431bdfb63d', '6f4ccddfbbd468554a9bd8a2352b4115', 'f48954e9e37fe6c5ce996e52bd721fee', 'dd4ee5cdfc800b3e76f6cff521816ca2', '296b655ddee8c8f14f0a5cb6cd77c0d8', 'c25397417edda840bba21abbbbadaab2', 'ab768fe08c1ecd058b2b6176976d3383', 'fd92fc7bee112b2d9415961bf779af61', '6e9fc3ba6533f6bf6bbb40980a4e4a61', '953243dd6411c1ee1c2c569cb38a9836', '968abe53c19c0d37e1472bb23640158a', '32aff748b9306b10d4325646791e8bcb', '20f51a30f90e231716ee0f3c314cc807', '2fea2328764b99b4ab77951a0df95aaa', 'acfff4731886f88d279137a9ce66ed46', 'cf4eea9d0e46af6ad70d0db0afc856b2', 'e4af4a6f4af978ab80b78527037ab036', 'fec9e3fdf30044c962dbc4cc55646d48', '1b9d12e35f65938bb8e3a062db8ce44d', '4c31a0a6fd4a289f21874c24543c38b7', 'd766533d131390ff666d238eddc962fa', 'db5bb99a0d312a177dbc6afaa7c07743', '0df83f162d91d58fd8c3c50e9ff9b4d7', '0db2c7b4c1f8e4e6e917c49b4f977c27', '8b40000c05a203f9c3d554f8054b9e8f', '66173c7035366a3e0616bc1bc3b9248a', '24df48c108d59e0b3fdbc1826bacb0fd', '2f381478210b0abddc4efa4dfba35ec8', '0f15da5b871984f43f2247775fe1597e', '3751730cc6fba80ae7ebc21153159d04', '106da3ea05a8f551a2c5bebb91899ac9', '805df018500b9e0c128dc444f59f68fc', 'c1b217b3ad26653d1e0b95204c9360d2', 'f9925970d7a5e7113010a5f4b0b4d9a1', '4d80825329f0b9bb460d9d81d7ba11b5', '0bbda0cd2ebafd26cb5c48d388460afb', '3ada36a60001cc36d43853bceaeac7de', '699fe2d062b97fad08ea29aa14f6beb5', 'c4ed1b95241c11d15744ee4bd201be74', '2814ab35dc4ca993860998bc51f50fc9', '7894068f476439fe698dd24fd8a66ea6', 'fb1efce108cb883b14f282e609c1889a', '4f7d3ee606540d63085f45547ce59015', '52c46381e1cfd65a67afc6f4cc079ac5', 'c4a6d4df9fbcb4f67f0808e2fa2edc94', '9b23ffb51e3a65d2d3a20810483f5699', 'bea1e8b3e72e9a67ca3163d52cac5d6b', 'baf306d8268b4a1cafeb99dcda91aee5', 'c37903b8802e30b7f078ac7c37e8f01c', 'e2a1a55ba8f08fa0b95a87c902cb50d3', 'f0e4f0a532c7f16599d34e583565042c', 'ec75b64b66d2a9b4d96b857e72c15237', 'e7b5f0d8d6e54254a2fa3769c74820a6', 'b695e730ddd05d24d10c53783541eada', 'ea9230105da4158d1e6423ccd9ae3efd', '8c29f6bd5e66c17b59055ffcb6ea87f2', 'dde9a41d2afe1ec2ad12a47fb06d24c7', '6b2f41318c53ab5466a7b615471cb653', '796ec28a795f2906b374811082f5fa11', 'cbb9d2ac0cb2d0be1811352b1c889591', '6f24cab77c04dc5ff05a655ffd472e47', 'f13baa4476163efd25db337d55120213', '23da1af339c3040237c8f0d101aece18', 'ad2ed9a9489a698114af963de9d49c36', '502f9437ff291f2c8a534a39bdff72b6', '471306900add2b602f2a0de6bb8581b8', '5d13380d00e49bab34089ac36175bfd5', '0cb7963e6fbabeff4e91909fcf1052ee', '4f984c644985a95a3b82306194dfd9ef', 'e45b0febb82d4391dcc5562e62bca163', '229bef7f22ffb158e4ac462f1163bd3c', 'e886e0e68124fe2ca48c47410f9b4f4d', '510820d4ac7c317f4d54691f4f684e61', '5b2a608abaad5a32d4da9fcf8dfe88f7', 'd0105579202790d279f768c04a2aea96', 'a5b120541e3f7f469828504671f2ea29', '13b3898c878e0d65dd01b79a62b8599a', '6aa42befa01ab56820d959528034538c', 'dd55f8035c4ac8f001b7b2cc515e96fc', '923b12a5fa74397f04253bbe0f209aaa', '9b96d9f3f86c2292261f6264bf18c60b', 'aae6d35e2a490ca4bf92352bad9d275b', 'cbd932302545cd87a1309c57c7fd8e5a', '3cdf640a89c97628878934c1305f764c', 'ef8c0a06d9425e05261bad97095ed049', '21302ae557983f75fecbfd0852e14fee', 'da8909b7add8b0d49c09358cde30b039', '0e3d0a3ca181c48c87573abf8a3b2e0d', '2875cb86033515442ce7a29dd2d3a4ba', 'c1d0d65621ad1675f73f6beaadf7b8b5', '1d02d4a059092ccf0420cb3782704154', 'e947c2d3bba3ece0889e806664ae9580', '8d986fc9b25fc4fb6ecbff64ef0936bd', '5207a9aefb4cc17ec311316af23640d0', 'e819bd05b758acda7df8345cecd9907b', '92e830f580719b47d7e3613e3edca273', 'b310e268d7bdcf56a399a850bf376e83', '96ccd68f840ed1e3b5c939ac9dae62af', 'aa63680eab769e6a4eb70aae2ee26598', 'aded64452c7a7e76b01e23b33651cdb3', '23ba1cf1bf75a0ffbc356ad217350d41', '9d92228688f436e141885549d499e8e5', '82f8fd70f928e5a777093a459bb57c80', 'dc7de1f0332ac164c8256150af2c9493', 'eedfc0505e7064684b2a8ec5d7a0981b', '091ffbdccd9fed0b7947f202f70dabfc', 'e2c03509f9b4238fd98fd6648e4952f6', 'c109cec28dd5e9722b5a23808441c49c', '290d9bf2841d0eef8ce3c9bb9401ed0e', 'b7743e5cfb3cf437222db8fae2428235', '70998965294371566a95d4ac5b46be37', '3f4ddbe3c7be6b7dc15aa951922aac10', 'a2cab25420c16351270a8156195f5f2b', '81faacbe1bc115ec76f8caa46e0bacba', '93680f97bb440b9dbe5b1e70ff3c3b5f', '96782efbf6641fdf75baea6f648c9faf', 'cf95436216b0be618680273722464c26', '20c96cad4776496184393b0aa332fcc8', 'f716ce432da6da0ff4063e278bc987c0', 'd7eac7e5bb5df6fbd8b9bb5e5d64091b', 'e3548d0ff229beb5c903484a91513d7a', '6a0543eb34f658b5b32f3066cd476eb3', 'b491604e9075224900cb2aae6bc13de0', 'dcd9c1745b028ed2b930572b6131c6a8', 'f065d37d2b4a95c50aa0ad798ef92748', '711758c240f80c13b91a575c69307eb5', '1dae3822e7409a8bbce2f3a852a5ecff', '0aa5b649e21620d2d8f4246063423d32', '30eb04e896948f3c86abc991212acec0', 'e27b1bd0774c5b8efcb5810a3a2c5b16', 'bc840bf2dfda8812d33c0eee6b577e91', '6df7bc16b75c961a64d5065f5504a40e', '50f179583910a0cccb16f2d2e404fc80', '0ca50f1274df1bbfea62ac932053c03a', 'e526f6682c4476bf3f84a2b62728fab3', 'a47ebe755c6059ae73ce535e77bf2399', '1ecece8097499e97b3b275c61a0de17b', 'e5f5263acbf793b4f1a56446e10cf815', '156e96719c718c7a80e6530d018d5242', '78702d57e8ca83290b5b8e2b7e3774fb', '2161df76e88db52ba79f999caeeffde7', 'b1243e32099f7dbe2e1aef32d630a7e3', '8e5d968bd5a66b3f11b5f6e9d4934c04', 'c144448cd025c026fc7a83545146303e', '351326f8025f72d93c08d234cca6a229', '6127d3bef33f862b363076d1e9015932', '39117f0c68080253ecec4b31acc307cd', '527d3da139c6577df78cd7433cc4cc8a', 'eaeda8ef1b27f691d700817025fd3c3a', '0eb52c9dc265c2cd0faafb1020aec606', 'c79c1f3f97407e93b757a10256fd6bf3', 'fc4f872a766db8977fa8af297384aba4', '892f733a189efc8cf8a238a2b9bd809f', 'bdaf4c2386ba1a7de1bb23a406be634b', '69971cdcdbd13c02f423adddc5a62b8e', '0641cb9fc6280a7db295c85b865a26ca', 'e59feecae3bcd99795e45103c12fe665', '19dbfe5c420102aadd8a2c63294ba630', '7d8543c3ad7f1d103b3dd8be79b25f5f', '6a086ad012a921764dca7223dc73d3c4', '9f7f24e17bb47b18fe649326616818dd', 'f7b62b68b005846477953e205b69de82', 'a409a7606f161814fda1bd6d0ff99574', 'b8e0d29323595480bc4114fab08750cf', 'ebd81596b48d41972100e097ede3a555', 'd871f791f7243eab42a5b70f8e17769d', 'c394b568894816bc08f3c96b827796d5', '125b28013778ba5c59d1ccf67ea9b12e', '2b4260d03e9fc1398b422b5b91699b9a', 'bf47dedf4a7f6847e1936279f6d40367', '85fdd4f6600810fc4f2e6b98ac4a834f', '9fe98950c080fd9ddeed09e7e3d5bd0b', '3378df1c1047a04f624f64f8b2f0b8a5', 'e52b97ea0354bddba5a297f3e876936f', '00121652a75c10d545a9468b70c1cdfa', 'a745f73ff3db6186c17bb90eb1a2a8f3', 'a9a85510aea298f4db97cd9a2063ed19', 'adb8f6c5b894a4cbaf9c312f5b2489a8', 'fb32eb2849f90e19682e840ad7a44fdd', 'e5b29838be0116df4774114e185b7f94', '5516705508b8a16adfac774995bd9d24', '29e5268cf727b3889286869fb19c11f8', 'eeb27a50737bc78f1074536214a86da0', '05f4b51673119d7c999eb7b66f0f6079', '7d0f150c1d79f3e14c9823ad01676677', 'eb86dc6f2dad3fffa6937430e4557feb', 'b9d18582bc5177bd14d0db5b0f6f337b', '4e0ce925d99d0887d278697f391a8602', '70677aa8d30945e379ce888956516a6c', '11415f485be80a7f7324dfeac2a31e9c', 'e90dc7a7ffdf4d6a4319751f74ea0a24', '7d454dce14d0d3bf510849f973eaa867', '07dd59dbb0c5298436d47c6187451fab', 'c50f6e30de3cbf27a9b718b230eb5efd', 'f7a19ad62efd257352859a65fe3ffa93', '90abc1a47a2c7fd65d49502bf4d2ee36', '2990531143e73f4c1d3b32dfb31b116a', '2b458369790a2a5a2801874e18159239', '46ae8a2619b20bfe05ec68299a9e40d5', '07600fcac102e07047d7ccf12bd9f184', '7c47cc823db2deffc397c666a3fd7781', '185dbbe110d7d369eee567d358def012', 'df3347fb110cf909d0038ddcaa153a88', '6f450783540094e56acd9ad0c2e7b9a8', '844d70fc5582e2418c74fe0038d63bad', 'c9d2852dea413ebe9750d9ccbfcc1473', 'e1ee0e21aad0e386f54cd75394a87df4', '854145847ae6ed033d9cf94b1e7eb2ac', 'ed24df1cf8375b268ea1b962b938f695', 'c73e9178a10425ada021679766ac472b', '6591d581f50644d04a008b1b91b85a82', '15c7b0f57d78dc5ff50bea157d323ff9', '8cc44a1092a8324c2ccca8f9316eb396', '310273b3a44b9ec493777e4d574938e4', '50056f8c9ebe7d674dbf49a481215f58', '5da49cd058a2817a9612a8d14a1f5273', '4a7834fd513dd0e7e944014963c6c121', 'f2652a0cb3d70b90e23d1a734792928d', '1ff968ec04afb95c078a722ebf649f2c', '70a119d97db8bd276319e594e07ed670', 'ca6fb466c339b8bebb1802397d74c2f1', '984ccdb63c0e9120e3e6ae4589aa4c77', '58f3c6e4f0132fddc3c1761091b2032b', 'd98336158f1e9108b802360d05bd1e69', 'ec65bf7513f090945b0bf83c0c804e69', '2312d456250985e5bb4af96b33fd7284', '15fec1254a96bb911e07c947baae95cd', '6259c152b5097c1e297701f048dd233c', 'd9ae3b9587c80a071ddec68a9a131028', 'f92ce5738ca46ef0c78208e59679fbc3', '6c7b9ce83e3299ce46a3ea817371dc1d', 'f0ffa51a10c2e169f82e79e81f1c8905', '6ce445906f8595003f2172bd9f9c470f', '6b1c022859c346848fe62cc2d308f5a2', '5f2f25014827e90a53644e6a4021453d', 'dd6f4ca9d656ba11669f170e2e5d9b45', 'fc68b4d1be24be7276e1f6e5775f19de', '50e68d3c537b28c2d1f84b3109eb086c', 'ff13051e23342bd95adb8bbb894e2d98', '0329898c5d6fdd7e32751bacf072bf52', 'e2f2a1b2b841d274e9ea606c47f80594', '3034da7ab25afadfd6658bc83d9184a7', 'ead7dcd5627703322cb802d9982dc4e5', '9c6b9694dcbe54e0d54fa07c4b024965', '0d570b30e9ac4b7575901aca6c010709', '6dd1cd609497cc5e4f87be2ab451117b', '4987dbf6fae0d5cfa54265ae6a087c0e', 'fa736630ab6e134f5c53e1d6be0dd1d5', '7794e159bee02f3dfb197da1a47ec018', '8d7fc712383474670f237f2b3cd8a033', '33e3f76bd4580731f6727e43818d6a0e', '680f418d9dbf583c41b5542255101831']


def generate(context):
    participant = context['participant']

    task_id = task_ids[participant.id % len(task_ids)]

    return TaskStatement(TITLE, STATEMENT % task_id)
