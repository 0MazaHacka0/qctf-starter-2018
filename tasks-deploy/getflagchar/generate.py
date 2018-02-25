#!/usr/bin/env python3

TITLE = "Сервера Министерства обороны Курляндии были взломаны"

STATEMENT = '''
Хакеры из группировки KXVX заявили, что они взломали сервера Министерства обороны Курляндии и в качестве
подтверждения опубликовали [бинарный файл](/static/files/rrbymaqomnwdhhs/%s/scanner), полученный с одного из серверов.

Файл был выложен в сеть без какого-либо описания, однако 
исследователи полагают, что это модуль, отвечающий за аутентификацию.

Сотрудник одного из силовых ведомств Курляндии, который попросил не называть его имя, выразил опасение 
фактом публикации файла. По его мнению, внимательно изучив модуль, киберпреступники могут обнаружить в нём
уязвимости и использовать их, чтобы получить конфиденциальную информацию.

Мы обратились за комментариями в официальное представительство Министерства обороны Курляндии,
но пока не получили ответа.
'''

task_ids = ['c082818f8f4bd1999d967cb84faf9d1e', '3ef70a50b75965894d84c4fa1df63dff', '5e822e60866d9415c75cf6e272e9e965', '752f82cea780de2bb5cdf9b1807a8848', '8e4929487b335cc2c78f0b2759d6c646', 'aa469c9e9309ea38471c14b986b3384d', '58f722991a89cfe4b888008514df5522', 'ce8ae3f1376399ab7a71305247b15c47', 'a8c1dc02c2c095d9163515e135a70fde', 'c9c5c37b9f5c65653918188744f34f8f', '18aba85a63d4e5eaab22e986a26605d3', 'fc045977a498a5369755b1c9a2103a5d', '3404d9aed78f825a810724b2b51f553d', '316be75b9fe9f74baa58e9b889ec18b4', 'f91a81d28cf9852032cd01b20e9d3b74', '20e47897df157376527a72cb27501d43', 'b008c7691ec4812dc586d10b986cacdf', '637804ad99865852179086110a43f8a9', '6eec29d74cbc2a64b3729ecd43ea1eab', 'f63caaceda8a6395336d710fd997e991', '3f7c42d74cfaff27249b57575f88b64c', '61ac5d0f158c40033c9ec860dedf6934', '53c156930f8aa292391aa37c0211987f', '7fc1c7a1f9b29fdc7fd83ad80e277266', '9a464f8a4c94bc16cb889b715dc9901c', '90e11afdc94530359300366d2c67c5a6', 'ae8c9df986c65d632fc8258edb4b36ff', 'd15378fc27b1dffa42b48d322863271c', 'aa9217d086be5404724b66cbc44c59ec', '0771fa53d6ba0df7c3ffcb1f6229999e', 'ff07b32d178af9546fa8af5cd254058b', 'c838da8a084470864ddd7b9b6223e34c', '1dd567748ee802497d8dcd47f4869991', '917d1e1917f1b58d439ca80cd763c4cc', '47d7579b9250f59e9993c786086865f5', '0f038ac26dd28ade63d7d3e44aa97eb3', '2a24be76eaffff2589acfa306af00d00', 'deb7a114ff31e44da7e1f84b7b7edba6', '53828c0f8f7bff09376b4a533d63a772', '10986ace0bef5b1c213b93edd8e03353', '4a64cbdebb2dc9698f7d75bcbf20ba3a', 'f7da5cedc271e4791501bf2604c55837', '79309ee14702002b7ec0bb4635763c7c', 'c8f1b9c2aee384e1cf0c8c6118565c94', '4684fd6138a637bef3d63f15cbf19b79', 'd4ebb65ad5bda596e2eacc19ecd4a552', 'ebe690f983771768f6409e8864d3d473', '7d08ea420d623f9cfde8c45a5ef0c367', 'e5fa9f79094cb203620ef2a647b61c2b', 'ab96133abd0f86f3bdd7b1b7a69fb894', '00f549edee4da7836915cfab56e7ef43', 'c4091f7f33554616cf5cafad7971e736', '076677ec045ad2fa8b552eb572652104', '99dadb7a8c3f571aa23da864f789285a', 'a26b1ef549eb0c6a1baf4f0562159d3f', '706f1edacaffb913c0c83a6ae530f52f', '6e3f4f6395e0780fc42b6861db689bf9', '42592899147a2c8b5602d7246ef60c67', '1206414a77644ca730c7f278f6a1f3f4', '0f0110f5ab31239c857e6d5353b0976b', '975ffc8de6407d0bf04439fe9589b1be', '5c6eff1c3491c413411bfe5cfb32cc63', '390126258a591dbd9baf3612c99bae7b', 'b7ceec2b018407ba8d3be38c820e2b23', '1c9f23a431e8a4b085d400bb6b0ec127', '3db17c9c832b537505ec6715bcf33e28', 'b691cd9ba27086225534c2b017a0b6b1', '3b165c331f1c754f2db768aecec9ad3b', 'c1e5908a2c44de1ecd737dc1bd20cca2', 'c1c516bcd81bd3b4e0af3a0c760842ea', 'f69716c2ffc5b7d4a491abcc1b220e2f', '5a5f977d71b30598317bde8abafd9d8b', 'eed480f2c8e6dba11f09bc7c0cf45f64', '0b4c1841f50b0fff8c5e4a9195ba28c4', '3a7da865d903b840a64d8ed3aa1f0993', '986ee76d994e766ef5d41e27ffb96c80', '1af07c9c5728348486707cb30ecca527', '821749ea9d8b5339f1821aba26c3876a', '3b3cd88a0efc81bf83ed757ed1dd3c97', 'b42feca5933d42c9684994ee81f3f2cb', '76bbe8a15085b87931cc59ce0d54105d', '10c3772cb7a1983d66596bc0c9e76439', 'f71c9411d36a6c19ca7bbbe89f524079', 'b119daf185c7d2a552cbc24ca198e39f', '2c0c42ce6d4f5494d3aabe4e2e9bce34', '86d632e71bf1ea6fdb9d77a960be9501', 'ef34b1771191331577846dab6a8e8f92', '4cc5b453c411d774af4e285090ca58da', '7fd04be7dd83633bfa0427a07e6b3b82', 'dd3bea11ae7c9863d7e62c96218cb783', '5f6d7a29ead20790f0de4f18686e1bbb', '7f4f5487b00a28e6fd22ad18775a18e3', 'fc3fabb581d353785cbdbf2421a4f275', '3fac535157914d3f69e09a9f29f689ad', '89f50aa6866947469fcddac99e9cd258', '4d28d71748998ca50428458e103b46a0', '07a9338d938157774b4b4d463fa344c4', 'cab37852e021977f0118f8b80e8a493a', '661aad0203839ff21fddfff047d2897c', 'bd72856f0d15302d741822de89416c8d', '127406c3b5466e24c39648fbddbdbff2', '61628dfc5998f782be14e4e73801a94d', '6a281c1935e54cf3a32388ca3b48bdc5', '7b5b316bf07b7d3aa3bf779ff2d1581c', 'b4cb8ff1c46f7a3680eebc76f3e9515e', '7631f557e9a5851289a129d2f62974cc', 'e0b93c2904a667bf96b51998a6958449', '9ee8258b2a6946cfdc14223b1801bff7', '6c95ca87f073bdac9f83e7d85f4de310', '7e23de99e26cd4461bf5cc72df44d218', '8381f8a433ce930df9902aa14ec99ade', '582c5962c078cd057199a9a05c12a2ba', 'efdc4d434d611c35995a79f05c98b773', '59cdcb275277850c927e4e15f01dbe9d', '6ebaed391cd7181bc5b510366d47bec6', 'a5ce139092821ef45a17f463b541e9fe', '02b2474f7e745f1a18161102dc5c9852', '0dbce7ed09ab624e881c884eec08a08f', '9d94200a834e2a8ba9588e3abb55887d', 'a33244b5367a0ac394212a3a8d5a5352', 'ec13f28f9c364b565e97a73f003b2004', 'd7d8df051ba72de96ad8caafc2f54bea', '0ea801c850d79edeed1933012e28c07d', '5b25b34b79d48c0c0028ee7ba5251dae', '3429231126c4f19eb64e3e36440636f9', 'a3f5ca515f6109b20910d71f1978c63e', 'ec1038571bf510dcd0ce1fefef588ab0', '32c18e3d12d8ee4b4b40a7f6bfbc0739', '769349794c21fb4b3ca104e67dc12353', '3f9cb4e97fe9e39eff11b10c5032d793', '83fe4712006cf1914102a52ad842d485', '27522eb600263b19a9b2da3462482322', 'a7e6438739663fa717caade29d29e767', 'f0f713aa76f2974fb63b90968add9e63', '5e551818aeb3d10992a310b7f1ae3c4e', '9752401fd1c43f5c285228a3bbf6b9a1', 'd68964a06f5e356b9e32ba28134c6744', '9d972b742dba8fd18c37812f7cb19bfb', '5cb6135690e8232e31ad928951b72a24', 'fd4228155d5cba88d56e3b168f23a220', '95ab840020824448db900b909ab8dd89', '8d5eb1d012caf49add055de9ca1d4f45', 'e66f4f7abe46e350dc1591d4886446ec', '3b53e1e58250d0e83422634c0b370811', '3906ec4dc0f89512949f41d1740ee0c5', '0a50ed930244838db5dc36182f9a0c45', 'c399a53aa75b607b6b9ff5a7f7feb42f', '088067cde912898e064766f6a5d0bb02', '6c838dffe95793a9b9d347c7d5ee224d', 'bb1893a4b518401c5a5a68b0891d492c', '7eb49066b2309eb2ea14b64228c3865c', 'ba0bca5b72e389a46afd8fff37003bcf', '6827bb3a3c554e3241fd8234ac4c7072', 'ee98a4e7a29141e5db06d9f3a050218f', 'e7ececb884b6712d350175e3d8093bfa', '22e124781df673b0a29e5a366a5fa039', '7fa26c9a9ba0f52fe82148cef86db4a0', 'b8d18f43599ca1dc2f925538d89cea35', '5e28a7119e730aab2e60b45c07881640', '2e737b783c4fe8df3727b1c298db2af6', '8f3de8a6921767fd86e27c2c6e57c91f', '2d2d4db01e0497966893573d160f752e', '57d2fb5a4d60d69612dd3c12601e96b1', '133dd015cd6ba7e43aa19f0f5a47a2ad', 'bd3c119ddaaee32ee9b6e33d0ca62100', 'ca3b99dfcd32f3969bcf12371b2b6bdc', '536a87e35bf566c331ab7f446c493f03', '893c6b2fa4a43d47adea15c1f741836c', 'a04247b86d6edf1ecd9f4ddb42104a2c', 'e357ef37ccfacd99c188bb1d855afdd4', '8b2cd777fb820bb00c9825d084e60ea5', '585212f6aec58e343eb35dad3af86cca', '024b47fe227a5abd13b7bcd6be10a016', '55a4eb8ad8b112d4ef36573f01b8745d', 'ead25f5900cd34243b5577ce89ea5d13', 'ba65fae770414cea0fb24fb9bd8cb36d', '3d786661b9ccd9c8dae47e3b682d4814', '2dc6c8c43ef4b71f0b017bf9e8a36b9e', 'c4614ab94cc8d2840c341d80986a1197', 'd748e0746c6e78acc0a1cfd635d1d09f', 'fac837ebcf95591abb1a0243e4bfc779', 'b505f4ad1478961e4b3b438a726c59b2', 'bc778bc3bcaa84d58789d52c5cd85769', '74ec3b2dbe2c8ad03e991808dcbe9e0c', '969d58c746f74e8f12287caaecf52d34', '5fe29a0dd51d36c1a149d58a53ff6bfd', '07579d4ea83e0f91b1c629eb9a6e53ed', '7594b8c11caeb42f9b0aa7ccee2e221c', '1518c62ba87e564f0485c5cf03dbf039', '5b68ece2102ebc2587228043a47f5efb', 'de27bb3dfc5aedd8eea53945cd2ebbcc', '6dce9cf37bc41566cc6aead3aacc136d', 'd4d1cf20b6322986fa05f941de13603b', '2f6bdfcd25261c53035f4e1a25cfe4d7', 'bbe3deff4718d3d93f67d9f7086f64e3', 'b8d0d4cfdb5c37986877e07956466872', 'dc6beb90194e62346ba3766aa728f84e', 'dd4798d33bacfe80b121527d369c2cfd', '7c89c5ab8ed0deb771a635ef3fc8d0ca', 'ebf77e11c1dd255e76678e05e6772d7d', 'e094c102843eeb0826741dfd6fb4725a', '4f30740256e9bee3e7dda8350629877d', '83ddf7b1258ae2adfec978d2f3db8a73', 'b930960b69c459ab13825cfb060be233', '02c559dcbaa30803ddb285be1cc30912', 'ed7753fc5ac7e5c69bf7f89af297ad99', '4321d8a129eecc6aeb7b360a1558d8e2', 'ab16cbfd508e2f34d6839ec86608a9cd', '5b0866a1da798e15664462f6894f0c37', '30ddecf9662ade3719274fb5cf22e155', '60f1036d7ab9c4cc4dc77e3018014883', '95a9ff23e4d0f686f1085f698766e2ae', '05e3188794cc7e62e078f72c07727c7f', '4f345cc2d3477585c185194522b6a39b', 'd721e4a97b6d59d9b01706ae977a971d', '7e7d93ec1dc273e0caf3ae36e4d68431', 'd6845204b064d8a1ec897a7d42795a24', '11be13958b61fc779ca7eede6b5eea4c', 'f831ee7031651a3af735832605555c8e', '01301369a5d6f3c699c6e4659afeff65', '54cd08a04c1766842801af78aafc6055', 'c9833440449b08413db4d3f80057a784', '51e7d9ebb04ac05e91b806fe4f677617', '1581c39f26992177da2fb42a15c76c36', '696677917e43fce6647e7f28a222a517', '08331438574101e8bd90a0430d8a58f8', '56648a73a1232c364996f16a36979e7f', 'a1df443c396b85001ccf33a91324156b', '92060f5aed754bee012b58d9a9227d98', '54534d55fefad97731d7640982e10562', '45a3fe9815c1f2fd522e021e66907cdc', 'ba5f27e59201db8e094674cf5c07af5e', 'e19785e2dccfdadee72a15235caff980', '16136f6985279dbb639cd051034b5a85', 'cf36b989c0bbe963adc818cf1ed487c3', '57b20b32946076a3dbdd98b0b3326c1b', '8261d7cbfd235771227509fa2fcd4ad7', '20cc9c243aa1d6b01a4d4f83de5483da', 'dbe5b933558fc88200718d993bc5aaf4', '9dbab6914683978ff1f6b6a33daf1083', '82ada5f45680d2745f6dff9c1aa00993', 'c5d6c3c2dde19ed6911939d3520ac8f2', '94c95680a9f98297722d2e58e929a3a6', '6e4ef91a74bf652936f0d89aa2c061ed', 'b9aaaac11412ef89b8bc263043461e1e', '03b135a64db97ece95e129520130060b', 'cee108bd6b534ac10d9fa5e7c844c84b', 'fe939f284ec1409ed8572b5de20d7d27', 'c5b8b3bc0715f134962ba4884e376390', '021a06b56fde315b3ee2d21b817b0e3b', 'c2d184483f234027e2adf40fbc3d1533', '6223ae7393479cb2ce8a3441dbe6bc67', '1d995d6aa487d86eb424ed65a71e2da7', 'd2c59a64c4bb070fed540eb69a3fda2c', '4cd0ed287002db90447d44037be3432c', 'e5735615df7b01e0e945086873c1633c', 'bcc5e7b74618e2ec616a94aa9d3423e8', 'd895c53516aed389ec98cb52eb4068e0', '5624958443aee6af033ed203d9334b09', '873744b1937db7a119b2f5c0ad9eb85b', '4f15f392543e8d6c3c21a31bc60fd1a3', 'c5fc38798ad18fbe70ce72962087c79d', '0b8d59b734c3eef75302901c4ccd0a93', '492d056a59ffcf6d7911b3f62e906bef', '24cae1a52343e2125b0787007db7d283', '9934901ce0054898775c840c0c098dda', 'b908811cbb4df7ca077627cce3358e73', '890577f5f42e48c8e58da7179fdefa9a', '10084e86ce244c0de35534422a6035ba', '3dda8ab55a7268d53d4f7df77afe1df0', '6a792a6e3de6b27435950fd76fe2f921', '10db818d048eba870caf6c99472c49eb', 'b7ed7344bef83549210a5955009db303', '76977fc5cb6bc92a11c6b3685a839156', 'f78b75c5fac4b86800b232bccb0559f9', '135cc5a3f64ec33bfe53ef22f5835350', '76c5a1d9237032d7c3df33691a877f58', 'acf9f42c82e68965ca424000816f79c7', '7399637c3ff6c69bac4f593f2b131e10', '08927f029914cecbf8e561d378bc0245', 'f14870002e629c10d966bc0b8eceb4de', '9f8703ed7b9c9824dd0d5b5583763cd8', 'bdc3e4981d040685db6d7a2cdc04d161', 'b07196ce273b16ad31c63bcde23e202a', 'd018d2a921e4573e02203887640405b7', '00f78c766e4533b3613f2cf0deacc74d', 'da5d6aabb9ba2617d2ff4f02acc49038', '2e6fcb15e6801ca31812916788100042', '7c7d0ccf4df61982382bb0c57bc85a61', 'cea0b1d54e0e0ace7ea7e03003eb592e', 'e5c045ee4124c188208e369603df359a', '30f4af01978157984c403d82073a3064', 'cfa0954198d3115d8ea1523dd47ac094', '467f05c1d02d7b4c92d9d49d0ac3b2a0', '6dfa4c4f4e7192f72fdd2c509ecf76a7', 'e3884d378e2e6df2d4af8f720a3e6342', '35eb92a77d063f9761e0321e9ab9b1c2', '29054af3c8cd10667e811a9f9ac4ed6a', 'f06b16cc88fcab889a55b64898a4fe64', '2036aa3af9a93a127decda7a342191a4', '51a1ea2f3024bc9a0910c3d9138a2f57', '55c2d71180701f63af7ed3baffc5c7f8', 'cd1e8ab53385489b030028bb885ee1f3', 'ca9af1e8e3457b39ae660a1b61b43d07', '72163e4e744333e799d73436ddf956db', '2040499b086794ed3413cb499f5e756b', 'b22de898670648b78eee0feb1ad14a63', 'fac009c3253d5ce033071a62d1899978', 'fd1445952d3b7813876a7772bf8fa982', '0b5c9863b771e861ee75036bc0951799', '917bbc3efbf42ea3413d0d5d23657a81', '77f0d24e582c20dfb6773e0aaf579d1c', '5693b54ee2a2d98528cad51f5b76a800', '0dcd51b3e7214eb99a7787ff74f80093', 'ec44e38a37d6c88c1d46e7d5f2aeed08', '1c9a911004ef1a04083e98e245dffe0a', '09f84914cdb4e8f9d7be116e80eac8e9', '12f1bfb9357b2922e93731d60d1b5e5e', '842755b1e4a4cdff6244bc215af9a423', '2391deeba48fd25b222dab3879b2f201', '8e519daef180d872e20afb64c75fb514', '325a6edf26d5f4b960bed671bf468929', '134b286743bc475fea741d408246b5a5', '008144b57d322fdacd57a314bbff45c8', 'f1086042bb2734a627e240c921409ed2', '39dd426d96f18ab58a59f47d06b33cc1', '903a007621b63060b8c7c141476879c4', 'ac81960ded1d2fca5f864f2e41e034cf', '7738e48bd668d0abc6a169385e23d259', '7b19c233612df806cb03def17b032079', '198dad93d259f59936d52c4da6ce82c9', '4e63c1ce0de0d8ba23a8070375796317', 'de6a664b85cd88c2b34f28701c40e171', '1e83a07cfc00613a85aa3f3e5ac8d051', 'ae2cb906b2291355b3697a110421969b', '53ee19459782a983e4466c6c74f1a8f0', '12f57632bb148c0987907388ad71a611', '7bbe811fa029a55bfe4d4b2ea0e8f98c', '0ef4cd331de28ee4765d796d4947c456', '0ef190d2e7d8ae90d1df2ba44e3074d1', '5e6994e901b494ebc9b793507c8ae4eb', '23490628418b138fd461d1f839136321', 'e6f31c9098b2fcd09a0ba5c5d2579d08', 'adced762fe5f2309300980fcb272aae8', 'ab8834aec8e2a7dff1b72143270482b5', '0557e43e4b822f7e40dc6af633669dde', '8e41a9676fee4a60cb91e3591b4c5346', '09b275b230c0c27c9b9f11369f023313', '7980f5d3ab495b8e68d42e2898388884', '6cb049d5e4056bfbe27c68c27055aea7', '824e98618a238d231add7febf5a8af3c', 'e7931a0ad3aa8d2739d76b9bf806e156', 'd6d7e9d6e9eef85f8b34c4151961cc93', '005263bed033c3c3229c17cad740f965', 'fcb78e4dab30bdd9a7b36ece19e33b2a', '7b43010fbe21dde0a337292d639c391d', 'a53b6c2dba6017b032287bae83b0e5ef', '5d9ae9992810b1de11111b6354969cbc', 'dc30801084668cc15b874c0e35244118', '07ec775aee310d220f4f27a6d7ecd1d6', '9fe26db62a6dfd4b20f85f449b40b0c1', '48adf170260594fc9b159459a0155318', '1a97c5a75a8313ca67c4a9b6415760a3', 'ca432bad0ede385492a9f886772cf71d', 'b4d4faa5e7e1f0422e37ad98bc0a5c1b', 'bee712746a386747b549aa23e1bb02ba', 'a9d22ea03f42949a2bcf6c25f63fc3b0', '853085cffee9eda7ce1fbb6fce8452e0', 'a4ad0a08cb97cfa137a573ad4e435d2b', 'c7e7fb1564c9b5bd6b58d4426225d9e2', 'fd64c1a1d6fbb67fc4c604268050b23e', '86ba05461c9a8c46d4e3f739d1f73797', '184c415446ba7bddb8cb77fbc16a4b48', 'f3186f09922f775b3d7b68f812ea25ef', '99374ccf233c246315f595b9ec7c5048', 'de974fc239c7f22952934578d7c24ec1', '31f37110b1d280b11bfcdbb4a57a16c4', '96b57ebd300e1310ae45bb9e9ee6774f', '8181e7577c2951da2e45f7ee7087b44e', '56f1862b6232d51b8265812b67f74be4', 'bc2f359b47c85546460eef0503ec078c', '86b1f1a4774acef8fda3ce563af242e2', '8d563c4f6e815c2770a06a7f46eb22b1', 'a4673081dad59e5b69e81d7cafc554c4', 'b710adfabd7a8673519688c9a86cb743', 'ddc68a69afe03eeee8b4c243dcff79ba', '8fb62e3c1146d1c0e229bbfdec79d518', '37b84702388cd184b9323a6f24ea9467', 'c53dc70ea924c1c4ab65a2fc0c913628', '4ee6a2d4480b80a58a8d9d5284ce92a5', 'a5ca397cc516ee5f3d4f3d155c5db132', '463fbb483c3990480c1337bf922309f2', '4bb5fb9a5b6ff90e5c36040c9374f7ed', '3a51753548646cc413b96f041dd85155', '09f4daab50857fc9c65c608a1458ef89', 'bb32a4633354eccec0da955a5ef6e080', 'cc2d638d9e96ed55b398c193eb963fec', '7063ca5300a7dd25a93a2497f60c623a', '0e3151ab1cfda7252dbf0c545b0117d7', '37007b599637fd7f35a6889b2a6b6be1', 'cda60ae9db4259ccdb6f6ec019cb06ac', '8f8b3fdc93ebe59beed2f110bf94098e', '51b89f43a2e184bb4adc8c61a2e60dc2', 'fa132ec82a048078f1a7c30b732c7989', '3c5f4c07e6e03cf77417616725d062cd', 'd4827204549816d93bf7934d00dbb2cd', '382992ed66b3b15b3314b017390976fa', 'f3ad8a616ce8599cc1512db66f7b6b36', 'd7c617ba343e52b6c1006320d89f4090', 'facb4902241c1ba56c1126efbcf330f6', '236cc38446352206406ec9b353de9328', 'e30a8497085c8b0b1e52abdce38150d8', 'df90bab5b3ccf149bb1fab72e0c9dc62', '7539920b8314d3ad2eb7e6ae07f12ee1', 'b153dce4102d6e370cbfadd245afcf78', 'c4ed1f90561a4b600fe9173f7b3a4439', '73917a4e9998302a4979e3c4bcbd0617', 'cfeb81fb22aad0d41843ddaec5b99589', 'e7e4e9b2f51085f3d71a268e91ba384f', '563de210c02182d7882ddeef4198991a', 'df7bcffa897c43f8ea9ce255880495c6', '86f622a8da6f2caf04aa9512c5987761', '8fc38766ff5f699a82d2263613f4de9e', '23fa5941f4c1477b13f728d62086a2dc', 'db61de413c392b9934e73ea6d32efc49', '414bf896c903e37e76f588226d6ceba7', 'e3175cc6ae171dd7952541af0312cb4e', '7ea3a057dff81d357d00d0930d25ae0b', '75a19c527e5af5ed46413fbe6acec78b', 'e7818cae2ef831a2f2ff7550a25d0445', 'f3c447b7e6e79932a47fe8edaaa176af', '003baf3f5e3f856044bed5529d076142', '5b198d764d78ecb84bcf3b00f7ccb546', '33a5d21af057837c94244342ba2428a9', 'b1d5bb2bb636c7121e4c9a5e49bcce68', '40f741a67de63b232ede50b8d561b19d', 'e056a33abed3f27ea0eced47ce1b6f54', '1729871b5d22fec4d5fd6db78b1fdb2b', '362fadea517199b54fb4ce3d6a215f6d', 'be1ca427cd8efd3ea6f8a63406f24165', '9190a7394260f8418a7482e2831b2309', 'a1d14b75782db0e7ee89a5b83e5f10f5', '9853e49d7d56ef753f19f42af886ea0b', 'badd4fb5ab5ea112308a2a1f6f989be7', '0957668349374e07ced80bf989275306', '54a51cd29225eba219c5cfd24e900051', 'b47a76fed05a2bd51ef0186878b5db1a', 'c4cdd68c0523a58388ffe0d371accdda', 'ebe764c75e6984b713452d807f4a06d1', 'e488daa3aa0682cf90d18367cfc6cc17']


def generate(context):
    participant = context['participant']

    task_id = task_ids[participant.id % len(task_ids)]

    return TaskStatement(TITLE, STATEMENT % task_id)
