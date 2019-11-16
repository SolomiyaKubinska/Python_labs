import re

def output(pattern, string):
    if re.match(pattern, string):
        print("Match")
    else:
        print("Not match")

def All_Lessons():
    """All Lessons"""
    print("\n-exercise 1-----------")
    match1 = ["abcdefg", "abc"]
    for i in range(len(match1)):
        print(f"Match\t{match1[i]}")
        pat = r"abc"
        print(f"pattern - {pat}")
        output(pat, match1[i])

    print("\n-exercise 1.5-----------")
    match2 = ["abc123xyz", "define \"123\""]
    for i in range(len(match2)):
        print(f"Match\t{match2[i]}")
        pat = r"([\w\D\"]+)[1-3]([\D\";]+)"
        print(f"pattern - {pat}")
        output(pat, match2[i])

    print("\n-exercise 2-----------")
    match3 = ["cat.", "?=+."]
    for i in range(len(match3)):
        print(f"Match\t{match3[i]}")
        pat = r".*\.$"
        print(f"pattern - {pat}")
        output(pat, match3[i])

    print("\n-exercise 3-----------")
    match4 = ["can", "man"]
    skip1 = ["ran"]
    for i in range(len(match4)):
        print(f"Match\t{match4[i]}")
        pat = r"[cm]an"
        print(f"pattern - {pat}")
        output(pat, match4[i])
    for i in range(len(skip1)):
        print(f"Skip\t{skip1[i]}")

    print("\n-exercise 4-----------")
    match5 = ["hog", "dog"]
    skip2 = ["bog"]
    for i in range(len(match5)):
        print(f"Match\t{match5[i]}")
        pat = r"[^b]og"
        print(f"pattern - {pat}")
        output(pat, match5[i])
    for i in range(len(skip2)):
        print(f"Skip\t{skip2[i]}")

    print("\n-exercise 5-----------")
    match6 = ["Ana", "Bob"]
    skip3 = ["aax", "bby"]
    for i in range(len(match6)):
        print(f"Match\t{match6[i]}")
        pat = r"[A-B][n-o][a-b]"
        print(f"pattern - {pat}")
        output(pat, match6[i])
    for i in range(len(skip3)):
        print(f"Skip\t{skip3[i]}")

    print("\n-exercise 6-----------")
    match7 = ["wazzzzzup", "wazzzup"]
    skip4 = ["wazup"]
    for i in range(len(match7)):
        print(f"Match\t{match7[i]}")
        pat = r"waz{3,5}up"
        print(f"pattern - {pat}")
        output(pat, match7[i])
    for i in range(len(skip4)):
        print(f"Skip\t{skip4[i]}")

    print("\n-exercise 7-----------")
    match8 = ["aaaabcc", "aabbbbc", "aacc"]
    skip5 = ["a"]
    for i in range(len(match8)):
        print(f"Match\t{match8[i]}")
        pat = r"^a+b*c+$"
        print(f"pattern - {pat}")
        output(pat, match8[i])
    for i in range(len(skip5)):
        print(f"Skip\t{skip5[i]}")

    print("\n-exercise 8-----------")
    match9 = ["1 file found?", "2 files found?", "24 files found?"]
    skip6 = ["No files found?"]
    for i in range(len(match9)):
        print(f"Match\t{match9[i]}")
        pat = r"\d+ files? found\?"
        print(f"pattern - {pat}")
        output(pat, match9[i])
    for i in range(len(skip6)):
        print(f"Skip\t{skip6[i]}")

    print("\n-exercise 9-----------")
    match10 = ["1.  abc", "2.   abc", "3.    abc"]
    skip7 = ["4.abc"]
    for i in range(len(match10)):
        print(f"Match\t{match10[i]}")
        pat = r"\d\.\s+abc"
        print(f"pattern - {pat}")
        output(pat, match10[i])
    for i in range(len(skip7)):
        print(f"Skip\t{skip7[i]}")

    print("\n-exercise 10-----------")
    match11 = ["Mission: successful"]
    skip8 = ["Last Mission: unsuccessful", "Next Mission: successful upon capture of target"]
    for i in range(len(match11)):
        print(f"Match\t{match11[i]}")
        pat = r"^Mission: successful$"
        print(f"pattern - {pat}")
        output(pat, match11[i])
    for i in range(len(skip8)):
        print(f"Skip\t{skip8[i]}")

    print("\n-exercise 11-----------")
    match12 = ["file_record_transcript.pdf", "file_07241999.pdf"]
    skip9 = ["testfile_fake.pdf.tmp"]
    for i in range(len(match12)):
        print(f"Capture\t{match12[i]}")
        pat = r"^(file.+)\.pdf$"
        print(f"pattern - {pat}")
        output(pat, match12[i])
    for i in range(len(skip9)):
        print(f"Skip\t{skip9[i]}")

    print("\n-exercise 12-----------")
    match13 = ["Jan 1987", "May 1969", "Aug 2011"]
    capture1 = ["Jan 1987 1987", "May 1969 1969", "Aug 2011 2011"]
    for i in range(len(match13)):
        print(f"Capture\t{match13[i]}\t{capture1[i]}")
        pat = r"(\w+ (\d+))"
        print(f"pattern - {pat}")
        output(pat, match13[i])

    print("\n-exercise 13-----------")
    match14 = ["1280x720", "1920x1600", "1024x768"]
    capture2 = ["1280 720", "1920 1600", "1024 768"]
    for i in range(len(match14)):
        print(f"Capture\t{match14[i]}\t{capture2[i]}")
        pat = r"(\d+)x(\d+)"
        print(f"pattern - {pat}")
        output(pat, match14[i])

    print("\n-exercise 14-----------")
    match15 = ["I love cats", "I love dogs"]
    skip10 = ["I love logs", "I love cogs"]
    for i in range(len(match15)):
        print(f"Match\t{match15[i]}")
        pat = r"I love (cats|dogs)"
        print(f"pattern - {pat}")
        output(pat, match15[i])
    for i in range(len(skip10)):
        print(f"Skip\t{skip10[i]}")

    print("\n-exercise 15-----------")
    match16 = ["The quick brown fox jumps over the lazy dog.",
               "There were 614 instances of students getting 90.0% or above.",
               "The FCC had to censor the network for saying &$#*@!."]
    for i in range(len(match16)):
        print(f"Match\t{match16[i]}")
        pat = r".*"
        print(f"pattern - {pat}")
        output(pat, match16[i])

