#!/usr/bin/env python3

task_ids = ['ja2j5gdj', 'ex0r3dtw', 'y4slpt1b', '9df7v7by', 'scickcnv', 'h2n5zv49', 'idyom6ub', 'o7kf9x45', 'de5ov258', 'yn606fze', 'fv17r8dj', 'z00e5fv9', 'po5mjtxw', 'uspkf0g7', 'w1a4l8lz', 'nby0vl7b', '4j7p92ka', 'pdcwkkeq', 'lgap80a0', '48r5t5u1', '1srzpns9', 'u4j1s1j9', 'a5bgdveo', '257920k1', '6620oyka', 'nj10svez', 'xr1eqeoz', 'o8l7h5mu', 'ng08yw5w', 'pxsfx980', '17ql6f7i', 'onnngo5u', 'v2nwz29f', '6rgdhhdm', 'oemj5xd1', 'gv7wwto7', '5wb28klw', 'uugogacn', 'ybpwemnq', 'n9hnoho8', 'h9hhw6df', 'tnv5lz38', '6ry4gjbz', 'y3cvuiid', 'ixuxef8u', '9689rl9h', 'zu4c0gdt', 'c45vx7bi', '6p78qqe7', 'qok84zkq', '9w0vnm4o', 'eadfgvhr', 'z0zugrpp', 'zvxx1onb', '41yp4vw0', 'fejgcght', 'lcrsl2xu', '1dtoy6tf', 'fxkj7hqs', 'rfo2elsw', 'h33mevrt', 'jrbnpi1q', 'vgvyno6i', 'ep5i72f1', '8r1xifzy', 'cvaakjbk', 'mzljwpij', '3zpx8t2a', 'ugd7tojr', '4fk84n58', '4789kfex', 'dvklku8i', 'h69nuyqb', '1byzrfek', 'm8m0zdyp', 'hf0l3wvt', 'q7ej0ckc', '1gyw9edm', 'l034la9m', 'ouzkx73y', 'm1sczyzm', '1hmhbli3', 'lm1zd00e', 'j4n4ut0i', '1jkyq4mk', 'a1qgeybp', 'lkd6gghg', '62zek9to', 'lkcqn1tu', '6u6yfa65', 'nvh3742f', '8yd6966u', 'o5dqpqdx', 's1xuflxk', '4k5ogne9', 'vzrodu4d', '34z1xx9v', 'd1iv4x6i', 'ln6ryp2v', 'xfb15y03', 'pwj94df0', 'hwnewo71', '2iitiu5f', 'vx8dkcrl', 'z350y2n0', 'urirzdck', 'zzdiq6b6', '72s17nx9', 'rps4v9tg', 'y7lve6th', 'iio739vf', '8uiiqsqg', 'wzutw3bb', '8kwv1g3p', 'nc3kc0u8', 'gu2z8et3', 'z78p7bnc', 'j2lca3kq', 'r9ax4vp0', '77t035un', 'pm3bis2h', '6yr0u46u', '46dph4ue', 'uwkik9e3', 'flvpnvcv', 'feu0prdf', 'ruuybnlx', 'wx7pdroc', 'wsika9qu', 'olqx8jet', 'b8o2c10p', '9nfe5evr', 'lprv4x0a', '5vcg5pj4', 'q1g6iyt0', 'cqjfs8p2', 'tfyq6cbm', '1wfmzxd6', 'pq680kg1', 'fqas129l', 'xvl3o1h7', 'mhg5p670', 'ncygu71d', 'qrzjvlw9', 'h5xx8z2n', 'jsxtm7uq', '5unwrydc', '04hky1b3', 'tg40m2i3', 'idil3lld', 'gdqq2eod', 'qldxa0rd', 'jsdwl8xm', 'y1qq4sv2', '212mh5xi', '4tl3neif', 'rc63ql1b', 'ihsw2jdd', 'dumjjrve', 'il7tkhjd', 'dvfqlhzn', 'qaslnif8', 'ifenmach', 'jdpwc6p4', 'jzwlkok1', '6qbsw60q', 'lq55ewi9', 'icrxjfuj', 'h0634qzl', 'qfagvsu6', '6zpp9n25', 'repg8d9t', 'l1zc67fg', 'dcqt34r2', '7rob466g', 'd8agr09j', 'bamke53n', 'n2av0cqd', '61v5hh3n', 'vh21n0u0', 's0pa3tlg', 'ijvjwosd', 'xxgnnqfl', 'jnhwffs8', 'i5w7ogv2', 's000snhl', 'nc3rtvym', 'hurkmjef', 'it791z7z', 'dogx23ea', '4qhetggs', 'd4uxl0vf', 's5qlkx5a', '9th1jnle', '35mh0qx3', '32b867md', 'oiiiztel', 'f9z1005o', 'z3r67aqi', 'jvej8feb', 'quwiojm2', 'rx2w3m5j', 'rk39ekz6', '4pl6r40v', '2l5er13i', 'yh6l2auc', 'xyxrois6', 's3tfs2kf', '9e3a5pds', '9cc91z5j', 'pmr64l0s', 's3orbp96', 'i6bgvb7n', 'hoswtfk0', 'i2933hby', 'jpcdw6e0', 'x2d6sew8', 'akzl5jpn', '0xqzsix0', 'sp6qlw2j', '0p1c2e15', 'mybfjmd1', 'ryjo9il4', '3zuiq4pe', 'qzmyq5q3', 't7x03kcw', 'mv5ve0l5', '8vll96bi', 'ae8f7dq5', 'wr9wxz6j', 'a89fd7xu', '4rc3la5e', 'ya4x8i8t', 'uowvhjaw', 'c45wxwcc', 'hkl8zkq1', 'c4ouhwxz', '6u9950hx', 'nbj5rrqx', 'k02ao8wd', 'wlt1p6bi', '9amla8xe', '1tpk61md', 'ko9bfrlb', 'bgkpe95f', 'eu5lz9ir', '8ij2ldcl', '5r6m6xac', 'ppcpgzra', 'se6rqhzp', 'vu9utizh', 'omlrhwju', 'quatdo8f', 'z4zu975d', 'eax79f4l', 'l0xnk30x', 'ps67tl72', '0qpw2ud0', '904vgv41', 'eahkj5ic', 'lv3i8hiy', 'oryqhtcj', 'slkaunc7', 'eja2q26a', 'fswkmftv', '4ug0dryd', '2ljiuwa8', 'vkzph5rm', '1s9bc3s7', '02edmdqt', '3sl4htaj', '9mcfqmnc', 'b3gn638p', 'gjrr3knd', 'db1ok3xm', '1u8lh37z', '2gamranq', 'm9jqyvnr', 'vck72sn6', 'pggz9r7d', 'w5bejzjm', 'jwe4ie78', 'kxonl9ju', '7ruv2xpi', 'q1zy3ahn', '57k60mum', '7f81ozd3', 'idegfm6m', 'o4uudha8', 'ygjn52d5', '50i8jd1u', '2acv2hkt', 'w5zrc5fq', 'yj2p70fe', 'tbp1npnz', 'anq9fb9w', 'dka2vc82', 'gg48702d', 'i251x008', '3dg0yt71', 'rq9p1ahj', '7izd5kzu', 'u4l06ccs', 'xy0jtrwq', 'ivxgw6ys', 'tbw1ws41', '151jox1q', '5mb47n6a', 'gv0icr5t', '6u900421', '8g32grv0', 'rofr013g', 'b85gydn2', 'dvuzc5ci', 'jolmmhup', 'd114lmna', 'evj03g9k', 'nx1fqxpn', 'l9d9nbc4', 'lqa47q1c', 'od4ubaxe', 'zw4av1fs', 'nbs1m9if', 'g34duq5g', '3ytcyxep', 'e12lx1c9', 'amfp5faa', 'ivzj9nuu', 'bh7q8loq', 'lmcf9o1o', 'x3vmog1d', 'wcud3gjm', 'cqc8ovlm', '7oh6m9e2', 'pwyl0knp', 'qvzms5e7', 'qhgqqn7b', 'u0j3wbs2', 'pg3f1z43', 'nyds1wx3', '5wy2wfzr', '89dlq1ac', '2vld8kdt', 'jwbuwr3p', 'lecxtv30', '5xsoysjy', '779aoy39', 'oifadu6f', 'lmnyva2w', 'zzrf79if', 's0o0t09a', '5qjz6d3g', 'rqp54amy', 'o3jjftdg', 'rjmn0pdk', '0bam5ybt', '5q2i0rbi', '4jltcr1m', '1o4nhb9v', 'k1fzfk7h', 'nmunhhkq', 'c7r7527s', 'jkpiav8c', '5ru0ih7v', 'xyfk9toe', 'nmkrq3o6', 'iq6q6o7f', 'ci7mm69b', 'jdpt3h1w', '219432bx', 'xnfofuj7', '8qay6g9l', 'w5j99eq1', '7qp03am2', 'tctjdxuj', 'by4pj7qw', 'kr9qor5s', 'r1mbzj8y', '0leuvey4', 'hkrx9m70', 'syh7iuay', 'omi17ydb', 'ku7hu0oy', 'pb9b6vxq', 'my1g9m28', 'ppjs3wz0', '5rmguhi0', 'shzab6iw', 'bry416x7', 'vqw2351a', 'zna56s0o', '818qgwsn', 'h5ued2c8', 'wa62jjp1', 'x88z3v7w', '6sf08k3j', 'bbex17vv', 'ztonlnnu', 'vi554nyf', 'u1wrx4o0', 'q0dnqxjw', 'l29kny56', '8yi7tqd4', '06h10qhd', '2gn84a9e', 'edxh1bb1', 'kqcq7on1', '5pl2o9ni', '6vlecrwq', 'gblojzp4', 'zn3kj2vs', 'n2n1x93b', '49vbpux2', 'dq2jxsip', 'g49hpj7a', 'y8r7cprd', 'tj7bgb1n', 'jg3iyhf9', 'rxlzb7tv', 'vgxnodsq', 'y3mwful3', 'wz0plz31', '218k8hzc', '07jw3zck', 'qlzq0fo5', 'k2egliqa', 'vlnrgmm7', 'ixys5g3t', 'unsrng0i', 'k6va1ng0', 'oauo390r', '77vlrgn7', 'mblob09k', 'f5jzolu1', 'be6lnj9v', 'vdi3ylnf', 'j4y2umsy', 'vq0c9ty3', '0n73alat', 'a100rg75', 'kkwo4gz2', '6aq01dg6', '7fewhgp4', 'r67jmi8t', 'e8zgc2c3', 'a38wtjyk', 'qn9k7osv', 'y3w4ixv2', 'c8hngdug', 'kpldcz7b', 'hkms6e8l', '1un7wnxt', 'a10k82ul', 'pozf5r3e', 'v7h923u5', 'oirxe6ws', 'wctuzzn2', 'ju7jzn19', '2guj4klv', 's5tf6jxu', '2g00vcnz', 'qy9ycgi1', 'g5rycsps', 'j76cy0py', 'yljmae1q', '11s34e25', 'pr1am1dl', 'qzy3wg9y', 'vnwp3ar0', '5z2gzs9h', 'mu5jedxz', 'kd2pjvnt', '3pe18ttx', '3bk9528q', 'fv8e4omn', 'urkjgted', '6k3q8off', 'nl1545h1', 't9axcxj5', 'vy1edti9', 'yarmyipr', 'jbwd0fne', 'zwms138b', 'luugou9g', '172v6zw2', 'igbkq6br', 'v20ou8ks', 'l0b9z91o', '9nensmrq', 'bsyumk52', 'ixa5v53x', 'vd6iyjc1', 'jm2wns2b', 'pw01ji1y', '2qiywy5r', '9ijuchkl', 'ckahtr52', 'agezndlc', 'jx1jqvg9', 'lxkar0ro']

TITLE = '''Сайт нашего регионального подразделения взломан'''

STATEMENT='''Пару часов назад мы начали получать сообщения о взломе [сайта регионального подразделения нашей газеты](https://get-flag.contest.qctf.ru/%s). Злоумышленники сообщили, что выложили в открытый доступ конфиденциальную информацию, но найти её сможет лишь тот, кто знает где искать. Проверьте сайт и сообщите, что они нашли.'''

def generate(context):
    participant = context['participant']

    task_id = task_ids[participant.id % len(task_ids)]

    return TaskStatement(TITLE, STATEMENT % task_id)