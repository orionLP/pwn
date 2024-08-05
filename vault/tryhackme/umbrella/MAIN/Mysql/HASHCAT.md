
## HASHES

```txt
| claire-r | 2ac9cb7dc02b3c0083eb70898e549b63 |   360 |
| chris-r  | 0d107d09f5bbe40cade3de5c71e9e9b7 |   420 |
| jill-v   | d5c0607301ad5d5c1528962a83992ac8 |   564 |
| barry-b  | 4a04890400b5d7bac101baace5d7e994 | 47893 |
```

These are md5 hashes.

## CRACK

```bash
 hashcat -m 0 hashes ../../Tools/rockyou.txt  

2ac9cb7dc02b3c0083eb70898e549b63:Password1
0d107d09f5bbe40cade3de5c71e9e9b7:letmein
d5c0607301ad5d5c1528962a83992ac8:sunshine1
4a04890400b5d7bac101baace5d7e994:sandwich
```

And we are inside the application in [[PORT 8080]]

Turns out we can also use claire-r in [[PORT 22]]