All_Lessons()

def Practise_Problems():
    """Practice Problems"""
    print("\n-exercise 1-----------")
    match1 = ["3.14529", "128", "1.9e10", "123,340.00"]
    skip1 = ["720p"]
    for i in range(len(match1)):
        print(f"Match\t{match1[i]}")
        pat = r"^-?\d+(,\d+)*(\.\d+(e\d+)?)?$"
        print(f"pattern - {pat}")
        output(pat, match1[i])
    for i in range(len(skip1)):
        print(f"Skip\t{skip1[i]}")

    print("\n-exercise 2-----------")
    match2 = ["415-555-1234", "(416)555-3456", "202 555 4567", "4035555678", "1 416 555 9292"]
    capture2 = ["415", "416", "202", "403", "416"]
    for i in range(len(match2)):
        print(f"Capture\t{match2[i]}\t{capture2[i]}")
        pat = r"1?[\s-]?\(?(\d{3})\)?[\s-]?\d{3}[\s-]?\d{4}"
        print(f"pattern - {pat}")
        output(pat, match2[i])

    print("\n-exercise 3-----------")
    match3 = ["tom@hogwarts.com", "tom.riddle@hogwarts.com", "tom.riddle+regexone@hogwarts.com"]
    capture3 = ["tom", "tom.riddle", "tom.riddle"]
    for i in range(len(match3)):
        print(f"Capture\t{match3[i]}\t{capture3[i]}")
        pat = r"^([\w\.]*)"
        print(f"pattern - {pat}")
        output(pat, match3[i])

    print("\n-exercise 4-----------")
    match4 = ["img0912.jpg", "favicon.gif", "updated_img0912.png"]
    skip4 = ["documentation.html", ".bash_profile"]
    for i in range(len(match4)):
        print(f"Match\t{match4[i]}")
        pat = r"^(\w+).(jpg|png|gif)$"
        print(f"pattern - {pat}")
        output(pat, match4[i])
    for i in range(len(skip4)):
        print(f"Skip\t{skip4[i]}")

    print("\n-exercise 5-----------")
    match5 = ["				The quick brown fox...", "   jumps over the lazy dog."]
    for i in range(len(match5)):
        print(f"Capture\t{match5[i]}")
        pat = r"^\s*(.*)\s*$"
        print(f"pattern - {pat}")
        output(pat, match5[i])

    print("\n-exercise 6-----------")
    match6 = ["E/( 1553):   at widget.List.makeView(ListView.java:1727)	"]
    skip6 = ["W/dalvikvm( 1553): threadid=1: uncaught exception"]
    for i in range(len(match6)):
        print(f"Match\t{match6[i]}")
        pat = r"E/\( \d+\):\s+\D+\.(\w+)\((\w+.\w+):(\d+)\)"
        print(f"pattern - {pat}")
        output(pat, match6[i])
    for i in range(len(skip6)):
        print(f"Skip\t{skip6[i]}")

    print("\n-exercise 7-----------")
    match7 = ["ftp://file_server.com:21/top_secret/life_changing_plans.pdf", "file://localhost:4040/zip_file"]
    capture7 = ["ftp file_server.com 21", "file localhost 4040"]
    for i in range(len(match7)):
        print(f"Capture\t{match7[i]}\t{capture7[i]}")
        pat = r"(\w+)://(\w+-?(\w+)?(\.com)?)[:/]?(\d+)?([/\w+]+)?([\.\w+]+)?"
        print(f"pattern - {pat}")
        output(pat, match7[i])

Practise_Problems()

def main():
    All_Lessons()
    Practise_Problems()

if __name__ == '__main__':
    main()