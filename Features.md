# Comparison of features

### Feature overview

|| Feature | Support by PE Studio | Support by CL version |
|-| ------- |:-------------------:|:---------------------:|
|1. | Submit to Virus Total | Yes | Yes, if API key available |
|2. | Check for TLS callbacks | Yes | Yes, all callbacks are listed |
|3. | Show information from file header | Yes, highlights suspicious fields | Yes, highlights invalid date-time field only |
|4. | Check imports against blacklisted libraries and functions. Cluster them according to their field | Yes | Yes |
|5. | Prints exports of the PE file | Yes | Yes |
|6. | Print summary of resources | Yes | Yes |
|7. | Check for resources against list of known resources | Yes | Yes |
|8. | Save selected resource to file to analyze it further | Yes | No |
|9. | Show embedded certificates | Yes | No |
|10. | Show relocations | Yes | Yes |
|11. | Check for signatures in the file (e.g. packers, malware pattern). Note: database seems not to be up-to-date | Yes | Yes |
|12. | Show blacklisted strings in the file by group | Yes | Yes |
|13. | XML output of results | Yes | Yes |
|14. | JSON output of results | No | Yes |
|15. | Yara support for more rules | No | Yes |


### Indicators
In addition to PE Studio:
* Show summary of complete analysis of file
* Check for entropy in sections to quickly spot packers
* Check for imphashes
* List suspicious (= non-standard) section names because they can provide a hint to packers

All the indicators which should be supported by PE Studio and comparison to our version

