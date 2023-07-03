
- [About](#about)
	- [To do](#to-do)
- [What is new](#what-is-new)
	- [Installation](#installation)
- [pestudio-cli](#pestudio-cli)
	- [Goal](#goal)
	- [Dependencies](#dependencies)

# About

This is a project from [Forensics class at Eurecom (spring 2023)](https://www.eurecom.fr/en/course/forensics-2023spring) . The aims of this project is to improve pestudio-cli tool from  [https://github.com/KuechA/pestudio-cli](https://github.com/KuechA/pestudio-cli):

## To do

- [ ] Update the project pestudio-cli (now it throws exceptions due to changes to the lief library).

- [ ] Update it with the newer data and features of pestudio.

- [ ] Add a hole-detection feature which detects whether there is any data "outside" of sections.

# What is new

We first fixed the tools. Some errors and correction result is in [notes/readme.md #identify-errors-and-correction-results](notes/readme.md#identify-errors-and-correction-results).

Then we update the folder xml with newest file from pestudio 9.53. There is a lot of changes: they introduces new files, remove some files. The structures, key words inside the xml files also changes a lot.

After update the folder xml, we fix all the python files to be able using the new xml folder. Some indicators have to remove since there are no corresponding indicator and threshold to compare in the new xml file.

Then we implement a new feature name HolesDetection. For detail, see [notes/readme.md#holes-detection-feature](notes/readme.md#hole-detection-feature).

We haven't update the file [Features.md](Feature.md) with the new version of xml folder yet.

You can check the folder [xml_old](xml_old/) to see the old version of xml folder.

## Installation 
Run the file setup.sh to install the depences.

Below are some example of running (suppose that we are in the root folder of the project).

To run our feature:
```zsh
python3 pestudio.py
>> f tests/tls_upx.exe
>> help
>> holes
>> q
```
Other features:
```zsh
python3 PeAnalyzer.py -f tests/tls_upx.exe
```
```zsh
python3 SignatureMatcher.py -f tests/tls_upx.exe
```
To check file on VirusTotal, you need to have an api key. For the experiment, we provide one key. Make sure to connect to the internet and you may need to re-run to make it works (because of the internet):
```zsh
echo f4008db665dba98aa1d22766cd4befea393b5505a4f9041d84005e03be5a69b1 > VirusTotalApiKey
python3 VirusTotalClient.py -f tests/tls_upx.exe
```

If you want to checkout the old verion of the file (with old version of xml folder) after correcting run

```git
git checkout 7d611285bfc0ff1ee5b299b875eafc7afb3f09da
```

---

The part below is originally from pestudio-cli

---

# pestudio-cli

## Goal

Our goal is the implementation of a python-based command-line tool which can be used to check PE files for known malicious patterns. We therefore
* Submit the file to VirusTotal and present a summary of the result to the user
* Match the PE file against signatures of known malicious programs (the signatures are imported from PEStudio). Currently, these are signatures of packers
* Check if the binary uses blacklisted libraries/imports
* Check for suspicious resources
* Examine the strings of the binary to find blacklisted values
* Show various information and highlight anomalies about the PE file like the PE header (time date stamp in the future), TLS callbacks or the relocations
* Check the presence of more than 100 features in the PE file.
* On top, we check various suspicious values, among others a high entropy, known imphashes, anomalies of the entry-point address, sections, headers, data, ...
* Include support for yara rules by calling the yara-python library (if installed)

We support multiple output formats and make the output result highly configurable:
* Many options can be used to specify which analysis should be performed
* Output an xml file containing the desired information
* Output a JSON representation with the requested information
* A human-readable representation containing all the requested information at once
* An interactive mode can be used in order to show only selected information at a time

## Dependencies
* prettytable python library: `pip3 install prettytable`
* LIEF to parse the PE file `pip3 install setuptools --upgrade; pip3 install lief`
* In case files should be submitted to VirusTotal in order to retrieve their score, a [VirusTotal API key](https://www.virustotal.com/en/documentation/public-api/#getting-started) has to be stored in the file `VirusTotalApiKey` in the root of the directory.
* In order to use the functionality to check the file against [yara](https://virustotal.github.io/yara/) signatures, yara-python is required: `pip3 install yara-python`. Therefore, an installation of yara is required
