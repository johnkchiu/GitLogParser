GitLogParser
============

Python script to parse 'git log'

## Usage
Script is intented to be used via commandline where you pipe 'git log' output to the script.  For example:

	> git log | gitLogParser.py

## Example
### git log output:

	commit 80eab6766c4718cb27d4f6aa40bf71e79ba3ebcc
	Author: John Chiu <jchiu@paypal.com>
	Date:   Sun Oct 13 17:59:43 2013 -0700

	    Upgraded to 4.X and added Fragments

	commit 30ce75f436a0b8a493e022c20e4c3d7138126030
	Author: johnkchiu <johnkchiu@yahoo.com>
	Date:   Sun Oct 13 17:00:24 2013 +0000

	    Created new branch dev

	commit 2677b9d6d8b100d85fbd6da1b4a4187a21b676ab
	Author: John Chiu <jchiu@paypal.com>
	Date:   Tue Oct 16 20:33:33 2012 -0700

	    - Rewrote song properties
	    - Added Android Support Library
	    - Clean up some code

	commit 55b61986d82842f20788310cf7ffe4a02ca49437
	Author: Chiu <jchiu@LM-SJN-00713306.(none)>
	Date:   Thu Apr 5 23:43:30 2012 -0700

	    Added back Eclipse files
	...

### script output:


	[jchiu@laptop]$ git log | ~/bin/gitLogParser.py
	Author           Email                 Hash      Message
	=================================================================================
	John Chiu        jchiu@paypal.com      80eab67   Upgraded to 4.X and added Fragments
	johnkchiu        johnkchiu@yahoo.com   30ce75f   Created new branch dev
	John Chiu        jchiu@paypal.com      2677b9d   - Rewrote song properties
	Chiu             jchiu@LM-SJN-0071330  55b6198   Added back Eclipse files
	Chiu             jchiu@LM-SJN-0071330  1af4d7d   Added songs.properties file and data models
	Chiu             jchiu@LM-SJN-0071330  884293f   Merge branch 'master' of https://bitbucket.org/... 
	Chiu             jchiu@LM-SJN-0071330  006b306   Added splash screen and refactor filenames
	Chiu             jchiu@LM-SJN-0071330  7b9ce47   Added splash screen and refactor filenames
	Chiu             jchiu@LM-SJN-0071330  5885eb7   Working MediaService, SongList and SongView
	Chiu             jchiu@LM-SJN-0071330  c6f4003   Remove bin and gen directories