|   | Indicators | Support by CL version | Note |
|---| ---------- |:---------------------:| ---- |
|1. | The file is not an executable file | No | Our program won't parse the file correctly | 
|2. | The MZ signature is missing | No | |
|3. | The size (%i bytes) of the file is suspicious | No | |
|4. | The size (%i bytes) of the optional-header is suspicious | Yes | |
|5. | The size (%i bytes) of the file-header is suspicious | No | |
|6. | The size (%i bytes) of the certificate is suspicious | No | |
|7. | The content of the certificate is suspicious | No | |
|8. | The file is Self-Extractable (SFX) | No | |
|9. | The file references a certificate (offset: 0x%08X, size: %i bytes) | No | |
|10. | The file is managed by .NET | No | |
|11. | The file references (%s) debug symbol(s) | No | |
|12. | The file references the Reflective DLL Injection technique | No | |
|13. | The file is bound to (%i) library | No | |
|14. | The file is Code-less | Yes | |
|15. | The file exposes a TLS-callback (%s:%08X) | Yes | We can list all TLS callbacks |
|16. | The entry-point is located in a section (name: %s) that is not executable | Yes | |
|17. | The file checksum is invalid | No | |
|18. | The entry-point is outside the file | Yes | |
|19. | The certificate issuer (%s) has expired (%s) | Yes | |
|20. | The certificate subject (%s) has expired (%s) | Yes | |
|21. | The file does not contain a digital Certificate | Yes | |
|22. | The file has no Manifest | Yes | |
|23. | The Export table contains (%i) gap(s) | No | |
|24. | The file implements Control Flow Guard (CFG) | Yes | |
|25. | The file will be copied and run from to the system swap when started from the Network | No | |
|26. | The file will be copied and run from to the system swap when started from a Removable Media | No | |
|27. | The file runs in the Visual Basic Virtual Machine (VBVM) | No | |
|28. | The file is a Device Driver | Yes | |
|29. | The file is statically linked to the C Runtime Library | No | |
|30. | The file opts for Data Execution Prevention (DEP) | Yes | |
|31. | The file ignores Data Execution Prevention (DEP) | Yes | |
|32. | The file opts for Address Space Layout Randomization (ASLR) | Yes | |
|33. | The file ignores Address Space Layout Randomization (ASLR) | Yes | |
|34. | The file ignores Structured Exception Handling (SEH) | Yes | |
|35. | The file opts for cookies on the stack (GS) | Yes | |
|36. | The file ignores cookies on the stack (GS) | Yes | |
|37. | The file ignores Code Integrity | Yes | |
|38. | The file is isolation aware but should not be isolated | No | |
|39. | The file references Safe Structured Exception Handling (SafeSEH) | No | |
|40. | The file registers (%i) Exception handlers | No | |
|41. | The overlay is scored (%i/%i) by virustotal | No | |
|42. | The MS-DOS Header has been found at (0x%08X) offset | No | |
|43. | The value of the checksum is different than the checksum computed | No | |
|44. | The file is scored (%i/%i) by virustotal | Yes | |
|45. | The file has been compiled with Delphi | Yes | |
|46. | The preferred AV engine (%s) detects the file as infected | No | |
|47. | The preferred AV engine (%s) detects the file as clean | No | |
|48. | The file references a debug symbols file (path:"%s") | Yes | Not sure if the debug file is found/parsed correctly |
|49. | The debug file name extension is suspicous | Yes | Not sure if the debug file is found/parsed correctly |
|50. | The GUID (%s) of the debug symbols is suspicious | No | |
|51. | The path of the debug symbols is suspicious | No | |
|52. | The age (%i) of the debug file is suspicious | No | |
|53. | The value (0x%08X) of 'PointerToSymbolTable' is suspicious | No | |
|54. | The value (%i) of 'NumberOfSymbols' is suspicious | No | |
|55. | The value of 'SizeOfCode' is suspicious | No | |
|56. | The value (0x%08X) of 'BaseOfCode' is suspicious | No | |
|57. | The value (0x%08X) of 'BaseOfData' is suspicious | No | |
|58. | The value of 'FileAlignment' is suspicious | No | |
|59. | The value of 'SizeOfImage' is suspicious | Yes | |
|60. | The size of initialized data reached the max (%i bytes) threshold | No | |
|61. | The value of 'SizeOfHeaders' is suspicious | No | |
|62. | The value (%i) of 'NumberOfRvaAndSizes' is suspicious | No | |
|63. | The address of the entry-point is zero | Yes | |
|64. | The shared section(s) reached the max (%i) threshold | Yes | |
|65. | The file references a library (%s) that is missing | No | |
|66. | The count of nameless sections reached the max (%i) threshold | No | |
|67. | The file-ratio (%i) of the resources is suspicious | Yes | |
|68. | The last section (name:%s) is executable | Yes | |
|69. | The first section (name:%s) is writable | Yes | |
|70. | The entry-point is outside the first section | No | We could add this feature|
|71. | The entry-point is inside the first section | No | We could add this feature |
|72. | The file size of the section (name:%s) reached the min (%i bytes) threshold | No | |
|73. | The file signature is '%s' | No | |
|74. | The file is resource-less | Yes | |
|75. | The file references (%i) languages in the Resources | No | |
|76. | The file contains (%i) custom resource item(s) | No | |
|77. | The file contains (%i) built-in resources item(s) | No | |
|78. | The file contains (%i) resource(s) in a blacklisted language (%s) | No | |
|79. | The resource (type: %s, name: %s) is invalid | No | |
|80. | The signature of the resource (%s:%s) is unknown | No | |
|81. | The file references a resource (%s:%s) which is not supported anymore | No | |
|82. | The manifest does not contain trust information | No | |
|83. | The manifest identity name is "%s" | No | |
|84. | The manifest description name (%s) is different than the file name (%s) | No | |
|85. | The size of the resource (%s.%s) reached the min (%i bytes) threshold | No | |
|86. | The size of the resource (%s.%s) is bigger than the max (%i bytes) threshold | No | |
|87. | The section (name:%s) is blacklisted | Yes | Non-standard section names are result of the output |
|88. | The count of executable sections reached the max (%i) threshold | Yes | |
|89. | The file has no Executable section | Yes | |
|90. | The count of blacklisted sections reached the max (%i) threshold | No | |
|91. | The file references (%i) unknown resource(s) | No | |
|92. | The file exports (%i) obsolete function(s) | No | |
|93. | The file exports (%i) anonymous function(s) | No | |
|94. | The file exports (%i) forwarded function(s) | No | |
|95. | The file exports (%i) decorated function(s) | No | |
|96. | The file exports (%i) duplicated function(s) | No | |
|97. | The file exports blacklisted function(s) | No | |
|98. | The dos-stub message ("%s") is unusual | No | |
|99. | The dos-stub message is missing | No | |
|100. | The file imports (%i) deprecated function(s) | No | |
|101. | The file imports (%i) anonymous function(s) | No | |
|102. | The file imports (%i) forwarded function(s) | No | |
|103. | The file imports (%i) decorated function(s) | No | |
|104. | The count (%i) of imports is suspicious | Yes | |
|105. | The file imports blacklisted function(s) | Yes | |
|106. | The file references (%i) whitelist strings | Yes | |
|107. | The file references (%i) blacklisted library | Yes | |
|108. | The count (%i) of antidebug functions reached the max (%i) threshold | Yes | |
|109. | The count (%i) of undocumented functions reached the max (%i) threshold | No | |
|110. | The count (%i) of ordinal functions reached the max (%i) threshold | No | |
|111. | The count (%i) of deprecated functions reached the max (%i) threshold | No | |
|112. | The dos-stub is missing | Yes | |
|113. | The file iterates through running processes | No | We check if functions that can be used for it are imported |
|114. | The file iterates through files on the disk | No | We check if functions that can be used for it are imported |
|115. | The file imports (%i) undocumented function(s) | No | |
|116. | The file subsystem is Unknown | No | |
|117. | The %s directory is missing | No | |
|118. | The %s directory is invalid | No | |
|119. | The %s directory is outside the file | No | |
|120. | The Offset (0x%08X) of the %s Directory is outside a section | No | |
|121. | The Virtual Address (0x%08X) of the %s Directory is suspicious | No | |
|122. | The count (%i) of empty directories reached the max (%i) threshold | No | |
|123. | The time-stamp (Year:%i) of the compiler is suspicious | Yes | |
|124. | The time-stamp (Year:%i) of the debugger is suspicious | Yes | |
|125. | The file expects Administrative permission | No | |
|126. | The file requests User Interface Privilege Isolation (UIPI) | No | |
|127. | The file has no Cave | No | |
|128. | The original file name is "%s" | No | |
|129. | The file references (%i) blacklisted string(s) | No | |
|130. | The strings reached the min (%i) threshold | No | |
|131. | The file references an Object Indentifier (%s) | No | |
|132. | The file references a MIME64 encoding string | No | |
|133. | The file references a URL pattern (%s) | No | |
|134. | The count (%i) of blacklisted strings reached the min (%i) threshold | No | |
|135. | The file references a URL (%s) scored (%i/%i) by virustotal | No | |
|136. | The file references a URL (%s) unknown by virustotal | No | |
|137. | The file references function names mapped to other names | No | |
|138. | The certificate references a URL (%s) | No | |
|139. | The file imports (%i) library(s) with invalid name | No | |
|140. | The file imports (%i) library(s) with suspicious name | No | |
|141. | The count (%i) of libraries is suspicious | No | We could add this|
|142. | The size (%i bytes) of the Version resource is bigger than the max (%i bytes) threshold | No | |
|143. | The version '%s' is suspicious | No | |
|144. | The version translation block internal name is misspelled | No | |
|145. | The file supports OLE Self-Registration | No | |
|146. | The file version has no Root | No | |
|147. | The file contains another file (type: %s, location: %s, file-offset: 0x%08X) scored (%i/%i) by virustotal | No | |
|148. | The file is target for % machine | No | We can parse the machine type but do not mention it as the indicators |
|149. | The file references (%i) insulting string(s) | Yes | |
|150. | The elevated functions reached the max (%i) threshold | No | |
|151. | The registered exception handlers reached the max (%i) threshold | No | |
|152. | The file contains another file (type: %s, location: %s, file-offset: 0x%08X) | No | |
|153. | The size of the dos-header reached the min (%i bytes) threshold | No | |
|154. | The size of the dos-header reached the max (%i bytes) threshold | No | |
|155. | The file seems to be a fake Microsoft executable | No | |
|156. | The size (%i bytes) of the dos-stub is suspicious | No | |
|157. | The hash of the resource (%s.%s) is well-known | No | |
|158. | The entry-point is located in the last section (name:%s) | Yes | |
|159. | The count (%i) of sections is suspicious | No | We could add this |
|160. | The file references the '%s' Windows builtin service | No | |
|161. | The version information is missing | No | |
|162. | The file is self-extractable with IEXPRESS | No | |
|163. | The strings (type: %s) reached the max (%i) threshold | No | |
|164. | The size of code (%i bytes) is bigger than the size (%i bytes) of code sections | Yes | |
|165. | The file references Regular Expression (Regex) patterns | No | We check all strings |
|166. | The section (name:%s) is not readable | No | |
|167. | The file references (%i) Windows built-in privilege(s) | No | |
|168. | The file signature (%s) is blacklisted | No | |
|169. | The file signature (%s) of the overlay is blacklisted | No | |
|170. | The file signature (%s) of the resource (%s.%s) is blacklisted | No | |
|171. | The file contains self-modifying code | No | |
|172. | The file extensions (%i) reached the max (%i) threshold | No | |
|173. | The file references (%i) %s string(s) | No | |
|174. | The file references (%i) functions of the '%s' API group | No | |
|175. | The file references (%i) keyboard keys like a Keylogger | Yes | |
|176. | The file references (%i) file extensions like a Ransomware (or a Wiper) | No | |
|177. | The file references (%i) passwords like a Brute-forcer | Yes | |


All the features and functions of a PE file that should be checked. We can check all of them with the same logic as the original. However, not all of them seem to be supported by PEStudio (at least we couldn't find any library/function that is checked to perform the functionality of several of these messages)

|| Feature/Functions | Support by CL version |
|-| ----------------- |:---------------------:|
|1. | The file references the Smartcard API | Same as original |
|2. | The file references a Virtual Machine (VM) | Same as original |
|3. | The file references the Remote Desktop Session Host Server | Same as original |
|4. | The file references the Protected Storage | Same as original |
|5. | The file references the Active Directory (AD) | Same as original |
|6. | The file references the Windows Native API | Same as original |
|7. | The file references the Simple Network Management Protocol (SNMP) | Same as original |
|8. | The file references the Security Descriptor Definition Language (SDDL) | Same as original |
|9. | The file references the Cabinet (CAB) library | Same as original |
|10. | The file references the eXtension for Financial Services (XFS) library | Same as original |
|11. | The file references the Lightweight Directory Access Protocol (LDAP) | Same as original |
|12. | The file modifies the Registry | Same as original |
|13. | The file references the Security Account Manager (SAM) | Same as original |
|14. | The file references the Clipboard | Same as original |
|15. | The file references the installation of Hooks | Same as original |
|16. | The file enumerates the list of running processes | Same as original |
|17. | The file references the Service Control Manager (SCM) | Same as original |
|18. | The file references the Reflective DLL Library injection technique | Same as original |
|19. | The file references the Windows Indexing engine | Same as original |
|20. | The file enumerates the list of loaded modules | Same as original |
|21. | The file references the Desktop window | Same as original |
|22. | The file references the Router Administration API | Same as original |
|23. | The file references the Mail (MAPI) API | Same as original |
|24. | The file references the Microsoft Identity Manager | Same as original |
|25. | The file references the Windows Socket (winsock) API | Same as original |
|26. | The file references the Internet Protocol Helper API | Same as original |
|27. | The file references libraries at runtime | Same as original |
|28. | The file spawns another process | Same as original |
|29. | The file references the Microsoft Digest Access API | Same as original |
|30. | The file references the Windows Cryptographic Primitives API | Same as original |
|31. | The file references the Local Security Authority Server (LSASS) | Same as original |
|32. | The file references the Local Security Authority (LSA) | Same as original |
|33. | The file references the Internet Explorer Zone Manager | Same as original |
|34. | The file references the Credential Manager User API | Same as original |
|35. | The file references the Windows Setup API | Same as original |
|36. | The file references the Windows Cryptographic API | Same as original |
|37. | The file references the Windows Debug Helper API | Same as original |
|38. | The file references the Windows IP Helper API | Same as original |
|39. | The file references the Power Profile Helper API | Same as original |
|40. | The file references the Multiple Provider Router (MPR) API | Same as original |
|41. | The file references the File Transfer Protocol (FTP) API | Same as original |
|42. | The file references users credentials | Same as original |
|43. | The file references the resources of an executable | Same as original |
|44. | The file enumerates files | Same as original |
|45. | The file references the Backup API | Same as original |
|46. | The file references the Global Atom Table | Same as original |
|47. | The file creates or modifies file(s) | Same as original |
|48. | The file references the Remote Access Service (RAS) API | Same as original |
|49. | The file references the Performance Counters | Same as original |
|50. | The file references the Event Log | Same as original |
|51. | The file references the system Power | Same as original |
|52. | The file references the HTML Help Control | Same as original |
|53. | The file queries for Processes and Modules | Same as original |
|54. | The file references Pipes | Same as original |
|55. | The file references the Console | Same as original |
|56. | The file references the Tasks Scheduler | Same as original |
|57. | The file references the Windows Management Instrumentation (WMI) | Same as original |
|58. | The file downloads bits from the Internet and save them to a file | Same as original |
|59. | The file references the Windows default safe DLL search path | Same as original |
|60. | The file references a Printer Driver | Same as original |
|61. | The file references Dynamic Data Exchange (DDE) | Same as original |
|62. | The file enumerates the list of registered windows | Same as original |
|63. | The file references Function(s) callback executed when the program exits | Same as original |
|64. | The file transfers control to a Debugger | Same as original |
|65. | The file references the AutoIt scripting Engine | Same as original |
|66. | The file references Microsoft the Setup Interface (MSI) | Same as original |
|67. | The file references Microsoft Detour to trojanize other executable | Same as original |
|68. | The file references the Domain Name System (DNS) API | Same as original |
|69. | The file references temporary file(s) | Same as original |
|70. | The file references the WLAN interface | Same as original |
|71. | The file references the Environment variables | Same as original |
|72. | The file references a Control Panel Application callback | Same as original |
|73. | The file monitors Registry operations | Same as original |
|74. | The file references the passwords of Internet Explorer | Same as original |
|75. | The file references the DHCP Client Service | Same as original |
|76. | The file references the NetBIOS or the DNS name of the local computer | Same as original |
|77. | The file references the Windows Internet (WinINet) library | Same as original |
|78. | The file references data on a Socket | Same as original |
|79. | The file references the Internet Explorer (IE) server | Same as original |
|80. | The file logs the Internet Explorer (IE) hits | Same as original |
|81. | The file synthesizes Mouse motion and Buttons clicks | Same as original |
|82. | The file references the protection of the Virtual Address space | Same as original |
|83. | The file references the RPC Network Data Representation (NDR) Engine | Same as original |
|84. | The file references the Windows Software Quality Metrics (SQM) | Same as original |
|85. | The file references the Event Tracing for Windows (ETW) framework | Same as original |
|86. | The file inserts itself in the chain of the Clipboard Listeners | Same as original |
|87. | The file references the Open Database Connectivity (ODBC) installer | Same as original |
|88. | The file references the Single-Instance Store (SIS) backup framework | Same as original |
|89. | The file installs a Device or a Driver | Same as original |
|90. | The file references the ODBC Driver Tracing mechanism | Same as original |
|91. | The file references Bitlocker | Same as original |
|92. | The file registers itself as a boot Driver | Same as original |
|93. | The file walks up and records the stack information | Same as original |
|94. | The file references the Windows Scripting Host (WSH) engine | Same as original |
|95. | The file references the Console Based Script Host engine | Same as original |
|96. | The file references the HTML Application Host engine | Same as original |
|97. | The file references the VB Scripting Encoder/Decoder engine | Same as original |
|98. | The file references the Java Scripting Encoder/Decoder engine | Same as original |
|99. | The file references the Windows File Protection (WFP) | Same as original |
|100. | The file simulates the Keyboard | Same as original |
|101. | The file references the Multimedia Class Scheduler service (MMCSS) | Same as original |
|102. | The file references the Group Policy (GP) | Same as original |
|103. | The file references a communications device | Same as original |
|104. | The file monitors a communications device | Same as original |
|105. | The file references the local Running Object Table (ROT) | Same as original |
|106. | The file references the Human Interface Devices (HID) Protocol | Same as original |
|107. | The file references Simple Mail Transfer Protocol (SMTP) | Same as original |
|108. | The file references the Internet Control Message Protocol (ICMP) | Same as original |
|109. | The file fingerprints Antivirus or monitoring tools | Same as original |
|110. | The file references the Windows network Capture Library | Same as original |
|111. | The file references Microsoft Office | Same as original |
|112. | The file enumerates Network resources | Same as original |
|113. | The file references Alternate Data Stream (ADS) | Same as original |
|114. | The file fingerprints Web browsers | Same as original |
|115. | The file fingerprints Sandboxes | Same as original |
|116. | The file fingerprints Email clients | Same as original |
|117. | The file references the Firefox API | Same as original |
|118. | The file references the Shim Engine | Same as original |
|119. | The file references the Windows Address Book (WAB) | Same as original |
|120. | The file references the Recycle Bin | Same as original |
|121. | The file references the Volume Shadow Administration (vssadmin) tool | Same as original |
|122. | The file references the Windows Scripting runtime | Same as original |
|123. | The file references the gzip compression library | Same as original |
|124. | The file enumerates the list of running threads | Same as original |
|125. | The file enumerates the list of mounted folders | Same as original |
|126. | The file installs an Exception Handler | Same as original |
|127. | The file enumerates the existing Logon sessions | Same as original |
|128. | The file enumerates the Display devices on the computer | Same as original |
|129. | The file enumerates the Display monitors on the computer | Same as original |
|130. | The file enumerates the cache of Internet Explorer | Same as original |
|131. | The file references zLibDll, an open source ZLIB compression library | Same as original |
|132. | The file references the Security Management API | Same as original |
|133. | The file references the Authorization API | Same as original |
|134. | The file references the Registry API | Same as original |
|135. | The file references the Memory Management API | Same as original |
|136. | The file references the Tool Help API | Same as original |
|137. | The file references the Backup API | Same as original |
|138. | The file references the Event Logging API | Same as original |
|139. | The file references the Event Tracing API | Same as original |
|140. | The file references the Error Handling API | Same as original |
|141. | The file references the Directory Management API | Same as original |
|142. | The file references the Debugging API | Same as original |
|143. | The file references the Console API | Same as original |
|144. | The file references the ImageHlp API | Same as original |
|145. | The file references the COM API | Same as original |
|146. | The file references the System Information API | Same as original |
|147. | The file references the Package Query API | Same as original |
|148. | The file references the Setup API | Same as original |
|149. | The file references the Structured Storage API | Same as original |
|150. | The file references the Dynamic Data Exchange Management Library (DDEML) API | Same as original |
|151. | The file references the Clipboard API | Same as original |
|152. | The file references the WinINet API | Same as original |
|153. | The file references the Dynamic-Link Library API | Same as original |
|154. | The file references the Process and Thread API | Same as original |
|155. | The file references the WinHttp API | Same as original |
|156. | The file references the (Zw) Native API | Same as original |
|157. | The file references the (Rtl) Native API | Same as original |
|158. | The file references the (Nt) Native API | Same as original |
|159. | The file references the DHCP Server Management API | Same as original |
|160. | The file references the Network Management API | Same as original |
|161. | The file references the DNS API | Same as original |
|162. | The file references the Mailslot API | Same as original |
|163. | The file references the RPC API | Same as original |
|164. | The file references the Structured Exception Handling (SEH) API | Same as original |
|165. | The file references the Service API | Same as original |
|166. | The file references the File Management API | Same as original |
|167. | The file references the Video Capture API | Same as original |
|168. | The file references the Cabinet API | Same as original |
|169. | The file references the Single-Instance Store (SIS) Backup API | Same as original |
|170. | The file references the Performance Counters API | Same as original |
|171. | The file references the Atom API | Same as original |
|172. | The file references the Device Management API | Same as original |
|173. | The file references the Remote Access Service Custom Scripting API | Same as original |
|174. | The file references the WinSNMP API | Same as original |
|175. | The file references the Router Information API | Same as original |
|176. | The file references the Network Data Representation (Ndr) API | Same as original |
|177. | The file references the Power Management API | Same as original |
|178. | The file references the Remote Desktop API | Same as original |
|179. | The file references the WLAN API | Same as original |
|180. | The file references the SNMP API | Same as original |
|181. | The file references the WinDbgExt API | Same as original |
|182. | The file references the DDE API | Same as original |
|183. | The file references a Directory Notification watcher | Same as original |
|184. | The file enumerates files on a FTP server | Same as original |
|185. | The file references Meterpreter service | Same as original |


### Summary
What we support:
* Use customizable xml files (same as the original)
* Checking for (up to) 185 APIs and features which are referenced or implemented by the PE file
* Checking for blacklisted imports, resources and patterns (signature of packers)
* Extraction of all strings in the file and check against blacklisted strings
* XML and JSON output
* Interactive mode on command line
* Various command line options to specify the output
* Show TLS callbacks
* Show relocations
* Check file against yara rules
* Extract resources and save them in a file in order to allow further analysis (the analysis is not implemented)

Main missing features:
* Extracting resources and analyzing them further
* 131 of 177 Indicators are not implemented